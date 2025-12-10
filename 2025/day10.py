import os
import re
from itertools import product

def parse_input(input_filename):
    """Parse the input file into list of (target, buttons, joltage) tuples."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, input_filename)
    
    machines = []
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            # Extract indicator light pattern [...]
            pattern_match = re.search(r'\[([.#]+)\]', line)
            pattern = pattern_match.group(1)
            target = [1 if c == '#' else 0 for c in pattern]
            
            # Extract button schematics (...)
            buttons = []
            for btn_match in re.finditer(r'\(([0-9,]+)\)', line):
                indices = [int(x) for x in btn_match.group(1).split(',')]
                buttons.append(indices)
            
            # Extract joltage requirements {...}
            joltage_match = re.search(r'\{([0-9,]+)\}', line)
            joltage = [int(x) for x in joltage_match.group(1).split(',')]
            
            machines.append((target, buttons, joltage))
    
    return machines

def solve_machine(target, buttons):
    """Find minimum button presses to reach target state from all-off.
    
    Uses Gaussian elimination over GF(2) to find solutions,
    then finds the one with minimum number of presses.
    """
    n_lights = len(target)
    n_buttons = len(buttons)
    
    # Build the button matrix: each column is a button's effect
    # matrix[i][j] = 1 if button j toggles light i
    matrix = [[0] * n_buttons for _ in range(n_lights)]
    for j, btn in enumerate(buttons):
        for light_idx in btn:
            if light_idx < n_lights:
                matrix[light_idx][j] = 1
    
    # Augmented matrix [A | b] for Ax = b over GF(2)
    aug = [row[:] + [target[i]] for i, row in enumerate(matrix)]
    
    # Gaussian elimination over GF(2)
    pivot_cols = []
    row = 0
    for col in range(n_buttons):
        # Find pivot
        pivot_row = None
        for r in range(row, n_lights):
            if aug[r][col] == 1:
                pivot_row = r
                break
        
        if pivot_row is None:
            continue
        
        # Swap rows
        aug[row], aug[pivot_row] = aug[pivot_row], aug[row]
        pivot_cols.append(col)
        
        # Eliminate
        for r in range(n_lights):
            if r != row and aug[r][col] == 1:
                for c in range(n_buttons + 1):
                    aug[r][c] ^= aug[row][c]
        
        row += 1
    
    # Check for inconsistency (row of form [0 0 ... 0 | 1])
    for r in range(row, n_lights):
        if aug[r][n_buttons] == 1:
            return None  # No solution
    
    # Find free variables (columns not pivot columns)
    free_cols = [c for c in range(n_buttons) if c not in pivot_cols]
    
    # Try all combinations of free variables to find minimum solution
    min_presses = float('inf')
    
    for free_vals in product([0, 1], repeat=len(free_cols)):
        # Build solution
        solution = [0] * n_buttons
        for i, col in enumerate(free_cols):
            solution[col] = free_vals[i]
        
        # Back-substitute for pivot variables
        for i in range(len(pivot_cols) - 1, -1, -1):
            pivot_col = pivot_cols[i]
            val = aug[i][n_buttons]
            for c in range(pivot_col + 1, n_buttons):
                val ^= aug[i][c] * solution[c]
            solution[pivot_col] = val
        
        presses = sum(solution)
        min_presses = min(min_presses, presses)
    
    return min_presses

def solve_part1(input_filename='day10-input.txt'):
    """Find minimum total button presses to configure all machines."""
    machines = parse_input(input_filename)
    
    total = 0
    for target, buttons, joltage in machines:
        presses = solve_machine(target, buttons)
        if presses is not None:
            total += presses
    
    return total

def solve_joltage(joltage, buttons):
    """Find minimum button presses to reach joltage targets from all-zero.
    
    Uses direct Integer Linear Programming for optimal solution.
    """
    from scipy.optimize import milp, Bounds, LinearConstraint
    import numpy as np
    
    n_counters = len(joltage)
    n_buttons = len(buttons)
    
    if n_buttons == 0:
        # No buttons - check if all joltages are already 0
        return 0 if all(j == 0 for j in joltage) else None
    
    # Build the constraint matrix A where A[i][j] = 1 if button j affects counter i
    A = np.zeros((n_counters, n_buttons))
    for j, btn in enumerate(buttons):
        for counter_idx in btn:
            if counter_idx < n_counters:
                A[counter_idx, j] = 1
    
    b = np.array(joltage, dtype=float)
    
    # Objective: minimize sum of all button presses
    c = np.ones(n_buttons)
    
    # Equality constraints: A @ x == b
    constraints = LinearConstraint(A, b, b)
    
    # Bounds: x >= 0, with reasonable upper bound
    max_jolt = max(joltage) if joltage else 1
    large_bound = max_jolt * 100
    bounds = Bounds(lb=np.zeros(n_buttons), ub=np.full(n_buttons, large_bound))
    
    # All variables must be integers
    integrality = np.ones(n_buttons, dtype=int)
    
    result = milp(c, integrality=integrality, bounds=bounds, constraints=constraints)
    
    if result.success:
        solution = [int(round(v)) for v in result.x]
        # Verify the solution
        achieved = [0] * n_counters
        for j, presses in enumerate(solution):
            for counter_idx in buttons[j]:
                if counter_idx < n_counters:
                    achieved[counter_idx] += presses
        if achieved == list(joltage) and all(x >= 0 for x in solution):
            return sum(solution)
    
    return None

def solve_part2(input_filename='day10-input.txt'):
    """Find minimum total button presses to configure all joltage counters."""
    machines = parse_input(input_filename)
    
    total = 0
    for target, buttons, joltage in machines:
        presses = solve_joltage(joltage, buttons)
        if presses is not None:
            total += presses
    
    return total

if __name__ == "__main__":
    result1 = solve_part1()
    print(f"Part 1: {result1}")
    
    result2 = solve_part2()
    print(f"Part 2: {result2}")
