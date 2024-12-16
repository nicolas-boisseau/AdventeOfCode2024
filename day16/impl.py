import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines
from day16.custom_astar import CustomAStar

download_input_if_not_exists(2024)

def get_last_move_at(x, y, path):
    for i in range(len(path)-1, 0, -1):
        s = path[i].split(",")
        if int(s[0]) == x and int(s[1]) == y:
            return s[2]
    return None

def print_path(lines, path):
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            lastMove = get_last_move_at(x, y, path)
            if lastMove is not None:
                print(lastMove, end="")
            else:
                print(c, end="")
        print()
    print(flush=True)


def part1(lines):
    nodes, e, s = extract_nodes_and_e_s(lines)

    astar = CustomAStar(nodes, use_adminissible_heuristic=False)

    start = f"{s},>"
    possibles_ends = [f"{e},^", f"{e},>", f"{e},v", f"{e},<"]
    possibles_scores = []
    for end in possibles_ends:
        path = list(astar.astar(start, end))
        possibles_scores += [score_path(nodes, path)]

    #print_path(lines, path)

    #print(path)

    return min(possibles_scores)


def extract_nodes_and_e_s(lines):
    nodes = {}
    dir = ["^", ">", "v", "<"]
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

                # can turn for cost 1000
                next_dir = dir[(dir.index(d_s) + 1) % 4]
                prev_dir = dir[(dir.index(d_s) - 1) % 4]
                nodes[node_key].append((f"{x},{y},{next_dir}", 1000))
                nodes[node_key].append((f"{x},{y},{prev_dir}", 1000))

                # can go forward for cost 1
                if d_s == "^" and y > 0 and lines[y - 1][x] != "#":
                    nodes[node_key].append((f"{x},{y - 1},{d_s}", 1))
                elif d_s == ">" and x < len(lines[y]) - 1 and lines[y][x + 1] != "#":
                    nodes[node_key].append((f"{x + 1},{y},{d_s}", 1))
                elif d_s == "v" and y < len(lines) - 1 and lines[y + 1][x] != "#":
                    nodes[node_key].append((f"{x},{y + 1},{d_s}", 1))
                elif d_s == "<" and x > 0 and lines[y][x - 1] != "#":
                    nodes[node_key].append((f"{x - 1},{y},{d_s}", 1))
    return nodes, e, s


def score_path(nodes, path):
    score = 0
    for i in range(len(path) - 1):
        next = nodes[path[i]]
        for n in next:
            if n[0] == path[i + 1]:
                score += n[1]
                break
    return score

def part2(lines):
    return 4


if __name__ == '__main__':

    part = 1
    expectedSampleResult = 7036

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2024, part, result)
        print(f"Part {part} result posted !")
