#!/usr/bin/env python3

import numpy as np

SIZE = 3001330

elves = np.arange(SIZE, dtype=int)
elves = elves + 1
elves[-1] = 0
n_left = SIZE

current = 0
midpoint = 0
n_before = 0
n_after = SIZE - 1
while current != elves[current]:

    # True up midpoint
    while n_before + 2 < n_after:
        midpoint = elves[midpoint]
        n_before += 1
        n_after -= 1

    # Delete and move up
    elves[midpoint] = elves[elves[midpoint]]
    current = elves[current]
    n_before -= 1

print(current + 1)
