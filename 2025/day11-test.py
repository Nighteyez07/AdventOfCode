"""Tests for Advent of Code 2025 - Day 11"""

import unittest
from day11 import solve_part1, solve_part2


class TestDay11(unittest.TestCase):
    
    def test_part1_with_test_input(self):
        """Test Part 1 with test input."""
        result = solve_part1('day11-test.txt')
        self.assertEqual(result, 5)  # 5 paths from you to out
    
    def test_part1_with_main_input(self):
        """Test Part 1 with main input."""
        result = solve_part1('day11-input.txt')
        self.assertEqual(result, 607)
    
    def test_part2_with_test_input(self):
        """Test Part 2 with test input."""
        result = solve_part2('day11-test.txt')
        self.assertEqual(result, 2)  # 2 paths visit both dac and fft
    
    def test_part2_with_main_input(self):
        """Test Part 2 with main input."""
        result = solve_part2('day11-input.txt')
        self.assertEqual(result, 506264456238938)


if __name__ == '__main__':
    unittest.main()
