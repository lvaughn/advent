#!/usr/bin/env python3

import re, sys, pprint
from collections import defaultdict

# This function is totally cribbed off the sub-reddit
def rotate_point(p, rotation):
    x, y, z = p
    if rotation == 0:
        return (x, y, z)
    if rotation == 1:
        return (x, -z, y)
    if rotation == 2:
        return (x, -y, -z)
    if rotation == 3:
        return (x, z, -y)
    if rotation == 4:
        return (-x, -y, z)
    if rotation == 5:
        return (-x, -z, -y)
    if rotation == 6:
        return (-x, y, -z)
    if rotation == 7:
        return (-x, z, y)
    if rotation == 8:
        return (y, x, -z)
    if rotation == 9:
        return (y, -x, z)
    if rotation == 10:
        return (y, z, x)
    if rotation == 11:
        return (y, -z, -x)
    if rotation == 12:
        return (-y, x, z)
    if rotation == 13:
        return (-y, -x, -z)
    if rotation == 14:
        return (-y, -z, x)
    if rotation == 15:
        return (-y, z, -x)
    if rotation == 16:
        return (z, x, y)
    if rotation == 17:
        return (z, -x, -y)
    if rotation == 18:
        return (z, -y, x)
    if rotation == 19:
        return (z, y, -x)
    if rotation == 20:
        return (-z, x, -y)
    if rotation == 21:
        return (-z, -x, y)
    if rotation == 22:
        return (-z, y, x)
    if rotation == 23:
        return (-z, -y, -x)


def point_diff(a, b):
    return tuple(x - y for x, y in zip(a, b))


def point_add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
class Scanner:
    def __init__(self, id):
        self.id = id
        self.points = []


scanner_re = re.compile(r'(\d+)')
with open(sys.argv[1], "r") as infile:
    scanners = []
    scanner = None
    for line in infile:
        if line.startswith('---'):
            m = scanner_re.search(line)
            scanner = Scanner(int(m[1]))
            scanners.append(scanner)
        elif line.strip():
            pt = tuple(int(a) for a in line.split(','))
            scanner.points.append(pt)
            offsets = defaultdict(int)

base_scanner = scanners.pop()
beacons_placed = set(base_scanner.points)
scanner_locs = [[0,0,0]]
while len(scanners) > 0:
    candidate_scanner = scanners.pop(0)
    is_match = False
    for rot in range(24):  # Our rotations
        offsets = defaultdict(int)
        for beacon in candidate_scanner.points:
            rot_pt = rotate_point(beacon, rot)
            for placed in beacons_placed:
                offsets[point_diff(rot_pt, placed)] += 1
        for offset, count in offsets.items():
            if count >= 12:
                is_match = True
                scanner_loc = tuple(-1 * a for a in offset)
                scanner_locs.append(scanner_loc)
                for beacon in candidate_scanner.points:
                    loc = rotate_point(beacon, rot)
                    beacons_placed.add(point_add(scanner_loc, loc))
        if is_match:
            break
    if not is_match:
        scanners.append(candidate_scanner)

print(f"Part 1: {len(beacons_placed)}")

longest_dist = -1
for i in range(len(scanner_locs) -1):
    for j in range(i, len(scanner_locs)):
        longest_dist= max(longest_dist, manhattan_dist(scanner_locs[i], scanner_locs[j]))

print(f"Part 2: {longest_dist}")
