import unittest

from common.common import read_input_lines
from impl import part1, part2


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        score, _ = part1(read_input_lines("sample.txt"))
        self.assertEqual(140, score)

    def test_part1_sample2(self):
        score, _ = part1(read_input_lines("sample2.txt"))
        self.assertEqual(772, score)

    def test_part1_sample3(self):
        score, _ = part1(read_input_lines("sample3.txt"))
        self.assertEqual(1930, score)

    def test_part1_input(self):
        score, _ = part1(read_input_lines("input.txt"))
        self.assertEqual(1473276, score)

    def test_part2_sample(self):
        self.assertEqual(80, part2(read_input_lines("sample.txt")))

    def test_part2_sample2(self):
        self.assertEqual(436, part2(read_input_lines("sample2.txt")))

    def test_part2_sample4(self):
        self.assertEqual(236, part2(read_input_lines("sample4.txt")))

    def test_part2_sample5(self):
        self.assertEqual(368, part2(read_input_lines("sample5.txt")))

    def test_part1_test_nico(self):
        _, nb = part1(read_input_lines("test_nico.txt"))
        _, nb2 = part1(read_input_lines("test_nico2.txt"))
        _, nb3 = part1(read_input_lines("test_nico3.txt"))
        self.assertEqual(12, nb+nb2+nb3)

    def test_part2_input(self):
        self.assertEqual(4, part2(read_input_lines("input.txt")))


if __name__ == '__main__':
    unittest.main()
