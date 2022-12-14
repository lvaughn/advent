#!/usr/bin/env python3
import numpy as np
import sys

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

X_OFFSET = 300
grid = np.zeros((400, 175), dtype=int)


# Testing setup
# X_OFFSET = 480
# grid = np.zeros((40, 15), dtype=int)

def add_sand(gr, x, y):
    # Returns the location where the last grain was deposited
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
            return x, y
    return False


largest_y = -1
for l in lines:
    parts = l.split(' -> ')
    start_x, start_y = map(int, parts[0].split(','))
    largest_y = max(start_y, largest_y)
    for p in parts[1:]:
        x, y = map(int, p.split(','))
        largest_y = max(y, largest_y)
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
            # print("LGV", min_x, max_x)
            for i in range(min_x, max_x + 1):
                # print(i - X_OFFSET, i, y)
                grid[i - X_OFFSET, y] = 1
        start_x, start_y = x, y

grid[:, largest_y + 2] = 1
while add_sand(grid, 500, 0) != (500, 0):
    answer += 1
answer += 1

# for y in range(grid.shape[1]):
#     l = ""
#     for x in range(grid.shape[0]):
#         if grid[x, y] == 0:
#             l += "."
#         elif grid[x, y] == 1:
#             l += '#'
#         else:
#             assert grid[x, y] == 2
#             l += 'o'
#     print(l)

print("Part 2", answer)
