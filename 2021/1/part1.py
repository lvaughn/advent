#!/usr/bin/env python3

import numpy as np

with open("input.txt", "r") as infile:
    values = [int(line) for line in infile]

n_inc = 0
for i in range(1, len(values)):
    if values[i-1] < values[i]:
        n_inc += 1

print(n_inc)

values = np.array(values)

trips = values[:-2] + values[1:-1] + values[2:]
n_inc = 0
for i in range(1, len(trips)):
    if trips[i-1] < trips[i]:
        n_inc += 1

print(n_inc)