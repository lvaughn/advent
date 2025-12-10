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
from functools import cache
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
    
segments = [] # [(points[-1], points[0])]
for a, b in zip(points[:], points[1:]):
    segments.append((a, b))
 
 
def intersects_segment(pt1, pt2):
    # Does the rectangle for these points intersect any segment? 
    x1, y1 = pt1
    x2, y2 = pt2
    
    max_x = max(x1, x2)
    max_y = max(y1, y2)
    min_x = min(x1, x2)
    min_y = min(y1, y2)
            
    for seg in segments:
        (seg_x1, seg_y1), (seg_x2, seg_y2) = seg
        
        if seg_x1 == seg_x2:  # Vertical 
            x = seg_x1
            y_min_seg = min(seg_y1, seg_y2)
            y_max_seg = max(seg_y1, seg_y2)
            
            if min_x < x < max_x and max(y_min_seg, min_y) < min(y_max_seg, max_y):
                return True
        
        elif seg_y1 == seg_y2:  # Horizontal 
            y = seg_y1
            x_min_seg = min(seg_x1, seg_x2)
            x_max_seg = max(seg_x1, seg_x2)
            
            if min_y < y < max_y and max(x_min_seg, min_x) < min(x_max_seg, max_x):
                return True
    return False 

for i, a in enumerate(points):
    for b in points[i+1:]:
        max_x = max(a[0], b[0])
        min_x = min(a[0], b[0])
        max_y = max(a[1], b[1])
        min_y = min(a[1], b[1])
        area = (1+ max_x - min_x) * (1+ max_y - min_y)
        if area <= answer:
            continue # No need to see if it's any good
        if intersects_segment(a, b):
            continue
        answer = area 

print("Part 2", answer)
