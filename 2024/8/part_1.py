#!/usr/bin/env python3
import sys
#import numpy as np
import re
from collections import Counter, defaultdict, deque, namedtuple
#from string import ascii_uppercase, ascii_lowercase, digits
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
# from z3 import Solver, BitVec, Distinct
# from networkx import networkx as nx  
#import pprint


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

def get_antinodes(ls):
    for i, a in enumerate(ls[:-1]):
        for b in ls[i+1:]:
            r_diff = a[0] - b[0]
            c_diff = a[1] - b[1]
            new_r, new_c = a[0] + r_diff, a[1] + c_diff
            if 0 <= new_r < height and 0 <= new_c < width:
                yield(new_r, new_c)
            new_r, new_c = b[0] - r_diff, b[1] - c_diff
            if 0 <= new_r < height and 0 <= new_c < width:
                yield(new_r, new_c)
            

nodes = defaultdict(list)
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch != '.' and ch != '#':
            nodes[ch].append((r, c))
            
locations = set()

for freq in nodes:
    for antinode in get_antinodes(nodes[freq]):
        locations.add(antinode)

# print(nodes)
# print(locations)
answer = len(locations)
print("Part 1", answer)

# 359