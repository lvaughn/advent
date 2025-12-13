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
from shapely import Polygon

# import pprint
# from functools import cache
# import numpy as np
# import re
from pprint import pprint 

# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

# directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

points = []
for l in lines:
    x, y = l.split(",")
    points.append((int(x), int(y)))
    
polygon_points = points + [points[0]]
polygon = Polygon(polygon_points)

for i, a in enumerate(points):
    for b in points[i+1:]:
        max_x = max(a[0], b[0])
        min_x = min(a[0], b[0])
        max_y = max(a[1], b[1])
        min_y = min(a[1], b[1])
        area = (1+ max_x - min_x) * (1+ max_y - min_y)
        if area <= answer:
            continue # No need to see if it's any good
        rect = Polygon([(min_x, min_y), (min_x, max_y), (max_x, max_y), (max_x, min_y), (min_x, min_y)])
        if polygon.contains(rect):
            answer = area  # we already know it's bigger

print("Part 2", answer)
