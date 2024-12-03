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

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

mul_re = re.compile(r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))')

answer = 0
enabled = True
for l in lines:
    for m in mul_re.findall(l):
        if m[0] == 'do()':
            enabled = True
        elif m[0] == "don't()":
            enabled = False
        else:
            if enabled:
                answer += int(m[1])*int(m[2])

print("Part 2", answer)
