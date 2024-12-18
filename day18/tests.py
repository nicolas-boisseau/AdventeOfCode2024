import unittest

from common.common import read_input_lines
from impl import part1, part2


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual(22, part1(read_input_lines("sample.txt"), 6, 6, 12))

    def test_part1_input(self):
        # not 140
        self.assertEqual(316, part1(read_input_lines("input.txt"), 70, 70, 1024))

    def test_part2_sample(self):
        self.assertEqual("6,1", part2(read_input_lines("sample.txt"), 6, 6, 12))

    def test_part2_input(self):
        self.assertEqual("45,18", part2(read_input_lines("input.txt"), 70, 70, 1024))


if __name__ == '__main__':
    unittest.main()
