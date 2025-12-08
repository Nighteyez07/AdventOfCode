import os
import math
from collections import defaultdict


def parse_input(input_filename):
    """Parse the input file into list of (x, y, z) coordinates."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, input_filename)
    
    coords = []
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                x, y, z = map(int, line.split(','))
                coords.append((x, y, z))
    
    return coords


def distance(p1, p2):
    """Calculate Euclidean distance between two 3D points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)


class UnionFind:
    """Union-Find data structure for tracking circuits."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Union two sets. Returns True if they were in different sets."""
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True
    
    def get_circuit_sizes(self):
        """Get sizes of all circuits."""
        sizes = defaultdict(int)
        for i in range(len(self.parent)):
            root = self.find(i)
            sizes[root] = self.size[root]
        return list(sizes.values())


def solve_part1(input_filename='day08-input.txt', num_connections=1000):
    """Connect the closest pairs and return product of 3 largest circuit sizes."""
    coords = parse_input(input_filename)
    n = len(coords)
    
    # Calculate all pairwise distances
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(coords[i], coords[j])
            distances.append((dist, i, j))
    
    # Sort by distance
    distances.sort()
    
    # Use Union-Find to connect pairs
    uf = UnionFind(n)
    
    # Process the first num_connections pairs (whether they connect or not)
    for idx in range(min(num_connections, len(distances))):
        dist, i, j = distances[idx]
        uf.union(i, j)  # May or may not actually connect
    
    # Get the 3 largest circuit sizes and multiply
    sizes = sorted(uf.get_circuit_sizes(), reverse=True)
    # Pad with 1s if we have fewer than 3 circuits
    while len(sizes) < 3:
        sizes.append(1)
    return sizes[0] * sizes[1] * sizes[2]


def solve_part2(input_filename='day08-input.txt'):
    """Connect all junction boxes into one circuit, return product of X coords of last pair."""
    coords = parse_input(input_filename)
    n = len(coords)
    
    # Calculate all pairwise distances
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(coords[i], coords[j])
            distances.append((dist, i, j))
    
    # Sort by distance
    distances.sort()
    
    # Use Union-Find to connect pairs until all are in one circuit
    uf = UnionFind(n)
    num_circuits = n  # Start with n separate circuits
    last_i, last_j = 0, 0
    
    for dist, i, j in distances:
        if uf.union(i, j):
            # Successfully connected two different circuits
            num_circuits -= 1
            last_i, last_j = i, j
            
            # All connected when we have just one circuit
            if num_circuits == 1:
                break
    
    # Return product of X coordinates of last connected pair
    return coords[last_i][0] * coords[last_j][0]


if __name__ == "__main__":
    result1 = solve_part1()
    print(f"Part 1: {result1}")
    
    result2 = solve_part2()
    print(f"Part 2: {result2}")
