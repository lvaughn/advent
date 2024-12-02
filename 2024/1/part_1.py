#!/usr/bin/env python3
import sys
#import numpy as np
#import re
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

first = []
second = []
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

for l in lines:
    a, b = l.split(r'   ')
    first.append(int(a))
    second.append(int(b))
    
first.sort()
second.sort()

answer = 0
for a, b in zip(first, second):
    answer += abs(a - b)
print("Part 1", answer)

counts = Counter(second)
answer = 0
for n in first:
    answer += n * counts[n]
print("Part 2", answer)
