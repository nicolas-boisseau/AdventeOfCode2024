import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def extract_rules_and_sequences(lines):
    rules = []
    current = lines.pop(0)
    while current != "":
        a, b = current.split("|")
        rules.append((int(a), int(b)))
        current = lines.pop(0)

    sequences = []
    for l in lines:
        sequences.append([int(x) for x in l.split(",")])
    return rules, sequences

def first_pass(rules, sequences):
    score = 0
    rejected_sequences = []
    for s in sequences:
        if validate_rules(rules, s):
            score += s[int(len(s) / 2)]
        else:
            rejected_sequences.append(s)

    return score, rejected_sequences


def validate_rules(rules, s):
    for rule in rules:
        a, b = rule
        try:
            if a in s and s.index(a) > s.index(b):
                return False
        except ValueError:
            pass
    return True


def part1(lines):
    rules, sequences = extract_rules_and_sequences(lines)

    score, _ = first_pass(rules, sequences)

    return score



def part2(lines):
    rules, sequences = extract_rules_and_sequences(lines)

    score, rejected_sequences = first_pass(rules, sequences)

    for s in rejected_sequences:
        while not validate_rules(rules, s):
            for rule in rules:
                a, b = rule
                if a in s and b in s and s.index(a) > s.index(b):
                    a_i = s.index(a)
                    b_i = s.index(b)
                    if a_i > b_i:
                        s[a_i], s[b_i] = s[b_i], s[a_i]

    new_score, _ = first_pass(rules, rejected_sequences)

    return new_score


if __name__ == '__main__':

    part = 2
    expectedSampleResult = 123

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2024, part, result)
        print(f"Part {part} result posted !")
