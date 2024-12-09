import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

class Block:
    def __init__(self, id, size, isFree):
        self.id = id
        self.size = size
        self.isFree = isFree


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

def firstFreeBlock(blocks):
    for b in blocks:
        if b.isFree:
            return b
    return None

def checksum(intlist):
    score = 0
    for i in range(len(intlist)):
        if intlist[i] != -1:
            score += intlist[i] * i
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
    return 4


if __name__ == '__main__':

    part = 1
    expectedSampleResult = 1928

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2024, part, result)
        print(f"Part {part} result posted !")
