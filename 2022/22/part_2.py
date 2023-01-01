#!/usr/bin/env python3
import re
import sys

NUMBER_RE = re.compile(r'^(\d+)')

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

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
    return sides[side][r - 1][c - 1]


def turn(current, change):
    if change == 'R':
        return (current + 1) % 4
    if change == 'L':
        return (current - 1) % 4


def next_pos(r, c, s, d):
    assert 0 < r <= 50
    assert 0 < c <= 50
    if d == RIGHT:
        c += 1
        if c > 50:
            # Move to the correct side
            if s == 'a':
                c = 1
                s = 'b'
            elif s == 'b':
                s = 'e'
                d = LEFT
                c = 50
                r = 51 - r
            elif s == 'c':
                s = 'b'
                d = UP
                c = r
                r = 50
            elif s == 'd':
                s = 'e'
                c = 1
            elif s == 'e':
                s = 'b'
                d = LEFT
                c = 50
                r = 51 - r
            else:  # s == 'f'
                s = 'e'
                d = UP
                c = r
                r = 50
        return r, c, s, d
    if d == DOWN:
        r += 1
        if r > 50:  # Moved off the bottom
            # Move to the correct side
            if s == 'a':
                r = 1
                s = 'c'
            elif s == 'b':
                s = 'c'
                d = LEFT
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
                d = LEFT
                r = c
                c = 50
            else:  # s == 'f'
                s = 'b'
                r = 1
        return r, c, s, d
    if d == LEFT:
        c -= 1
        if c == 0:
            # Move to the correct side
            if s == 'a':
                c = 1
                s = 'd'
                d = RIGHT
                r = 51 - r
            elif s == 'b':
                s = 'a'
                c = 50
            elif s == 'c':
                s = 'd'
                d = DOWN
                c = r
                r = 1
            elif s == 'd':
                s = 'a'
                c = 1
                d = RIGHT
                r = 51 - r
            elif s == 'e':
                s = 'd'
                c = 50
            else:  # s == 'f'
                s = 'a'
                d = DOWN
                c = r
                r = 1
        return r, c, s, d
    if d == UP:
        r -= 1
        if r == 0:
            # Move to the correct side
            if s == 'a':
                d = RIGHT
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
                d = RIGHT
            elif s == 'e':
                s = 'c'
                r = 50
            else:  # s == 'f'
                s = 'd'
                r = 50
        return r, c, s, d
    assert False


# Starting location
row = 1
col = 1
dir = RIGHT
side = 'a'

while len(moves) > 0:
    m = NUMBER_RE.search(moves)
    if m is not None:
        for _ in range(int(m[1])):
            n_r, n_c, n_side, n_dir = next_pos(row, col, side, dir)
            if value(n_side, n_r, n_c) == '.':
                row, col, side, dir = n_r, n_c, n_side, n_dir
                row_offset, col_offset = offsets[side]
        moves = moves[len(m[1]):]
    else:
        dir = turn(dir, moves[0])
        moves = moves[1:]

row_off, col_off = offsets[side]
print("Part 2", (1000 * (row + row_off)) + (4 * (col + col_off)) + dir)
