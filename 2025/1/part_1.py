#!/usr/bin/env python3
import sys
#import numpy as np
import re
# from collections import Counter, defaultdict, deque, namedtuple
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


answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

location = 50
for l in lines:
    dir = l[0]
    dist = int(l[1:])
    
    if dir == 'R':
        location += dist 
        location = location % 100 
    else:
        assert dir == 'L'
        location -= dist 
        while location < 0: 
            location += 100
    if location == 0:
        answer += 1
        


print("Part 1", answer)

answer = 0
location = 50
for l in lines:
    dir = l[0]
    dist = int(l[1:])
    
    if dir == 'R':
        for _ in range(dist):
            location += 1
            location = location % 100 
            if location == 0: 
                answer += 1
    else:
        assert dir == 'L'
        for _ in range(dist):
            location -= 1
            if location < 0: 
                location += 100
            if location == 0: 
                answer += 1
                
print("Part 2", answer) 
