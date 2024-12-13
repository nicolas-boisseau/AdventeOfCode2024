import unittest

from common.common import read_input_lines
from impl import part1, part2


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual(140, part1(read_input_lines("sample.txt")))

    def test_part1_sample2(self):
        self.assertEqual(772, part1(read_input_lines("sample2.txt")))

    def test_part1_sample3(self):
        self.assertEqual(1930, part1(read_input_lines("sample3.txt")))

    def test_part1_input(self):
        self.assertEqual(1473276, part1(read_input_lines("input.txt")))

    def test_part2_sample(self):
        self.assertEqual(80, part2(read_input_lines("sample.txt")))

    def test_part2_sample2(self):
        self.assertEqual(436, part2(read_input_lines("sample2.txt")))

    def test_part2_sample4(self):
        self.assertEqual(236, part2(read_input_lines("sample4.txt")))

    def test_part2_sample5(self):
        self.assertEqual(368, part2(read_input_lines("sample5.txt")))

    def test_part2_input(self):
        self.assertEqual(4, part2(read_input_lines("input.txt")))


if __name__ == '__main__':
    unittest.main()
