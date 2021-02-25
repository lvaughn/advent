#!/usr/bin/env python3

from heapq import heapify, heappop, heappush

CAVE_DEPTH = 6969
TARGET_LOC = (9, 796)

GEO_INDEX_CACHE = {
    (0, 0): 0,
    TARGET_LOC: 0
}


def get_geo_index(x, y):
    key = (x, y)
    if key not in GEO_INDEX_CACHE:
        if y == 0:
            GEO_INDEX_CACHE[key] = x * 16807
        elif x == 0:
            GEO_INDEX_CACHE[key] = y * 48271
        else:
            GEO_INDEX_CACHE[key] = get_erosion_level(x, y - 1) * get_erosion_level(x - 1, y)
    return GEO_INDEX_CACHE[key]


def get_erosion_level(x, y):
    return (get_geo_index(x, y) + CAVE_DEPTH) % 20183

CAVE_TYPE_CACHE = {}
def get_cave_type(loc):
    if loc not in CAVE_TYPE_CACHE:
        CAVE_TYPE_CACHE[loc] = get_erosion_level(loc[0], loc[1]) % 3
    return CAVE_TYPE_CACHE[loc]


# Queue contains (minutes, loc, tool)
# Tools:
# 0 - Neither
# 1 - Torch
# 2 - Climbing Gear
#
# region type: 0 - Rocky    1 - Wet     2 - Narrow
#
# tool can't equal region type
fastest = {}  # (loc, tool) => min(minutes to get there)
queue = [(0, (0, 0), 1)]
while len(queue) > 0:
    minutes, loc, tool = heappop(queue)
    if loc == TARGET_LOC and tool == 1:
        print("Found path that took {} minutes".format(minutes))
        break
    if (loc, tool) in fastest:
        continue
    fastest[loc, tool] = minutes
    # Add tool changes
    for t in range(3):
        if t != tool and t != get_cave_type(loc) and (loc, t) not in fastest:
            heappush(queue, (minutes + 7, loc, t))
    # Look at moves
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x = loc[0] + dx
        y = loc[1] + dy
        if x < 0 or y < 0:
            continue
        if get_cave_type((x, y)) != tool:
            heappush(queue, (minutes + 1, (x, y), tool))

