import os.path

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
    moves = []
    for c in lines[i+1]:
        moves.append(c)

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
    return False

def push_robot_in_direction(x, y, dx, dy, grid):
    _, (nx, ny) = is_place_free_in_direction(x, y, dx, dy, grid)
    cur_x, cur_y = x, y
    while not (cur_x, cur_y) == (nx, ny):
        prev_val = grid[cur_y][cur_x]
        grid[cur_y][cur_x] = "."
        grid[cur_y+dy][cur_x+dx] = prev_val
        cur_x += dx
        cur_y += dy

def try_move_robot(m_dir, x, y, grid):
    dir = {
        ">": (1, 0),
        "<": (-1, 0),
        "^": (0, -1),
        "v": (0, 1)
    }
    reversed_dir = {
        ">": "<",
        "<": ">",
        "^": "v",
        "v": "^"
    }
    dx, dy = dir[m_dir]

    # # get all in the line before "#"
    # cur_x, cur_y = x, y
    # to_move = []
    # while grid[cur_y][cur_x] != "#":
    #     if grid[cur_y][cur_x] in ["@", "O"]:
    #         to_move += [(cur_x, cur_y)]
    #     cur_x += dx
    #     cur_y += dy
    # wall_x, wall_y = (cur_x, cur_y)

    cur_x, cur_y = x, y
    while is_place_free_in_direction(cur_x, cur_y, dx, dy, grid):
        push_robot_in_direction(cur_x, cur_y, dx, dy, grid)
        cur_x += dx
        cur_y += dy

    # move and all others
    # to_move.reverse()
    # back_dir = reversed_dir[m_dir]
    # bdx, bdy = dir[back_dir]
    # cur_x, cur_y = wall_x+bdx, wall_y+bdy
    # for x, y in to_move:
    #     if cur_y == y and cur_x == x:
    #         break
    #     grid[cur_x][cur_y] = grid[x][y]
    #     grid[x][y] = "."
    #     cur_x += bdx
    #     cur_y += bdy


def print_grid(grid):
    for l in grid:
        for c in l:
            print(c, end="")
        print()
    print()





def part1(lines):
    grid, moves = extract_grid_and_moves(lines)
    print_grid(grid)

    for m in moves:
        print(f"Move {m}")
        x, y = find_robot_position(grid)
        try_move_robot(m, x, y, grid)
        print_grid(grid)
    print_grid(grid)
    return 4

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
