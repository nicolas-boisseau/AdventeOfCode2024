import unittest

from common.common import read_input_lines
from impl import part1, part2


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual("4,6,3,5,6,3,5,2,1,0", part1(read_input_lines("sample.txt")))

    def test_part1_input(self):
        # not 6,1,1,4,4,3,3,7,0
        self.assertNotEqual("6,1,1,4,4,3,3,7,0", part1(read_input_lines("input.txt")))
        self.assertEqual("7,3,5,7,5,7,4,3,0", part1(read_input_lines("input.txt")))

    def test_part2_sample2(self):
        self.assertEqual(117440, part2(read_input_lines("sample2.txt")))

    def test_part2_input(self):
        self.assertEqual(4, part2(read_input_lines("input.txt")))


if __name__ == '__main__':
    unittest.main()
