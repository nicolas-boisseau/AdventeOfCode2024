import os.path

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
        dont = text[prev:].index("don't()")
    except ValueError:
        pass
    try:
        do = text[prev:].index("do()")
    except ValueError:
        pass
    if dont == do == 99999999999:
        return text[prev:], -1, False
    if dont < do:
        return text[prev:prev+dont + 7], prev+dont + 7, False
    else:
        return text[prev:prev+do + 4], prev+do + 4, True

def part2(lines):
    fulltext = "".join(lines)
    s = 0

    # xmul(2,4)&mul[3,7]!^  don't()_mul(5,5)+mul(32,64](mul(11,8)un  do()?mul(8,5))
    nextText, pos, next_state = find_next_text(fulltext)
    print(nextText)
    do = True
    toStop = False
    while not toStop:
        toStop = pos == -1
        if do:
            values = capture_all(r"mul\(([0-9]+),([0-9]+)\)", nextText)
            print(values)
            s = s + sum([int(a) * int(b) for a, b in values])

        do = next_state
        nextText, pos, next_state = find_next_text(fulltext, pos)
        print(nextText)

    return s


if __name__ == '__main__':

    part = 2
    expectedSampleResult = 48

    part_func = part1 if part == 1 else part2
    sample = "sample.txt" if part == 1 else "sample2.txt"
    if part_func(read_input_lines(sample)) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2024, part, result)
        print(f"Part {part} result posted !")
