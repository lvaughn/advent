#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase
#from collections import Counter, defaultdict, deque, namedtuple
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
#import numpy as np
import re
#import pprint
import sys


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

NUMBER_RE = re.compile(r'^(\d+)')

with open(sys.argv[1], 'r') as infile:
    lines = [l.rstrip('\n') for l in infile]

    grid = lines[:-2]
    moves = lines[-1]

max_width = max(len(r) for r in grid)
for i, line in enumerate(grid):
    if len(line) < max_width:
        grid[i] = line + " " * (max_width - len(line))


def value(r, c):
    return grid[r - 1][c - 1]

def turn(current, change):
    if change == 'R':
        return (current + 1) % 4
    if change == 'L':
        return (current - 1) % 4


def next_pos(r, c, d):
    if d == 0:  # Right
        c += 1
        if c > len(grid[r-1]):
            c -= len(grid[r-1])
        while value(r, c) == ' ':
            c += 1
            if c > len(grid[r-1]):
                c -= len(grid[r-1])
        return r, c
    if d == 1:  # Down
        r += 1
        if r > len(grid):
            r -= len(grid)
        while value(r, c) == ' ':
            r += 1
            if r > len(grid):
                r -= len(grid)
        return r, c
    if d == 2:  # Left
        c -= 1
        if c == 0:
            c = len(grid[r-1])
        while value(r, c) == ' ':
            c -= 1
            if c == 0:
                c = len(grid[r-1])
        return r, c
    if d == 3:  # Up
        r -= 1
        if r == 0:
            r = len(grid)
        while value(r, c) == ' ':
            r -= 1
            if r == 0:
                r = len(grid)
        return r, c
    print(r, c, d)
    assert False


row = 1
col = 1
dir = 0
while value(row, col) == ' ':
    col += 1

while len(moves) > 0:
    m = NUMBER_RE.search(moves)
    if m is not None:
        for _ in range(int(m[1])):
            n_r, n_c = next_pos(row, col, dir)
            if value(n_r, n_c) == '.':
                row, col = n_r, n_c
        moves = moves[len(m[1]):]
    else:
        dir = turn(dir, moves[0])
        moves = moves[1:]

print(row, col, dir)
print("Part 1",1000 *row +  4*col + dir)
