#!/usr/bin/env python3
from string import ascii_lowercase
from collections import deque
import numpy as np
import sys

letter_values = {'S': 0, 'E': 25}
for i, letter in enumerate(ascii_lowercase):
    letter_values[letter] = i


def is_valid(row, col, n_rows, n_cols):
    if row < 0 or col < 0:
        return False
    if row >= n_rows or col >= n_cols:
        return False
    return True


answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

for i, l in enumerate(lines):
    v = l.find('S')
    if v > -1:
        start_col = v
        start_row = i
    v = l.find('E')
    if v > -1:
        end_row = i
        end_col = v

rows = len(lines)
cols = len(lines[0])

visited = np.zeros((rows, cols), dtype=bool)

queue = deque([(start_row, start_col, [])])
while len(queue) > 0:
    row, col, so_far = queue.popleft()
    if row == end_row and col == end_col:
        print("Part 1", len(so_far))
        sys.exit()
    val = letter_values[lines[row][col]]
    if is_valid(row - 1, col, rows, cols):
        if not visited[row - 1, col]:
            if val + 1 >= letter_values[lines[row - 1][col]]:
                queue.append((row - 1, col, so_far + ['^']))
                visited[row - 1, col] = True
    if is_valid(row + 1, col, rows, cols):
        if not visited[row + 1, col]:
            if val + 1 >= letter_values[lines[row + 1][col]]:
                queue.append((row + 1, col, so_far + ['v']))
                visited[row + 1, col] = True
    if is_valid(row, col + 1, rows, cols):
        if not visited[row, col + 1]:
            if val + 1 >= letter_values[lines[row][col + 1]]:
                queue.append((row, col + 1, so_far + ['>']))
                visited[row, col + 1] = True
    if is_valid(row, col - 1, rows, cols):
        if not visited[row, col - 1]:
            if val + 1 >= letter_values[lines[row][col - 1]]:
                queue.append((row, col - 1, so_far + ['<']))
                visited[row, col - 1] = True
