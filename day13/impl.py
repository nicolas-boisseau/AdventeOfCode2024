import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def solve(a1, b1, c1, a2, b2, c2):
    # Calculer le déterminant
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None  # Pas de solution unique

    # Utiliser la méthode d'élimination pour trouver x et y
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant

    return x, y

def extract(lines):
    i=0
    while i < len(lines):
        a = capture(r"Button A: X\+([0-9]+), Y\+([0-9]+)", lines[i])
        a_x, a_y = a[0], a[1]
        b = capture(r"Button B: X\+([0-9]+), Y\+([0-9]+)", lines[i+1])
        b_x, b_y = b[0], b[1]
        p = capture(r"Prize: X\=([0-9]+), Y\=([0-9]+)",lines[i+2])
        p_x, p_y = p[0], p[1]
        yield (int(a_x), int(a_y), int(b_x), int(b_y), int(p_x), int(p_y))
        i += 4

def part1(lines):
    nb_tokens = 0
    for a_x, a_y, b_x, b_y, p_x, p_y in extract(lines):
        print(a_x, a_y, b_x, b_y, p_x, p_y)

        sol = solve(a_x, b_x, p_x, a_y, b_y, p_y)
        if sol is None or (not sol[0].is_integer() or not sol[1].is_integer()):
            print("No solution")
        else:
            print(sol)
            nb_tokens += sol[0]*3 + sol[1]*1


    return nb_tokens

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
