#!/usr/bin/env python3
import sys
#import numpy as np
import re
from collections import Counter, defaultdict, deque, namedtuple
# from string import ascii_uppercase, ascii_lowercase, digits
# from itertools import count, product, permutations, combinations, combinations_with_replacement
# from sortedcontainers import SortedSet, SortedDict, SortedList
# from z3 import Solver, BitVec, Distinct
# from networkx import networkx as nx  
# import pprint
# import sympy as sym
# from functools import cache


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

# directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def normalize(conn): 
    if conn[3:5] < conn[0:2]:
        return f"{conn[3:5]}-{conn[0:2]}"

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

connections = defaultdict(set)
for l in lines:
    a, b = l.split('-')
    connections[a].add(b)
    connections[b].add(a)
    
triplets = set()
for start in connections: 
    for dest in connections[start]:
        if dest > start: 
            common = connections[start] & connections[dest]
            for c in common:
                if c[0] == 't' or start[0] == '1' or dest[0] == 't':
                    triplets.add(frozenset({c, start, dest})) 
                

            

print("Part 1", len(triplets))
