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
from functools import cache


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

# directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def is_possible(st, towels):
    if len(st) == 0:
        return True 
    for t in towels:
        if st.startswith(t):
            if is_possible(st[len(t):], towels):
                return True 
    return False

@cache
def ways_possible(st):   
    if len(st) == 0:
        return 1
    result = 0
    for t in towels:
        if st.startswith(t):
            result += ways_possible(st[len(t):])
    return result 
    
answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

towels = [x.strip() for x in lines[0].split(',')]

for l in lines[2:]:
    if is_possible(l, towels):
        answer += 1
        
print("Part 1", answer)

@cache
def ways_possible(st):   
    if len(st) == 0:
        return 1
    result = 0
    for t in towels:
        if st.startswith(t):
            result += ways_possible(st[len(t):])
    return result 

answer = 0 
for l in lines[2:]:
    answer += ways_possible(l)

print("Part 2", answer)
