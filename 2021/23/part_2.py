#!/usr/bin/env python3

import heapq, sys
from collections import defaultdict


REACHABILITY = defaultdict(list)
n_per_row = 4

def add(start, end, length, blocking):
    REACHABILITY[start].append((end, length, blocking))
    REACHABILITY[end].append((start, length, blocking))

def walk_down(start, top_pos, start_dist, blocking_on_way):
    extra_blocks = set()
    for i in range(n_per_row):
        blocking = list(sorted(extra_blocks | blocking_on_way))
        add(start, top_pos + i, start_dist + i, blocking)
        extra_blocks.add(top_pos + i)

top_row = [0, 1, 6, 11, 16, 21, 22]
bottom_rows = [2, 7, 12, 17]
for origin, b in enumerate(bottom_rows):
    other_blocking = set()
    if origin > 0:
        for n in top_row[2:2 + origin]:
            other_blocking.add(n)
    walk_down(0, b, 3 + 2 * origin, {1} | other_blocking)
    walk_down(1, b, 2 + 2 * origin, other_blocking)

# From 6
walk_down(6, 2, 2, set())
walk_down(6, 7, 2, set())
walk_down(6, 12, 4, set([11]))
walk_down(6, 17, 6, set([11, 16]))

# From 11
walk_down(11, 2, 4, set([6]))
walk_down(11, 7, 2, set())
walk_down(11, 12, 2, set())
walk_down(11, 17, 4, set([16]))

# From 16
walk_down(16, 2, 6, set([7, 12]))
walk_down(16, 7, 4, set([12]))
walk_down(16, 12, 2, set())
walk_down(16, 17, 2, set())

for origin, b in enumerate(reversed(bottom_rows)):
    other_blocking = set()
    if origin > 0:
        for n in top_row[4:4 - origin:-1]:
            other_blocking.add(n)
    walk_down(21, b, 2 + 2 * origin, other_blocking)
    walk_down(22, b, 3 + 2 * origin, {21} | other_blocking)

# import pprint
# pprint.pprint(REACHABILITY)

#############
#...........#
###B#C#A#B###
###D#C#B#A#
###D#B#A#C#
###C#D#D#A#
###########


start_positions = [0, 0, 2, 4, 4, 3, 0, 3, 3, 2, 4, 0, 1, 2, 1, 4, 0, 2, 1, 3, 1, 0, 0]
energy_by_type = {1: 1, 2: 10, 3: 100, 4: 1000}
tops_positions = {0, 1, 6, 11, 16, 21, 22}
home_positions = {1: {2, 3, 4, 5}, 2: {7, 8, 9, 10}, 3: {12, 13, 14, 15}, 4: {17, 18, 19, 20}}

# Test data
#start_positions = [0, 0, 2, 4, 4, 1, 0, 3, 3, 2, 4, 0, 2, 2, 1, 3, 0, 4, 1, 3, 1, 0, 0]

assert len(start_positions) == 23
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
        print(f"Part 2: {energy}")
        break
    for origin in range(len(position)):
        if position[origin] == 0:
            continue
        critter = position[origin]
        for dest, length, blocking in REACHABILITY[origin]:
            if position[dest] != 0:
                continue
            if origin in tops_positions and dest not in home_positions[critter]:
                continue
            if origin in tops_positions:
                if any(position[a] not in {0, critter} for a in home_positions[critter]):
                    continue
            if any(position[a] != 0 for a in blocking):
                continue
            # We can do the move
            new_pos = list(position)
            new_pos[dest] = critter
            new_pos[origin] = 0
            new_pos = tuple(new_pos)
            new_energy = energy + length * energy_by_type[critter]
            if new_pos in cache and cache[new_pos] <= new_energy:
                continue
            cache[new_pos] = new_energy
            heapq.heappush(queue, (new_energy, new_pos))


