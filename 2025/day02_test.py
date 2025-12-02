import unittest
from day02 import is_invalid_id_part1, is_invalid_id_part2, find_invalid_ids_in_range, solve_part1, solve_part2


class TestDay02(unittest.TestCase):
    def test_is_invalid_id_part1(self):
        """Test the part 1 invalid ID checker (exactly twice)."""
        self.assertTrue(is_invalid_id_part1(55))
        self.assertTrue(is_invalid_id_part1(6464))
        self.assertTrue(is_invalid_id_part1(123123))
        self.assertTrue(is_invalid_id_part1(1010))
        
        self.assertFalse(is_invalid_id_part1(101))
        self.assertFalse(is_invalid_id_part1(12))
        self.assertFalse(is_invalid_id_part1(111))  # 3 times, not 2
    
    def test_is_invalid_id_part2(self):
        """Test the part 2 invalid ID checker (at least twice)."""
        self.assertTrue(is_invalid_id_part2(55))
        self.assertTrue(is_invalid_id_part2(111))       # 1 three times
        self.assertTrue(is_invalid_id_part2(999))       # 9 three times
        self.assertTrue(is_invalid_id_part2(12341234))  # 1234 two times
        self.assertTrue(is_invalid_id_part2(123123123)) # 123 three times
        self.assertTrue(is_invalid_id_part2(1212121212))# 12 five times
        self.assertTrue(is_invalid_id_part2(1111111))   # 1 seven times
        
        self.assertFalse(is_invalid_id_part2(101))
        self.assertFalse(is_invalid_id_part2(12))
        self.assertFalse(is_invalid_id_part2(1234))
    
    def test_range_11_22(self):
        """11-22 has two invalid IDs: 11 and 22."""
        invalid = find_invalid_ids_in_range(11, 22, is_invalid_id_part1)
        self.assertEqual(invalid, [11, 22])
    
    def test_range_95_115_part1(self):
        """95-115 has one invalid ID for part 1: 99."""
        invalid = find_invalid_ids_in_range(95, 115, is_invalid_id_part1)
        self.assertEqual(invalid, [99])
    
    def test_range_95_115_part2(self):
        """95-115 has two invalid IDs for part 2: 99 and 111."""
        invalid = find_invalid_ids_in_range(95, 115, is_invalid_id_part2)
        self.assertEqual(invalid, [99, 111])
    
    def test_range_998_1012_part2(self):
        """998-1012 has two invalid IDs for part 2: 999 and 1010."""
        invalid = find_invalid_ids_in_range(998, 1012, is_invalid_id_part2)
        self.assertEqual(invalid, [999, 1010])
    
    def test_range_565653_565659_part2(self):
        """565653-565659 has one invalid ID for part 2: 565656."""
        invalid = find_invalid_ids_in_range(565653, 565659, is_invalid_id_part2)
        self.assertEqual(invalid, [565656])
    
    def test_range_824824821_824824827_part2(self):
        """824824821-824824827 has one invalid ID for part 2: 824824824."""
        invalid = find_invalid_ids_in_range(824824821, 824824827, is_invalid_id_part2)
        self.assertEqual(invalid, [824824824])
    
    def test_range_2121212118_2121212124_part2(self):
        """2121212118-2121212124 has one invalid ID for part 2: 2121212121."""
        invalid = find_invalid_ids_in_range(2121212118, 2121212124, is_invalid_id_part2)
        self.assertEqual(invalid, [2121212121])
    
    def test_part1_with_test_input(self):
        """Test input should sum to 1227775554 for part 1."""
        result = solve_part1('day02-test.txt')
        self.assertEqual(result, 1227775554)
    
    def test_part2_with_test_input(self):
        """Test input should sum to 4174379265 for part 2."""
        result = solve_part2('day02-test.txt')
        self.assertEqual(result, 4174379265)
    
    def test_part1_with_main_input(self):
        """Run part 1 with the main puzzle input."""
        result = solve_part1('day02-input.txt')
        print(f"\nPart 1 answer: {result}")
        self.assertGreater(result, 0)
    
    def test_part2_with_main_input(self):
        """Run part 2 with the main puzzle input."""
        result = solve_part2('day02-input.txt')
        print(f"Part 2 answer: {result}")
        self.assertGreater(result, 0)


if __name__ == '__main__':
    unittest.main()
