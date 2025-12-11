"""Advent of Code 2025 - Day 11"""


def parse_input(filename='day11-input.txt'):
    """Parse the input file into a directed graph."""
    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')
    
    # Build adjacency list (directed graph)
    graph = {}
    for line in lines:
        parts = line.split(': ')
        source = parts[0]
        destinations = parts[1].split() if len(parts) > 1 else []
        if source not in graph:
            graph[source] = []
        graph[source].extend(destinations)
        # Ensure destination nodes exist in graph
        for dest in destinations:
            if dest not in graph:
                graph[dest] = []
    
    return graph


def count_paths(graph, start, end, required_nodes=None):
    """Count all paths from start to end using DFS with cycle detection.
    
    If required_nodes is provided, only count paths that visit all required nodes.
    """
    if required_nodes is None:
        required_nodes = frozenset()
    else:
        required_nodes = frozenset(required_nodes)
    
    # Memoization cache: (node, visited_required) -> count
    cache = {}
    
    def dfs(node, visited_required, path):
        # Update visited required nodes
        if node in required_nodes:
            visited_required = visited_required | frozenset({node})
        
        if node == end:
            # Only count if all required nodes were visited
            return 1 if visited_required == required_nodes else 0
        
        # Check cache
        cache_key = (node, visited_required)
        if cache_key in cache:
            return cache[cache_key]
        
        total = 0
        for neighbor in graph.get(node, []):
            if neighbor not in path:  # Avoid cycles
                total += dfs(neighbor, visited_required, path | {neighbor})
        
        cache[cache_key] = total
        return total
    
    return dfs(start, frozenset(), {start})


def solve_part1(input_filename='day11-input.txt'):
    """Solve Part 1 - count all paths from 'you' to 'out'."""
    graph = parse_input(input_filename)
    return count_paths(graph, 'you', 'out')


def solve_part2(input_filename='day11-input.txt'):
    """Solve Part 2 - count paths from 'svr' to 'out' that visit both 'dac' and 'fft'."""
    graph = parse_input(input_filename)
    required = {'dac', 'fft'}
    return count_paths(graph, 'svr', 'out', required_nodes=required)


if __name__ == "__main__":
    result1 = solve_part1()
    print(f"Part 1: {result1}")
    
    result2 = solve_part2()
    print(f"Part 2: {result2}")
