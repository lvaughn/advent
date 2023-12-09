#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase, digits
from collections import Counter, defaultdict, deque, namedtuple
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
#import numpy as np
#import re
#import pprint
import sys


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
answer = 0

orbiting = {}
reachable = defaultdict(list)
for line in lines:
    center, sat = line.split(')')
    orbiting[sat] = center 
    reachable[sat].append(center)
    reachable[center].append(sat)
    
CACHE = {'COM': 0}
def get_orbit_count(obj):
    if obj not in CACHE:
        CACHE[obj] = 1 + get_orbit_count(orbiting[obj])
    return CACHE[obj]
    
for object in orbiting:
    answer += get_orbit_count(object)
print("Part 1", answer)

start_at = orbiting['YOU']
queue = deque([(start_at, 0)])
distances = {start_at: 0}
while len(queue) > 0:
    loc, dist = queue.popleft()
    for dest in reachable[loc]:
        if dest not in distances:
            distances[dest] = dist + 1
            queue.append((dest, dist + 1))
print("Part 2", distances['SAN'] - 1) # Subtract one because you're not orbiting Santa, but what he's orbiting