#!/usr/bin/env python3

import numpy as np
import re

board = np.zeros((1000, 1000), dtype=int)

claims = []
with open('input.txt', 'r') as f:
    line_re = re.compile(r'#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)')
    for line in f:
        m = line_re.match(line)
        piece_id, x, y, width, height = m[1], int(m[2]), int(m[3]), int(m[4]), int(m[5])
        claims.append((piece_id, x, y, width, height))
        board[x:x + width, y:y + height] += 1

print("Part 1", np.count_nonzero(board > 1))

for piece_id, x, y, width, height in claims:
    if np.count_nonzero(board[x:x + width, y:y + height] > 1) == 0:
        print("Part 2", piece_id)
