import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def find_guard(lines):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "^":
                #print(f"Found ^ at {x}, {y}")
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

    if lines[y + dy][x + dx] == "#" or lines[y + dy][x + dx] == "O":
        return move_guard(guard, turn_dir_right(dir), lines)
    else:
        if lines[y + dy][x + dx] in ["^", "v", "<", ">"] and get_symbol_by_dir(dir) == lines[y + dy][x + dx]:
            raise Exception("Loop detected")
        return (y + dy, x + dx), dir

def score(lines):
    score = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "X" or lines[y][x] == "^" or lines[y][x] == "v" or lines[y][x] == "<" or lines[y][x] == ">":
                score += 1
    return score

def compute_score_and_output(lines):
    guard, dir = find_guard(lines)

    while True:
        try:
            guard, dir = move_guard(guard, dir, lines)
            y, x = guard
            symbol = get_symbol_by_dir(dir)
            lines[y] = lines[y][:x] + symbol + lines[y][x + 1:]
            # print(score(lines))
            # print_map(lines)
        except ValueError:
            #print("Out of bounds")
            break

    return score(lines), lines

def part1(lines):
    final_score, _ = compute_score_and_output(lines)

    return final_score


def get_symbol_by_dir(direction):
    symbol = "X"
    if direction == (-1, 0):
        symbol = "^"
    elif direction == (0, 1):
        symbol = ">"
    elif direction == (1, 0):
        symbol = "v"
    elif direction == (0, -1):
        symbol = "<"
    return symbol


def part2(lines):
    saved_map = lines.copy()
    _, final_map = compute_score_and_output(lines)

    # compute all new maps with placing a symbol "O" in the way of the guard
    all_maps = []
    for y in range(len(final_map)):
        for x in range(len(final_map[y])):
            if final_map[y][x] in ["X", "^", "v", "<", ">"]:
                new_map = saved_map.copy()
                new_map[y] = new_map[y][:x] + "O" + new_map[y][x + 1:]
                #print_map(new_map)
                #print("")
                all_maps.append(new_map)

    # now try each map and detect if the guard is stuck in a loop
    nb_loops = 0
    for m in all_maps:
        try:
            _, _ = compute_score_and_output(m)
        except Exception as e:
            if str(e) == "Loop detected":
                nb_loops += 1
                continue
        except ValueError:
            continue

    return nb_loops



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
