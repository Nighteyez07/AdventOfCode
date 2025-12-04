import unittest
from day03 import solve_part1, solve_part2, max_joltage, max_joltage_n


class TestDay03(unittest.TestCase):
    def test_max_joltage_examples(self):
        """Test individual bank examples."""
        self.assertEqual(max_joltage("987654321111111"), 98)
        self.assertEqual(max_joltage("811111111111119"), 89)
        self.assertEqual(max_joltage("234234234234278"), 78)
        self.assertEqual(max_joltage("818181911112111"), 92)
    
    def test_max_joltage_n_examples(self):
        """Test 12-digit joltage examples."""
        self.assertEqual(max_joltage_n("987654321111111", 12), 987654321111)
        self.assertEqual(max_joltage_n("811111111111119", 12), 811111111119)
        self.assertEqual(max_joltage_n("234234234234278", 12), 434234234278)
        self.assertEqual(max_joltage_n("818181911112111", 12), 888911112111)
    
    def test_part1_with_test_input(self):
        """Test part 1 with test input."""
        result = solve_part1('day03-test.txt')
        self.assertEqual(result, 357)
    
    def test_part2_with_test_input(self):
        """Test part 2 with test input."""
        result = solve_part2('day03-test.txt')
        self.assertEqual(result, 3121910778619)
    
    def test_part1_with_main_input(self):
        """Run part 1 with the main puzzle input."""
        result = solve_part1('day03-input.txt')
        print(f"\nPart 1 answer: {result}")
        self.assertGreater(result, 0)
    
    def test_part2_with_main_input(self):
        """Run part 2 with the main puzzle input."""
        result = solve_part2('day03-input.txt')
        print(f"Part 2 answer: {result}")
        self.assertGreater(result, 0)


if __name__ == '__main__':
    unittest.main()
