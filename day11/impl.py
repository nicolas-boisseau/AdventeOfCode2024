import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

class Stone:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def read_stones(values):
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
    stats = {
        "even": 0,
        "zero": 0,
        "others": 0
    }
    while current_stone is not None:
        if current_stone.value == "0":
            current_stone.value = "1"
            current_stone = current_stone.next
            stats["zero"] += 1
        elif len(current_stone.value) % 2 == 0:
            cur_value = current_stone.value
            current_stone.value = str(int(cur_value[:len(cur_value) // 2]))
            newStone = Stone(str(int(cur_value[len(cur_value) // 2:])))
            newStone.next = current_stone.next
            newStone.prev = current_stone
            current_stone.next = newStone
            current_stone = newStone.next
            stats["even"] += 1
        else:
            current_stone.value = str(int(current_stone.value) * 2024)
            current_stone = current_stone.next
            stats["others"] += 1
    return stats

def stones_count(stone):
    count = 0
    while stone is not None:
        count += 1
        stone = stone.next
    return count

def blink_x_times(stone, x):
    for i in range(x):
        blink(stone)
        print(i)
        #print_stones(stone)
    return stone

def part1(lines, iterations = 25):
    first_stone = read_stones(lines[0].split(" "))

    print_stones(first_stone)

    for i in range(iterations):
        stats = blink(first_stone)
        print(f"iteration {i} : {stones_count(first_stone)}, prev_stats = {stats}")
        if i < 6:
            print_stones(first_stone)

    return stones_count(first_stone)

def compute_score_25(c):
    unit_stone = read_stones([c])
    unit_stone = blink_x_times(unit_stone, 25)
    return stones_count(unit_stone), unit_stone

def part2(lines):
    final_score = 0
    cache = {}
    cache_miss = 0

    for c in lines[0].split(" "):
        if c not in cache:
            cache[c] = compute_score_25(c)
            print(f"Cache miss {cache_miss} for {c}")
            cache_miss += 1
        _, stone2 = cache[c]

        # 2nd pass for 25
        while stone2 is not None:
            c2 = stone2.value
            if c2 not in cache:
                cache[c2] = compute_score_25(c2)
                print(f"Cache miss {cache_miss} for {c2}")
                cache_miss += 1
            _, stone3 = cache[c2]
            #print("stone2 done")

            stone2 = stone2.next

            # 3rd pass for 25
            while stone3 is not None:
                c3 = stone3.value
                if c3 not in cache:
                    cache[c3] = compute_score_25(c3)
                    print(f"Cache miss {cache_miss} for {c3}")
                    cache_miss += 1
                sub_score3, _ = cache[c3]
                #print("stone3 done")

                final_score += sub_score3

                stone3 = stone3.next

        #print("stone1 done")

    return final_score




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
