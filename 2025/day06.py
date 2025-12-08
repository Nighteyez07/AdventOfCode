import os


def parse_input(input_filename):
    """Parse the input file."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, input_filename)
    
    with open(input_file, 'r') as f:
        # Don't strip - we need to preserve spacing
        lines = [line.rstrip('\n') for line in f.readlines()]
    
    return lines


def parse_worksheet(lines):
    """Parse the worksheet into individual problems."""
    if not lines:
        return []
    
    # Find the maximum width
    max_width = max(len(line) for line in lines)
    
    # Pad all lines to the same width
    padded_lines = [line.ljust(max_width) for line in lines]
    
    # Identify columns that are problems (not all spaces)
    problems = []
    col = 0
    
    while col < max_width:
        # Check if this column has any non-space characters
        has_content = any(line[col] != ' ' for line in padded_lines)
        
        if has_content:
            # Find the width of this problem (until we hit an all-space column)
            problem_start = col
            problem_end = col
            
            # Find where this problem ends
            while problem_end < max_width:
                # Check if column problem_end is all spaces
                is_separator = all(line[problem_end] == ' ' for line in padded_lines)
                if is_separator:
                    break
                problem_end += 1
            
            # Extract this problem
            problem_lines = []
            for line in padded_lines:
                problem_text = line[problem_start:problem_end].strip()
                if problem_text:
                    problem_lines.append(problem_text)
            
            if problem_lines:
                problems.append(problem_lines)
            
            col = problem_end + 1
        else:
            col += 1
    
    return problems


def solve_problem(problem_lines):
    """Solve a single problem (list of lines, last line is the operator)."""
    if not problem_lines:
        return 0
    
    # Last line is the operator
    operator = problem_lines[-1].strip()
    
    # All other lines are numbers
    numbers = [int(line.strip()) for line in problem_lines[:-1]]
    
    if not numbers:
        return 0
    
    # Perform the operation
    if operator == '+':
        result = sum(numbers)
    elif operator == '*':
        result = 1
        for num in numbers:
            result *= num
    else:
        result = 0  # Unknown operator
    
    return result


def solve_part1(input_filename='day06-input.txt'):
    """Solve part 1."""
    lines = parse_input(input_filename)
    problems = parse_worksheet(lines)
    
    grand_total = 0
    for problem in problems:
        answer = solve_problem(problem)
        grand_total += answer
    
    return grand_total


def parse_worksheet_cephalopod(lines):
    """Parse the worksheet reading right-to-left in cephalopod math style.
    
    1. Split by all-space columns to get separate problems
    2. For each problem, read columns right-to-left
    3. Each column (top-to-bottom, ignoring spaces) forms one number
    4. Operator is in the last row
    """
    if not lines:
        return []
    
    # Find the maximum width
    max_width = max(len(line) for line in lines)
    
    # Pad all lines to the same width
    padded_lines = [line.ljust(max_width) for line in lines]
    
    # The last line contains operators
    operator_line = padded_lines[-1]
    number_lines = padded_lines[:-1]
    
    # Find all-space columns (separators)
    space_columns = []
    for col in range(max_width):
        if all(line[col] == ' ' for line in padded_lines):
            space_columns.append(col)
    
    # Split into problem ranges based on space columns
    problem_ranges = []
    start = 0
    for space_col in space_columns:
        if space_col > start:
            problem_ranges.append((start, space_col))
        start = space_col + 1
    # Add the last range
    if start < max_width:
        problem_ranges.append((start, max_width))
    
    # Process each problem
    problems = []
    for problem_start, problem_end in problem_ranges:
        # Find the operator in this range
        operator = None
        for c in range(problem_start, problem_end):
            if operator_line[c] in ['*', '+']:
                operator = operator_line[c]
                break
        
        if not operator:
            continue
        
        # Read columns right-to-left within this problem range
        # Each column (top-to-bottom, ignoring spaces) forms one number
        numbers = []
        for col in range(problem_end - 1, problem_start - 1, -1):
            # Read this column top-to-bottom, collecting digits
            digits = []
            for row_idx in range(len(number_lines)):
                char = number_lines[row_idx][col]
                if char.isdigit():
                    digits.append(char)
            
            # If we found digits, form a number
            if digits:
                number = int(''.join(digits))
                numbers.append(number)
        
        if numbers:
            problems.append((operator, numbers))
    
    return problems


def solve_problem_cephalopod(operator, numbers):
    """Solve a single cephalopod problem."""
    if not numbers:
        return 0
    
    if operator == '+':
        return sum(numbers)
    elif operator == '*':
        result = 1
        for num in numbers:
            result *= num
        return result
    
    return 0


def solve_part2(input_filename='day06-input.txt'):
    """Solve part 2."""
    lines = parse_input(input_filename)
    problems = parse_worksheet_cephalopod(lines)
    
    grand_total = 0
    for operator, numbers in problems:
        answer = solve_problem_cephalopod(operator, numbers)
        grand_total += answer
    
    return grand_total


if __name__ == "__main__":
    result1 = solve_part1()
    print(f"Part 1: {result1}")
    
    result2 = solve_part2()
    print(f"Part 2: {result2}")
