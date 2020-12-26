#!/usr/bin/env python3

import numpy as np


def run_round(board, stuck=False):
    size = board.shape[1]
    new_board = np.zeros(board.shape, dtype=bool)
    for r in range(size):
        for c in range(size):
            n_on = np.count_nonzero(board[max(0, r - 1):min(r + 2, size), max(0, c - 1):min(c + 2, size)])
            if board[r, c]:
                if 3 <= n_on <= 4:  # bump by one beause we know the center is on
                    new_board[r, c] = True
            else:
                if n_on == 3:
                    new_board[r, c] = True
    if stuck:
        new_board[0, 0] = True
        new_board[0, -1] = True
        new_board[-1, 0] = True
        new_board[-1, -1] = True
    return new_board


initial_board = np.zeros((100, 100), dtype=bool)

with open('input.txt', 'r') as f:
    for r, row in enumerate(f):
        for c, ch in enumerate(row.strip()):
            if ch == '#':
                initial_board[r, c] = True

board = initial_board
for _ in range(100):
    board = run_round(board)
print("No stuck lights", np.count_nonzero(board))

board = initial_board
board[0, 0] = True
board[0, -1] = True
board[-1, 0] = True
board[-1, -1] = True
for _ in range(100):
    board = run_round(board, True)
print("Corners Stuck", np.count_nonzero(board))
