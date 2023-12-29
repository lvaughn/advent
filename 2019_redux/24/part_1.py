#!/usr/bin/env python3
import numpy as np
import sys


def step(grid):
    new_grid = np.zeros(grid.shape, dtype=int)
    for r in range(1, 6):
        for c in range(1, 6):
            adj = grid[r-1, c] + grid[r+1, c] + grid[r, c+1] + grid[r, c-1]
            if grid[r,c] == 1 and adj == 1:
                new_grid[r, c] = 1
            if  grid[r,c] == 0 and (adj == 1 or adj == 2):
                new_grid[r, c] = 1
    return new_grid
 
def to_tuple(grid):
     return tuple(grid[1:6,1:6].reshape((25,)))   
 
def get_biodiversity(values):
    answer = 0
    for i, val in enumerate(values):
        if val == 1:
            answer += 2**i 
    return answer             

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
height = len(lines)
width = len(lines[0])

grid = np.zeros((height+2, width+2), dtype=int)
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == '#':
            grid[r+1, c+1] = 1

seen = set()
tup = to_tuple(grid)
while tup not in seen:
    seen.add(tup)
    grid = step(grid)
    tup = to_tuple(grid)

print("Part 1", get_biodiversity(tup))
