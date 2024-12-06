import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def found_guard(lines):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "^":
                print(f"Found ^ at {x}, {y}")
                return (y, x), (-1, 0)

def print_map(lines):
    for l in lines:
        print(l)

def turn_dir_right(dir):
    if dir == (-1, 0):
        return (0, 1)
    elif dir == (0, 1):
        return (1, 0)
    elif dir == (1, 0):
        return (0, -1)
    elif dir == (0, -1):
        return (-1, 0)

def move_guard(guard, dir, lines):
    y, x = guard
    dy, dx = dir

    if y + dy < 0 or y + dy >= len(lines) or x + dx < 0 or x + dx >= len(lines[y]):
        raise ValueError("Out of bounds")

    if lines[y + dy][x + dx] == "#":
        return move_guard(guard, turn_dir_right(dir), lines)
    else:
        return (y + dy, x + dx), dir

def score(lines):
    score = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "X" or lines[y][x] == "^":
                score += 1
    return score

def part1(lines):
    guard, dir = found_guard(lines)

    #print_map(lines)

    while True:
        try:
            guard, dir = move_guard(guard, dir, lines)
            y, x = guard
            lines[y] = lines[y][:x] + "X" + lines[y][x+1:]
            #print(score(lines))
            #print_map(lines)
        except ValueError:
            print("Out of bounds")
            break

    return score(lines)

def part2(lines):
    return 4


if __name__ == '__main__':

    part = 1
    expectedSampleResult = 41

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2024, part, result)
        print(f"Part {part} result posted !")
