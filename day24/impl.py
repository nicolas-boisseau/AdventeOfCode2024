import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def extract_values_and_wires(lines):
    values = {}
    wires = []
    i = 0
    while lines[i] != "":
        s = lines[i].split(": ")
        values[s[0]] = int(s[1])
        i += 1
    i += 1  # skip empty line
    while i < len(lines):
        s = lines[i].split(" ")
        wires.append((s[0], s[1], s[2], s[4]))
        i += 1
    return values, wires

def part1(lines):
    values, wires = extract_values_and_wires(lines)

    values_to_wait = [w[3] for w in wires if w[3][0] == "z"]

    #print(values)
    #print(wires)

    while not all([v_wait in values.keys() for v_wait in values_to_wait]):
        for w in wires:
            if w[0] in values and w[2] in values.keys():
                if w[1] == "AND":
                    values[w[3]] = values[w[0]] & values[w[2]]
                elif w[1] == "OR":
                    values[w[3]] = values[w[0]] | values[w[2]]
                elif w[1] == "XOR":
                    values[w[3]] = values[w[0]] ^ values[w[2]]

    print("END !")

    z_keys = [k for k in values.keys() if k[0] == "z"]

    z_keys.sort(reverse=True)

    binary = "".join([str(values[k]) for k in z_keys])

    print("binary result = ", binary)

    return int(binary, 2)

def part2(lines):
    return part1(lines)


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
