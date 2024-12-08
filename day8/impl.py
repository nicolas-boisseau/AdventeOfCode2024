import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)


def print_map(lines):
    for l in lines:
        print(l)

def score(lines):
    score = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] in ["#"]:
                score += 1
    return score

def part1(lines):
    antennas = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] != ".":
                if lines[y][x] not in antennas:
                    antennas[lines[y][x]] = []
                antennas[lines[y][x]].append((y, x))

    for type, positions in antennas.items():
        print(f"{type}: {positions}")
        for p in positions:
            for other_p in positions:
                if p != other_p:
                    print(f"  {p} -> {other_p} : {abs(p[0] - other_p[0]) + abs(p[1] - other_p[1])}")
                    print(f" dist_y: {abs(p[0] - other_p[0])}, dist_x: {abs(p[1] - other_p[1])}")
                    a_y = p[0] + p[0] - other_p[0]
                    a_x = p[1] + p[1] - other_p[1]
                    if a_y < len(lines) and a_y >= 0 and a_x < len(lines[a_y]) and a_x >= 0:
                        lines[a_y] = lines[a_y][:a_x] + "#" + lines[a_y][a_x + 1:]
                    print_map(lines)

    return score(lines)

def part2(lines):
    return 4


if __name__ == '__main__':

    part = 1
    expectedSampleResult = 14

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2024, part, result)
        print(f"Part {part} result posted !")
