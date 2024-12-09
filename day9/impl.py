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

def extract_blocks(lines):
    i = 0
    blocks = []
    for c in lines[0]:
        if (i // 2 > 9):
            print("Too many blocks")
        blocks.append(Block(i // 2, int(c), not i % 2 == 0))
        i += 1
    return blocks

def firstFreeBlock(blocks):
    for b in blocks:
        if b.isFree:
            return b
    return None

def checksum(str):
    score = 0
    for i in range(len(str)):
        if str[i] != '.':
            score += int(str[i]) * i
    return score

def part1(lines):
    blocks = extract_blocks(lines)
    strb = blocks_to_string(blocks)
    print(strb)

    i = 0
    res = ""
    score = 0
    lastMax = len(strb) - 1
    while i < len(strb):
        if strb[i] == '.':
            j = lastMax
            while j > i:
                if strb[j] != '.':
                    res += strb[j]
                    score += int(strb[j]) * i
                    #print(f"Remove {strb[j:]}")
                    strb = strb[:i] + strb[j] + strb[i+1:]
                    strb = strb[:j] + "." + strb[j + 1:]
                    lastMax = j
                    break
                j -= 1
        else:

            res += strb[i]
            score += int(strb[i]) * i

        i += 1

    print(strb)
    print(f"Score: {score}")

    #print(res)

    return checksum(strb)



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
