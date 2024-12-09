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

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

numbers = [int(n) for n in lines[0]]
total_bytes = sum(numbers)
disk = np.zeros((total_bytes), dtype=int) - 1

# Load up the inital array
file_id = 0
loc = 0
for i in range(0, width, 2):
    size = numbers[i]
    for _ in range(size):
        disk[loc] = file_id
        loc += 1
    file_id += 1
    if i+1 < width:
        loc += numbers[i+1] # Skip the empty space
        
# do the moves
begin = 0
end = len(disk) - 1
while begin < end:
    if disk[end] == -1:
        end -= 1
    else:
        if disk[begin] != -1:
            begin += 1
        else: # Do the move
            disk[begin] = disk[end]
            disk[end] = -1
            begin += 1
            end -= 1
            
# print(disk)
        
for i, n in enumerate(disk):
    if n >= 0:
        answer += i * n


print("Part 1", answer)
