import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines
from day18.custom_astar import CustomAStar

download_input_if_not_exists(2024)

def print_grid(g):
    for l in g:
        print("".join(l))

def build_grid(lines, w, h, max_steps):
    g = [["." for _ in range(w+1)] for _ in range(h+1)]
    for l in lines[:max_steps]:
        x, y = l.split(",")
        g[int(y)][int(x)] = "#"
    return g

def part1(lines, w, h, max_steps):
    g = build_grid(lines, w, h, max_steps)
    #print_grid(g)

    dir = [(0,1), (0,-1), (1,0), (-1,0)]

    nodes = {}
    for y in range(len(g)):
        for x in range(len(g[y])):
            node_key = f"{x},{y}"
            nodes[node_key] = []

            for d in dir:
                dx, dy = d
                if x + dx >= 0 and x + dx < len(g[y]) and y + dy >= 0 and y + dy < len(g):
                    if g[y+dy][x+dx] != "#":
                        nodes[node_key].append((f"{x+dx},{y+dy}", 1))

    astar = CustomAStar(nodes)

    start = "0,0"
    end = f"{w},{h}"

    res = astar.astar(start, end)
    if res is None:
        return None
    path = list(res)

    return len(path) - 1



def part2(lines, w, h, start_at_step):

     i = start_at_step
     res = part1(lines, w, h, i)
     i+=1
     while res is not None:
        res = part1(lines, w, h, i)
        i += 1

     return lines[i-2]


if __name__ == '__main__':

    part = 1
    expectedSampleResult = 22

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2024, part, result)
        print(f"Part {part} result posted !")
