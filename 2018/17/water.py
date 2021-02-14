#!/usr/bin/env python3

import re
import numpy as np
from collections import deque


def tr(x):
    return x - x_offset

def print_earth(e):
    char_map = {0: '.', 1: '#', 2: '+', 3: '|', 4: '~'}
    for r in range(e.shape[0]):
        s = ''
        for c in range(e.shape[1]):
            s += char_map[e[r, c]]
        print(s)

def is_contained(board, row, col):
    # Head right
    c = col + 1
    while c < board.shape[1]:
        if board[row+1][c] == 0:
            # Open below
            return False
        if board[row][c] == 1:
            break  # We're contained to the right
        c += 1
    c = col - 1
    while c >= 0:
        if board[row+1][c] == 0:
            # Open below
            return False
        if board[row][c] == 1:
            break  # We're contained to the left
        c -= 1
    return True


min_x, min_y = 99999, 99999
max_x, max_y = -1, -1
with open('input.txt', 'r') as f:
    clay_pieces = []
    line_re = re.compile(r'([xy])=(\d+),\s+([xy])=(\d+)\.\.(\d+)')
    for line in f:
        m = line_re.match(line)
        if m[1] == 'x':
            x = int(m[2])
            y_min = int(m[4])
            y_max = int(m[5])
            min_x = min(min_x, x)
            min_y = min(min_y, y_min)
            max_x = max(max_x, x)
            max_y = max(max_y, y_max)
            clay_pieces.append(((x, x), (y_min, y_max)))
        else:
            y = int(m[2])
            x_min = int(m[4])
            x_max = int(m[5])
            min_x = min(min_x, x_min)
            min_y = min(min_y, y)
            max_x = max(max_x, x_max)
            max_y = max(max_y, y)
            clay_pieces.append(((x_min, x_max), (y, y)))

x_size = 5 + max_x - min_x
y_size = max_y + 2
x_offset = min_x - 2
print((min_x, min_y), (max_x, max_y), x_size, y_size, x_offset)

earth = np.zeros((y_size, x_size), dtype=int)
for piece in clay_pieces:
    for x in range(piece[0][0], piece[0][1]+1):
        for y in range(piece[1][0], piece[1][1]+1):
            earth[y, tr(x)] = 1
earth[0, tr(500)] = 2

queue = deque([(0, tr(500))])
#  {0: '.', 1: '#', 2: '+', 3: '|', 4: '~'}
while len(queue) > 0:
    r, c = queue.popleft()
    r += 1 # start one below the starting point
    if earth[r, c] == 3:
        continue
    # Go down until we either hit clay, or fall off the bottom
    while r < earth.shape[0] and earth[r, c] == 0:
        earth[r, c] = 3
        r += 1

    # We fell off the bottom
    if r == earth.shape[0]:
        continue
    r -= 1  # go above what stopped us
    contained = is_contained(earth, r, c)
    while contained:
        tmp = c
        while earth[r, tmp] != 1:
            earth[r, tmp] = 4
            tmp += 1
        tmp = c
        while earth[r, tmp] != 1:
            earth[r, tmp] = 4
            tmp -= 1
        r -= 1  # Move up
        contained = is_contained(earth, r, c)

    # Now, head left and right
    tmp = c + 1
    while earth[r+1, tmp] in [1, 4] and earth[r, tmp] in [0, 3]:
        earth[r, tmp] = 3
        tmp += 1
    if earth[r+1, tmp] == 0:
        earth[r, tmp] = 3
        queue.append((r, tmp))
    tmp = c
    while earth[r+1, tmp] in [1, 4] and earth[r, tmp] in [0, 3]:
        earth[r, tmp] = 3
        tmp -= 1
    if earth[r+1, tmp] == 0:
        earth[r, tmp] = 3
        queue.append((r, tmp))

print("Done!")
print_earth(earth)
print("Part 1: ", np.count_nonzero(earth[min_y:max_y+1, :] == 3) + np.count_nonzero(earth[min_y:max_y+1, :] == 4))
print("Part 2: ", np.count_nonzero(earth[min_y:max_y+1, :] == 4))
