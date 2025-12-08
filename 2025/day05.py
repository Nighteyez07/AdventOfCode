import os


def parse_input(input_filename):
    """Parse the input file."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, input_filename)
    
    with open(input_file, 'r') as f:
        content = f.read().strip()
    
    # Split by blank line - first section is ranges, second is ingredient IDs
    sections = content.split('\n\n')
    
    # Parse ranges (e.g., "3-5" -> (3, 5))
    ranges = []
    for line in sections[0].split('\n'):
        if line.strip():
            start, end = line.strip().split('-')
            ranges.append((int(start), int(end)))
    
    # Parse ingredient IDs
    ingredient_ids = []
    for line in sections[1].split('\n'):
        if line.strip():
            ingredient_ids.append(int(line.strip()))
    
    return ranges, ingredient_ids


def is_fresh(ingredient_id, ranges):
    """Check if an ingredient ID falls within any fresh range."""
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False


def solve_part1(input_filename='day05-input.txt'):
    """Solve part 1."""
    ranges, ingredient_ids = parse_input(input_filename)
    
    # Count how many ingredient IDs are fresh
    fresh_count = 0
    for ingredient_id in ingredient_ids:
        if is_fresh(ingredient_id, ranges):
            fresh_count += 1
    
    return fresh_count


def merge_ranges(ranges):
    """Merge overlapping ranges and return the total count of unique IDs."""
    if not ranges:
        return 0
    
    # Sort ranges by start position
    sorted_ranges = sorted(ranges)
    
    # Merge overlapping ranges
    merged = [sorted_ranges[0]]
    
    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        
        # If current range overlaps or is adjacent to the last merged range
        if current_start <= last_end + 1:
            # Extend the last merged range if needed
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            # No overlap, add as a new range
            merged.append((current_start, current_end))
    
    # Count total IDs in all merged ranges
    total = 0
    for start, end in merged:
        total += (end - start + 1)  # +1 because ranges are inclusive
    
    return total


def solve_part2(input_filename='day05-input.txt'):
    """Solve part 2."""
    ranges, ingredient_ids = parse_input(input_filename)
    
    # Count all unique ingredient IDs covered by the ranges
    result = merge_ranges(ranges)
    
    return result


if __name__ == "__main__":
    result1 = solve_part1()
    print(f"Part 1: {result1}")
    
    result2 = solve_part2()
    print(f"Part 2: {result2}")
