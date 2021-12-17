#!/usr/bin/env python3

import numpy as np
import re


def neighbors(x, y, shape):
    for dx in [-1, 0, 1]:
        new_x = x + dx
        if 0 <= new_x < shape[0]:
            for dy in [-1, 0, 1]:
                new_y = y + dy
                if 0 <= new_y < shape[1]:
                    if not (dx == 0 and dy == 0):
                        yield new_x, new_y


def do_step(grid):
    n_flashes = 0
    new_grid = grid + 1
    has_flashed = np.zeros(grid.shape, dtype=bool)
    xs, ys = np.nonzero(new_grid - 100 * has_flashed > 9)
    while len(xs) > 0:
        for x, y in zip(xs, ys):
            has_flashed[x, y] = True
            n_flashes += 1
            for nx, ny in neighbors(x, y, grid.shape):
                new_grid[nx, ny] += 1
        xs, ys = np.nonzero((new_grid - 100 * has_flashed) > 9)

    new_grid[has_flashed] = 0
    return n_flashes, new_grid


with open("input.txt", "r") as infile:
    lines = [[int(c) for c in line.strip()] for line in infile]
    starting_grid = np.array(lines, dtype=int)

grid = starting_grid.copy()
total_flashes = 0
for step in range(100):
    flashes, grid = do_step(grid)
    total_flashes += flashes
    # print(step + 1, flashes, total_flashes)
    # print(grid)
    # print()

print(f"Part 1: {total_flashes}")

grid = starting_grid.copy()
step = 0
while True:
    step += 1
    flashes, grid = do_step(grid)
    if flashes == grid.shape[0] * grid.shape[1]:
        print(f"Part 2: {step}")
        break
