#!/usr/bin/env python3
from collections import deque
import numpy as np
import sys

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

height = len(lines)
width = len(lines[0])

def get_starting_points(grid, r, c):
    results = []
    if r > 0 and lines[r-1][c] in ('|', '7', 'F', 'S'):
        results.append((r-1, c))
    if r < height - 1 and lines[r+1][c] in ('|', 'J', 'L', 'S'):
        results.append((r+1, c))
    if c > 0 and lines[r][c-1] in ('-', 'L', 'F', 'S'):
        results.append((r, c-1))
    if c < width - 1 and lines[r][c+1] in ('-', '7', 'J', 'S'):
        results.append((r, c+1))
    assert len(results) == 2, (r, c, results)
    return results

def get_adjoining_points(grid, r, c):
    ch = grid[r][c]
    if ch == '|':
        return [(r-1, c), (r+1, c)]
    if ch == '-':
        return [(r, c-1), (r, c+1)]
    if ch == '7':
        return [(r+1, c), (r, c-1)]
    if ch == 'L': 
        return [(r-1, c), (r, c+1)]
    if ch == 'F':
        return [(r+1, c), (r, c+1)]
    if ch == 'J':
        return [(r-1, c), (r, c-1)]
    assert False, f"Bad location {r},{c}"
    
def find_next(grid, path):
    loc = path[-1]
    pts = get_adjoining_points(grid, loc[0], loc[1])
    if pts[0] == path[-2]:
        return pts[1]
    return pts[0]

for r in range(height):
    for c in range(width):
        if lines[r][c] == 'S':
            start_r, start_c = r, c

next_points = get_starting_points(lines, start_r, start_c)
path_1 = [(start_r, start_c), next_points[0]]
path_2 = [(start_r, start_c), next_points[1]]

while path_1[-1] not in path_2:
    path_1.append(find_next(lines, path_1))
    path_2.append(find_next(lines, path_2))
    
print("Part 1", len(path_1) - 1)

def map_point(r, c):
    return 2*r+1, 2*c+1

def fill(grid, r, c):
    if grid[r, c] != 0:
        return
    queue = deque([(r, c)])
    while len(queue) > 0:
        r, c = queue.popleft()
        if grid[r, c] != 0:
            continue
        grid[r, c] = 2
        if r > 0 and grid[r-1, c] == 0:
            queue.append((r-1, c))
        if r < grid.shape[0] - 1 and grid[r+1, c] == 0:
            queue.append((r+1, c))
        if c > 0 and grid[r, c-1] == 0:
            queue.append((r, c-1))
        if c < grid.shape[1] - 1 and grid[r, c+1] == 0:
            queue.append((r, c+1))
    

def draw_lines(grid, path):
    for src, dest in zip(path[:-1], path[1:]):
        if src[0] == dest[0]: # Same row
            min_col = min(src[1], dest[1])
            max_col = max(src[1], dest[1])
            grid[2*src[0]+1, 2*min_col+1:2*max_col + 2] = 1
        else:
            assert src[1] == dest[1]
            min_row = min(src[0], dest[0])
            max_row = max(src[0], dest[0])
            grid[2*min_row+1:2*max_row+2, 2*src[1]+1] = 1

new_grid = np.zeros((height*2+1, width*2+1), dtype=int)
draw_lines(new_grid, path_1)
draw_lines(new_grid, path_2)
fill(new_grid, 0, 0) # The outside rows are connect4ed, so one point is enough
    
answer = 0
for r in range(height):
    for c in range(width):
        if (r, c) not in path_1 and (r, c) not in path_2:
            mapped_r, mapped_c = map_point(r, c)
            if new_grid[mapped_r, mapped_c] == 0:
                answer += 1
                                
print("Part 2", answer)



    




    
