import unittest

from common.common import read_input_lines
from impl import part1, part2, all_combinations


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual(0, part1(read_input_lines("sample.txt")))

    def test_part1_input(self):
        self.assertEqual(1, part1(read_input_lines("input.txt")))

    def test_part2_sample(self):
        self.assertEqual(2, part2(read_input_lines("sample.txt")))

    def test_part2_input(self):
        self.assertEqual(4, part2(read_input_lines("input.txt")))

    def test_combinations(self):
        combinations = all_combinations("v>")
        for c in combinations:
            self.assertTrue(c in [">v", "v>"])

        combinations = all_combinations("v>^")
        for c in combinations:
            self.assertTrue(c in [">v^", ">^v", "v>^", "v^>", "^>v", "^v>"])


if __name__ == '__main__':
    unittest.main()
