#!/usr/bin/env python3

import numpy as np
import re

import_re = re.compile(r'(\d+),(\d+)\D*(\d+),(\d+)')

line_segments = []
with open("input.txt", "r") as infile:
    for line in infile:
        m = import_re.match(line)
        segment = ((int(m[1]), int(m[2])), (int(m[3]), int(m[4])))
        line_segments.append(segment)

board = np.zeros((1000, 1000), dtype=int)
for segment in line_segments:
    ((x1, y1), (x2, y2)) = segment
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            board[x1, y] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            board[x, y1] += 1
    else:
        assert(abs(x1-x2) == abs(y1-y2))
        x_step = 1
        if x2 < x1:
            x_step = -1
        y_step = 1
        if y2 < y1:
            y_step = -1
        n_steps = abs(x1 - x2)
        for i in range(n_steps+1):
            board[x1 + (i*x_step), y1 + (i*y_step)] += 1

n_overlap = (board > 1).sum()
print(n_overlap)