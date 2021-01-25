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

board = np.ones((max_x + 3, max_y + 3), dtype=int) * -1

for x in range(min_x - 2, max_x + 3):
    for y in range(min_y - 2, max_y + 3):
        best_point = None
        best_dist = max_x + max_y + 100
        for pt_id, pt in enumerate(points):
            dist = abs(x - pt[0]) + abs(y - pt[1])
            if dist < best_dist:
                best_dist = dist
                best_point = pt_id
            elif dist == best_dist:
                best_point = -2  # Mark it as a tie
        board[x, y] = best_point

infinite = set()
for pt_id in board[min_x - 2, :]:
    infinite.add(pt_id)
for pt_id in board[min_x + 2, :]:
    infinite.add(pt_id)
for pt_id in board[:, min_y - 2]:
    infinite.add(pt_id)
for pt_id in board[:, min_y + 2]:
    infinite.add(pt_id)

best_pt = None
best_area = -1
for pt_id in range(len(points)):
    if pt_id not in infinite:
        area = np.count_nonzero(board == pt_id)
        if area > best_area:
            best_area = area
            best_pt = pt_id
print(best_area)
