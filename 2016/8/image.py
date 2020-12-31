#!/usr/bin/env python3

import numpy as np
import re

HEIGHT = 6
WIDTH = 50

board = np.zeros((HEIGHT, WIDTH), dtype=bool)


def print_board():
    for r in range(board.shape[0]):
        line = ''
        for c in range(board.shape[1]):
            if board[r, c]:
                line += '#'
            else:
                line += '.'
        print(line)


with open('input.txt', 'r') as f:
    rect_re = re.compile(r'rect\s+(\d+)x(\d+)')
    rotate_re = re.compile(r'rotate\s+(row|column)\s+(x|y)=(\d+)\s+by\s+(\d+)')
    for line in f:
        if line.startswith('rect'):
            m = rect_re.match(line)
            board[:int(m[2]), :int(m[1])] = True
        else:  # Rotate
            m = rotate_re.match(line)
            if m[1] == 'row':
                row = int(m[3])
                shift = int(m[4])
                current = np.copy(board[row, :])
                board[row, shift:] = current[:len(current) - shift]
                board[row, :shift] = current[-shift:]
            else:
                col = int(m[3])
                shift = int(m[4])
                current = np.copy(board[:, col])
                board[shift:, col] = current[:len(current) - shift]
                board[:shift, col] = current[-shift:]
print_board()
print(np.count_nonzero(board))
