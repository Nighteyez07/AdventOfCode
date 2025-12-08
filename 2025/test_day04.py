import unittest
from day04 import solve_part1, solve_part2


class TestDay04(unittest.TestCase):
    def test_part1_with_test_input(self):
        """Test part 1 with test input - should find 13 accessible rolls."""
        result = solve_part1('day04-test.txt')
        self.assertEqual(result, 13)
    
    def test_part2_with_test_input(self):
        """Test part 2 with test input - should remove 43 total rolls."""
        result = solve_part2('day04-test.txt')
        self.assertEqual(result, 43)
    
    def test_part1_with_main_input(self):
        """Run part 1 with the main puzzle input."""
        result = solve_part1('day04-input.txt')
        print(f"\nPart 1 answer: {result}")
        self.assertGreater(result, 0)
    
    def test_part2_with_main_input(self):
        """Run part 2 with the main puzzle input."""
        result = solve_part2('day04-input.txt')
        print(f"Part 2 answer: {result}")
        self.assertGreater(result, 0)


if __name__ == '__main__':
    unittest.main()
