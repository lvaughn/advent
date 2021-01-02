#!/usr/bin/env python3

import numpy as np

SIZE = 3001330

elves = np.arange(SIZE, dtype=int)
elves = elves + 1
elves[-1] = 0
n_left = SIZE
current = 0

while current != elves[current]:
    to_delete = elves[current]
    elves[current] = elves[to_delete]
    current = elves[current]

print(current + 1)
