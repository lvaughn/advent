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
file_size = []
file_locations = []
for i in range(0, width, 2):
    size = numbers[i]
    file_size.append(size)
    file_locations.append(loc)
    for _ in range(size):
        disk[loc] = file_id
        loc += 1
    file_id += 1
    if i+1 < width:
        loc += numbers[i+1] # Skip the empty space
        
# do the moves
# print(file_size)
# print(file_locations)
earliest_free_space = file_size[0] # The earliest (possible) free space
for i in range(len(file_locations) - 1, 0, -1): # We can skip zero, since it's at the start
    # Find a place (if any) to move it
    for j in range(earliest_free_space, file_locations[i]):
        file_len = file_size[i]
        if sum(disk[j:j+file_len]) == -file_len:
            disk[j:j+file_len] = i
            loc = file_locations[i]
            disk[loc:loc+file_len] = -1
            if j == earliest_free_space:
                while disk[earliest_free_space] != -1:
                    earliest_free_space += 1
            break 
            
# print(disk)
        
for i, n in enumerate(disk):
    if n >= 0:
        answer += i * n


print("Part 1", answer)
