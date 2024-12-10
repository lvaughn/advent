#!/usr/bin/env python3
import sys
import numpy as np
import re
#from collections import Counter, defaultdict, deque, namedtuple
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

class File: 
    def __init__(self, id, start, size):
        self.id = id
        self.start = start 
        self.size = size 
        
    def __repr__(self):
        return f"File({self.id},{self.start},{self.size})"
        
    def checksum(self):
        result = 0
        for i in range(self.size):
            result += self.id * (i + self.start)
        return result 


answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

numbers = [int(n) for n in lines[0]]
files = []
# Load up the inital array
file_id = 0
loc = 0

for i in range(0, width, 2):
    size = numbers[i]
    f = File(file_id, loc, size)
    files.append(f)
    loc += size
    file_id += 1
    if i+1 < width:
        loc += numbers[i+1] # Skip the empty space
        
# Move everything
full_through = 0
to_move = len(files) - 1
while full_through < to_move:
    # print(f"LGV:to_move={to_move} full_through={full_through}")
    # Find where to insert, if possible
    loc = full_through
    moved = False
    while loc < to_move:
        current_file = files[loc]
        space_between = files[loc+1].start - files[loc].start - files[loc].size
        if space_between >= files[to_move].size:
            # move it
            f = files[to_move]
            f.start = current_file.start + current_file.size
            files = files[:loc+1] + [f] + files[loc+1:to_move] + files[to_move+1:]
            moved = True 
            
            # Move up starting loc if needed
            if loc == full_through:
                while files[full_through].start + files[full_through].size == files[full_through+1].start:
                    full_through += 1
            break
        else:
            loc += 1
    if not moved:
        to_move -= 1 # if we did move, the re-arrangment leaves to_move intact
               
# print(files)
for f in files:
    answer += f.checksum()

print("Part 2", answer)
