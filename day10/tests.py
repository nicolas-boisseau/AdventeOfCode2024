import unittest

from common.common import read_input_lines
from impl import part1, part2


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual(1, part1(read_input_lines("sample.txt")))

    def test_part1_sample2(self):
        self.assertEqual(2, part1(read_input_lines("sample2.txt")))

    def test_part1_sample3(self):
        self.assertEqual(4, part1(read_input_lines("sample3.txt")))

    def test_part1_sample4(self):
        self.assertEqual(3, part1(read_input_lines("sample4.txt")))

    def test_part1_sample5(self):
        self.assertEqual(36, part1(read_input_lines("sample5.txt")))

    def test_part1_input(self):
        self.assertEqual(514, part1(read_input_lines("input.txt")))

    def test_part2_sample5(self):
        self.assertEqual(81, part2(read_input_lines("sample5.txt")))

    def test_part2_input(self):
        self.assertEqual(1162, part2(read_input_lines("input.txt")))


if __name__ == '__main__':
    unittest.main()
