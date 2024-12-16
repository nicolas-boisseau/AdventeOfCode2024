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
    s, e = None, None
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            node_key = f"{x},{y}"
            if lines[y][x] == "S":
                s = node_key
            elif lines[y][x] == "E":
                e = node_key
            nodes[node_key] = []
            if x > 0 and line[x-1] != "#":
                nodes[node_key].append((f"{x-1},{y}", 1))
            if y > 0 and lines[y-1][x] != "#":
                nodes[node_key].append((f"{x},{y-1}", 1))
            if x < len(line)-1 and line[x+1] != "#":
                nodes[node_key].append((f"{x+1},{y}", 1))
            if y < len(lines)-1 and lines[y+1][x] != "#":
                nodes[node_key].append((f"{x},{y+1}", 1))

    astar = CustomAStar(nodes, use_adminissible_heuristic=True)

    start = s
    end = e
    path = list(astar.astar(start, end))

    print_path(lines, path)

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
