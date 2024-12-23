import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

class Computer:
    def __init__(self, name):
        self.name = name
        self.connected = set()

    def connect(self, other, dont_callback=False):
        self.connected.add(other)
        if not dont_callback:
            other.connect(self, dont_callback=True)

    def __str__(self):
        return self.name

def sort_alphabetically(l):
    return sorted(l, key=lambda x: x.split("-")[0])

def extract_computers(lines):
    computers = {}
    for line in lines:
        connections = line.split("-")
        if connections[0] not in computers:
            c0 = Computer(connections[0])
            computers[connections[0]] = c0
        else:
            c0 = computers[connections[0]]
        if connections[1] not in computers:
            c1 = Computer(connections[1])
            computers[connections[1]] = c1
        else:
            c1 = computers[connections[1]]

        c0.connect(c1)
    return computers

def part1(lines):
    computers = extract_computers(lines)

    output = set()
    for c in computers:
        c1 = computers[c]
        for c2 in c1.connected:
            for c3 in c2.connected:
                if c3 in c1.connected and c2 in c3.connected:
                    if c1.name[0] == "t" or c2.name[0] == "t" or c3.name[0] == "t":
                        res = sort_alphabetically((c1.name, c2.name, c3.name))
                        output.add(res[0] + "-" + res[1] + "-" + res[2])

    return len(output)

def dfs(computer):
    path = set()
    remaining = [computer]
    visited = set()
    while len(remaining) > 0:
        current = remaining.pop(0)
        if current not in visited:
            visited.add(current)
            path.add(current)
            for c in current.connected:
                if c not in visited and all([c in p.connected for p in path]):
                    remaining.append(c)
                    path.add(c)
    return path

def part2(lines):
    computers = extract_computers(lines)

    max_key = ""
    max_value = 0
    for c in computers:
        path = dfs(computers[c])
        npath = sort_alphabetically([p.name for p in path])

        if len(path) > max_value:
            max_key = ",".join(npath)
            max_value = len(path)

    print(max_key)

    return max_key


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
