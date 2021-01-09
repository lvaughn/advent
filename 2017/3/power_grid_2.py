#!/usr/bin/env python3

import numpy as np

SIZE = 20
target = 361527

board = np.zeros((SIZE, SIZE), dtype=int)
x, y = SIZE // 2, SIZE // 2
board[x, y] = 1
x += 1
board[x, y] = 1
dir = 'n'
toMove = 1
last_written = 1
while last_written <= target:
    if dir == 'e':
        for _ in range(toMove):
            x += 1
            last_written = np.sum(board[x - 1:x + 2, y - 1:y + 2])
            board[x, y] = last_written
            if last_written > target:
                break
        dir = 'n'
    elif dir == 'n':
        for _ in range(toMove):
            y += 1
            last_written = np.sum(board[x - 1:x + 2, y - 1:y + 2])
            board[x, y] = last_written
            if last_written > target:
                break
        toMove += 1
        dir = 'w'
    elif dir == 'w':
        for _ in range(toMove):
            x -= 1
            last_written = np.sum(board[x - 1:x + 2, y - 1:y + 2])
            board[x, y] = last_written
            if last_written > target:
                break
        dir = 's'
    elif dir == 's':
        for _ in range(toMove):
            y -= 1
            last_written = np.sum(board[x - 1:x + 2, y - 1:y + 2])
            board[x, y] = last_written
            if last_written > target:
                break
        toMove += 1
        dir = 'e'

print(last_written)
