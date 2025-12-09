import os

def parse_input(input_filename):
    """Parse the input file into list of (x, y) coordinates of red tiles."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, input_filename)
    
    coords = []
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                x, y = map(int, line.split(','))
                coords.append((x, y))
    return coords

def solve_part1(input_filename='day09-input.txt'):
    """Find largest rectangle using two red tiles as opposite corners."""
    coords = parse_input(input_filename)
    
    # For each pair of red tiles, calculate the rectangle area
    # Rectangle area includes boundaries: (|x2 - x1| + 1) * (|y2 - y1| + 1)
    # We need the tiles to be opposite corners (not same row/column)
    max_area = 0
    n = len(coords)
    
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            
            # Opposite corners means different x AND different y
            if x1 != x2 and y1 != y2:
                area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
                max_area = max(max_area, area)
    
    return max_area

def solve_part2(input_filename='day09-input.txt'):
    """Find largest rectangle using only red and green tiles."""
    red_tiles = parse_input(input_filename)
    n = len(red_tiles)
    
    # Build edges between consecutive red tiles
    edges = []
    for i in range(n):
        p1 = red_tiles[i]
        p2 = red_tiles[(i + 1) % n]
        edges.append((p1, p2))
    
    # Collect all unique x and y coordinates from red tiles
    # These define the grid lines we care about
    x_coords = sorted(set(p[0] for p in red_tiles))
    y_coords = sorted(set(p[1] for p in red_tiles))
    
    def point_in_polygon(x, y):
        """Check if point is inside or on the polygon using ray casting."""
        # First check if on an edge
        for (x1, y1), (x2, y2) in edges:
            if x1 == x2:  # Vertical edge
                if x == x1 and min(y1, y2) <= y <= max(y1, y2):
                    return True
            else:  # Horizontal edge  
                if y == y1 and min(x1, x2) <= x <= max(x1, x2):
                    return True
        
        # Ray casting to the right
        crossings = 0
        for (x1, y1), (x2, y2) in edges:
            if x1 == x2 and x1 > x:  # Vertical edge to the right
                y_min, y_max = min(y1, y2), max(y1, y2)
                if y_min <= y < y_max:
                    crossings += 1
        return crossings % 2 == 1
    
    def rectangle_in_polygon(rx1, ry1, rx2, ry2):
        """Check if entire rectangle is inside the polygon.
        
        For a rectilinear polygon made of axis-aligned edges,
        a rectangle is fully inside if:
        1. All 4 corners are inside/on the polygon
        2. No polygon edge crosses through the rectangle interior
        """
        # Check all 4 corners
        corners = [(rx1, ry1), (rx1, ry2), (rx2, ry1), (rx2, ry2)]
        for cx, cy in corners:
            if not point_in_polygon(cx, cy):
                return False
        
        # Check if any polygon edge crosses through the rectangle
        for (x1, y1), (x2, y2) in edges:
            if x1 == x2:  # Vertical edge
                # Does this vertical edge cross through rectangle horizontally?
                if rx1 < x1 < rx2:  # Edge x is strictly inside rectangle x range
                    edge_y_min, edge_y_max = min(y1, y2), max(y1, y2)
                    # Check if edge overlaps with rectangle y range
                    if edge_y_min < ry2 and edge_y_max > ry1:
                        return False
            else:  # Horizontal edge
                # Does this horizontal edge cross through rectangle vertically?
                if ry1 < y1 < ry2:  # Edge y is strictly inside rectangle y range
                    edge_x_min, edge_x_max = min(x1, x2), max(x1, x2)
                    # Check if edge overlaps with rectangle x range
                    if edge_x_min < rx2 and edge_x_max > rx1:
                        return False
        
        return True
    
    # For each pair of red tiles as opposite corners, check if rectangle is valid
    max_area = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]
            
            # Must be opposite corners
            if x1 == x2 or y1 == y2:
                continue
            
            rx1, rx2 = min(x1, x2), max(x1, x2)
            ry1, ry2 = min(y1, y2), max(y1, y2)
            
            if rectangle_in_polygon(rx1, ry1, rx2, ry2):
                area = (rx2 - rx1 + 1) * (ry2 - ry1 + 1)
                max_area = max(max_area, area)
    
    return max_area

if __name__ == "__main__":
    result1 = solve_part1()
    print(f"Part 1: {result1}")
    
    result2 = solve_part2()
    print(f"Part 2: {result2}")
