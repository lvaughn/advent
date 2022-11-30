#!/usr/bin/env python3

import numpy as np

def decode(ch):
    if ch == '.':
        return 0
    if ch == '>':
        return 1
    if ch == 'v':
        return 2

def will_move_east(grid):
    will_move = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 1 and grid[r, (c+1)%cols] == 0:
                will_move.append((r, c))
    return will_move

def will_move_south(grid):
    will_move = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 2 and grid[(r+1)%rows, c] == 0:
                will_move.append((r, c))
    return will_move

def move_east(grid, to_move):
    for r, c in to_move:
        grid[r, c] = 0
        grid[r, (c+1) % grid.shape[1]] = 1

def move_south(grid, to_move):
    for r, c in to_move:
        grid[r, c] = 0
        grid[(r+1)%grid.shape[0], c] = 2

with open('input.txt', 'r') as infile:
    lines = [[decode(c) for c in line.strip()] for line in infile]

new_grid = np.array(lines, dtype=int)
grid = np.zeros((1, 1))

steps = 0
while not np.array_equal(new_grid, grid):
    grid = new_grid
    new_grid = grid.copy()

    move_east(new_grid, will_move_east(new_grid))
    move_south(new_grid, will_move_south(new_grid))

    steps += 1

print("Part 1", steps)
