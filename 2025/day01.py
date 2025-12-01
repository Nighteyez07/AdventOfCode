def solve_part1(input_filename='day01-input.txt'):
    """Count times the dial lands on 0 after a rotation."""
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, input_filename)
    
    with open(input_file, 'r') as f:
        instructions = [line.strip() for line in f.readlines()]
    
    position = 50
    zero_count = 0
    
    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])
        
        if direction == 'R':
            position = (position + steps) % 100
        else:
            position = (position - steps) % 100
        
        if position == 0:
            zero_count += 1
    
    return zero_count


def solve_part2(input_filename='day01-input.txt'):
    """Count all times the dial points at 0, including during rotations."""
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, input_filename)
    
    with open(input_file, 'r') as f:
        instructions = [line.strip() for line in f.readlines()]
    
    position = 50
    zero_count = 0
    
    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])
        
        if direction == 'R':
            # Count how many times we hit 0 while rotating right
            if steps >= 100 - position and position != 0:
                first_crossing = 100 - position
                zero_count += 1 + (steps - first_crossing) // 100
            elif steps > 0 and position == 0:
                zero_count += steps // 100
            
            position = (position + steps) % 100
        else:
            # Count how many times we hit 0 while rotating left
            if steps >= position and position != 0:
                first_crossing = position
                zero_count += 1 + (steps - first_crossing) // 100
            elif steps > 0 and position == 0:
                zero_count += steps // 100
            
            position = (position - steps) % 100
    
    return zero_count


def solve(input_filename='day01-input.txt'):
    return solve_part1(input_filename)


if __name__ == "__main__":
    result_part1 = solve_part1()
    print(f"Part 1: The dial lands on 0 a total of {result_part1} times")
    
    result_part2 = solve_part2()
    print(f"Part 2: The dial points at 0 a total of {result_part2} times")
