#!/usr/bin/env python3

import numpy as np
import sys

N_ROCKS = 10000
PIT_DEPTH = N_ROCKS * 4 + 5


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
    if (pit[bottom:bottom + rows, pos:pos + cols] + rock > 1).any():
        return False
    return True


# Create the rocks
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

pit = np.zeros((PIT_DEPTH, 7))
n_rocks = 0
gusts = 0
highests = []
highest = 0
while n_rocks < N_ROCKS:
    rock = rocks[n_rocks % 5]
    n_rocks += 1

    # Find the start
    highest = get_highest(pit, highest)
    highests.append(highest)
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

arr = np.array(highests, dtype=int)
diffs = arr[1:] - arr[:-1]

b = N_ROCKS // 3  # Arbitrary starting place
base = diffs[b:b + 10]
cycle_starts = [b]
base_range = diffs[b:b + 10]
for i in range(b + 10, len(diffs) - 10):
    if (base_range == diffs[i:i + 10]).all():
        cycle_starts.append(i)

assert(cycle_starts[1] - cycle_starts[0] == cycle_starts[2]-cycle_starts[1])

cycle = cycle_starts[1] - cycle_starts[0]
print(f"Cycle Length {cycle}")
goal = 1000000000000
m = goal % cycle
start_loc = m + cycle * 3
start = highests[start_loc]
step = highests[start_loc + cycle] - start
n_cycles = (goal - start_loc) // cycle
assert ((goal - start_loc) % cycle == 0)
print("Part 2", start + n_cycles * step)
