import unittest
from day01 import solve_part1, solve_part2


class TestDay01(unittest.TestCase):
    def test_part1_with_test_input(self):
        """Test that the test input returns 3 zero crossings for part 1"""
        result = solve_part1('day01-test.txt')
        self.assertEqual(result, 3, f"Expected 3 zero crossings, got {result}")
    
    def test_part2_with_test_input(self):
        """Test that the test input returns 6 zero crossings for part 2"""
        result = solve_part2('day01-test.txt')
        self.assertEqual(result, 6, f"Expected 6 zero crossings (including during rotations), got {result}")
    
    def test_part1_with_main_input(self):
        """Test part 1 with the main puzzle input"""
        result = solve_part1('day01-input.txt')
        print(f"\nPart 1 answer: The dial lands on 0 a total of {result} times")
        self.assertGreater(result, 0)
    
    def test_part2_with_main_input(self):
        """Test part 2 with the main puzzle input"""
        result = solve_part2('day01-input.txt')
        print(f"Part 2 answer: The dial points at 0 a total of {result} times")
        self.assertGreater(result, 0)


if __name__ == '__main__':
    unittest.main()
