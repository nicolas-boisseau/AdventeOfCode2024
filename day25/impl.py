import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def extract_keys_and_locks(lines):
    keys = []
    locks = []
    current_entry = []
    i = 0
    while i < len(lines):
        l = lines[i]
        current_entry.append(l)

        if l == "":
            read_key_or_lock(current_entry, keys, locks)

            current_entry = []

        i += 1

    # read last entry :
    read_key_or_lock(current_entry, keys, locks)

    return keys, locks


def read_key_or_lock(current_entry, keys, locks):
    # current entry is done
    heights = [-1, -1, -1, -1, -1] # sart at -1 to exclude the first "#####"
    for cl in current_entry:
        for j in range(len(cl)):
            heights[j] += 1 if cl[j] == "#" else 0
    is_key = all([c == "." for c in current_entry[0]])
    if is_key:
        keys.append(tuple(heights))
    else:
        locks.append(tuple(heights))

def add(list1, list2):
    return [a + b for a, b in zip(list1, list2)]

def part1(lines):
    keys, locks = extract_keys_and_locks(lines)

    score = 0
    already_found_locks = set()
    already_found_keys = set()
    for lock in locks:
        if lock in already_found_locks:
            continue
        for key in keys:
            res = add(key, lock)
            if all([r < 6 for r in res]):
                score += 1
                already_found_locks.add(lock)
                already_found_keys.add(key)

    return score


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
