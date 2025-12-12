import unittest
from day12 import solve_part1, solve_part2


class TestDay12(unittest.TestCase):
    def test_part1_with_test_input(self):
        """Test part 1 with test input."""
        result = solve_part1('day12-test.txt')
        # TODO: Update expected value
        self.assertEqual(result, 0)
    
    def test_part2_with_test_input(self):
        """Test part 2 with test input."""
        result = solve_part2('day12-test.txt')
        # TODO: Update expected value
        self.assertEqual(result, 0)
    
    def test_part1_with_main_input(self):
        """Run part 1 with the main puzzle input."""
        result = solve_part1('day12-input.txt')
        print(f"\nPart 1 answer: {result}")
        self.assertGreater(result, 0)
    
    def test_part2_with_main_input(self):
        """Run part 2 with the main puzzle input."""
        result = solve_part2('day12-input.txt')
        print(f"Part 2 answer: {result}")
        self.assertGreater(result, 0)


if __name__ == '__main__':
    unittest.main()
