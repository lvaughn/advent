#!/usr/bin/env python3
# from string import ascii_uppercase, ascii_lowercase
# from collections import Counter, defaultdict, deque, namedtuple
# from itertools import count, product, permutations, combinations, combinations_with_replacement
# from sortedcontainers import SortedSet, SortedDict, SortedList
# import numpy as np
import re
# import pprint
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

sides = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': []}
for row in range(50):
    r = grid[row]
    sides['a'].append(r[50:100])
    sides['b'].append(r[100:150])
for row in range(50, 100):
    r = grid[row]
    sides['c'].append(r[50:100])
for row in range(100, 150):
    r = grid[row]
    sides['d'].append(r[:50])
    sides['e'].append(r[50:100])
for row in range(150, 200):
    r = grid[row]
    sides['f'].append(r[:50])

offsets = {
    'a': (0, 50),
    'b': (0, 100),
    'c': (50, 50),
    'd': (100, 0),
    'e': (100, 50),
    'f': (150, 0)
}


def value(side, r, c):
    # print(side, r, c)
    return sides[side][r - 1][c - 1]


# for s in ['a', 'b', 'c', 'd', 'e', 'f']:
#     for r in range(1, 51):
#         for c in range(1, 51):
#             assert value(s, r, c) in {'.', '#'}
#             r_off, c_off = offsets[s]
#             assert value(s, r, c) == grid[r+r_off-1][c+c_off-1]

def turn(current, change):
    if change == 'R':
        return (current + 1) % 4
    if change == 'L':
        return (current - 1) % 4


def next_pos(r, c, s, d):
    print('next_pos', r, c, s, d)
    assert 0 < r <= 50
    assert 0 < c <= 50
    if d == 0:  # Right
        c += 1
        if c > 50:
            # Move to the correct side
            if s == 'a':
                c = 1
                s = 'b'
            elif s == 'b':
                s = 'e'
                d = 2
                c = 50
                r = 51 - r
            elif s == 'c':
                s = 'b'
                d = 3
                c = r
                r = 50
            elif s == 'd':
                s = 'e'
                c = 1
            elif s == 'e':
                s = 'b'
                d = 2
                c = 50
                r = 51 - r
            else: # s == 'f'
                s = 'e'
                d = 3
                c = r
                r = 50
        return r, c, s, d
    if d == 1:  # Down
        r += 1
        if r > 50:  # Moved off the bottom
            # Move to the correct side
            if s == 'a':
                r = 1
                s = 'c'
            elif s == 'b':
                s = 'c'
                d = 2
                r = c
                c = 50
            elif s == 'c':
                s = 'e'
                r = 1
            elif s == 'd':
                s = 'f'
                r = 1
            elif s == 'e':
                s = 'f'
                d = 2
                r = c
                c = 50
            else:  # s == 'f'
                s = 'b'
                r = 1
        return r, c, s, d
    if d == 2:  # Left
        c -= 1
        if c == 0:
            # Move to the correct side
            if s == 'a':
                c = 1
                s = 'd'
                d = 0
                r = 51 - r
            elif s == 'b':
                s = 'a'
                c = 50
            elif s == 'c':
                s = 'd'
                d = 1
                c = r
                r = 1
            elif s == 'd':
                s = 'a'
                c = 1
                d = 0
                r = 51 - r
            elif s == 'e':
                s = 'd'
                c = 50
            else:  # s == 'f'
                s = 'a'
                d = 1
                c = r
                r = 1
        return r, c, s, d
    if d == 3:  # Up
        r -= 1
        if r == 0:
            # Move to the correct side
            if s == 'a':
                d = 0
                r = c
                c = 1
                s = 'f'
            elif s == 'b':
                s = 'f'
                r = 50
            elif s == 'c':
                s = 'a'
                r = 50
            elif s == 'd':
                s = 'c'
                r = c
                c = 1
                d = 0
            elif s == 'e':
                s = 'c'
                r = 50
            else:  # s == 'f'
                s = 'd'
                r = 50
        return r, c, s, d
    print(r, c, s, d)
    assert False


#
row = 1
col = 1
dir = 0
side = 'a'

while len(moves) > 0:
    m = NUMBER_RE.search(moves)
    if m is not None:
        for _ in range(int(m[1])):
            n_r, n_c, n_side, n_dir = next_pos(row, col, side, dir)
            if value(side, n_r, n_c) == '.':
                row, col, side, dir = n_r, n_c, n_side, n_dir
        moves = moves[len(m[1]):]
    else:
        dir = turn(dir, moves[0])
        moves = moves[1:]

print(row, col, dir, side)
row_off, col_off = offsets[side]
print("Part 2", (1000 * (row+row_off)) + (4 * (col+ col_off)) + dir)
# 9171 == too low
# 46094 == too low
# 141051 Wrong
