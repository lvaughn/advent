#!/usr/bin/env python3

import re
import sys


def time_to_distance(t, total_time):
    return t * (total_time - t)
    

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

times = re.split(r'\s+', lines[0])
distances = re.split(r'\s+', lines[1])

answer = 1
for t, d in zip(times[1:], distances[1:]):
    t = int(t)
    d = int(d)
    works = 0
    for i in range(t+1):
        if time_to_distance(i, t) > d:
            works += 1 
    answer *= works 
    
print("Part 1", answer)

big_time = int("".join(times[1:]))
big_dist = int("".join(distances[1:]))

# Assume the half way point works 
assert(time_to_distance(big_time//2, big_time) > big_dist)

# Binary search for the answer
low = 0
high = big_time // 2
while low < high:
    mid = (low + high) // 2
    if time_to_distance(mid, big_time) > big_dist:
        high = mid
    else:
        low = mid + 1
        
bottom = low 

low = big_time // 2
high = big_time
while low < high:
    mid = (low + high) // 2
    if time_to_distance(mid, big_time) > big_dist:
        low = mid + 1
    else:
        high = mid
        
top = low - 1 

print("Part 2: ", top - bottom + 1)

