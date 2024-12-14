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


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def move(self):
        self.x += self.vx
        self.y += self.vy 
        
        self.x = self.x % 101
        self.y = self.y % 103
        
        

answer = 0
robot_re = re.compile(r'p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)')
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

robots = []
for l in lines:
    m = robot_re.match(l)
    assert m is not None 
    r = Robot(int(m[1]), int(m[2]), int(m[3]), int(m[4]))
    robots.append(r)
    
for _ in range(100):
    for r in robots:
        r.move()
        
a = 0
b = 0
c = 0 
d = 0 

for r in robots:
    if r.x < 50 and r.y < 51:
        a += 1
    elif r.x > 50 and r.y < 51:
        b += 1
    elif r.x < 50 and r.y > 51:
        c += 1
    elif r.x > 50 and r.y > 51:
        d += 1
    else: 
        assert r.x == 50 or r.y == 51, f"{r.x},{r.y}"

print("Part 1", a*b*c*d)
