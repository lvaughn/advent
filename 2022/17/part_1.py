#!/usr/bin/env python3

import numpy as np
import sys


def get_highest(grid, start=0):
    row = start
    while sum(grid[row, :]) > 0:
        row += 1
    return row


def print_bottom(grid):
    for r in range(15, -1, -1):
        s = ''
        for c in range(grid.shape[1]):
            if grid[r, c] == 0:
                s += ' '
            else:
                s += '#'
        print(s, r)
    print('0123456')


def would_fit(pit, rock, bottom, pos):
    if pos < 0 or pos + rock.shape[1] > 7:
        return False
    if bottom < 0:
        return False
    rows, cols = rock.shape
    pit_part = pit[bottom:bottom + rows, pos:pos + cols]
    if (pit_part + rock > 1).any():
        return False
    return True


bar = np.ones((1, 4), dtype=int)
plus = np.zeros((3, 3), dtype=int)
plus[1, :] = 1
plus[:, 1] = 1
l = np.zeros((3, 3), dtype=int)
l[:, 2] = 1
l[0, :] = 1
pipe = np.ones((4, 1), dtype=int)
square = np.ones((2, 2))
rocks = [bar, plus, l, pipe, square]

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    moves = lines[0]

pit = np.zeros((4000, 7))
n_rocks = 0
gusts = 0
highest = 0
while n_rocks < 2022:
    rock = rocks[n_rocks % 5]
    n_rocks += 1
    highest = get_highest(pit, highest)
    bottom = highest + 3
    hor_pos = 2
    keep_going = True
    while keep_going:
        # Move left/right
        gust_dir = moves[gusts % len(moves)]
        gusts += 1
        if gust_dir == '<' and would_fit(pit, rock, bottom, hor_pos - 1):
            hor_pos -= 1
        elif gust_dir == '>' and would_fit(pit, rock, bottom, hor_pos + 1):
            hor_pos += 1
        else:
            assert (False, "Bad direction")

        # See if we can move down
        if would_fit(pit, rock, bottom - 1, hor_pos):
            bottom -= 1
        else:
            keep_going = False

    # Place the rock
    rows, cols = rock.shape
    pit[bottom:bottom + rows, hor_pos:hor_pos + cols] += rock

print(get_highest(pit))
