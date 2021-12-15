#!/usr/bin/env python3

import numpy as np
from collections import deque


def get_neighbors(row, col):
    global ROWS, COLS
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        r = row + dr
        c = col + dc
        if 0 <= r < ROWS and 0 <= c < COLS:
            yield r, c


with open("input.txt", "r") as infile:
    lines = [[int(a) for a in line.strip()] for line in infile]

grid = np.array(lines, dtype=int)

answer = np.zeros(grid.shape, dtype=int)
ROWS, COLS = grid.shape
answer[-1, -1] = grid[-1, -1]
queue = deque()
queue.append((ROWS - 1, COLS - 1))
while len(queue) > 0:
    row, col = queue.popleft()
    for r, c in get_neighbors(row, col):
        risk = answer[row, col] + grid[r, c]
        if answer[r, c] == 0 or answer[r, c] > risk:
            answer[r, c] = risk
            queue.append((r, c))

print(answer[0, 0] - grid[0, 0])
