import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)


def findZeroPositions(lines):
    zeros = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '0':
                zeros += [(x, y)]
    return zeros

def can_go_right(x, y, lines):
    return (x < len(lines[y]) - 1 and
            lines[y][x + 1] != "." and
            int(lines[y][x + 1]) == int(lines[y][x]) + 1)

def can_go_left(x, y, lines):
    return (x > 0 and
            lines[y][x - 1] != "." and
            int(lines[y][x - 1]) == int(lines[y][x]) + 1)

def can_go_up(x, y, lines):
    return (y > 0 and
            lines[y - 1][x] != "." and
            int(lines[y - 1][x]) == int(lines[y][x]) + 1)

def can_go_down(x, y, lines):
    return (y < len(lines) - 1 and
            lines[y + 1][x] != "." and
            int(lines[y + 1][x]) == int(lines[y][x]) + 1)

def print_lines_with_current_position(x, y, lines):
    for i in range(len(lines)):
        line = list(lines[i])
        line[x] = "X" if i == y else line[x]
        print("".join(line))
    print()

def try_reach_nine_step_by_step(x, y, lines, current_score: int = 0, already_scored = []) -> int:
    #print_lines_with_current_position(x, y, lines)

    if lines[y][x] != "." and int(lines[y][x]) == 9:
        #print(already_scored)
        #print(f"Reached 9 at {(x, y)}")
        if (x, y) not in already_scored:
            #print("already scored modified")
            already_scored += [(x, y)]
            #print("+1")
            return current_score + 1
    else:
        if can_go_right(x, y, lines):
            current_score = try_reach_nine_step_by_step(x + 1, y, lines, current_score, already_scored)
        if can_go_left(x, y, lines):
            current_score = try_reach_nine_step_by_step(x - 1, y, lines, current_score, already_scored)
        if can_go_up(x, y, lines):
            current_score = try_reach_nine_step_by_step(x, y - 1, lines, current_score, already_scored)
        if can_go_down(x, y, lines):
            current_score = try_reach_nine_step_by_step(x, y + 1, lines, current_score, already_scored)
    return current_score

def part1(lines):
    zeros = findZeroPositions(lines)

    total_score = 0
    for z in zeros:
        #print("Starting from", z)
        already_scored = []
        sub_score = try_reach_nine_step_by_step(z[0], z[1], lines, 0, already_scored)
        #print(sub_score)
        total_score += sub_score
        #print("-----")

    return total_score


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
