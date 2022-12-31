#!/usr/bin/env python3
import numpy as np
import sys

B_UP = 1
B_DOWN = 2
B_LEFT = 4
B_RIGHT = 8

def get_next_board(board: np.array) -> np.array:
    new_board = np.zeros(board.shape, dtype=int)
    n_rows, n_cols = board.shape
    for r in range(n_rows):
        for c in range(n_cols):
            val = board[r, c]
            if val == 100:
                new_board[r, c] = 100
            else:
                if val & B_UP:
                    if r == 1:
                        new_board[n_rows-2, c] += B_UP
                    else:
                        new_board[r-1, c] += B_UP
                if val & B_DOWN:
                    if r == n_rows - 2:
                        new_board[1, c] += B_DOWN
                    else:
                        new_board[r + 1, c] += B_DOWN
                if val & B_LEFT:
                    if c == 1:
                        new_board[r, n_cols - 2] += B_LEFT
                    else:
                        new_board[r, c-1] += B_LEFT
                if val & B_RIGHT:
                    if c == n_cols - 2:
                        new_board[r, 1] += B_RIGHT
                    else:
                        new_board[r, c+1] += B_RIGHT
    return new_board

def get_moves(board, row, col):
    if board[row, col] == 0:  # Wait
        yield row, col
    if row > 0 and board[row - 1, col] == 0:  # Up
        yield row - 1, col
    if row < board.shape[0] - 1 and board[row + 1, col] == 0:  # Down
        yield row + 1, col
    if board[row, col + 1] == 0:  # Right
        yield row, col + 1
    if board[row, col - 1] == 0:  # Left
        yield row, col - 1


with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

board = np.zeros((len(lines), len(lines[0])), dtype=int)
char_map = {'.': 0, '#': 100, '^': B_UP, 'v': B_DOWN, '>': B_RIGHT, '<': B_LEFT}
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        board[r, c] = char_map[ch]

starting_location = (0, 1)
ending_location = (board.shape[0]-1, board.shape[1]-2)
rounds = 0
starting_pos = set([starting_location])
while ending_location not in starting_pos:
    rounds += 1
    new_pos = set()
    board = get_next_board(board)
    for row, col in starting_pos:
        for p in get_moves(board, row, col):
            new_pos.add(p)
    starting_pos = new_pos

# Go back
starting_pos = set([ending_location])
while starting_location not in starting_pos:
    rounds += 1
    new_pos = set()
    board = get_next_board(board)
    for row, col in starting_pos:
        for p in get_moves(board, row, col):
            new_pos.add(p)
    starting_pos = new_pos

# Return to end
starting_pos = set([starting_location])
while ending_location not in starting_pos:
    rounds += 1
    new_pos = set()
    board = get_next_board(board)
    for row, col in starting_pos:
        for p in get_moves(board, row, col):
            new_pos.add(p)
    starting_pos = new_pos

print("Part 2", rounds)




