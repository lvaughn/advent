#!/usr/bin/env python3

import numpy as np
import sys


def walk_out(grid, x, y, dx, dy):
    steps = 0
    val = grid[x, y]
    x += dx
    y += dy
    while 0 <= x < grid.shape[0] and \
            0 <= y < grid.shape[1]:
        if grid[x, y] >= val:
            return steps + 1
        x += dx
        y += dy
        steps += 1
    return steps


with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

grid = [[int(x) for x in l] for l in lines]
grid = np.array(grid, dtype=int)

best = -1
for r in range(1, grid.shape[0] - 1):
    for c in range(1, grid.shape[1] - 1):
        best = max(best,
                   walk_out(grid, r, c, 1, 0) *
                   walk_out(grid, r, c, -1, 0) *
                   walk_out(grid, r, c, 0, 1) *
                   walk_out(grid, r, c, 0, -1))

print("Part 2", best)
