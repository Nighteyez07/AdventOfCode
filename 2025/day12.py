import os


def parse_input(input_filename):
    """Parse the input file."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, input_filename)
    
    with open(input_file, 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    
    # Parse shapes and regions
    shapes = {}
    regions = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        if not line.strip():
            i += 1
            continue
        
        # Check if it's a shape definition (starts with number:)
        if ':' in line and line.split(':')[0].strip().isdigit():
            shape_idx = int(line.split(':')[0].strip())
            shape_lines = []
            i += 1
            # Read the shape pattern
            while i < len(lines) and lines[i].strip() and ':' not in lines[i]:
                shape_lines.append(lines[i])
                i += 1
            shapes[shape_idx] = shape_lines
        # Check if it's a region definition (starts with dimensions like 4x4:)
        elif 'x' in line and ':' in line:
            parts = line.split(':')
            dims = parts[0].strip().split('x')
            width = int(dims[0])
            height = int(dims[1])
            counts = list(map(int, parts[1].strip().split()))
            regions.append((width, height, counts))
            i += 1
        else:
            i += 1
    
    return shapes, regions


def get_shape_cells(shape_lines):
    """Extract the cells (coordinates) that are part of a shape."""
    cells = []
    for r, line in enumerate(shape_lines):
        for c, ch in enumerate(line):
            if ch == '#':
                cells.append((r, c))
    return cells


def rotate_90(cells):
    """Rotate cells 90 degrees clockwise."""
    return [(c, -r) for r, c in cells]


def flip_horizontal(cells):
    """Flip cells horizontally."""
    return [(r, -c) for r, c in cells]


def normalize_cells(cells):
    """Normalize cells so the top-left corner is at (0, 0)."""
    if not cells:
        return []
    min_r = min(r for r, c in cells)
    min_c = min(c for r, c in cells)
    return tuple(sorted((r - min_r, c - min_c) for r, c in cells))


def get_all_orientations(shape_lines):
    """Get all unique orientations (rotations and flips) of a shape."""
    cells = get_shape_cells(shape_lines)
    orientations = set()
    
    current = cells
    for _ in range(4):  # 4 rotations
        orientations.add(normalize_cells(current))
        orientations.add(normalize_cells(flip_horizontal(current)))
        current = rotate_90(current)
    
    return list(orientations)


def can_place(grid, cells, row, col):
    """Check if a shape can be placed at a given position."""
    # Early exit if empty
    if not cells:
        return False
    
    height = len(grid)
    width = len(grid[0])
    
    # Quick bounds check on extent
    max_dr = max(dr for dr, dc in cells)
    max_dc = max(dc for dr, dc in cells)
    if row + max_dr >= height or col + max_dc >= width:
        return False
    
    for dr, dc in cells:
        r, c = row + dr, col + dc
        if r < 0 or r >= height or c < 0 or c >= width:
            return False
        if grid[r][c] != '.':
            return False
    return True


def place_shape(grid, cells, row, col, mark):
    """Place a shape on the grid."""
    for dr, dc in cells:
        r, c = row + dr, col + dc
        grid[r][c] = mark


def remove_shape(grid, cells, row, col):
    """Remove a shape from the grid."""
    for dr, dc in cells:
        r, c = row + dr, col + dc
        grid[r][c] = '.'


def try_fit_presents(width, height, presents_list, shape_orientations):
    """Try to fit all presents into a region using backtracking."""
    grid = [['.' for _ in range(width)] for _ in range(height)]
    
    # Sort presents by size (larger first) for better pruning
    presents_with_sizes = []
    for shape_idx in presents_list:
        # Size is the number of cells in the shape
        size = len(shape_orientations[shape_idx][0])
        presents_with_sizes.append((size, shape_idx))
    presents_with_sizes.sort(reverse=True)
    sorted_presents = [shape_idx for _, shape_idx in presents_with_sizes]
    
    # For each shape, precompute valid positions for each orientation
    valid_positions = {}
    for shape_idx in set(sorted_presents):
        valid_positions[shape_idx] = []
        for orientation in shape_orientations[shape_idx]:
            positions = []
            # Only check positions where the shape could actually fit
            max_dr = max(dr for dr, dc in orientation) if orientation else 0
            max_dc = max(dc for dr, dc in orientation) if orientation else 0
            for row in range(height - max_dr):
                for col in range(width - max_dc):
                    positions.append((orientation, row, col))
            valid_positions[shape_idx].append(positions)
    
    def backtrack(present_idx):
        if present_idx >= len(sorted_presents):
            return True  # All presents placed successfully
        
        shape_idx = sorted_presents[present_idx]
        
        # Try each orientation with its valid positions
        for positions in valid_positions[shape_idx]:
            for orientation, row, col in positions:
                if can_place(grid, orientation, row, col):
                    place_shape(grid, orientation, row, col, str(present_idx))
                    
                    if backtrack(present_idx + 1):
                        return True
                    
                    remove_shape(grid, orientation, row, col)
        
        return False
    
    return backtrack(0)


def solve_part1(input_filename='day12-input.txt'):
    """Solve part 1."""
    shapes, regions = parse_input(input_filename)
    
    # Precompute all orientations for each shape
    shape_orientations = {}
    for idx, shape_lines in shapes.items():
        shape_orientations[idx] = get_all_orientations(shape_lines)
    
    count = 0
    total = len(regions)
    for i, (width, height, counts) in enumerate(regions):
        if i % 100 == 0:
            print(f"Progress: {i}/{total} regions, {count} successful...")
        
        # Build list of presents to place
        presents_list = []
        for shape_idx, quantity in enumerate(counts):
            for _ in range(quantity):
                presents_list.append(shape_idx)
        
        # Quick check: if total cells needed > grid size, skip
        total_needed = sum(len(shape_orientations[idx][0]) for idx in presents_list)
        if total_needed > width * height:
            continue
        
        # Try to fit all presents
        if try_fit_presents(width, height, presents_list, shape_orientations):
            count += 1
    
    return count


if __name__ == "__main__":
    result1 = solve_part1()
    print(f"Part 1: {result1}")
