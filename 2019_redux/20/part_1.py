#!/usr/bin/env python3
from string import ascii_uppercase, ascii_lowercase, digits
from collections import Counter, defaultdict, deque, namedtuple
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
#import numpy as np
#import re
import pprint
import sys

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l for l in infile]
height = len(lines)
width = len(lines[0])

# Get the locations of portals     
portal_locations = defaultdict(list)

for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch in ascii_uppercase:
            if c < width - 1 and lines[r][c+1] in ascii_uppercase:
                name = lines[r][c:c+2]
                if c > 0 and lines[r][c-1] == '.':
                    portal_locations[name].append((r, c-1))
                elif c < width-2 and lines[r][c+2] == '.':
                    portal_locations[name].append((r, c+2))
                else:
                    assert False, f"Couldn't find portal in line {r} {line}"
            if r < height - 1 and lines[r+1][c] in ascii_uppercase:
                name = ch + lines[r+1][c]
                if r > 0 and lines[r-1][c] == '.':
                    portal_locations[name].append((r-1, c))
                elif r < height - 2 and lines[r+2][c] == '.':
                    portal_locations[name].append((r+2, c))
                else:
                    assert False, f"Can't find portal at {r}, {c}"
                
point_to_portal = {}
for portal in portal_locations:
    for loc in portal_locations[portal]:
        point_to_portal[loc] = portal
        
starting_point = portal_locations['AA'][0]
ending_point = portal_locations['ZZ'][0]
points_visited = set()
queue = deque([(starting_point, 0)]) # state is (location, distance)

while len(queue) > 0:
    loc, dist = queue.popleft()
    if loc == ending_point:
        answer = dist 
        break # We're done 
    if loc in points_visited:
        continue 
    points_visited.add(loc)
    r, c = loc 
    for dr, dc in [(0, 1), (0,-1), (1,0), (-1, 0)]:
        new_r, new_c = r + dr, c + dc 
        if new_r < 0 or new_r >= height or new_c < 0 or new_c >= width:
            continue # Actually shouldn't happen given the file setup 
        if lines[new_r][new_c] == '#':
            continue 
        elif lines[new_r][new_c] in ascii_uppercase:
            # we hit a portal 
            portal_name = point_to_portal[loc]
            dests = portal_locations[portal_name]
            if len(dests) > 1:
                dest = [d for d in dests if d != loc][0]
                queue.append((dest, dist+1))
        else:
            assert lines[new_r][new_c] == '.'
            queue.append(((new_r, new_c), dist+1))
            
        
print("Part 1", answer)
