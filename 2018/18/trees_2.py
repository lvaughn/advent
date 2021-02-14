#!/usr/bin/env python3

import numpy as np
from collections import defaultdict

def to_tuple(m):
    rows = []
    for r in range(m.shape[0]):
        rows.append(tuple(m[r, :]))
    return tuple(rows)

def print_map(m):
    key = {0: '.', 1: '|', 2: '#'}
    for r in range(m.shape[0]):
        s = ''
        for c in range(m.shape[1]):
            s += key[m[r, c]]
        print(s)


def surround(map, row, col):
    return map[max(0, row - 1):min(row + 2, map.shape[0]), max(0, col - 1):min(col + 2, map.shape[1])]


def calculate_round(m):
    new = np.zeros(m.shape, dtype=int)
    for r in range(m.shape[0]):
        for c in range(m.shape[1]):
            if m[r, c] == 0:
                # Goes to trees if 3 or more adjacent are trees
                if np.count_nonzero(surround(m, r, c) == 1) >= 3:
                    new[r, c] = 1
                else:
                    new[r, c] = 0
            elif m[r, c] == 1:
                # Converts to lumber yard if 3 more or adjacent are lumber yards
                if np.count_nonzero(surround(m, r, c) == 2) >= 3:
                    new[r, c] = 2
                else:
                    new[r, c] = 1
            else:
                assert m[r, c] == 2
                # Stays a lumberyard if it's next to at least one other one and next to trees
                next_to = surround(m, r, c)
                if np.count_nonzero(next_to == 1) >= 1 and np.count_nonzero(next_to == 2) >= 2:
                    new[r, c] = 2
                else:
                    new[r, c] = 0
    return new


with open('input.txt', 'r') as f:
    starting = [l.strip() for l in f]

# 0 == open
# 1 == tree
# 2 == lumber yard
map = np.zeros((len(starting), len(starting[0])), dtype=int)
for r, row in enumerate(starting):
    for c, ch in enumerate(row):
        if ch == '|':
            map[r, c] = 1
        elif ch == '#':
            map[r, c] = 2
seen = defaultdict(list)
for i in range(1000):
    map = calculate_round(map)
    n_trees = np.count_nonzero(map == 1)
    n_yards = np.count_nonzero(map == 2)
    t_map = to_tuple(map)
    value = n_trees * n_yards
    # if t_map in seen:
    #     old_round, val = seen[t_map]
    #     #print("Matching rounds {} and {} (diff={}) (value)".format(old_round, i, i-old_round, val))
    seen[t_map].append((i+1, value))

step = 1000000000 % 28  # number of steps in cycle
print("Looking for step", step)
for board, ls in seen.items():
    r, value = ls[-1]
    if (1000000000 - r) % 28 == 0:
        print("Part 2:", r, value)
        print(ls[-4:])
