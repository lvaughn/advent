#!/usr/bin/env python3

import numpy as np
import re

line_re = re.compile(r'(turn on|turn off|toggle)\s+(\d+),(\d+)\s+through\s(\d+),(\d+)')
grid = np.zeros((1000, 1000), dtype=bool)

with open('input.txt', 'r') as f:
    for line in f:
        m = line_re.match(line)
        start_x = int(m[2])
        start_y = int(m[3])
        end_x = int(m[4]) + 1
        end_y = int(m[5]) + 1
        if m[1] == 'turn on':
            grid[start_x:end_x, start_y:end_y] = 1
        elif m[1] == 'turn off':
            grid[start_x:end_x, start_y:end_y] = 0
        elif m[1] == 'toggle':
            grid[start_x:end_x, start_y:end_y] = grid[start_x:end_x, start_y:end_y] - 1
        else:
            assert False

print(np.count_nonzero(grid))