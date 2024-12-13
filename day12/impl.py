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

def propagate(current_symbol, x, y, lines, visited={}, area=1, perimeter=0, outside={}):
    visited[(x, y)] = True
    if (x+1,y) not in visited.keys():
        if can_go_right(x, y, lines, current_symbol):
            a,p,v,o = propagate(current_symbol, x + 1, y, lines, visited, area, 0, outside)
            area = a+1
            perimeter += p
            visited = {**visited, **v}
            outside = {**outside, **o}
        else:
            perimeter += 1
            outside[(x+1, y, 1, 0)] = True
    if (x-1,y) not in visited.keys():
        if can_go_left(x, y, lines, current_symbol):
            a,p,v,o = propagate(current_symbol, x - 1, y, lines, visited, area, 0, outside)
            area = a+1
            perimeter += p
            visited = {**visited, **v}
            outside = {**outside, **o}
        else:
            perimeter += 1
            outside[(x - 1, y, -1, 0)] = True
    if (x,y-1) not in visited.keys():
        if can_go_up(x, y, lines, current_symbol):
            a,p,v,o = propagate(current_symbol, x, y - 1, lines, visited, area, 0, outside)
            area = a+1
            perimeter += p
            visited = {**visited, **v}
            outside = {**outside, **o}
        else:
            perimeter += 1
            outside[(x, y - 1, 0, -1)] = True
    if (x,y+1) not in visited.keys():
        if can_go_down(x, y, lines, current_symbol):
            a,p,v,o = propagate(current_symbol, x, y + 1, lines, visited, area, 0, outside)
            area = a+1
            perimeter += p
            visited = {**visited, **v}
            outside = {**outside, **o}
        else:
            perimeter += 1
            outside[(x, y + 1, 0, 1)] = True


    return area, perimeter, visited, outside


def get_first_position_of_each_symbol(lines, visited):
    positions = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if (x,y) not in visited.keys() and lines[y][x] not in positions and lines[y][x] != "." and lines[y][x] != '\n':
                positions[lines[y][x]] = (x, y)
    return positions

def part1(lines):
    all_visited = {}
    score = 0
    nb_symbol = 0
    while True:
        symbol_positions = get_first_position_of_each_symbol(lines, all_visited)
        if len(symbol_positions) == 0:
            break
        for symbol, (x, y) in symbol_positions.items():
            area, perimeter, visited, _ = propagate(symbol, x, y, lines, {}, 1, 0)
            #print(f"Symbol={symbol}, Area: {area}, Perimeter: {perimeter}")
            sub_score = area * perimeter
            #print(f"Symbol={symbol}, Area: {area}, Perimeter: {perimeter}, Score: {sub_score}")
            if str.isdigit(symbol):
                int_symbol = int(symbol)
                sub_score *= int_symbol
                nb_symbol += int_symbol

            score += sub_score
            all_visited = {**all_visited, **visited}

    return score, nb_symbol

def build_outside(outside, dir):
    max_x = max([x for x, y, dx, dy in outside])
    min_x = min([x for x, y, dx, dy  in outside])
    max_y = max([y for x, y, dx, dy in outside])
    min_y = min([y for x, y, dx, dy in outside])

    output = []
    for y in range(min_y, max_y+1):
        l = ""
        for x in range(min_x, max_x+1):
            nb = 0
            nb += 1 if (x,y,1,0)  in outside and dir == (1,0) else 0
            nb += 1 if (x,y,-1,0)  in outside and dir == (-1,0) else 0
            nb += 1 if (x,y,0,1) in outside and dir == (0,1) else 0
            nb += 1 if (x,y,0,-1) in outside and dir == (0,-1) else 0
            if nb == 0:
                l += "."
                #print(".", end="")
            else:
                l += str(nb)
                #print(nb, end="")
        #print()
        output += [l]
    #print()

    return output

def part2(lines):
    all_visited = {}
    score = 0
    while True:
        symbol_positions = get_first_position_of_each_symbol(lines, all_visited)
        if len(symbol_positions) == 0:
            break
        for symbol, (x, y) in symbol_positions.items():
            area, perimeter, visited, outside = propagate(symbol, x, y, lines, {}, 1, 0, {})
            total_sides = 0

            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dir in directions:
                outside_lines = build_outside(outside.keys(), dir)
                _, sides = part1(outside_lines)
                total_sides += sides


            print(f"Symbol={symbol}, Area: {area}, Sides: {total_sides}")
            score += area * total_sides
            all_visited = {**all_visited, **visited}

    return score


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
