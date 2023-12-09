#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]


def draw_lines(moves) -> set:
    r, c = 0, 0
    grid = set()
    for move in moves:
        dir = move[0]
        dist = int(move[1:])
        if dir == 'U':
            for _ in range(dist):
                r += 1
                grid.add((r, c)) 
        if dir == 'D':
            for _ in range(dist):
                r -= 1
                grid.add((r, c))  
        if dir == 'R':
            for _ in range(dist):
                c += 1
                grid.add((r, c)) 
        if dir == 'L':
            for _ in range(dist):
                c -= 1
                grid.add((r, c))
    return grid 
            
grid_a = draw_lines(lines[0].split(','))
grid_b = draw_lines(lines[1].split(','))

best = 10000000
for r, c in grid_a & grid_b:
    dist = abs(r) + abs(c)
    best = min(dist, best)

print("Part 1", best)
