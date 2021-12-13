#!/usr/bin/env python3

import numpy as np
import re


def do_x_flip(x, grid):
    return np.clip(grid[:x, :] + np.flipud(grid[x + 1:, :]), 0, 1)


def do_y_flip(y, grid):
    return np.clip(np.fliplr(grid[:, :y]) + grid[:, y + 1:], 0, 1)


fold_re = re.compile(r'fold along (.)=(\d+)')
with open("input.txt", "r") as infile:
    points = []
    folds = []
    for line in infile:
        if not line.strip():
            pass
        elif line.startswith("fold"):
            m = fold_re.match(line)
            axis, loc = m[1], int(m[2])
            folds.append((axis, loc))
        else:
            x, y = [int(a) for a in line.split(',')]
            points.append((x, y))

max_x = max(a[0] for a in points) + 1
max_y = max(a[1] for a in points) + 1

sheet = np.zeros((max_x, max_y), dtype=int)
for x, y in points:
    sheet[x, y] = True

for axis, n in folds[:1]:
    print(f"Flipping on {axis} at {n} shape={sheet.shape}")
    if axis == 'x':
        sheet = do_x_flip(n, sheet)
    else:
        sheet = do_y_flip(n, sheet)

print(f"Part 1: {sum(sum(sheet))}")

for axis, n in folds[1:]:
    if axis == 'x':
        sheet = do_x_flip(n, sheet)
    else:
        sheet = do_y_flip(n, sheet)

for y in reversed(range(sheet.shape[1])):
    line = ''
    for x in range(sheet.shape[0]):
        if sheet[x, y] == 1:
            line += '*'
        else:
            line += ' '
    print(line)
