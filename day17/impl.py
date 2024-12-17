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

def part1(lines):
    regA, regB, regC, prog_entries = extract_reg_and_prog(lines)
    instr_pointer = 0

    while instr_pointer < len(prog_entries):

        instr = prog_entries[instr_pointer]
        if instr == 0: # adv - division regA / combo^2



        instr_pointer += 2




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
