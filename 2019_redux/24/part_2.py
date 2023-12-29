#!/usr/bin/env python3
import numpy as np
import sys

def get_adjacent_cells(shape, row, col, level):
    rows, cols, levels = shape 
    if row == 2 and col == 2:
        return []
    # Add the ones they all have
    result = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_r, new_c = row + dr, col + dc 
        if new_r == 2 and new_c == 2: # We'll get these later
            continue
        if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
            # We'll also get these later
            continue 
        result.append((new_r, new_c, level))
    
    # Now do the other levels 
    # First, if we're on the outside, add that single cell
    if row == 0:
        result.append((1, 2, level - 1))
    if col == 0:
        result.append((2, 1, level - 1))
    if row == rows - 1:
        result.append((3, 2, level - 1))
    if col == cols - 1:
        result.append((2, 3, level - 1))
        
    # Now, if we're on the inside, add 5(!) cells from level n+1
    if row == 1 and col == 2:
        for c in range(cols):
            result.append((0, c, level + 1))
    if row == 3 and col == 2:
        for c in range(cols):
            result.append((rows - 1, c, level + 1))
    if row == 2 and col == 1:
        for r in range(rows):
            result.append((r, 0, level + 1))
    if row == 2 and col == 3:
        for r in range(rows):
            result.append((r, cols-1, level + 1))
    return result

def step(grid):
    new_grid = np.zeros(grid.shape, dtype=int)
    rows, cols, levels = grid.shape
    for l in range(1, levels-1):
        for r in range(rows):
            for c in range(cols):
                n_adj = 0
                for ar, ac, al in get_adjacent_cells(grid.shape, r, c, l):
                    n_adj += grid[ar, ac, al]
                if grid[r,c,l] == 1 and n_adj == 1:
                    new_grid[r,c,l] = 1
                if grid[r,c,l] == 0 and n_adj in (1, 2):
                    new_grid[r,c,l] = 1
    return new_grid
 
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
height = len(lines)
width = len(lines[0])
rounds = int(sys.argv[2])

grid = np.zeros((height, width, 2*rounds+1), dtype=int)
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == '#':
            grid[r, c, rounds] = 1

for i in range(rounds):
    grid = step(grid)
    
print("Part 2", grid.sum())

