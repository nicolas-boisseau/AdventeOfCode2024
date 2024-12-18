import math
import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def extract_reg_and_prog(lines):
    regA = int(lines[0].split(": ")[1])
    regB = int(lines[1].split(": ")[1])
    regC = int(lines[2].split(": ")[1])

    prog_raw = lines[4].split(": ")[1]
    prog_entries = [int(i) for i in prog_raw.split(",")]

    return regA, regB, regC, prog_entries

def get_combo(literal, regA, regB, regC):
    if literal in [0, 1, 2, 3]:
        return literal
    elif literal == 4:
        return regA
    elif literal == 5:
        return regB
    elif literal == 6:
        return regC
    else:
        raise("NOT VALID PROGRAM !!")

def part1(lines):
    regA, regB, regC, prog_entries = extract_reg_and_prog(lines)

    output = execute(prog_entries, regA, regB, regC)

    print(output)
    output_str = ",".join([str(i) for i in output])
    print(output_str)
    return output_str


def execute(prog_entries, regA, regB, regC):
    instr_pointer = 0
    output = []
    while instr_pointer < len(prog_entries):

        instr = prog_entries[instr_pointer]
        literal = prog_entries[instr_pointer + 1]

        if instr == 0:  # adv - division regA / combo^2
            numerator = regA
            combo = get_combo(literal, regA, regB, regC)
            denominator = math.pow(2, combo)
            regA = int(numerator / denominator)
        elif instr == 1:  # bxl bitwise XOR regB and literal
            regB = regB ^ literal
        elif instr == 2:  # bst combo%8
            combo = get_combo(literal, regA, regB, regC)
            regB = combo % 8
        elif instr == 3:  # jnz nothing if regA == 0 else jump to literal
            if regA != 0:
                instr_pointer = prog_entries[instr_pointer + 1]
                continue
        elif instr == 4:  # bxc XOR regB and regC => regB
            regB = regB ^ regC
        elif instr == 5:  # out -
            combo = get_combo(literal, regA, regB, regC)
            o = combo % 8
            output.append(o)
        elif instr == 6:  # bdv - like adv but store in regB
            numerator = regA
            combo = get_combo(literal, regA, regB, regC)
            denominator = math.pow(2, combo)
            regB = int(numerator / denominator)
        elif instr == 7:  # cdv - like adv but store in regC
            numerator = regA
            combo = get_combo(literal, regA, regB, regC)
            denominator = math.pow(2, combo)
            regC = int(numerator / denominator)

        instr_pointer += 2
    return output

def reverse(prog_entries, aggr=0, index=-99):
    if index == -99:
        # start with last output
        index = len(prog_entries) - 1

    if index < 0:
        return aggr

    current_entry = prog_entries[index]

    for i in range(8):
        to_test = aggr * 8 + i

        out = execute(prog_entries[:-2], to_test, 0, 0)[0]

        if out == current_entry:
            next = reverse(prog_entries, to_test, index-1)
            if next is not None:
                return next

    return None

def part2(lines):
    _, _, _, prog_entries = extract_reg_and_prog(lines)

    regA = reverse(prog_entries)

    if execute(prog_entries, regA, 0, 0) == prog_entries:
        print("FOUND")
    return regA


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
