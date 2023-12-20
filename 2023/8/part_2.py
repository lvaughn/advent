#!/usr/bin/env python3

import re
import sys
import math 

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
def all_zs(locations):
    for l in locations:
        if l[-1] != 'Z':
            return False 
    return True 
    
connections = {}
line_re = re.compile(r'(\w\w\w)\s+=\s+\((\w\w\w),\s+(\w\w\w)\)')
for line in lines[2:]:
    m = line_re.match(line)
    connections[m.group(1)] = (m.group(2), m.group(3))
    
moves = lines[0]

locations = [l for l in connections if l[2] == 'A']
    
distances = []
for l in locations:
    start = l 
    dist = 0
    while l[-1] != 'Z':
        for ch in moves:
            dist += 1
            if ch == 'L':
                l = connections[l][0]
            else:
                l = connections[l][1]
    distances.append(dist)
    
answer = 1
for d in distances:
    answer = (answer * d)//math.gcd(answer, d)
        

print("Part 2", answer)
