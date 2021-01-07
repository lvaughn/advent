#!/usr/bin/env python3

from collections import deque
from itertools import permutations

# Read in the maze
maze = []
number_locs = {}
with open('input.txt', 'r') as f:
    row = 0
    for line in f:
        column = []
        for col, ch in enumerate(line.strip()):
            if ch not in {'.', '#'}:
                val = int(ch)
                column.append(val)
                number_locs[val] = (row, col)
            else:
                column.append(ch)
        maze.append(column)
        row += 1



# Find the distances from each of the points to all the others
distances = {}
def run_search(start):
    row, col = number_locs[start]
    max_row = len(maze)
    max_col = len(maze[0])
    queue = deque()
    queue.append((row, col, 0))
    sure_to_find = set(range(start+1, len(number_locs)))
    visited = set()
    while len(queue) > 0 and len(sure_to_find) > 0:
        r, c, moves = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        if maze[r][c] not in {'.', '#'}:
            val = maze[r][c]
            sure_to_find.discard(val)
            distances[(start, val)] = moves
            distances[(val, start)] = moves
        for dx, dy in [(0,1), (0,-1), (1, 0), (-1, 0)]:
            new_r = r + dx
            new_c = c + dy
            if 0 <= new_r < max_row and 0 <= new_c < max_col and (new_r, new_c):
                if maze[new_r][new_c] != '#' and (new_r, new_c not in visited):
                    queue.append((new_r, new_c, moves+1))

for starting_pt in number_locs.keys():
    run_search(starting_pt)

# Now, do the real work
best_dist = len(maze)*len(maze[1]) + 1000
for path in permutations(range(1, len(number_locs))):
    dist = distances[(0, path[0])]
    for i in range(len(path)-1):
        dist += distances[(path[i], path[i+1])]
    if dist < best_dist:
        best_dist = dist
        print("New best", dist, [0] + list(path))

print("shortest path", best_dist)

# Now, do the real work
best_dist = len(maze)*len(maze[1]) + 1000
for path in permutations(range(1, len(number_locs))):
    dist = distances[(0, path[0])]
    for i in range(len(path)-1):
        dist += distances[(path[i], path[i+1])]
    dist += distances[(path[-1], 0)]
    if dist < best_dist:
        best_dist = dist
        print("New best", dist, [0] + list(path) + [0])

print("shortest roundtrip", best_dist)