#!/usr/bin/env python3

import sys
import numpy as np

with open(sys.argv[1]) as infile:
    rows = [a.strip() for a in infile]


def do_round(cube):
    x, y, z = cube.shape
    new_cube = np.zeros(cube.shape, dtype=bool)
    for i in range(x):
        for j in range(y):
            for k in range(z):
                neighbors = cube[max(i - 1, 0):min(i + 2, x), max(j - 1, 0):min(j + 2, y), max(k - 1, 0):min(k + 2, z)]
                n_occupied = np.count_nonzero(neighbors)
                # print((i,j,k), neighbors.shape, cube[i,j,k], n_occupied)
                if cube[i, j, k]:
                    if 3 <= n_occupied <= 4:  # one higher than specs since we're counting this too
                        new_cube[i, j, k] = True
                else:
                    if n_occupied == 3:
                        new_cube[i, j, k] = True
    return new_cube


square_size = 12 + len(rows)
start_cube = np.zeros((square_size, square_size, 13), dtype=bool)
for i, row in enumerate(rows):
    for j, active in enumerate(row):
        if active == '#':
            start_cube[i + 6, j + 6, 6] = True

for i in range(6):
    cube = do_round(start_cube)
    print("Round {}: {} active".format(i+1, np.count_nonzero(cube)))
    start_cube = cube
