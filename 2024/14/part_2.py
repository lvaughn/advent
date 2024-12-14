#!/usr/bin/env python3
import sys
import numpy as np
import re
from collections import Counter, defaultdict, deque, namedtuple
import os 
import time 
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
        # self.locations = set()
        # self.locations.add((x,y))
    
    def move(self):
        self.x += self.vx
        self.y += self.vy 
        
        self.x = self.x % 101
        self.y = self.y % 103
        
        # is_in = (self.x, self.y) in self.locations
        
        # self.locations.add((self.x, self.y))
        
        # return is_in
        
        
def display_robots(bots):
    board = np.zeros((101, 103), dtype=int)
    for b in bots:
        board[b.x, b.y] += 1
    
    for y in range(103):
        s = ""
        for x in range(101):
            if board[x, y] > 0:
                s += "*"
            else:
                s += " "
        print(s)    
    
def is_symetric(bots):
    n_left = 0
    n_right = 0
    for b in bots:
        if b.x < 50:
            n_left += 1
        if b.x > 50:
            n_right += 1
    return n_left == n_right

CORNER = 15
def no_corners(bots):
    for b in bots:
        if b.y < CORNER:
            if b.x < CORNER - b.y or b.x > (101-CORNER) + b.y:
                return False 
    return True 
    
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
    
# I noticed that on a semi-regular basis there seemed to be a strong vertical or horizontal 
# "thing" going on, so I found the periods and skipping by that makes it obvious (and in fact,
# the intersection of both periods is the time you see the tree)
for i in range(101*103):
    if i % 103 == 76: #i%101 == 4: 
        os.system('clear')
        display_robots(robots)
        print(f"Step {i}")
        time.sleep(0.5)
    for r in robots:
        r.move()

# 4, 105
# 76, 179, 282