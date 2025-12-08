import unittest
from day08 import solve_part1, solve_part2


class TestDay08(unittest.TestCase):
    def test_part1_with_test_input(self):
        """Test part 1 with test input - 10 connections should give 40."""
        result = solve_part1('day08-test.txt', num_connections=10)
        self.assertEqual(result, 40)
    
    def test_part2_with_test_input(self):
        """Test part 2 with test input - last connection is 216,146,977 and 117,168,530."""
        result = solve_part2('day08-test.txt')
        # Product of X coordinates: 216 * 117 = 25272
        self.assertEqual(result, 25272)
    
    def test_part1_with_main_input(self):
        """Run part 1 with the main puzzle input."""
        result = solve_part1('day08-input.txt')
        print(f"\nPart 1 answer: {result}")
        self.assertGreater(result, 0)
    
    def test_part2_with_main_input(self):
        """Run part 2 with the main puzzle input."""
        result = solve_part2('day08-input.txt')
        print(f"Part 2 answer: {result}")
        self.assertGreater(result, 0)


if __name__ == '__main__':
    unittest.main()
