import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def check_xmas(y, x, lines, dx, dy):
    if lines[y][x] == "X" and 0 <= x + 3 * dx < len(lines[y]) and 0 <= y + 3 * dy < len(lines):
        return (lines[y + dy][x + dx] == "M" and
                lines[y + 2 * dy][x + 2 * dx] == "A" and
                lines[y + 3 * dy][x + 3 * dx] == "S")
    return False

def part1(lines):
    xmas = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            for dx, dy in directions:
                if check_xmas(y, x, lines, dx, dy):
                    xmas += 1
    return xmas

def check_mas(y, x, lines, dx1, dy1, dx2, dy2):
    return ((lines[y + dy1][x + dx1] == "M" and lines[y + dy2][x + dx2] == "S") or
            (lines[y + dy1][x + dx1] == "S" and lines[y + dy2][x + dx2] == "M"))

def cross(x, y, lines) -> bool:
    if x == 0 or x == len(lines[y]) - 1 or y == 0 or y == len(lines) - 1:
        return False

    crosses = 0
    if lines[y][x] == "A":
        if check_mas(y, x, lines, 1, -1, -1, 1):
            crosses += 1
        if check_mas(y, x, lines, -1, -1, 1, 1):
            crosses += 1
    return crosses == 2

def part2(lines):
    xmas = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if cross(x, y, lines):
                xmas += 1
    return xmas



if __name__ == '__main__':

    part = 2
    expectedSampleResult = 9

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2024, part, result)
        print(f"Part {part} result posted !")
