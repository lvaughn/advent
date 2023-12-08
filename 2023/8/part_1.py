#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase, digits
#from collections import Counter, defaultdict, deque, namedtuple
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
#import numpy as np
import re
#import pprint
import sys


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
connections = {}
line_re = re.compile(r'(\w\w\w)\s+=\s+\((\w\w\w),\s+(\w\w\w)\)')
for line in lines[2:]:
    m = line_re.match(line)
    connections[m.group(1)] = (m.group(2), m.group(3))
    
moves = lines[0]

loc = 'AAA'
while loc != 'ZZZ':
    for ch in moves:
        answer += 1
        if ch == 'L':
            loc = connections[loc][0]
        else:
            loc = connections[loc][1]
    

print("Part 1", answer)
