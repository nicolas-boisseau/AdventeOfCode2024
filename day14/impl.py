import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def part1(lines, grid_size=(11, 7)):
    # p=0,4 v=3,-3
    vectors = []
    for line in lines:
        cap = capture("p=([0-9-]+),([0-9-]+) v=([0-9-]+),([0-9-]+)", line)
        p = (int(cap[0]), int(cap[1]))
        v = (int(cap[2]), int(cap[3]))
        vectors.append((p, v))

    # move 100
    for i in range(1000):
        for j in range(len(vectors)):
            p, v = vectors[j]
            new_p_x = (p[0] + v[0]) % grid_size[0]
            new_p_y = (p[1] + v[1]) % grid_size[1]
            vectors[j] = ((new_p_x, new_p_y), v)
            print(i)
            print_grid(grid_size, vectors)

    # print
    #print_grid(grid_size, vectors)

    quadrants = (0, 0, 0, 0)
    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            nb_robots = len([v[0] for v in vectors if v[0] == (x, y)])
            if x < grid_size[0] // 2 and y < grid_size[1] // 2:
                quadrants = (quadrants[0] + nb_robots, quadrants[1], quadrants[2], quadrants[3])
            elif x > grid_size[0] // 2 and y < grid_size[1] // 2:
                quadrants = (quadrants[0], quadrants[1] + nb_robots, quadrants[2], quadrants[3])
            elif x < grid_size[0] // 2 and y > grid_size[1] // 2:
                quadrants = (quadrants[0], quadrants[1], quadrants[2] + nb_robots, quadrants[3])
            elif x > grid_size[0] // 2 and y > grid_size[1] // 2:
                quadrants = (quadrants[0], quadrants[1], quadrants[2], quadrants[3] + nb_robots)

    print_grid(grid_size, vectors)

    # multiply all 4 quadrants
    print(quadrants)
    score = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

    return score


def print_grid(grid_size, vectors):
    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            robots = [v[0] for v in vectors if v[0] == (x, y)]
            if len(robots) > 0:
                print(len(robots), end="")
            else:
                print(".", end="")
        print()


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
