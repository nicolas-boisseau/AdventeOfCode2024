import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def xmas_right(y, x, lines):
    if lines[y][x] == "X" and x + 3 < len(lines[y]):
        return lines[y][x+1] == "M" and lines[y][x+2] == "A" and lines[y][x+3] == "S"

def xmas_left(y, x, lines):
    if lines[y][x] == "X" and x - 3 >= 0:
        return lines[y][x-1] == "M" and lines[y][x-2] == "A" and lines[y][x-3] == "S"

def xmas_down(y, x, lines):
    if lines[y][x] == "X" and y + 3 < len(lines):
        return lines[y+1][x] == "M" and lines[y+2][x] == "A" and lines[y+3][x] == "S"

def xmas_up(y, x, lines):
    if lines[y][x] == "X" and y - 3 >= 0:
        return lines[y-1][x] == "M" and lines[y-2][x] == "A" and lines[y-3][x] == "S"

def xmas_right_down(y, x, lines):
    if lines[y][x] == "X" and x + 3 < len(lines[y]) and y + 3 < len(lines):
        return lines[y+1][x+1] == "M" and lines[y+2][x+2] == "A" and lines[y+3][x+3] == "S"

def xmas_right_up(y, x, lines):
    if lines[y][x] == "X" and x + 3 < len(lines[y]) and y - 3 >= 0:
        return lines[y-1][x+1] == "M" and lines[y-2][x+2] == "A" and lines[y-3][x+3] == "S"

def xmas_left_down(y, x, lines):
    if lines[y][x] == "X" and x - 3 >= 0 and y + 3 < len(lines):
        return lines[y+1][x-1] == "M" and lines[y+2][x-2] == "A" and lines[y+3][x-3] == "S"

def xmas_left_up(y, x, lines):
    if lines[y][x] == "X" and x - 3 >= 0 and y - 3 >= 0:
        return lines[y-1][x-1] == "M" and lines[y-2][x-2] == "A" and lines[y-3][x-3] == "S"

def part1(lines):
    xmas = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if xmas_right(y, x, lines):
                xmas += 1
            if xmas_left(y, x, lines):
                xmas += 1
            if xmas_down(y, x, lines):
                xmas += 1
            if xmas_up(y, x, lines):
                xmas += 1
            if xmas_right_down(y, x, lines):
                xmas += 1
            if xmas_right_up(y, x, lines):
                xmas += 1
            if xmas_left_down(y, x, lines):
                xmas += 1
            if xmas_left_up(y, x, lines):
                xmas += 1
    return xmas

def mas_up_right_to_down_left(y, x, lines):
    return ((lines[y-1][x+1] == "M" and lines[y+1][x-1] == "S") or
            (lines[y-1][x+1] == "S" and lines[y+1][x-1] == "M"))
def mas_down_right_to_up_left(y, x, lines):
    return ((lines[y-1][x-1] == "M" and lines[y+1][x+1] == "S") or
            (lines[y-1][x-1] == "S" and lines[y+1][x+1] == "M"))

def cross(x, y, lines) -> bool:
    if x == 0 or x == len(lines[y]) - 1 or y == 0 or y == len(lines) - 1:
        return False

    crosses = 0
    if lines[y][x] == "A":
        if mas_up_right_to_down_left(y, x, lines):
            crosses += 1
        if mas_down_right_to_up_left(y, x, lines):
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
