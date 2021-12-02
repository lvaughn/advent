#!/usr/bin/env python3

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


total_danger = 0
for x in range(TARGET_LOC[0]+1):
    for y in range(TARGET_LOC[1] + 1):
        total_danger += get_erosion_level(x, y) % 3

print("Part 1:", total_danger)