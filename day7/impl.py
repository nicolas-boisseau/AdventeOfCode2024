import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def try_combinations(numbers, target, current=0) -> bool:
    next = numbers.pop(0)
    if len(numbers) == 0:
        if current + next == target:
            return True
        elif current * next == target:
            return True
    else:
        return try_combinations(numbers.copy(), target, current + next) or try_combinations(numbers.copy(), target, current * next)



def part1(lines):
    score = 0
    for l in lines:
        split = l.split(": ")
        target = int(split[0])
        numbers = [int(n) for n in split[1].split(" ")]
        print(target, numbers)
        if try_combinations(numbers, target):
            score += target
    return score



def part2(lines):
    return 4


if __name__ == '__main__':

    part = 2
    expectedSampleResult = 11387

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2024, part, result)
        print(f"Part {part} result posted !")
