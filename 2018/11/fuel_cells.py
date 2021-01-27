#!/usr/bin/env python3

import numpy as np

SERIAL_NUMBER = 7511

rack_numbers = np.arange(11, 311)

cells = np.zeros((300,300), dtype=int)

for y in range(300):
    arr = (y+1) * rack_numbers
    arr = arr + SERIAL_NUMBER
    arr = arr * rack_numbers
    arr = arr // 100
    arr = (arr % 10) - 5
    cells[:, y] = arr

# Find the best 3x3
best_x, best_y = 0, 0
best_size = 1
best_total = -90000
for size in range(1, 300):
    for x in range(301-size):
        for y in range(301-size):
            total = np.sum(cells[x:x+size, y:y+size])
            if total > best_total:
                best_total = total
                best_x, best_y = x, y
                best_size = size
print(best_x+1, best_y+1, best_size)