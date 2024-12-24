import unittest

from common.common import read_input_lines
from day21.impl import create_keypad_astar_graph, create_numeric_pad_astar_graph
from impl import part1, part2, all_combinations


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual(126384, part1(read_input_lines("sample.txt")))

    def test_part1_input(self):
        self.assertEqual(202274, part1(read_input_lines("input.txt")))

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

    def test_astar_graph(self):
        g = create_keypad_astar_graph()
        path = g.astar("A", "<")
        to_robot_moves = {
            "A,>": "v",
            "A,^": "<",
            "^,A": ">",
            "^,v": "v",
            ">,A": "^",
            ">,v": "<",
            "v,>": ">",
            "v,^": "^",
            "v,<": "<",
            "<,v": ">",
        }
        #print([p for p in path][1:])

        i = 1
        buttons = [p for p in path]
        robots_moves = ""
        while i < len(buttons):
            robots_moves += to_robot_moves[f"{buttons[i-1]},{buttons[i]}"]
            i += 1
        print("translated to robot moves :")
        print(robots_moves)

    def test_numeric_astar_graph(self):
        g = create_numeric_pad_astar_graph()
        path = g.astar("A", "8")
        to_robot_moves = {
            "A,3": "^",
            "A,0": "<",
            "0,1": "^",
            "0,A": ">",
            "1,2": ">",
            "1,4": "^",
            "2,1": "<",
            "2,5": "^",
            "2,3": ">",
            "2,0": "v",
            "3,2": "<",
            "3,6": "^",
            "3,A": "v",
            "4,1": "v",
            "4,5": ">",
            "4,7": "^",
            "5,2": "v",
            "5,8": "^",
            "5,4": "<",
            "5,6": ">",
            "6,3": "v",
            "6,9": "^",
            "6,5": "<",
            "7,4": "v",
            "7,8": ">",
            "8,5": "v",
            "8,9": ">",
            "8,7": "<",
            "9,6": "v",
            "9,8": "<"
        }
        # print([p for p in path][1:])

        i = 1
        buttons = [p for p in path]
        robots_moves = ""
        while i < len(buttons):
            robots_moves += to_robot_moves[f"{buttons[i - 1]},{buttons[i]}"]
            i += 1
        print("translated to robot moves :")
        print(robots_moves)

    def test_combinations(self):
        combinations = all_combinations("v>")
        for c in combinations:
            self.assertTrue(c in [">v", "v>"])

        combinations = all_combinations("v>^")
        for c in combinations:
            self.assertTrue(c in [">v^", ">^v", "v>^", "v^>", "^>v", "^v>"])

        combinations = all_combinations("abc")
        for c in combinations:
            self.assertTrue(c in ["abc", "acb", "bac", "bca", "cab", "cba"])


if __name__ == '__main__':
    unittest.main()
