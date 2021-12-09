#!/usr/bin/env python3

import numpy as np
import re


def neighbors(r, c, shape):
    for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        new_row = r + dr
        if 0 <= new_row < shape[0]:
            new_col = c + dc
            if 0 <= new_col < shape[1]:
                yield new_row, new_col


def map_basin(r, c, extent, grid):
    if grid[r, c] == 9 or extent[r, c] == 1:
        return
    extent[r, c] = 1
    for nr, nc in neighbors(r, c, grid.shape):
        map_basin(nr, nc, extent, grid)


with open("input.txt", "r") as infile:
    lines = [[int(a) for a in line.strip()] for line in infile]
grid = np.array(lines, dtype=int)

total_risk = 0
low_points = []
for r in range(grid.shape[0]):
    for c in range(grid.shape[1]):
        is_low = True
        for nr, nc in neighbors(r, c, grid.shape):
            if grid[r, c] >= grid[nr, nc]:
                is_low = False
                break
        if is_low:
            total_risk += 1 + grid[r, c]
            low_points.append((r, c))

print(f"Part 1: {total_risk}")

basin_sizes = []
for basin in low_points:
    extent = np.zeros(grid.shape, dtype=int)
    map_basin(basin[0], basin[1], extent, grid)
    size = sum(sum(extent))
    basin_sizes.append(size)

basin_sizes.sort()
print(basin_sizes)
print(f"Part 2: {basin_sizes[-2] * basin_sizes[-1] * basin_sizes[-3]}")
