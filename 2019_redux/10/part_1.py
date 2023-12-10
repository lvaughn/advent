#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase, digits
from collections import Counter, defaultdict, deque, namedtuple
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
#import numpy as np
#import re
#import pprint
import sys
from fractions import Fraction 


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

def find_slope(a: tuple, b: tuple):
    ax, ay = a
    bx, by = b
    
    run = bx - ax 
    if run == 0:
        return 'vert'
    return Fraction(by-ay, run) # rise/run

def how_many_visible(pt, asteroids):
    # Sort by slope
    by_slope = defaultdict(list)
    for a in asteroids:
        if a == pt:
            continue
        by_slope[find_slope(a, pt)].append(a)
        
    # Now count
    result = 0
    for slope in by_slope:
        points = by_slope[slope]
        if len(points) > 1:
            # see how they're set up
            if slope == 'vert':
                if len([a for a in points if a[1] > pt[1]]) > 0:
                    result += 1
                if len([a for a in points if a[1] < pt[1]]) > 0:
                    result += 1
            else:
                if len([a for a in points if a[0] > pt[0]]) > 0:
                    result += 1
                if len([a for a in points if a[0] < pt[0]]) > 0:
                    result += 1
        else:
            result += 1
    return result, by_slope

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
asteroids = []
for y, line in enumerate(lines):
    for x, ch in enumerate(line):
        if ch == '#':
            asteroids.append((x, y))
            
best_point = None
most_visible = -1
slopes = {}          
for a in asteroids:
    n_visible, by_slope = how_many_visible(a, asteroids)
    if n_visible > most_visible:
        most_visible = n_visible
        best_point = a 
        slopes = by_slope
        
print("Part 1", most_visible)

destroyed = [] 
# One rotation will do it, since the answer to part 1 was more than 200

# start straight up
up_and_down = slopes['vert']
best_x, best_y = best_point
above = sorted(pt for pt in up_and_down if pt[1] < best_y)
destroyed.append(above[-1])

del slopes['vert'] # Deals with special case, we've stored this above
# Now, the first quadrant down (and including) slope 0
for slope in sorted([s for s in slopes.keys() if s <= 0]):
    pts_right = sorted(s for s in slopes[slope] if s[0] > best_x)
    if len(pts_right) > 0:
        destroyed.append(pts_right[0]) 

# Next, lower-right quardrant
for slope in sorted([s for s in slopes.keys() if s > 0]):
    pts_right = sorted(s for s in slopes[slope] if s[0] > best_x)
    if len(pts_right) > 0:
        destroyed.append(pts_right[0])
        
# Straight down
below = sorted(pt for pt in up_and_down if pt[1] > best_y)
destroyed.append(below[0])

# Lower-left quardrant, including negative x axis
for slope in sorted([s for s in slopes.keys() if s <= 0]):
    pts_left = list(sorted(s for s in slopes[slope] if s[0] < best_x))
    if len(pts_left) > 0:
        destroyed.append(pts_left[-1]) 

# Upper-left quadrant
for slope in sorted([s for s in slopes.keys() if s > 0]):
    pts_left = list(sorted(s for s in slopes[slope] if s[0] < best_x))
    if len(pts_left) > 0:
        destroyed.append(pts_left[-1])

answer_asteroid = destroyed[199]
print("Part 2", answer_asteroid[0] * 100 + answer_asteroid[1])




