import unittest

from common.common import read_input_lines
from impl import part1, part2, next_secret


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual(37327623, part1(read_input_lines("sample.txt")))

    def test_part1_input(self):
        self.assertEqual(16953639210, part1(read_input_lines("input.txt")))

    def test_part2_sample(self):
        self.assertEqual(2, part2(read_input_lines("sample.txt")))

    def test_part2_sample(self):
        self.assertEqual(23, part2(read_input_lines("sample2.txt"))[1])

    def test_part2_input(self):
        # 1926 is too high
        # 1911 is too high
        # 1855 is too low
        self.assertEqual(4, part2(read_input_lines("input.txt"))[1])

    def test_next_secret(self):
        self.assertEqual(15887950, next_secret(123))


if __name__ == '__main__':
    unittest.main()
