import os


def parse_input(input_filename):
    """Parse the input file."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, input_filename)
    
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    return lines


def max_joltage(bank):
    """Find the max two-digit joltage from a bank by picking two batteries."""
    max_val = 0
    # Try all pairs of positions (i, j) where i < j
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Form the two-digit number from digits at positions i and j
            joltage = int(bank[i] + bank[j])
            max_val = max(max_val, joltage)
    return max_val


def max_joltage_n(bank, n):
    """Find the max n-digit joltage from a bank by picking n batteries.
    
    Greedy approach: at each position, pick the largest digit that still
    leaves enough digits remaining to complete the selection.
    """
    result = []
    start = 0
    
    for i in range(n):
        digits_needed = n - i - 1  # how many more we need after this pick
        # Search window: from start to the last position that leaves enough digits
        end = len(bank) - digits_needed
        
        # Find the largest digit in this window
        best_idx = start
        for j in range(start, end):
            if bank[j] > bank[best_idx]:
                best_idx = j
        
        result.append(bank[best_idx])
        start = best_idx + 1
    
    return int(''.join(result))


def solve_part1(input_filename='day03-input.txt'):
    """Solve part 1."""
    banks = parse_input(input_filename)
    
    total = 0
    for bank in banks:
        total += max_joltage(bank)
    
    return total


def solve_part2(input_filename='day03-input.txt'):
    """Solve part 2."""
    banks = parse_input(input_filename)
    
    total = 0
    for bank in banks:
        total += max_joltage_n(bank, 12)
    
    return total


if __name__ == "__main__":
    result1 = solve_part1()
    print(f"Part 1: {result1}")
    
    result2 = solve_part2()
    print(f"Part 2: {result2}")
