import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

class Block:
    def __init__(self, id, size, isFree):
        self.id = id
        self.size = size
        self.isFree = isFree
        self.subBlocks = []

    def insert_sub_block(self, block):
        if (block.size > self.size):
            raise ValueError("Block is too big")
        self.subBlocks.append(block)
        self.size -= block.size
        if self.size == 0:
            self.isFree = False



def blocks_to_string(blocks):
    result = ""
    for b in blocks:
        if b.isFree:
            result += b.size * '.'
        else:
            result += b.size * str(b.id)
    return result

def blocks_to_int_list(blocks):
    result = []
    for b in blocks:
        if b.isFree:
            for i in range(b.size):
                result.append(-1)
        else:
            for i in range(b.size):
                result.append(b.id)
    return result

def extract_blocks(lines):
    i = 0
    blocks = []
    for c in lines[0]:
        blocks.append(Block(i // 2, int(c), not i % 2 == 0))
        i += 1
    return blocks

def firstFreeBlock(needed_size, blocks):
    i = 0
    for b in blocks:
        if b.isFree and b.size >= needed_size:
            return b, i
        i += 1
    return None, -1

def checksum(intlist):
    score = 0
    for i in range(len(intlist)):
        if intlist[i] != -1:
            score += intlist[i] * i
    return score

def checksum_str(strr):
    score = 0
    for i in range(len(strr)):
        if strr[i] != ".":
            score += int(strr[i]) * i
    return score

def print_intlist(intlist):
    result = ""
    for b in intlist:
        if b == -1:
            result += '.'
        else:
            result += str(b)
    return result

def part1(lines):
    blocks = extract_blocks(lines)
    intlist = blocks_to_int_list(blocks)
    print(intlist)
    print(print_intlist(intlist))

    i = 0
    res = []
    score = 0
    lastMax = len(intlist) - 1
    while i < len(intlist) and i <= lastMax:
        if intlist[i] == -1:
            j = lastMax
            while j > i:
                if intlist[j] != -1:
                    res.append(intlist[j])
                    score += intlist[j] * i
                    lastMax = j-1
                    break
                j -= 1
        else:
            res.append(intlist[i])
            score += intlist[i] * i

        i += 1

    print(res)
    print(print_intlist(res))
    print(f"Score: {score}")

    #print(res)

    return score



def part2(lines):
    blocks = extract_blocks(lines)

    i = len(blocks) - 1
    while i >= 0:
        current_block = blocks[i]
        if current_block.isFree:
            i -= 1
            continue
        nextFree, j = firstFreeBlock(current_block.size, blocks[:i])
        if nextFree is None:
            i -= 1
            continue
        blocks[j].insert_sub_block(Block(current_block.id, current_block.size, False))
        blocks[i].isFree = True
        i-=1

    res = []
    for b in blocks:
        if len(b.subBlocks) > 0:
            for sb in b.subBlocks:
                if sb.isFree:
                    for i in range(sb.size):
                        res.append(-1)
                    print("." * sb.size, end="")
                else:
                    for i in range(sb.size):
                        res.append(sb.id)
                    print(str(sb.id) * sb.size, end="")
            if b.size > 0:
                # print remaining free block
                for i in range(b.size):
                    res.append(-1)
                print("." * b.size, end="")
        elif b.isFree:
            for i in range(b.size):
                res.append(-1)
            print("."*b.size, end="")
        else:
            for i in range(b.size):
                res.append(b.id)
            print(str(b.id)*b.size, end="")


    return checksum(res)



if __name__ == '__main__':

    part = 2
    expectedSampleResult = 2858

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2024, part, result)
        print(f"Part {part} result posted !")
