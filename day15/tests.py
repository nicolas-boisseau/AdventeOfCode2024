import unittest

from common.common import read_input_lines
from impl import part1, part2


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual(2028, part1(read_input_lines("sample.txt")))

    def test_part1_sample2(self):
        self.assertEqual(10092, part1(read_input_lines("sample2.txt")))

    def test_part1_input(self):
        self.assertEqual(1457740, part1(read_input_lines("input.txt")))

    def test_part2_sample(self):
        self.assertEqual(2, part2(read_input_lines("sample_part2.txt")))

    def test_part2_sample2(self):
        self.assertEqual(9021, part2(read_input_lines("sample2.txt")))

    def test_part2_input(self):
        # not 1473493
        self.assertNotEqual(1473493, part2(read_input_lines("input.txt")))
        self.assertEqual(4, part2(read_input_lines("input.txt")))


if __name__ == '__main__':
    unittest.main()
