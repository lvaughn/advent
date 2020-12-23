#!/usr/bin/env python

import re
import itertools
import sys

dists = {}
locations = set()
with open('input.txt', 'r') as f:
    line_re = re.compile(r'(\w+)\s+to\s+(\w+)\s+=\s+(\d+)')
    for line in f:
        m = line_re.match(line)
        dists[(m[1], m[2])] = int(m[3])
        dists[(m[2], m[1])] = int(m[3])
        locations.add(m[1])
        locations.add(m[2])

best_path = sys.maxsize
worst_path = -1
for path in itertools.permutations(locations):
    dist = 0
    for i in range(len(path)-1):
        dist += dists[(path[i], path[i+1])]
    if dist < best_path:
        best_path = dist
    if dist > worst_path:
        worst_path = dist

print(best_path)
print(worst_path)