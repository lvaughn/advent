#!/usr/bin/env python3
from collections import deque
import numpy as np
import sys


def get_surface_area(grid, loc):
    x, y, z = loc
    result = 0
    if x == 0 or grid[x - 1, y, z] == 2:
        result += 1
    if grid[x + 1, y, z] == 2:
        result += 1
    if y == 0 or grid[x, y - 1, z] == 2:
        result += 1
    if grid[x, y + 1, z] == 2:
        result += 1
    if z == 0 or grid[x, y, z - 1] == 2:
        result += 1
    if grid[x, y, z + 1] == 2:
        result += 1
    return result


def fill_all(grid, x, y, z):
    queue = deque([(x, y, z)])
    while (len(queue) > 0):
        a, b, c = queue.popleft()
        if not 0 <= a < grid.shape[0]:
            continue
        if not 0 <= b < grid.shape[1]:
            continue
        if not 0 <= c < grid.shape[2]:
            continue
        if grid[a, b, c] != 0:
            continue
        grid[a, b, c] = 2
        queue.append((a - 1, b, c))
        queue.append((a + 1, b, c))
        queue.append((a, b - 1, c))
        queue.append((a, b + 1, c))
        queue.append((a, b, c - 1))
        queue.append((a, b, c + 1))


answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    triples = [list(map(int, l.split(','))) for l in lines]

max_dim = -1
for trip in triples:
    max_dim = max(max_dim, max(trip))

grid = np.zeros((max_dim + 4, max_dim + 4, max_dim + 4))
for x, y, z in triples:
    grid[x, y, z] = 1

fill_all(grid, 0, 0, 0)

for trip in triples:
    answer += get_surface_area(grid, trip)
print("Part 2", answer)
