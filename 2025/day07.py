import os


def parse_input(input_filename):
    """Parse the input file."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, input_filename)
    
    with open(input_file, 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    
    return lines


def find_start(grid):
    """Find the starting position marked with 'S'."""
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'S':
                return (row, col)
    return None


def simulate_beams(grid):
    """Simulate tachyon beams and count the number of splits."""
    start_pos = find_start(grid)
    if not start_pos:
        return 0
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Track active beams as (row, col) positions
    # Use a queue to process beams
    beams = [start_pos]
    
    # Track which splitters have been activated to count splits
    split_count = 0
    activated_splitters = set()
    
    # Track beam positions we've already processed to avoid infinite loops
    # For each column, track which beams are moving down through it
    visited = set()
    
    while beams:
        row, col = beams.pop(0)
        
        # Create a state identifier for this beam position
        state = (row, col)
        if state in visited:
            continue
        visited.add(state)
        
        # Move beam downward
        next_row = row + 1
        
        # Check if beam exits the manifold
        if next_row >= rows:
            continue
        
        # Check what's at the next position
        if col < len(grid[next_row]):
            next_char = grid[next_row][col]
            
            if next_char == '^':
                # Beam hits a splitter
                splitter_pos = (next_row, col)
                
                # Only count this split if we haven't activated this splitter yet
                if splitter_pos not in activated_splitters:
                    activated_splitters.add(splitter_pos)
                    split_count += 1
                    
                    # Create two new beams: left and right
                    left_col = col - 1
                    right_col = col + 1
                    
                    # Add left beam if in bounds
                    if left_col >= 0:
                        beams.append((next_row, left_col))
                    
                    # Add right beam if in bounds
                    if right_col < cols:
                        beams.append((next_row, right_col))
            else:
                # Empty space or other character, beam continues downward
                beams.append((next_row, col))
    
    return split_count


def solve_part1(input_filename='day07-input.txt'):
    """Solve part 1."""
    grid = parse_input(input_filename)
    result = simulate_beams(grid)
    return result


def simulate_quantum_beams(grid):
    """Simulate quantum tachyon beams and count unique timelines.
    
    Each timeline is a unique path through the manifold.
    When a particle hits a splitter, it creates two timelines.
    """
    start_pos = find_start(grid)
    if not start_pos:
        return 0
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Track all possible paths using DFS/BFS
    # Each path is represented by the sequence of columns visited at each row
    # Queue of (current_row, current_col)
    queue = [(start_pos[0], start_pos[1])]
    
    # Track all possible (row, col) states reachable
    # For each row, track which columns can be reached
    reachable = {}
    reachable[start_pos[0]] = {start_pos[1]}
    
    while queue:
        row, col = queue.pop(0)
        
        # Move beam downward
        next_row = row + 1
        
        # Check if beam exits the manifold
        if next_row >= rows:
            continue
        
        # Check what's at the next position
        if col < len(grid[next_row]):
            next_char = grid[next_row][col]
            
            if next_char == '^':
                # Particle hits a splitter - splits into left and right
                
                # Left path
                left_col = col - 1
                if left_col >= 0:
                    if next_row not in reachable:
                        reachable[next_row] = set()
                    if left_col not in reachable[next_row]:
                        reachable[next_row].add(left_col)
                        queue.append((next_row, left_col))
                
                # Right path
                right_col = col + 1
                if right_col < cols:
                    if next_row not in reachable:
                        reachable[next_row] = set()
                    if right_col not in reachable[next_row]:
                        reachable[next_row].add(right_col)
                        queue.append((next_row, right_col))
            else:
                # Empty space, beam continues downward
                if next_row not in reachable:
                    reachable[next_row] = set()
                if col not in reachable[next_row]:
                    reachable[next_row].add(col)
                    queue.append((next_row, col))
    
    # Now count the number of unique timelines
    # A timeline is a path from start to exit
    # We need to count all possible paths through the reachable states
    
    # Use dynamic programming to count paths
    # dp[row][col] = number of paths from (row, col) to exit
    
    # Start from bottom and work upward
    dp = {}
    
    # Bottom row - each position has 1 path (exit immediately)
    for row in range(rows - 1, -1, -1):
        if row not in reachable:
            continue
            
        for col in reachable[row]:
            next_row = row + 1
            
            if next_row >= rows:
                # Exits the manifold - this is one complete path
                dp[(row, col)] = 1
            else:
                # Count paths from next positions
                total_paths = 0
                
                if col < len(grid[next_row]):
                    next_char = grid[next_row][col]
                    
                    if next_char == '^':
                        # Splits into left and right
                        left_col = col - 1
                        right_col = col + 1
                        
                        if next_row in reachable:
                            if left_col in reachable[next_row]:
                                total_paths += dp.get((next_row, left_col), 0)
                            if right_col in reachable[next_row]:
                                total_paths += dp.get((next_row, right_col), 0)
                    else:
                        # Continues straight down
                        if next_row in reachable and col in reachable[next_row]:
                            total_paths += dp.get((next_row, col), 0)
                
                dp[(row, col)] = total_paths
    
    # Return the number of paths from the start position
    return dp.get(start_pos, 0)


def solve_part2(input_filename='day07-input.txt'):
    """Solve part 2."""
    grid = parse_input(input_filename)
    result = simulate_quantum_beams(grid)
    return result


if __name__ == "__main__":
    result1 = solve_part1()
    print(f"Part 1: {result1}")
    
    result2 = solve_part2()
    print(f"Part 2: {result2}")
