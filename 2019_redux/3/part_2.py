#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]


def draw_lines(moves) -> dict:
    r, c = 0, 0
    grid = {}
    n_moves = 0
    for move in moves:
        dir = move[0]
        dist = int(move[1:])
        if dir == 'U':
            for _ in range(dist):
                n_moves += 1
                r += 1
                if (r, c) not in grid:
                    grid[(r, c)] = n_moves
        if dir == 'D':
            for _ in range(dist):
                n_moves += 1
                r -= 1
                if (r, c) not in grid:
                    grid[(r, c)] = n_moves
        if dir == 'R':
            for _ in range(dist):
                n_moves += 1
                c += 1
                if (r, c) not in grid:
                    grid[(r, c)] = n_moves
        if dir == 'L':
            for _ in range(dist):
                n_moves += 1
                c -= 1
                if (r, c) not in grid:
                    grid[(r, c)] = n_moves
    return grid 
            
grid_a = draw_lines(lines[0].split(','))
grid_b = draw_lines(lines[1].split(','))

best = 10000000
for pt in grid_a:
    if pt in grid_b:
        dist = grid_a[pt] + grid_b[pt]
        best = min(dist, best)

print("Part 2", best)
