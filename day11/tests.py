import unittest

from common.common import read_input_lines
from impl import part1, part2


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample_6(self):
        self.assertEqual(22, part1(read_input_lines("sample.txt"), 6))

    def test_part1_sample_25(self):
        self.assertEqual(55312, part1(read_input_lines("sample.txt"), 25))

    def test_part1_input(self):
        self.assertEqual(194782, part1(read_input_lines("input.txt")))

    def test_part2_sample(self):
        self.assertEqual(55312, part2(read_input_lines("sample.txt")))

    def test_part1_input_75(self):
        self.assertEqual(4, part1(read_input_lines("input.txt"), 75))

    def test_part2_input(self):
        self.assertEqual(233007586663131, part2(read_input_lines("input.txt")))


if __name__ == '__main__':
    unittest.main()
