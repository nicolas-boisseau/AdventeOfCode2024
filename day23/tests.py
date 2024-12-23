import unittest

from common.common import read_input_lines
from impl import part1, part2


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual(7, part1(read_input_lines("sample.txt")))

    def test_part1_input(self):
        res = part1(read_input_lines("input.txt"))
        self.assertEqual(1314, res)

    def test_part2_sample(self):
        self.assertEqual('co,de,ka,ta', part2(read_input_lines("sample.txt")))

    def test_part2_input(self):
        self.assertEqual("bg,bu,ce,ga,hw,jw,nf,nt,ox,tj,uu,vk,wp", part2(read_input_lines("input.txt")))


if __name__ == '__main__':
    unittest.main()
