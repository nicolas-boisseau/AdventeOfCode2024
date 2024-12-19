import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def extract_patterns_and_designs(lines):
    patterns = lines[0].split(", ")
    designs = []
    for i in range(2, len(lines)):
        designs.append(lines[i])
    return patterns, designs

# def create_pattern_graph(patterns):
#     g = {}
#     for pattern in patterns:
#         for next_pattern in patterns:
#             if pattern not in g.keys():
#                 g[pattern] = []
#             g[pattern].append(next_pattern)
#     return g

def get_possible_next_patterns(design, patterns):
    possible_next_patterns = []
    for pattern in patterns:
        if design.startswith(pattern):
            possible_next_patterns.append(pattern)
    return possible_next_patterns

def try_design(design, patterns):
    if len(design) == 0:
        return True
    possible_next_patterns = get_possible_next_patterns(design, patterns)
    for next_pattern in possible_next_patterns:
        if try_design(design[len(next_pattern):], patterns):
            return True
    return False

def try_design_rec(design, patterns, nb=0):
    if len(design) == 0:
        return nb+1
    possible_next_patterns = get_possible_next_patterns(design, patterns)
    for next_pattern in possible_next_patterns:
        nb = try_design_rec(design[len(next_pattern):], patterns, nb)

    return nb


def part1(lines):
    patterns, designs = extract_patterns_and_designs(lines)

    #g = create_pattern_graph(patterns)

    nb_ok = 0
    for d in designs:
        ok= try_design(d, patterns)
        print(f"{d} : {ok}")
        if ok:
            nb_ok += 1

    return nb_ok

def part2(lines):
    patterns, designs = extract_patterns_and_designs(lines)

    nb_ok = 0
    for d in designs:
        nb = try_design_rec(d, patterns)
        print(f"{d} : {nb > 0} ({nb})")
        if nb > 0:
            nb_ok += nb

    return nb_ok


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
