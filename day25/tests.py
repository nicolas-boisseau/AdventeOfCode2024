import unittest

from common.common import read_input_lines
from impl import part1


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual(3, part1(read_input_lines("sample.txt")))

    def test_part1_input(self):
        self.assertEqual(3162, part1(read_input_lines("input.txt")))


if __name__ == '__main__':
    unittest.main()
