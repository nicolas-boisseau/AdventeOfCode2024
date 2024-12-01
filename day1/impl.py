import math
import os.path
import sys

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def part1(lines):

    l1, l2 = [], []
    distances = []
    for l in lines:
        all_values = capture_all(r"([0-9]+)   ([0-9]+)", l)
        l1.append(int(all_values[0][0]))
        l2.append(int(all_values[0][1]))

    l1.sort(reverse=True)
    l2.sort(reverse=True)

    while len(l1) > 0 and len(l2) > 0:
        m1, m2 = l1.pop(), l2.pop()
        distances.append(int(math.fabs(m1 - m2)))

    print(distances)

    return sum(distances)

def part2(lines):
    l1, l2 = [], []
    for l in lines:
        all_values = capture_all(r"([0-9]+)   ([0-9]+)", l)
        l1.append(int(all_values[0][0]))
        l2.append(int(all_values[0][1]))

    similarities = []
    for i1 in l1:
        similarity = [i2 for i2 in l2 if i2 == i1]
        similarities.append(i1 * len(similarity))

    return sum(similarities)


if __name__ == '__main__':

    part = 2
    expectedSampleResult = 31

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2024, part, result)
        print(f"Part {part} result posted !")
