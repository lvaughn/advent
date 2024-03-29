#!/usr/bin/env python3
from string import ascii_uppercase, ascii_lowercase, digits
from collections import Counter, defaultdict, deque, namedtuple
import heapq 
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
#import numpy as np
#import re
import pprint
import sys


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

def get_distances(start_loc, grid):
    fastest_paths = {} # Destination: distance
    visited = set()
    queue = deque([(start_loc, 0)])
    while len(queue) > 0:
        loc, dist = queue.popleft()
        if loc in visited:
            continue 
        visited.add(loc)
        r, c = loc 
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_loc = new_r, new_c = r+dr, c+dc 
            if new_loc in fastest_paths or new_loc == start_loc:
                continue 
            if grid[new_r][new_c] == '#':
                continue 
            elif grid[new_r][new_c] == '.':
                queue.append((new_loc, dist+1))
            else: 
                fastest_paths[new_loc] = dist+1
                
    return fastest_paths
    
answer = "Didn't work!!!"
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
height = len(lines)
width = len(lines[0])

n_keys = 0
start_loc = None

landmarks = []
starting_locations = []
for r, line in enumerate(lines):
    for c, ch in enumerate(line): 
        if ch in ascii_lowercase:
            n_keys += 1
        if ch == '@':
            starting_locations.append((r, c))
        if ch not in ('.', '#'):
            landmarks.append((r, c))
            
connections = {}
for l in landmarks:
    connections[l] = get_distances(l, lines)
    
# pprint.pprint(connections)
print(f"Starting at {starting_locations}, n_keys={n_keys}")
# distance_traveled, location, keys_collected
tried = set()
pri_queue = [(0, starting_locations, set())]
heapq.heapify(pri_queue)
while len(pri_queue) > 0:
    dist, locations, keys_collected = heapq.heappop(pri_queue)
    key = (tuple(locations), frozenset(keys_collected))
    if key in tried:
        continue 
    tried.add(key)
    for r, c in locations:
        if lines[r][c] in ascii_lowercase:
            keys_collected = keys_collected | {lines[r][c]}
    if len(keys_collected) == n_keys:
        answer = dist
        break 
    for i in range(len(locations)):
        loc = locations[i]
        for dest in connections[loc]:
            ch = lines[dest[0]][dest[1]]
            if ch in ascii_uppercase and ch.lower() not in keys_collected:
                continue 
            new_locations = locations[:i] + [dest] + locations[i+1:]
            new_item = (dist + connections[loc][dest], new_locations, keys_collected)
            heapq.heappush(pri_queue, new_item)

        
print("Part 2", answer)
