#!/usr/bin/env python3

import heapq

#############
#01.4.7.a.de#
###2#5#8#b###
###3#6#9#c#
###########

REACHABILITY = {
    0: [(2, 3, (1,)), (3, 4, (1, 2)), (5, 5, (1, 4)), (6, 6, (1, 4, 5)),
        (8, 7, (1, 4, 7)), (9, 8, (1, 4, 7, 8)), (11, 9, (1, 4, 7, 10)), (12, 10, (1, 4, 7, 10, 11))],
    1: [(2, 2, ()), (3, 3, (2,)), (5, 4, (4,)), (6, 5, (4, 5)),
        (8, 6, (4, 7)), (9, 7, (4, 7, 8)), (11, 8, (4, 7, 10)), (12, 9, (4, 7, 10, 11))],
    2: [(0, 3, (1,)), (1, 2, ()), (4, 2, ()), (7, 4, (4,)), (10, 6, (4, 7)), (13, 8, (4, 7, 10)),
        (14, 9, (4, 7, 10, 13))],
    3: [(0, 4, (1, 2)), (1, 3, (2,)), (4, 3, (2,)), (7, 5, (2, 4)), (10, 7, (2, 4, 7)), (13, 9, (2, 4, 7, 10)),
        (14, 10, (2, 4, 7, 10, 13))],
    4: [(2, 2, ()), (3, 3, (2,)), (5, 2, ()), (6, 3, (5,)), (8, 4, (7,)), (9, 5, (7, 8)),
        (11, 6, (7, 10)), (12, 7, (7, 10, 11))],
    5: [(0, 5, (1, 4)), (1, 4, (4,)), (4, 2, ()), (7, 2, ()), (10, 4, (7,)), (13, 6, (7, 10)),
        (14, 7, (7, 10, 13))],
    6: [(0, 6, (1, 4, 5)), (1, 5, (4, 5)), (4, 3, (5,)), (7, 3, (5,)), (10, 5, (5, 7)), (13, 7, (5, 7, 10)),
        (14, 8, (5, 7, 10, 13))],
    7: [(2, 4, (4,)), (3, 5, (2, 4)), (5, 2, ()), (6, 3, (5,)), (8, 2, ()), (9, 3, (8,)),
        (11, 4, (10,)), (12, 5, (10, 11))],
    8: [(0, 7, (1, 4, 7)), (1, 6, (4, 7)), (4, 4, (7,)), (7, 2, ()), (10, 2, ()), (13, 4, (10,)),
        (14, 5, (10, 13))],
    9: [(0, 8, (1, 4, 7, 8)), (1, 7, (4, 7, 8)), (4, 5, (7, 8)), (7, 3, (8,)), (10, 3, (8,)), (13, 5, (8, 10)),
        (14, 6, (8, 10, 13))],
    10: [(2, 6, (4, 7)), (3, 7, (2, 4, 7)), (5, 4, (7,)), (6, 5, (5, 7)), (8, 2, ()), (9, 3, (8,)),
         (11, 2, ()), (12, 3, (11,))],
    11: [(0, 9, (1, 4, 7, 10)), (1, 8, (4, 7, 10)), (4, 6, (7, 10)), (7, 4, (10,)), (10, 2, ()),
         (13, 2, ()), (14, 3, (13,))],
    12: [(0, 10, (1, 4, 7, 10, 11)), (1, 9, (4, 7, 10, 11)), (4, 7, (7, 10, 11)), (7, 5, (10, 11)),
         (10, 3, (11,)), (13, 3, (11,)), (14, 4, (11, 13))],
    13: [(2, 8, (4, 7, 10)), (3, 9, (2, 4, 7, 10)), (5, 6, (7, 10)), (6, 7, (5, 7, 10)),
         (8, 4, (10,)), (9, 5, (8, 10)), (11, 2, ()), (12, 3, (11,))],
    14: [(2, 9, (4, 7, 10, 13)), (3, 10, (2, 7, 10, 13)), (5, 7, (7, 10, 13)), (6, 8, (5, 7, 10, 13)),
         (8, 5, (10, 13)), (9, 6, (8, 10, 13)), (11, 3, (13,)), (12, 4, (11, 13))]
}

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


