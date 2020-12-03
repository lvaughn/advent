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
        c += 3
        if c >= len(rows[r]):
            c = c % len(rows[r])
        r += 1
    return n_trees


print(check_slope(3, 1))
