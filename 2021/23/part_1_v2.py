#!/usr/bin/env python3

import heapq, sys
from collections import defaultdict

#############
#01.4.7.a.de#
###2#5#8#b###
###3#6#9#c#
###########

REACHABILITY = defaultdict(list)
n_per_row = 2

def add(start, end, length, blocking):
    REACHABILITY[start].append((end, length, blocking))
    REACHABILITY[end].append((start, length, blocking))

def walk_down(start, top_pos, start_dist, blocking_on_way):
    extra_blocks = set()
    for i in range(n_per_row):
        blocking = list(sorted(extra_blocks | blocking_on_way))
        add(start, top_pos + i, start_dist + i, blocking)
        extra_blocks.add(top_pos + i)

top_row = [0, 1, 4, 7, 10, 13, 14]
bottom_rows = [2, 5, 8, 11]
for i, b in enumerate(bottom_rows):
    other_blocking = set()
    if i > 0:
        for n in top_row[2:2+i]:
            other_blocking.add(n)
    walk_down(0, b, 3+2*i, {1} | other_blocking)
    walk_down(1, b, 2+2*i, other_blocking)

# From 4
walk_down(4, 2, 2, set())
walk_down(4, 5, 2, set())
walk_down(4, 8, 4, set([7]))
walk_down(4, 11, 6, set([7, 10]))

# From 7
walk_down(7, 2, 4, set([4]))
walk_down(7, 5, 2, set())
walk_down(7, 8, 2, set())
walk_down(7, 11, 4, set([10]))

# From 10
walk_down(10, 2, 6, set([4, 7]))
walk_down(10, 5, 4, set([7]))
walk_down(10, 8, 2, set())
walk_down(10, 11, 2, set())

for i, b in enumerate(reversed(bottom_rows)):
    other_blocking = set()
    if i > 0:
        for n in top_row[4:4-i:-1]:
            other_blocking.add(n)
    walk_down(14, b, 3+2*i, {1} | other_blocking)
    walk_down(13, b, 2+2*i, other_blocking)


print(REACHABILITY)

#############
# ...........#
###B#C#A#B###
###C#D#D#A#
###########

start_positions = [0, 0, 'B', 'C', 0, 'C', 'D', 0, 'A', 'D', 0, 'B', 'A', 0, 0]
energy_by_type = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
tops_positions = {0, 1, 4, 7, 10, 13, 14}
home_positions = {'A': {2, 3}, 'B': {4, 5}, 'C': {8, 9}, 'D': {11, 12}}

start_positions = [0, 0, 2, 3, 0, 3, 4, 0, 1, 4, 0, 2, 1, 0, 0]
energy_by_type = {1: 1, 2: 10, 3: 100, 4: 1000}
tops_positions = {0, 1, 4, 7, 10, 13, 14}
home_positions = {1: {2, 3}, 2: {5, 6}, 3: {8, 9}, 4: {11, 12}}

# Test data
# start_positions = [0, 0, 2, 1, 0, 3, 4, 0, 2, 3, 0, 4, 1, 0, 0]

def is_done(pos):
    for ch in home_positions:
        for slot in home_positions[ch]:
            if pos[slot] != ch:
                return False
    return True

cache = {}
# State = (energy_used, positions)
queue = [(0, start_positions)]
iter = 0
while True:
    energy, position = heapq.heappop(queue)
    if iter % 10000 == 0:
        print(iter, len(queue))
    iter += 1
    position = position
    if is_done(position):
        print(position)
        print(f"Part 1: {energy}")
        break
    for i in range(len(position)):
        if position[i] == 0:
            continue
        critter = position[i]
        for dest, length, blocking in REACHABILITY[i]:
            if position[dest] != 0:
                continue
            if i in tops_positions and dest not in home_positions[critter]:
                continue
            if i in tops_positions:
                if any(position[a] not in {0, critter} for a in home_positions[critter]):
                    continue
            if any(position[a] != 0 for a in blocking):
                continue
            # We can do the move
            new_pos = list(position)
            new_pos[dest] = critter
            new_pos[i] = 0
            new_pos = tuple(new_pos)
            new_energy = energy + length * energy_by_type[critter]
            if new_pos in cache and cache[new_pos] <= new_energy:
                continue
            cache[new_pos] = new_energy
            heapq.heappush(queue, (new_energy, new_pos))


