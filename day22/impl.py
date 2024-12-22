import os.path

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines

download_input_if_not_exists(2024)

def next_secret(secret):
    output = ((secret * 64) ^ secret) % 16777216
    output = ((output // 32) ^ output) % 16777216
    output = ((output * 2048) ^ output) % 16777216
    return output


def part1(lines):
    score = 0
    for line in lines:
        secret = int(line)
        for i in range(2000):
            secret = next_secret(secret)
        score += secret
    return score

def part2(lines):
    score = 0
    sequences = {}
    for line in lines:
        secret = int(line)
        sub_sequences = {}
        for i in range(2000-3):  # skip last 3 secrets to avoid out of bounds
            secret2 = next_secret(secret)
            secret3 = next_secret(secret2)
            secret4 = next_secret(secret3)
            secret5 = next_secret(secret4)

            s1_last_digit = int(str(secret)[-1])
            s2_last_digit = int(str(secret2)[-1])
            s3_last_digit = int(str(secret3)[-1])
            s4_last_digit = int(str(secret4)[-1])
            s5_last_digit = int(str(secret5)[-1])

            key = f"{s2_last_digit-s1_last_digit},{s3_last_digit-s2_last_digit},{s4_last_digit-s3_last_digit},{s5_last_digit-s4_last_digit}"

            if key not in sub_sequences:
                sub_sequences[key] = s5_last_digit
            # else:
            #     sub_sequences[key] = max(sub_sequences[key], s5_last_digit)

            secret = secret2

        for sub_key in sub_sequences:
            if sub_key not in sequences:
                sequences[sub_key] = sub_sequences[sub_key]
            else:
                sequences[sub_key] += sub_sequences[sub_key]

        score += secret

    max_key = max(sequences, key=sequences.get)
    return max_key, sequences[max_key]


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
