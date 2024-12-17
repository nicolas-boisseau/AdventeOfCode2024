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


def try_to_reach_end(e, nodes, start):
    astar = CustomAStar(nodes, use_adminissible_heuristic=False)

    possibles_ends = [f"{e},^", f"{e},>", f"{e},v", f"{e},<"]
    possibles_scores = []
    best_path = None
    best_score = 9999999999999999999999999999999
    for end in possibles_ends:
        path = list(astar.astar(start, end))
        score = score_path(nodes, path)
        if score < best_score:
            best_score = score
            best_path = path
    return best_path, best_score

def part2(lines):
    nodes, end_pos, start_pos = extract_nodes_and_e_s(lines)
    mdir = {
        "^": (0,-1),
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0)
    }
    alldir = ["^", ">", "v", "<"]

    s_x,s_y = start_pos.split(",")
    start = f"{start_pos},>"
    best_path, best_score = try_to_reach_end(end_pos, nodes, start)

    best_nodes = {}
    for n in best_path:
        n_x,n_y,n_d = n.split(",")
        best_nodes[f"{n_x},{n_y}"] = n_d

    def print_best_nodes():
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if f"{x},{y}" in best_nodes:
                    print("O", end="")
                else:
                    print(lines[y][x], end="")
            print()

    remaining = best_path.copy()
    while len(remaining) > 0:
        next_best = remaining.pop(0)
        n_x,n_y,n_d = next_best.split(",")
        next_variations = [f"{n_x},{n_y},{d}" for d in ["^", ">", "v", "<"] if d != n_d]
        next_variations = []
        dir = mdir[n_d]
        if lines[int(n_y)+dir[0]][int(n_x)+dir[1]] == ".": # can move forward
            next_variations.append((f"{int(n_x)+dir[1]},{int(n_y)+dir[0]},{n_d}", 1))
        else:
            next_dir = alldir[(alldir.index(n_d) + 1) % 4]
            next_dir_v = mdir[next_dir]
            prev_dir = alldir[(alldir.index(n_d) - 1) % 4]
            prev_dir_v = mdir[prev_dir]
            if lines[int(n_y) + next_dir_v[0]][int(n_x) + next_dir_v[1]] == ".":  # turn right
                next_variations.append((f"{int(n_x) + next_dir_v[1]},{int(n_y) + next_dir_v[0]},{next_dir}", 1000))
            if lines[int(n_y) + prev_dir_v[0]][int(n_x) + prev_dir_v[1]] == ".":  # turn left
                next_variations.append((f"{int(n_x) + prev_dir_v[1]},{int(n_y) + prev_dir_v[0]},{prev_dir}", 1000))

        _, best_score = try_to_reach_end(end_pos, nodes, next_best)
        for (v,d) in next_variations:
            sub_path, score = try_to_reach_end(end_pos, nodes, v)
            if score <= best_score:
                for n in sub_path:
                    n_x, n_y, n_d = n.split(",")
                    best_nodes[f"{n_x},{n_y}"] = n_d

        #print_best_nodes()
    print_best_nodes()

    # print_path(lines, path)

    # print(path)



    return len(best_nodes)




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
