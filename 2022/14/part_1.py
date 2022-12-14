#!/usr/bin/env python3
import numpy as np
import sys

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

X_OFFSET = 480
grid = np.zeros((80, 170), dtype=int)


# X_OFFSET = 495
# grid = np.zeros((10, 12), dtype=int)

def add_sand(gr, x, y):
    # Returns true if the sand goes to the bottom
    while y < grid.shape[1] - 1:
        if gr[x - X_OFFSET, y + 1] == 0:
            y += 1
        elif gr[x - X_OFFSET - 1, y + 1] == 0:  # Left
            x -= 1
            y += 1
        elif gr[x - X_OFFSET + 1, y + 1] == 0:  # Right
            x += 1
            y += 1
        else:
            gr[x - X_OFFSET, y] = 2
            return True
    return False


for l in lines:
    parts = l.split(' -> ')
    start_x, start_y = map(int, parts[0].split(','))
    for p in parts[1:]:
        x, y = map(int, p.split(','))
        if x == start_x:
            min_y = min(y, start_y)
            max_y = max(y, start_y)
            for i in range(min_y, max_y + 1):
                # print(x-X_OFFSET, x, i)
                grid[x - X_OFFSET, i] = 1
        else:
            assert y == start_y
            min_x = min(x, start_x)
            max_x = max(x, start_x)
            for i in range(min_x, max_x + 1):
                grid[i - X_OFFSET, y] = 1
        start_x, start_y = x, y

while add_sand(grid, 500, 0):
    answer += 1

print("Part 1", answer)
