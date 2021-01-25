#!/usr/bin/env python3

import numpy as np

points = []
with open('input.txt', 'r') as f:
    for line in f:
        points.append([int(a.strip()) for a in line.split(',')])

min_x = min(a[0] for a in points)
max_x = max(a[0] for a in points)
min_y = min(a[1] for a in points)
max_y = max(a[1] for a in points)

board = np.ones((max_x + 20, max_y + 20), dtype=int) * 10000 + 1000

for x in range(min_x - 2, max_x + 15):
    for y in range(min_y - 2, max_y + 15):
        dist = 0
        for pt_id, pt in enumerate(points):
            dist += abs(x - pt[0]) + abs(y - pt[1])
        board[x, y] = dist

print(np.count_nonzero(board < 10000))
