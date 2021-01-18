#!/usr/bin/env python3

import numpy as np
from collections import deque

HASH_BASE = 'ffayrhll'


def hash_key(s):
    sizes = [ord(a) for a in s]
    sizes += [17, 31, 73, 47, 23]

    message = list(range(256))

    skip = 0
    loc = 0
    for _ in range(64):
        for size in sizes:
            end = loc + size
            if end > len(message):
                at_start = loc + size - len(message)
                at_end = size - at_start
                to_reverse = message[loc:] + message[:at_start]
                rev_portion = list(reversed(to_reverse))
                message = rev_portion[-at_start:] + message[at_start:loc] + rev_portion[:at_end]
            else:
                to_reverse = message[loc:loc + size]
                message = message[:loc] + list(reversed(to_reverse)) + message[loc + size:]
            loc = (loc + size + skip) % len(message)
            skip += 1

    output_binary = []
    for i in range(16):
        value = 0
        for j in range(16):
            value ^= message[i * 16 + j]
        output_binary.append(value)

    return ''.join(['{:02x}'.format(a) for a in output_binary])


bits_on = {'0': 0, '1': 1, '2': 1, '3': 2,
           '4': 1, '5': 2, '6': 2, '7': 3,
           '8': 1, '9': 2, 'a': 2, 'b': 3,
           'c': 2, 'd': 3, 'e': 3, 'f': 4}
ones = set(('1', '3', '5', '7', '9', 'b', 'd', 'f'))
twos = set(('2', '3', '6', '7', 'a', 'b', 'e', 'f'))
fours = set(('4', '5', '6', '7', 'c', 'd', 'e', 'f'))
eights = set(('8', '9', 'a', 'b', 'c', 'd', 'e', 'f'))

grid = np.zeros((128, 128), dtype=int)

total_on = 0
for i in range(128):
    hashed = hash_key('{}-{}'.format(HASH_BASE, i))
    for j, ch in enumerate(hashed):
        total_on += bits_on[ch]
        if ch in eights:
            grid[i, j * 4 + 0] = -1
        if ch in fours:
            grid[i, j * 4 + 1] = -1
        if ch in twos:
            grid[i, j * 4 + 2] = -1
        if ch in ones:
            grid[i, j * 4 + 3] = -1


def toggle_group(row, col, n):
    queue = deque([(row, col)])
    size = 0
    grid[row, col] = n
    while len(queue) > 0:
        (r, c) = queue.popleft()
        grid[r, c] = n
        size += 1
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            new_row = (r + dx)
            new_col = (c + dy)
            if 0 <= new_row < 128 and 0 <= new_col < 128 and grid[new_row, new_col] < 0:
                grid[new_row, new_col] = n
                queue.append((new_row, new_col))


n_groups = 0
for row in range(128):
    for col in range(128):
        if grid[row, col] < 0:
            toggle_group(row, col, n_groups + 1)
            n_groups += 1

print("Part 1:", total_on)
print("Part 2:", n_groups)
