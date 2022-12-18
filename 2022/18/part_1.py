#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase
#from collections import Counter, defaultdict, deque, namedtuple
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
import numpy as np
#import re
#import pprint
import sys


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

def get_surface_area(grid, loc):
    x, y, z = loc
    result = 0
    if x == 0 or grid[x-1, y, z] == 0:
        result += 1
    if grid[x+1, y, z] == 0:
        result += 1
    if y == 0 or grid[x, y-1, z] == 0:
        result += 1
    if grid[x, y+1, z] == 0:
        result += 1
    if z == 0 or grid[x, y, z-1] == 0:
        result += 1
    if grid[x, y, z+1] == 0:
        result += 1
    return result


answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    triples = [list(map(int, l.split(','))) for l in lines]

max_dim = -1
for trip in triples:
    max_dim=max(max_dim, max(trip))

grid = np.zeros((max_dim + 2, max_dim + 2, max_dim + 2))
for x, y, z in triples:
    grid[x, y, z] = 1

for trip in triples:
    answer += get_surface_area(grid, trip)
print("Part 1", answer)
