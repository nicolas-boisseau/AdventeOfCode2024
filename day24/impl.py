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

    run_machine(values, wires)

    print("END !")

    z_keys = [k for k in values.keys() if k[0] == "z"]
    z_keys.sort(reverse=True)
    binary = "".join([str(values[k]) for k in z_keys])
    print("z values : ", z_keys)
    print("z binary = ", binary)

    return int(binary, 2)


def run_machine(values, wires):
    values_to_wait = [w[3] for w in wires if w[3][0] == "z"]
    # print(values)
    # print(wires)
    while not all([v_wait in values.keys() for v_wait in values_to_wait]):
        for w in wires:
            if w[0] in values and w[2] in values.keys():
                if w[1] == "AND":
                    values[w[3]] = values[w[0]] & values[w[2]]
                elif w[1] == "OR":
                    values[w[3]] = values[w[0]] | values[w[2]]
                elif w[1] == "XOR":
                    values[w[3]] = values[w[0]] ^ values[w[2]]


def part2(lines):
    values, wires = extract_values_and_wires(lines)

    x_keys = [k for k in values.keys() if k[0] == "x"]
    x_keys.sort(reverse=True)

    binary = "".join([str(values[k]) for k in x_keys])
    print("x values : ", x_keys)
    print("x binary =  ", binary)

    y_keys = [k for k in values.keys() if k[0] == "y"]
    y_keys.sort(reverse=True)

    binary = "".join([str(values[k]) for k in y_keys])
    print("y values : ", y_keys)
    print("y binary =  ", binary)

    # ACT
    run_machine(values, wires)

    # Compute expected z_values
    expected_z_values = {}
    for i in range(len(x_keys)):
        index = str(i).rjust(2, "0")
        x = values[f"x{index}"]
        y = values[f"y{index}"]
        expected_z_values[f"z{index}"] = x & y

    print("EXPECTED VALUES : ")
    expected_z_keys = [k for k in expected_z_values.keys()]
    expected_z_keys.sort(reverse=True)
    binary = "".join([str(expected_z_values[k]) for k in expected_z_keys])
    print("z values : ", expected_z_values)
    print("z binary = ", binary)

    print("REAL VALUES : ")
    z_keys = [k for k in values.keys() if k[0] == "z"]
    z_keys.sort(reverse=True)
    binary = "".join([str(values[k]) for k in z_keys])
    print("z values : ", z_keys)
    print("z binary = ", binary)

    return 0



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
