import math
import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def part1(lines):
    reportSafes = 0
    for l in lines:
        numbers = [int(c) for c in capture_all(r"([0-9]+)", l)]

        if isSafe(numbers):
            reportSafes += 1

    return reportSafes


def isSafe(numbers):
    safe = True
    i = 0
    isInc = numbers[1] > numbers[0]

    if isInc:
        while i < len(numbers) - 1:
            if numbers[i] < numbers[i + 1] and math.fabs(numbers[i] - numbers[i + 1]) <= 3.0:
                i = i + 1
            else:
                safe = False
                break
    else:
        while i < len(numbers) - 1:
            if numbers[i] > numbers[i + 1] and math.fabs(numbers[i] - numbers[i + 1]) <= 3.0:
                i = i + 1
            else:
                safe = False
                break

    return safe

def mutations(numbers):
    mutations = []
    for i in range(len(numbers)):
        mutations.append(numbers[:i] + numbers[i + 1:])
    return mutations

def part2(lines):
    reportSafes = 0
    for l in lines:
        numbers = [int(c) for c in capture_all(r"([0-9]+)", l)]
        safe = True

        if isSafe(numbers):
            reportSafes += 1
        else:
            for mutation in mutations(numbers):
                if isSafe(mutation):
                    reportSafes += 1
                    break

    return reportSafes


if __name__ == '__main__':

    part = 2
    expectedSampleResult = 4

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2024, part, result)
        print(f"Part {part} result posted !")
