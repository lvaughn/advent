#!/usr/bin/env python3

from collections import deque

PUZZLE_INPUT = 1358

wall_cache = {}


def is_wall(x, y):
    key = (x, y)
    if key not in wall_cache:
        val = x * x + 3 * x + 2 * x * y + y + y * y + PUZZLE_INPUT
        ones = 0
        while val > 0:
            if val % 2 == 1:
                ones += 1
            val = val // 2
        wall_cache[key] = ones % 2 == 1
    return wall_cache[key]


moves = deque()
has_visited = set()
moves.append((1, 1, 0))
while len(moves) > 0:
    x, y, n_moves = moves.popleft()
    has_visited.add((x, y))
    if n_moves >= 50:
        continue
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x = x + dx
        new_y = y + dy
        if new_x < 0 or new_y < 0:
            continue
        if (new_x, new_y) in has_visited:
            continue
        if is_wall(new_x, new_y):
            continue
        moves.append((new_x, new_y, n_moves + 1))

print(len(has_visited))
