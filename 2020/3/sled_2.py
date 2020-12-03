#!/usr/bin/env python3

# Load the board
rows = []
with open('input', 'r') as infile:
    for l in infile:
        rows.append(l.strip())


def check_slope(right, down):
    r = 0
    c = 0
    n_trees = 0

    while r < len(rows):
        if rows[r][c] == '#':
            n_trees += 1
        c += right
        if c >= len(rows[r]):
            c = c % len(rows[r])
        r += down
    return n_trees


values = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
acc = 1
for r, d in values:
    acc *= check_slope(r, d)
print(acc)
