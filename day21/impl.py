import itertools
import os.path
from functools import lru_cache

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines
from day21.custom_astar import CustomAStar

download_input_if_not_exists(2024)

def cost_to_move(from_symbol, to_symbol):
    dist_between_symbol = {
        "A": {
            ">": 1,
            "v": 2,
            "<": 3,
            "^": 1
        },
        ">": {
            "A": 1,
            "^": 2,
            "v": 1,
            "<": 2
        },
        "^": {
            "A": 1,
            ">": 2,
            "v": 1,
            "<": 2
        },
        "v": {
            "A": 2,
            ">": 1,
            "^": 1,
            "<": 1
        },
        "<": {
            "A": 3,
            ">": 2,
            "^": 2,
            "v": 1
        }
    }

    dist_from = dist_between_symbol[from_symbol]
    if to_symbol in dist_from:
        return dist_from[to_symbol]
    else:
        return 0

def cost_to_move_on_keypad(sequence):
    if len(sequence) == 1:
        return 0
    cost = 0
    for i in range(len(sequence) - 1):
        cost += cost_to_move(sequence[i], sequence[i+1])

    return cost

def create_numeric_pad_astar_graph():

    to_a = {
        "3": "v",
        "0": ">",
    }
    to_nine = {
        "8": ">",
        "6": "^",
    }
    to_eight = {
        "9": "<",
        "7": ">",
        "5": "^",
    }
    to_seven = {
        "8": "<",
        "4": "^",
    }
    to_six = {
        "9": "v",
        "5": ">",
        "3": "^",
    }
    to_five = {
        "8": "v",
        "6": "<",
        "4": ">",
        "2": "^",
    }
    to_four = {
        "7": "v",
        "5": "<",
        "1": "^",
    }
    to_three = {
        "A": "^",
        "6": "v",
        "2": ">",
    }
    to_two = {
        "5": "v",
        "3": "<",
        "1": ">",
        "0": "^",
    }
    to_one = {
        "4": "v",
        "2": "<",
    }
    to_zero = {
        "A": "<",
        "2": "v",
    }
    go_to = {
        "A": to_a,
        "9": to_nine,
        "8": to_eight,
        "7": to_seven,
        "6": to_six,
        "5": to_five,
        "4": to_four,
        "3": to_three,
        "2": to_two,
        "1": to_one,
        "0": to_zero,
    }

    nodes = {}
    for node in ["A", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        nodes[node] = []
        for k in go_to[node].keys():
            nodes[node].append((k, 1))

    return CustomAStar(nodes)

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
def create_keypad_astar_graph():
    dist_between_symbol = {
        "A": {
            ">": 1,
            "^": 1
        },
        ">": {
            "A": 1,
            "v": 1,
        },
        "^": {
            "A": 1,
            "v": 1,
        },
        "v": {
            ">": 1,
            "^": 1,
            "<": 1
        },
        "<": {
            "v": 1
        }
    }

    nodes = {}
    for node in ["A", ">", "^", "v", "<"]:
        nodes[node] = []
        for d in dist_between_symbol[node]:
            nodes[node].append((d, dist_between_symbol[node][d]))

    return CustomAStar(nodes)

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
def push_dir_keypad(target_button, initial_button_pos):
    dist_between_symbol = {
        "A": {
            ">": 1,
            "v": 2,
            "<": 3,
            "^": 1
        },
        ">": {
            "A": 1,
            "^": 2,
            "v": 1,
            "<": 2
        },
        "^": {
            "A": 1,
            ">": 2,
            "v": 1,
            "<": 2
        },
        "v": {
            "A": 2,
            ">": 1,
            "^": 1,
            "<": 1
        },
        "<": {
            "A": 3,
            ">": 2,
            "^": 2,
            "v": 1
        }
    }
    to_a = {
        ">": "^",
        "^": ">",
        "<": ">^>",
        "v": "^>",
    }
    to_up = {
        "A": "<",
        ">": "^<",
        "<": ">^",
        "v": "^",
    }
    to_down = {
        "A": "v<",
        ">": "<",
        "<": ">",
        "^": "v",
    }
    to_left = {
        "A": "v<<",
        "^": "v<",
        ">": "<<",
        "v": "<",
    }
    to_right = {
        "A": "v",
        "^": "v>",
        "<": ">>",
        "v": ">",
    }
    go_to = {
        "A": to_a,
        "^": to_up,
        "v": to_down,
        "<": to_left,
        ">": to_right,
    }


    if target_button == initial_button_pos:
        return "A"

    go_to_code = go_to[target_button][initial_button_pos]

    return optimize(go_to_code + "A", initial_button_pos, target_button, True)

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
def push_numeric_keypad(target_button, initial_button_pos):
    to_a = {
        "9": "vvv",
        "8": ">vv",
        "7": ">>vvv",
        "6": "vv",
        "5": ">vv",
        "4": ">>vv",
        "3": "v",
        "2": "v>",
        "1": ">v>",
        "0": ">",
    }
    to_nine = {
        "A": "^^^",
        "8": ">",
        "7": ">>",
        "6": "^",
        "5": ">^",
        "4": ">>^",
        "3": "^^",
        "2": ">^^",
        "1": ">>^^",
        "0": ">^^^",
    }
    to_eight = {
        "A": "^^^<",
        "9": "<",
        "7": ">",
        "6": "^<",
        "5": "^",
        "4": ">^",
        "3": "^^<",
        "2": "^^",
        "1": ">^^",
        "0": "^^^",
    }
    to_seven = {
        "A": "^^^<<",
        "9": "<<",
        "8": "<",
        "6": "^<<",
        "5": "^<",
        "4": "^",
        "3": "^^<<",
        "2": "^^<",
        "1": "^^",
        "0": "^^^<",
    }
    to_six = {
        "A": "^^",
        "9": "v",
        "8": ">v",
        "7": ">>v",
        "5": ">",
        "4": ">>",
        "3": "^",
        "2": ">^",
        "1": ">>^",
        "0": ">^^",
    }
    to_five = {
        "A": "^^<",
        "9": "<v",
        "8": "v",
        "7": ">v",
        "6": "<",
        "4": ">",
        "3": "^<",
        "2": "^",
        "1": ">^",
        "0": "^^",
    }
    to_four = {
        "A": "^^<<",
        "9": "<<v",
        "8": "<v",
        "7": "v",
        "6": "<<",
        "5": "<",
        "3": "^<<",
        "2": "^<",
        "1": "^",
        "0": "^^<",
    }
    to_three = {
        "A": "^",
        "9": "vv",
        "8": ">vv",
        "7": ">>vv",
        "6": "v",
        "5": ">v",
        "4": ">>v",
        "2": ">",
        "1": ">>",
        "0": "^>",
    }
    to_two = {
        "A": "^<",
        "9": "<vv",
        "8": "vv",
        "7": ">vv",
        "6": "<v",
        "5": "v",
        "4": ">v",
        "3": "<",
        "1": ">",
        "0": "^",
    }
    to_one = {
        "A": "^<<",
        "9": "<<vv",
        "8": "<vv",
        "7": "vv",
        "6": "<<v",
        "5": "<v",
        "4": "v",
        "3": "<<",
        "2": "<",
        "0": "^<",
    }
    to_zero = {
        "A": "<",
        "9": "vvv<",
        "8": "vvv",
        "7": ">vvv",
        "6": "vv<",
        "5": "vv",
        "4": ">vv",
        "3": "<v",
        "2": "v",
        "1": ">v",
    }
    go_to = {
        "A": to_a,
        "9": to_nine,
        "8": to_eight,
        "7": to_seven,
        "6": to_six,
        "5": to_five,
        "4": to_four,
        "3": to_three,
        "2": to_two,
        "1": to_one,
        "0": to_zero,
    }

    if target_button == initial_button_pos:
        return ""

    go_to_code = go_to[target_button][initial_button_pos]

    return optimize(go_to_code + "A", initial_button_pos, target_button, False)

def optimize(code, start, end, is_keypad):
    if code == "":
        return code
    combinations = all_combinations(code[:-1])
    combinations = [c + "A" for c in combinations if is_possible_combinaison(c + "A", start, end, is_keypad)]
    costby_comb = {c: cost_to_move_on_keypad(c) for c in combinations}
    return min(costby_comb, key=costby_comb.get)

def get_numeric_part(code):
    return int("".join([c for c in code if c.isdigit()]))

def all_combinations(s):
    return [''.join(p) for p in itertools.permutations(s)]

def is_possible_combinaison(comb, start, end, is_keypad):
    if is_keypad:
        valid_keypad_moves = {
            ">": ["v", "A"],
            "^": ["v", "A"],
            "v": ["^", ">", "<"],
            "<": ["v"],
            "A": ["^", ">"],
        }
        current = start
        i = 0
        move = comb[i]
        while current != end and move in valid_keypad_moves[current]:
            i += 1
            current = move
            move = comb[i]
        return current == end
    else:

        valid_numeric_moves = {
            "A": [("^","3"), ("<","0")],
            "0": [("^","2"), (">", "A")],
            "1": [(">", "2"), ("^", "4")],
            "2": [("<","1"), (">","3"), ("^","5"), ("v","0")],
            "3": [("<","2"), ("^","6"), ("v", "A")],
            "4": [("v","1"), (">", "5"), ("^","7")],
            "5": [("v","2"), ("<","4"), (">","6"), ("^","8")],
            "6": [("v","3"), ("<","5"), ("^","9")],
            "7": [("v","4"), (">","8")],
            "8": [("v","5"), ("<","7"), (">","9")],
            "9": [("v","6"), ("<","8")],
        }
        current = start
        i = 0
        move = comb[i]
        while current != end and move in [v[0] for v in valid_numeric_moves[current]]:
            i += 1
            next_v = [v for v in valid_numeric_moves[current] if move == v[0]]
            current = next_v[0][1]
            move = comb[i]
        return current == end

keypad_astar = create_keypad_astar_graph()
cache = {}

@lru_cache(maxsize=None)
def compute_astar(start, end):
    if (start,end) in cache.keys():
        return cache[(start,end)]
    p = keypad_astar.astar(start, end)
    cache[(start,end)] = list(p)
    return cache[(start,end)]

def part1(lines, nb_robots=2):
    sub_part_cache = {}
    score = 0
    for code in lines:
        pos = "A"
        first_robot_all_moves = ""
        for c in code:
            needed_moves = push_numeric_keypad(c, pos)
            print(f"From {pos} to {c} with {needed_moves}")
            first_robot_all_moves += needed_moves
            pos = c
        print("first robot:", first_robot_all_moves)

        previous_moves = first_robot_all_moves
        for r in range(nb_robots):
            print(f"robot {r}")

            current_moves = ""
            #for i in range(len(previous_moves)):
            i = 0
            while i < len(previous_moves):
                next_a_index = previous_moves.find("A", i)
                sliding_windows = previous_moves[i:next_a_index+1] if next_a_index != -1 else previous_moves[i:]

                current_sliding_window_moves = compute_sliding_window(tuple(sliding_windows))

                current_moves += current_sliding_window_moves

                i = next_a_index + 1

            sub_part_cache[previous_moves] = current_moves
            previous_moves = current_moves

            n = get_numeric_part(code)
            sub_score = len(previous_moves) * n

            #print(f"robot {r} : {previous_moves}")
            print(f"robot {r} : len = {len(previous_moves)} * {n} = {sub_score}")


        n = get_numeric_part(code)
        sub_score = len(previous_moves) * n
        print(f"len = {len(previous_moves)} * {n} = {sub_score}")

        score += sub_score

    return score

to_robot_moves = {
    "A,>": "v",
    "A,^": "<",
    "^,A": ">",
    "^,v": "v",
    ">,A": "^",
    ">,v": "<",
    "v,>": ">",
    "v,^": "^",
    "v,<": "<",
    "<,v": ">",
}

@lru_cache(maxsize=None)
def compute_sliding_window(sliding_windows):
    current_sliding_window_moves = ""
    for k in range(len(sliding_windows)):
        current = sliding_windows[k]
        prev = sliding_windows[k - 1] if k > 0 else "A"

        path = compute_astar(prev, current)
        # path = keypad_astar.astar(prev, current)

        j = 1
        buttons = [p for p in path]
        robots_moves = ""
        while j < len(buttons):
            robots_moves += to_robot_moves[f"{buttons[j - 1]},{buttons[j]}"]
            j += 1

        current_sliding_window_moves += robots_moves + "A"
    return current_sliding_window_moves


def part2(lines):
    return part1(lines, 25-1)


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
