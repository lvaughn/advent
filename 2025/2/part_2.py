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

ranges = lines[0].split(',')
for r in ranges: 
    low, high = r.split('-')
    for n in range(int(low), int(high)+1):
        s = str(n)
        n_letters = len(s)
        for seg_length in range(1, (n_letters // 2)+1):
            if n_letters % seg_length != 0:
                continue 
            # print(s[:seg_length]), s[:seg_length] * (n_letters // seg_length)
            if s[:seg_length] * (n_letters // seg_length) == s:
                answer += n 
                break 

print("Part 2", answer)
