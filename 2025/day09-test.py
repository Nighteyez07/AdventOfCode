import unittest
from day09 import solve_part1, solve_part2

class TestDay09(unittest.TestCase):
    def test_part1_with_test_input(self):
        """Test part 1 with test input - largest rectangle area is 50."""
        result = solve_part1('day09-test.txt')
        self.assertEqual(result, 50)
    
    def test_part2_with_test_input(self):
        """Test part 2 with test input - largest valid rectangle area is 24."""
        result = solve_part2('day09-test.txt')
        self.assertEqual(result, 24)
    
    def test_part1_with_main_input(self):
        """Run part 1 with the main puzzle input."""
        result = solve_part1('day09-input.txt')
        print(f"\nPart 1 answer: {result}")
        self.assertGreater(result, 0)
    
    def test_part2_with_main_input(self):
        """Run part 2 with the main puzzle input."""
        result = solve_part2('day09-input.txt')
        print(f"Part 2 answer: {result}")
        self.assertGreater(result, 0)

if __name__ == '__main__':
    unittest.main()
