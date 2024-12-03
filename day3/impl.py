import os.path
from mailcap import subst

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def part1(lines):
    fulltext = "".join(lines)
    values = capture_all(r"mul\(([0-9]+),([0-9]+)\)", fulltext)

    return sum([int(a)*int(b) for a, b in values])

def find_next_text(text, prev=0):
    dont = 99999999999
    do = 99999999999
    try:
        dont = text.index("don't()")
    except ValueError:
        pass

    do = str.index(text, "do()")
    if dont < do:
        return text[:dont + 7],
    else:
        return text[:do + 4]

def part2(lines):
    fulltext = "".join(lines)

    nextText = find_next_text(fulltext)
    while nextText != "":

        values = capture_all(r"mul\(([0-9]+),([0-9]+)\)", nextText)
        nextText = find_next_text(nextText)

    print(values)

    return sum([int(a) * int(b) for a, b in values])


if __name__ == '__main__':

    part = 2
    expectedSampleResult = 43

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2024, part, result)
        print(f"Part {part} result posted !")
