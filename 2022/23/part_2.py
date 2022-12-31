#!/usr/bin/env python3
import numpy as np
import sys

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

height = len(lines)
width = len(lines[1])

grid = np.zeros((height, width), dtype=int)
for r, line in enumerate(lines):
    for c, val in enumerate(line):
        if val == '#':
            grid[r, c] = 1

directions = ['n', 's', 'w', 'e', 'n', 's', 'w', 'e']


def print_grid(grid: np.array):
    for r in range(grid.shape[0]):
        s = ''
        for c in range(grid.shape[1]):
            if grid[r, c] == 1:
                s += '#'
            else:
                s += '.'
        print(s)


def do_round(grid: np.array, round_no: int) -> np.array:
    # Resize grid if needed
    if np.any(grid[0, :] != 0) or np.any(grid[-1, :] != 0) or np.any(grid[:, 0] != 0) or np.any(grid[:, -1] != 0):
        new_grid = np.zeros((grid.shape[0] + 2, grid.shape[1] + 2), dtype=int)
        new_grid[1:-1, 1:-1] = grid
        grid = new_grid

    proposed = np.zeros(grid.shape, dtype=int)
    for r in range(1, grid.shape[0] - 1):
        for c in range(1, grid.shape[1] - 1):
            if grid[r, c] == 1:
                if np.sum(grid[r - 1:r + 2, c - 1:c + 2]) > 1:
                    # We have something next to it
                    start = round_no % 4
                    for dir in directions[start:start + 4]:
                        if dir == 'n':
                            if sum(grid[r - 1, c - 1:c + 2]) == 0:
                                proposed[r - 1, c] += 1
                                break
                        if dir == 'e':
                            if sum(grid[r - 1:r + 2, c + 1]) == 0:
                                proposed[r, c + 1] += 1
                                break
                        if dir == 's':
                            if sum(grid[r + 1, c - 1:c + 2]) == 0:
                                proposed[r + 1, c] += 1
                                break
                        if dir == 'w':
                            if sum(grid[r - 1:r + 2, c - 1]) == 0:
                                proposed[r, c - 1] += 1
                                break
    new_grid = np.zeros(grid.shape, dtype=int)
    for r in range(1, grid.shape[0] - 1):
        for c in range(1, grid.shape[1] - 1):
            if grid[r, c] == 1:
                if np.sum(grid[r - 1:r + 2, c - 1:c + 2]) == 1:
                    new_grid[r, c] = 1
                else:
                    start = round_no % 4
                    moved = False
                    for dir in directions[start:start + 4]:
                        if dir == 'n':
                            if sum(grid[r - 1, c - 1:c + 2]) == 0:
                                moved = True
                                if proposed[r - 1, c] == 1:
                                    new_grid[r - 1, c] = 1
                                else:
                                    new_grid[r, c] = 1
                                break
                        if dir == 'e':
                            if sum(grid[r - 1:r + 2, c + 1]) == 0:
                                moved = True
                                if proposed[r, c + 1] == 1:
                                    new_grid[r, c + 1] = 1
                                else:
                                    new_grid[r, c] = 1
                                break
                        if dir == 's':
                            if sum(grid[r + 1, c - 1:c + 2]) == 0:
                                moved = True
                                if proposed[r + 1, c] == 1:
                                    new_grid[r + 1, c] = 1
                                else:
                                    new_grid[r, c] = 1
                                break
                        if dir == 'w':
                            if sum(grid[r - 1:r + 2, c - 1]) == 0:
                                moved = True
                                if proposed[r, c - 1] == 1:
                                    new_grid[r, c - 1] = 1
                                else:
                                    new_grid[r, c] = 1
                                break
                    if not moved:
                        new_grid[r, c] = 1

    return new_grid


rounds = 1
new_grid = do_round(grid, rounds - 1)
while not np.array_equal(new_grid, grid):
    grid = new_grid
    rounds += 1
    new_grid = do_round(grid, rounds - 1)

print("Part 2", rounds)
