import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

class Stone:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def read_stones(lines):
    values = lines[0].split(" ")
    root_stone = Stone(values[0])
    current_stone = root_stone
    for v in values[1:]:
        newStone = Stone(v)
        current_stone.next = newStone
        newStone.prev = current_stone
        current_stone = newStone
    return root_stone

def print_stones(stone):
    result = ""
    while stone is not None:
        result += stone.value + " "
        stone = stone.next
    print(result)

def blink(stone):
    current_stone = stone
    while current_stone is not None:
        if current_stone.value == "0":
            current_stone.value = "1"
            current_stone = current_stone.next
        elif len(current_stone.value) % 2 == 0:
            cur_value = current_stone.value
            current_stone.value = str(int(cur_value[:len(cur_value) // 2]))
            newStone = Stone(str(int(cur_value[len(cur_value) // 2:])))
            newStone.next = current_stone.next
            newStone.prev = current_stone
            current_stone.next = newStone
            current_stone = newStone.next
        else:
            current_stone.value = str(int(current_stone.value) * 2024)
            current_stone = current_stone.next

def stones_count(stone):
    count = 0
    while stone is not None:
        count += 1
        stone = stone.next
    return count

def part1(lines, iterations = 25):
    first_stone = read_stones(lines)

    print_stones(first_stone)

    for i in range(iterations):
        blink(first_stone)
        print(f"iteration {i} : {stones_count(first_stone)}")
        if i < 6:
            print_stones(first_stone)

    return stones_count(first_stone)





def part2(lines):
    return 4


if __name__ == '__main__':

    part = 1
    expectedSampleResult = 55312

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2024, part, result)
        print(f"Part {part} result posted !")
