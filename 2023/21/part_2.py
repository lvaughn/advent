#!/usr/bin/env python3
from collections import Counter, defaultdict, deque, namedtuple
import numpy as np
import pprint
import sys


def print_grid(grid):
    for r in range(grid.shape[0]):
        l = ""
        for v in grid[r, :]:
            if v == 0:
                l += "."
            elif v == 1:
                l += "O"
            else:
                assert v == 2
                l += '#'
        print(l)
  
answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
def get_adjacent(r, c, shape):
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        new_r = r + dr 
        new_c = c + dc 
        if 0 <= new_r < shape[0] and 0 <= new_c < shape[1]:
            yield new_r, new_c
    
height = len(lines)
width = len(lines[0])

start_r = start_c = 0
starter_grid = np.zeros((height, width), dtype=int)
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == 'S':
            start_r = r 
            start_c = c
            starter_grid[r, c] = 0
        elif ch == '#':
            starter_grid[r,c] = 2 
                

TILES = 9
big_grid = np.zeros((TILES*height, TILES*width), dtype=int)
for i in range(TILES):
    for j in range(TILES):
        big_grid[i*height:(i+1)*height, j*width:(j+1)*width] = starter_grid[:, :]
        
center = TILES//2
big_grid[center*height+start_r, center*width + start_c] = 1

grid = big_grid 
print(np.count_nonzero(grid == 1))
counts = [1]
iterations = width * (TILES//2)
for i in range(iterations):
    new_grid = np.zeros(grid.shape, dtype=int)
    new_grid[grid == 2] = 2
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == 1:
                for new_r, new_c in get_adjacent(r, c, grid.shape):
                    if new_grid[new_r, new_c] != 2:
                        new_grid[new_r, new_c] = 1 
    grid = new_grid
    counts.append(np.count_nonzero(grid == 1))
    
target = 26501365
starting_point = (target % width) + width
points = counts[starting_point::width]
delta = points[1] - points[0]
second_der = (points[2]-points[1]) - (points[1]-points[0])

print(delta, second_der)

n = starting_point
answer = counts[starting_point]
print(n, answer)
while n < target:
    n += width
    answer += delta
    delta += second_der
    if n < len(counts):
        print(n, answer, counts[n])
    
assert n == target, f"n={n}, target={target}"
print("Part 2", answer)
    