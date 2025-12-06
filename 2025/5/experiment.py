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
from intervaltree import IntervalTree
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

dividing_line = lines.index('')
tree = IntervalTree()
for l in lines[:dividing_line]:
    bottom, top = l.split('-')
    tree[int(bottom):int(top)+1] = True
    
    
for l in lines[dividing_line+1:]:
    if tree[int(l)]:
        answer += 1
        
print("Part 1", answer)

tree.merge_overlaps()
part_2 = 0
for r in tree: 
    part_2 += r.end - r.begin
    
print("Part 2", part_2)
