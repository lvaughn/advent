#!/usr/bin/env python3

import numpy as np


def to_tupple(nparray):
    parts = []
    for i in range(nparray.shape[0]):
        parts.append(tuple(nparray[i, :]))
    return tuple(parts)


def to_array(s):
    rows = s.split('/')
    size = len(rows)
    board = np.zeros((size, size), dtype=bool)
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            if ch == '#':
                board[r, c] = True
    return board


mappings = {}
with open('input.txt', 'r') as f:
    for line in f:
        idx = line.index('=>')
        before = to_array(line[:idx].strip())
        after = to_array(line[idx + 2:].strip())
        flipped_before = np.fliplr(before)
        for i in range(4):
            key = to_tupple(np.rot90(before, i))
            if key not in mappings:
                mappings[key] = after
            key = to_tupple(np.rot90(flipped_before, i))
            if key not in mappings:
                mappings[key] = after

board = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]], dtype=bool)
for i in range(18):
    size = board.shape[0]
    if size % 2 == 0:
        new_board_size = (size // 2) * 3
        old_block = 2
        new_block = 3
    else:
        assert size % 3 == 0
        new_board_size = (size // 3) * 4
        old_block = 3
        new_block = 4
    new_board = np.zeros((new_board_size, new_board_size), dtype=bool)
    for r in range(size//old_block):
        for c in range(size // old_block):
            row = r * old_block
            col = c * old_block
            key = to_tupple(board[row:row+old_block,col:col+old_block])
            new_row = r * new_block
            new_col = c * new_block
            new_board[new_row:new_row+new_block, new_col:new_col + new_block] = mappings[key]
    board = new_board
    #print(new_board)
    print(i+1, np.count_nonzero(board))
