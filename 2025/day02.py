import os


def is_invalid_id_part1(n):
    """Check if number is a sequence repeated exactly twice (like 55, 6464, 123123)."""
    s = str(n)
    length = len(s)
    
    if length % 2 != 0:
        return False
    
    half = length // 2
    return s[:half] == s[half:]


def is_invalid_id_part2(n):
    """Check if number is a sequence repeated at least twice (like 55, 111, 123123123)."""
    s = str(n)
    length = len(s)
    
    # Try all possible pattern lengths from 1 to half the string
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repeats = length // pattern_len
            if repeats >= 2 and pattern * repeats == s:
                return True
    return False


def find_invalid_ids_in_range(start, end, checker=is_invalid_id_part1):
    """Find all invalid IDs in the given range."""
    invalid_ids = []
    for n in range(start, end + 1):
        if checker(n):
            invalid_ids.append(n)
    return invalid_ids


def parse_input(input_filename):
    """Parse the input file and return list of (start, end) ranges."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, input_filename)
    
    ranges = []
    with open(input_file, 'r') as f:
        content = f.read().replace('\n', '')
        for part in content.split(','):
            part = part.strip()
            if not part:
                continue
            start, end = part.split('-')
            ranges.append((int(start), int(end)))
    return ranges


def solve_part1(input_filename='day02-input.txt'):
    """Sum all invalid IDs (repeated twice) in the given ranges."""
    ranges = parse_input(input_filename)
    
    total = 0
    for start, end in ranges:
        invalid_ids = find_invalid_ids_in_range(start, end, is_invalid_id_part1)
        total += sum(invalid_ids)
    
    return total


def solve_part2(input_filename='day02-input.txt'):
    """Sum all invalid IDs (repeated at least twice) in the given ranges."""
    ranges = parse_input(input_filename)
    
    total = 0
    for start, end in ranges:
        invalid_ids = find_invalid_ids_in_range(start, end, is_invalid_id_part2)
        total += sum(invalid_ids)
    
    return total


if __name__ == "__main__":
    result1 = solve_part1()
    print(f"Part 1: Sum of all invalid IDs = {result1}")
    
    result2 = solve_part2()
    print(f"Part 2: Sum of all invalid IDs = {result2}")
