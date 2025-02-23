import os.path
from copy import deepcopy

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def extract_grid_and_moves(lines):
    grid = []
    i = 0
    for l in lines:
        if l == "":
            break
        grid.append([c for c in l])
        i += 1
    i+=1
    moves = []
    while i < len(lines):
        for c in lines[i]:
            moves.append(c)
        i += 1

    return grid, moves


def find_robot_position(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@":
                return x, y
    raise ValueError("No robot found")

def is_place_free_in_direction(x, y, dx, dy, grid):
    while y >= 0 and x >= 0 and y < len(grid) and x < len(grid[y]) and grid[y][x] != "#":
        if grid[y][x] in ["."]:
            return True, (x, y)
        x += dx
        y += dy
    return False, (-1, -1)

def push_robot_in_direction(x, y, dx, dy, grid):
    reversed_dir = {
        (1, 0): (-1,0),
        (-1, 0): (1,0),
        (0, 1): (0,-1),
        (0, -1): (0,1)
    }
    can_move, (nx, ny) = is_place_free_in_direction(x, y, dx, dy, grid)
    if not can_move:
        return
    cur_x, cur_y = (nx, ny)
    dnx, dny = reversed_dir[(dx, dy)]
    while not (cur_x, cur_y) == (x, y):
        to_move_val = grid[cur_y+dny][cur_x+dnx]
        prev_val = grid[cur_y][cur_x]
        grid[cur_y][cur_x] = to_move_val
        grid[cur_y+dny][cur_x+dnx] = prev_val
        cur_x += dnx
        cur_y += dny

def try_move_robot(m_dir, x, y, grid):
    dir = {
        ">": (1, 0),
        "<": (-1, 0),
        "^": (0, -1),
        "v": (0, 1)
    }
    dx, dy = dir[m_dir]
    push_robot_in_direction(x, y, dx, dy, grid)

def print_grid(grid):
    for l in grid:
        for c in l:
            print(c, end="")
        print()
    print()


def score_grid(grid):
    score = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "O":
                score += x + y * 100
    return score


def part1(lines):
    grid, moves = extract_grid_and_moves(lines)
    #print_grid(grid)

    for m in moves:
        #print(f"Move {m}")
        x, y = find_robot_position(grid)
        try_move_robot(m, x, y, grid)
        #print_grid(grid)
    #print_grid(grid)

    return score_grid(grid)

def elarge_width_grid(grid):
    new_grid = []
    replacements = {
        "#": "##",
        ".": "..",
        "O": "[]",
        "@": "@.",
    }
    for y in range(len(grid)):
        row = []
        for x in range(len(grid[y])):
            new = replacements[grid[y][x]]
            row += [new[0], new[1]]
        new_grid.append(row)

    return new_grid


def is_position_movable(x, y, dx, dy, grid, is_call_from_inside=False):
    if dx==0 and grid[y][x] == "@":
        can_move, to_move = is_position_movable(x+dx, y+dy, dx, dy, grid)
        return can_move, [(x,y)] + to_move
    if dx==0 and grid[y][x] == "[":
        u_x = x+dx
        u_y = y+dy
        under = grid[u_y][u_x]
        to_move = [(x,y)]
        if under == ".":
            under_is_free = True
        elif under == "#":
            under_is_free = False
        else:
            # check under
            under_is_free, u_to_move = is_position_movable(u_x, u_y, dx, dy, grid)
            to_move += u_to_move

        if is_call_from_inside:
            return under_is_free, to_move
        r_x = x+1
        r_y = y
        right_is_movable, r_to_move = is_position_movable(r_x, r_y, dx, dy, grid, is_call_from_inside=True)
        to_move += r_to_move

        return under_is_free and right_is_movable, to_move
    elif dx==0 and grid[y][x] == "]":
        u_x = x+dx
        u_y = y+dy
        under = grid[u_y][u_x]
        to_move = [(x,y)]
        if under == ".":
            under_is_free = True
        elif under == "#":
            under_is_free = False
        else:
            # check under
            under_is_free, u_to_move = is_position_movable(u_x, u_y, dx, dy, grid)
            to_move += u_to_move

        if is_call_from_inside:
            return under_is_free, to_move
        l_x = x-1
        l_y = y
        left_is_movable, l_to_move = is_position_movable(l_x, l_y, dx, dy, grid, is_call_from_inside=True)
        to_move += l_to_move

        return under_is_free and left_is_movable, to_move
    else:
        to_move = []
        while y >= 0 and x >= 0 and y < len(grid) and x < len(grid[y]) and grid[y][x] != "#":
            if grid[y][x] in ["."]:
                return True, to_move
            to_move += [(x,y)]
            x += dx
            y += dy
        return False, []


def remove_duplicates(array):
    return list(set(array))

def push_robot_in_direction2(x, y, dx, dy, grid):

    can_move, to_move = is_position_movable(x, y, dx, dy, grid)
    to_move = remove_duplicates(to_move)
    if can_move:
        if dx != 0:
            to_move.sort(key=lambda x: x[0], reverse=dx == 1)
        else:
            to_move.sort(key=lambda y: y[1], reverse=dy == 1)
        for (xx, yy) in to_move:
            to_move_val = grid[yy][xx]
            new_move_val = grid[yy+dy][xx+dx]
            grid[yy][xx] = new_move_val
            grid[yy+dy][xx+dx] = to_move_val


def try_move_robot2(m_dir, x, y, grid):
    dir = {
        ">": (1, 0),
        "<": (-1, 0),
        "^": (0, -1),
        "v": (0, 1)
    }
    dx, dy = dir[m_dir]
    push_robot_in_direction2(x, y, dx, dy, grid)


def score_grid2(grid):
    score = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "[":
                score += x + y * 100
    return score

def detect_malformed_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in ["[", "]"]:
                if grid[y][x] == "[":
                    if grid[y][x+1] != "]":
                        return True
                if grid[y][x] == "]":
                    if grid[y][x-1] != "[":
                        return True
    return False

def deep_copy_grid(grid):
    new_grid = []
    for y in range(len(grid)):
        new_grid.append(grid[y].copy())
    return new_grid

def part2(lines):
    grid, moves = extract_grid_and_moves(lines)
    new_grid = elarge_width_grid(grid)
    #print_grid(new_grid)

    i=0
    for m in moves:
        #print(f"About to move {m}")
        #print_grid(new_grid)

        x, y = find_robot_position(new_grid)
        try_move_robot2(m, x, y, new_grid)
        if detect_malformed_grid(new_grid):
            print(f"Malformed grid after move {i}")
            print_grid(new_grid)
            return -1
        i += 1
        #print_grid(new_grid)

    #print_grid(new_grid)
    return score_grid2(new_grid)


if __name__ == '__main__':

    part = 1
    expectedSampleResult = 2028

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2024, part, result)
        print(f"Part {part} result posted !")
