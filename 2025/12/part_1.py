#!/usr/bin/env python3
import sys
# from collections import Counter, defaultdict, deque, namedtuple
# from string import ascii_uppercase, ascii_lowercase, digits
# from itertools import count, product, permutations, combinations, combinations_with_replacement
# from sortedcontainers import SortedSet, SortedDict, SortedList
# from z3 import Solver, BitVec, Distinct, Int, Sum, sat, Optimize #pip install z3-solver
# from networkx import networkx as nx  
# import sympy as sym
# from intervaltree import IntervalTree

# import pprint
# from functools import cache
import numpy as np
# import re

# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

# directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# def expand_shape(shape: np.ndarray) -> list[np.ndarray]:
#     results = [shape]
#     for i in range(1, 4):
#         new_shape = np.rot90(shape, k=i)
#         sim_bools = [np.array_equal(s, new_shape) for s in results]
#         if not any(sim_bools):
#             results.append(new_shape)
#     flip_shape = np.fliplr(shape)        
#     sim_bools = [np.array_equal(s, flip_shape) for s in results]
#     if not any(sim_bools):
#         results.append(flip_shape)     
#     for i in range(1, 4):
#         new_shape = np.rot90(flip_shape, k=i)
#         sim_bools = [np.array_equal(s, new_shape) for s in results]
#         if not any(sim_bools):
#             results.append(new_shape)    
#     return results 
    

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]


# Load 5  3x3 shapes
init_shapes = []
for i in range(6):
    shape = np.zeros((3, 3), dtype=np.int8)
    for r in range(3):
        for c in range(3):
            if lines[i*5+1+r][c] == '#':
                shape[r, c] = 1
    init_shapes.append(shape)
    
# shapes = []
# for s in init_shapes:
#     shapes.append(expand_shape(s))
    
shape_sizes = [np.sum(s) for s in init_shapes]

cant_fit = 0
must_fit = 0
may_fit = 0
for row in lines[30:]:
    dims, counts = row.split(':')
    counts = [int(c) for c in counts.strip().split(' ')]
    height, width = dims.split('x')
    area = int(height) * int(width)
    min_area = sum(shape_sizes[i]*counts[i] for i in range(6))
    max_area = 9 * sum(counts)
    if area > max_area:
        must_fit += 1
    elif area < min_area:
        cant_fit += 1
    else:
        may_fit += 1
        
print(may_fit, must_fit, cant_fit)

print("Part 1", may_fit + must_fit)
