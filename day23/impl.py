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

    # def __str__(self):
    #     connecteds = ",".join([c.name for c in self.connected])
    #     return self.name + " -> " + connecteds

def sort_alphabetically(l):
    return sorted(l, key=lambda x: x.split("-")[0])


def part1(lines):
    computers = extract_computers(lines)

    # for c in computers:
    #     print(computers[c])

    output = set()
    for c in computers:
        c1 = computers[c]
        for c2 in c1.connected:
            for c3 in c2.connected:
                if c3 in c1.connected and c2 in c3.connected:
                    if c1.name[0] == "t" or c2.name[0] == "t" or c3.name[0] == "t":
                        res = sort_alphabetically((c1.name, c2.name, c3.name))
                        output.add(res[0] + "-" + res[1] + "-" + res[2])

    # for o in output:
    #     print(o)



    return len(output)


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


# def height(computer):
#     remaining = [computer]
#     visited = set()
#     while len(remaining) > 0:
#         current = remaining.pop()
#         visited.add(current)
#         for c in current.connected:
#             if c not in visited:
#                 connected = 0
#                 for c2 in c.connected:
#                     for c3 in c2.connected:
#                         if c3 in c.connected and c2 in c3.connected:
#                             connected += 1
#                 if connected > 2:
#                     remaining.append(c)
#     return len(visited)

def dfs(computer):
    path = []
    remaining = [computer]
    visited = set()
    while len(remaining) > 0:
        current = remaining.pop(0)
        if current not in visited:
            visited.add(current)
            path.append(current)
            for c in current.connected:
                if c not in visited:
                    remaining.append(c)
    return path

def part2(lines):
    computers = extract_computers(lines)

    for c in computers:
        print(f"dfs({c}) = {len(dfs(computers[c]))}")

    # output = {}
    # for c in computers:
    #     output[c] = height(computers[c])
    #     print(f"height({c}) : {height(computers[c])}")

    # keep only min height
    # min_height = min(output.values())
    # final = []
    # for o in output:
    #     if output[o] == min_height:
    #         final += [o]

    #print(output.keys())


    # for triplet in output:
    #     root,left,right = triplet
    #     root = Node(root)
    #     root.left = Node(left)
    #     root.right = Node(right)


    # for o in output:
    #     print(o)

    #return ",".join(sort_alphabetically(final))


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
