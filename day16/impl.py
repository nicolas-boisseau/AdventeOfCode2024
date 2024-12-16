import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines
from day16.custom_astar import CustomAStar

download_input_if_not_exists(2024)

def print_path(lines, path):
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if f"{x},{y}" in path:
                print("O", end="")
            else:
                print(c, end="")
        print()
    print(flush=True)


def part1(lines):
    nodes = {}
    dir = ["^", ">", "v", "<"]
    cost = {
        "^^": 1,
        ">>": 1,
        "vv": 1,
        "<<": 1,
        "^>": 1001,
        ">v": 1001,
        "v<": 1001,
        "<^": 1001,
        "^v": 2001,
        "v^": 2001,
        "<>": 2001,
        "><": 2001,
        "^<": 3001,
        "<v": 3001,
        "v>": 3001,
        ">^": 3001
    }
    s, e = None, None
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            node_key = f"{x},{y}"
            if lines[y][x] == "S":
                s = node_key
            elif lines[y][x] == "E":
                e = node_key
            for d_s in dir:
                node_key = f"{x},{y},{d_s}"
                nodes[node_key] = []
                if x > 0 and line[x-1] != "#":
                    for d_d in dir:
                        left_key = f"{x-1},{y},{d_d}"
                        nodes[node_key].append((left_key, cost[f"{d_s}{d_d}"]))
                if y > 0 and lines[y-1][x] != "#":
                    for d_d in dir:
                        up_key = f"{x},{y-1},{d_d}"
                        nodes[node_key].append((up_key, cost[f"{d_s}{d_d}"]))
                if x < len(line)-1 and line[x+1] != "#":
                    for d_d in dir:
                        right_key = f"{x+1},{y},{d_d}"
                        nodes[node_key].append((right_key, cost[f"{d_s}{d_d}"]))
                if y < len(lines)-1 and lines[y+1][x] != "#":
                    for d_d in dir:
                        down_key = f"{x},{y+1},{d_d}"
                        nodes[node_key].append((down_key, cost[f"{d_s}{d_d}"]))

    astar = CustomAStar(nodes, use_adminissible_heuristic=False)

    start = f"{s},>"
    end = f"{e},^"
    path = list(astar.astar(start, end))

    #print_path(lines, path)

    #print(path)

    return len(path) - 1



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
