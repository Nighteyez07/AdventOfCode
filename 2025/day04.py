import os


def parse_input(input_filename):
    """Parse the input file."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, input_filename)
    
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    return lines


def count_adjacent_rolls(grid, row, col):
    """Count the number of rolls (@) in the 8 adjacent positions."""
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                count += 1
    
    return count


def solve_part1(input_filename='day04-input.txt'):
    """Solve part 1 - count rolls accessible by forklift (fewer than 4 adjacent rolls)."""
    grid = parse_input(input_filename)
    
    accessible = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                if count_adjacent_rolls(grid, row, col) < 4:
                    accessible += 1
    
    return accessible


def solve_part2(input_filename='day04-input.txt'):
    """Solve part 2 - keep removing accessible rolls until none remain accessible."""
    lines = parse_input(input_filename)
    # Convert to mutable grid
    grid = [list(line) for line in lines]
    
    total_removed = 0
    
    while True:
        # Find all currently accessible rolls
        accessible = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '@':
                    if count_adjacent_rolls(grid, row, col) < 4:
                        accessible.append((row, col))
        
        if not accessible:
            break
        
        # Remove all accessible rolls
        for row, col in accessible:
            grid[row][col] = '.'
        
        total_removed += len(accessible)
    
    return total_removed


if __name__ == "__main__":
    result1 = solve_part1()
    print(f"Part 1: {result1}")
    
    result2 = solve_part2()
    print(f"Part 2: {result2}")
