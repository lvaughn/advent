#!/usr/bin/env python3

import numpy as np

rows = []
with open('input.txt', 'r') as f:
    for line in f:
        rows.append(line.strip())

width = len(rows[0])
height = len(rows)
BUFFER = 200

# Create and load the board
board = np.zeros((height + 2 * BUFFER, width + 2 * BUFFER), dtype=int)
for r, row in enumerate(rows):
    for c, ch in enumerate(row):
        if ch == '#':
            board[BUFFER + r, BUFFER + c] = 1

# Clean = 0
# Infected = 1
# flagged = 2
# weakend = 3

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir = 0
row = BUFFER + height // 2
col = BUFFER + width // 2
n_infected = 0
for burst in range(10000000):
    if board[row, col] == 0:  # Clean
        dir = (dir - 1) % 4
        board[row, col] = 3
    elif board[row, col] == 1:  # Infected
        dir = (dir + 1) % 4
        board[row, col] = 2
    elif board[row, col] == 2:  # Flagged
        dir = (dir + 2) % 4
        board[row, col] = 0
    else:  # Weakened
        # No turn
        n_infected += 1
        board[row, col] = 1

    d_r, d_c = moves[dir]
    row += d_r
    col += d_c

print("Part 2", n_infected)
