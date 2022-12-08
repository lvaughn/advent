#!/usr/bin/env python3

import numpy as np
import sys

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

grid = [[int(x) for x in l] for l in lines]
grid = np.array(grid, dtype=int)

visible = np.zeros(grid.shape, dtype=int)

visible[0, :] = 1
visible[-1, :] = 1
visible[:, 0] = 1
visible[:, -1] = 1

for r in range(1, grid.shape[0]-1):
    for c in range(1, grid.shape[1]-1):
        if all(grid[r, c] > grid[r, :c]) or \
            all(grid[r, c] > grid[r, c+1:]) or \
            all(grid[r, c] > grid[:r, c]) or \
            all(grid[r, c] > grid[r+1:, c]):
            visible[r, c] = 1

print("Part 1", sum(sum(visible)))
