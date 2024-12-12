import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def can_go_right(x, y, lines, current_symbol):
    return (x < len(lines[y]) - 1 and
            lines[y][x + 1] == current_symbol)

def can_go_left(x, y, lines, current_symbol):
    return (x > 0 and
            lines[y][x - 1] == current_symbol)

def can_go_up(x, y, lines, current_symbol):
    return (y > 0 and
            lines[y - 1][x] == current_symbol)

def can_go_down(x, y, lines, current_symbol):
    return (y < len(lines) - 1 and
            lines[y + 1][x] == current_symbol)

def propagate(current_symbol, x, y, lines, visited={}, area=1, perimeter=0):
    visited[(x, y)] = True
    if (x+1,y) not in visited.keys():
        if can_go_right(x, y, lines, current_symbol):
            a,p,v = propagate(current_symbol, x + 1, y, lines, visited, area, 0)
            area = a+1
            perimeter += p
            visited = {**visited, **v}
        else:
            perimeter += 1
    if (x-1,y) not in visited.keys():
        if can_go_left(x, y, lines, current_symbol):
            a,p,v = propagate(current_symbol, x - 1, y, lines, visited, area, 0)
            area = a+1
            perimeter += p
            visited = {**visited, **v}
        else:
            perimeter += 1
    if (x,y-1) not in visited.keys():
        if can_go_up(x, y, lines, current_symbol):
            a,p,v  = propagate(current_symbol, x, y - 1, lines, visited, area, 0)
            area = a+1
            perimeter += p
            visited = {**visited, **v}
        else:
            perimeter += 1
    if (x,y+1) not in visited.keys():
        if can_go_down(x, y, lines, current_symbol):
            a,p,v = propagate(current_symbol, x, y + 1, lines, visited, area, 0)
            area = a+1
            perimeter += p
            visited = {**visited, **v}
        else:
            perimeter += 1

    return area, perimeter, visited


def get_first_position_of_each_symbol(lines, visited):
    positions = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if (x,y) not in visited.keys() and lines[y][x] not in positions:
                positions[lines[y][x]] = (x, y)
    return positions

def part1(lines):
    all_visited = {}
    score = 0
    while True:
        symbol_positions = get_first_position_of_each_symbol(lines, all_visited)
        if len(symbol_positions) == 0:
            break
        for symbol, (x, y) in symbol_positions.items():
            area, perimeter, visited = propagate(symbol, x, y, lines, {}, 1, 0)
            print(f"Symbol={symbol}, Area: {area}, Perimeter: {perimeter}")
            score += area * perimeter
            all_visited = {**all_visited, **visited}

    return score

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
