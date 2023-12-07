#!/usr/bin/env python3

import re
import math
import sys


def number_of_solutions(total_time, total_dist):
    """
    Find the number of integers where:
    
    x * (total_time - x) - total_dist
     
    is positive. 
    """
    
    # -x**2 + total_time * x - total_dist > 0
    a = -1
    b = total_time
    c = -(total_dist+1) # Make sure it beats it
    
    # Use the quadratic formula
    determinate = b**2 - 4*a*c
    lower = (-b + math.sqrt(determinate)) / (2*a)
    upper = (-b - math.sqrt(determinate)) / (2*a)
    return math.floor(upper) - math.ceil(lower) + 1 # Avoid fencepost errors
    

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

times = re.split(r'\s+', lines[0])
distances = re.split(r'\s+', lines[1])

answer = 1
for t, d in zip(times[1:], distances[1:]):
    t = int(t)
    d = int(d)
    answer *= number_of_solutions(t, d) 
    
print("Part 1", answer)

big_time = int("".join(times[1:]))
big_dist = int("".join(distances[1:]))

print("Part 2: ", number_of_solutions(big_time, big_dist))

