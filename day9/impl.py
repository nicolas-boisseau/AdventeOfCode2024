import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

class Block:
    def __init__(self, id, size, isFree):
        self.id = id
        self.size = size
        self.isFree = isFree


def print_blocks(blocks):
    for b in blocks:
        if b.isFree:
            print(b.size * '.', end='')
        else:
            print(b.size * str(b.id), end='')
    print()


def extract_blocks(i, lines):
    blocks = []
    for c in lines[0]:
        blocks.append(Block((i // 2)+1, int(c), not i % 2 == 0))
        i += 1
    return blocks

def firstFreeBlock(blocks):
    for b in blocks:
        if b.isFree:
            return b
    return None

def part1(lines):
    i = 0
    blocks = extract_blocks(i, lines)
    print_blocks(blocks)

    copy=blocks.copy()
    newBlocks = []
    while len(copy) > 0:
        b = copy.pop(0)
        if b.isFree:

        else:
            newBlocks.append(Block(b.id, b.size, True))
            newBlocks.append(Block(b.id, b.size, False))

    print_blocks(blocks)


def part2(lines):
    return 4


if __name__ == '__main__':

    part = 1
    expectedSampleResult = -1

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2024, part, result)
        print(f"Part {part} result posted !")
