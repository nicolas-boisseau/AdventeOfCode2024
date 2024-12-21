import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
def push_dir_keypad(target_button, initial_button_pos):
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
    return go_to[target_button][initial_button_pos] + "A"

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
    return go_to[target_button][initial_button_pos] + "A"


def get_numeric_part(code):
    return int("".join([c for c in code if c.isdigit()]))

def all_combinations(str):
    # "abc" -> ["abc", "acb", "bac", "bca", "cab", "cba"]
    if len(str) == 1:
        return [str]
    if len(str) == 2:
        return [str, str[::-1]]
    return [str[0] + s for s in all_combinations(str[1:])] + [str[0] + s for s in all_combinations(str[1:])[::-1]]

def part1(lines):

    for code in lines[:1]:
        pos = "A"
        first_robot_all_moves = ""
        for c in code:
            needed_moves = push_numeric_keypad(c, pos)
            print(f"From {pos} to {c} with {needed_moves}")
            first_robot_all_moves += needed_moves
            pos = c
        print("first robot:", first_robot_all_moves)

        #print("second robot:")
        pos2 = "A"
        second_robot_all_moves = ""
        for c2 in str(first_robot_all_moves):
            needed_moves = push_dir_keypad(c2, pos2)
            #print(f"From {pos2} to {c2} with {needed_moves}")
            second_robot_all_moves += needed_moves
            pos2 = c2
        print("second robot:", second_robot_all_moves)

        #print("third robot:")
        pos3 = "A"
        third_robot_all_moves = ""
        for c3 in str(second_robot_all_moves):
            needed_moves = push_dir_keypad(c3, pos3)
            #print(f"From {pos3} to {c3} with {needed_moves}")

            third_robot_all_moves += needed_moves
            pos3 = c3
        print("third robot:", third_robot_all_moves)

        n = get_numeric_part(code)
        print(f"len = {len(third_robot_all_moves)} * {n} = {len(third_robot_all_moves) * n}")

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
