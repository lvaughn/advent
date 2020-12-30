#!/usr/bin/env python3

pad = (
    (None, None, '1', None, None),
    (None, '2', '3', '4', None),
    ('5', '6', '7', '8', '9'),
    (None, 'A', 'B', 'C', None),
    (None, None, 'D', None, None)
)
row = 2
col = 0

combo = []
with open('input.txt', 'r') as f:
    for line in f:
        for c in line.strip():
            if c == 'U':
                new_row = max(0, row - 1)
                if pad[new_row][col] is not None:
                    row = new_row
            elif c == 'D':
                new_row = min(4, row + 1)
                if pad[new_row][col] is not None:
                    row = new_row
            elif c == 'L':
                new_col = max(0, col - 1)
                if pad[row][new_col] is not None:
                    col = new_col
            elif c == 'R':
                new_col = min(4, col + 1)
                if pad[row][new_col] is not None:
                    col = new_col
        combo.append(pad[row][col])

print(''.join(combo))
