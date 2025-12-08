#!/usr/bin/env python3
import sys
from collections import Counter, defaultdict, deque, namedtuple
# from string import ascii_uppercase, ascii_lowercase, digits
# from itertools import count, product, permutations, combinations, combinations_with_replacement
# from sortedcontainers import SortedSet, SortedDict, SortedList
# from z3 import Solver, BitVec, Distinct
# from networkx import networkx as nx  
# import sympy as sym
# from intervaltree import IntervalTree

# import pprint
# from functools import cache
# import numpy as np
# import re
import math 

# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

# directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

def find_network(pt, network, reachability):
    if pt in network:
        return
    network.add(pt)
    for p in reachability[pt]:
        find_network(p, network, reachability) 
    

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
points = []
for l in lines:
    a, b, c = l.split(",")
    points.append((int(a), int(b), int(c)))
    
distances = []
for i, a in enumerate(points[:-1]):
    for b in points[i+1:]:
        distances.append((distance(a, b), a, b))
        
distances.sort()

reachable = defaultdict(list)
for dist, a, b in distances:
    reachable[a].append(b)
    reachable[b].append(a)
    
    network = set()
    find_network(a, network, reachable)
    if len(network) == len(lines):
        answer = a[0] * b[0]
        break
    
print("Part 2", answer)
