#!/usr/bin/env python3

import numpy as np

rows = []
with open('input.txt', 'r') as f:
    for line in f:
        rows.append(line.strip())

width = len(rows[0])
height = len(rows)
BUFFER = 50

# Create and load the board
board = np.zeros((height+2*BUFFER, width+2*BUFFER), dtype=bool)
for r, row in enumerate(rows):
    for c, ch in enumerate(row):
        if ch == '#':
            board[BUFFER+r, BUFFER+c] = True

directions = ['n', 'e', 's', 'w']
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir = 0
row = BUFFER + height // 2
col = BUFFER + width // 2
n_turned_on = 0
for burst in range(10000):
    if board[row, col]:
        dir = (dir + 1) % 4
        board[row, col] = False
    else:
        dir = (dir - 1) % 4
        board[row, col] = True
        n_turned_on += 1

    d_r, d_c = moves[dir]
    row += d_r
    col += d_c

print("Part 1", n_turned_on)
