#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase, digits
from collections import Counter, defaultdict, deque, namedtuple
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
#import numpy as np
#import re
#import pprint
import sys
import heapq


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

width = len(lines[0])
height = len(lines)

def get_directions(x, y, dir, n_in_row):
    global height, width
    results = []
    if dir == 'n':
        if n_in_row < 4:
            if y > 0:
                results.append((x, y-1, 'n', n_in_row + 1))
            return results 
        if n_in_row < 10 and y > 0:
            results.append((x, y-1, 'n', n_in_row + 1))
        if x > 0:
            results.append((x - 1, y, 'w', 1))
        if x < width - 1:
            results.append((x + 1, y, 'e', 1))
    elif dir =='s':
        if n_in_row < 4:
            if y < height - 1:
                results.append((x, y+1, 's', n_in_row + 1))
            return results
        if n_in_row < 10 and y < height - 1:
            results.append((x, y+1, 's', n_in_row + 1))
        if x > 0:
            results.append((x - 1, y, 'w', 1))
        if x < width - 1:
            results.append((x + 1, y, 'e', 1))
    elif dir == 'e':
        if n_in_row < 4:
            if x < width - 1:
                results.append((x+1, y, 'e', n_in_row + 1))
            return results 
        if n_in_row < 10 and x < width - 1:
            results.append((x+1, y, 'e', n_in_row + 1))     
        if y > 0:
            results.append((x, y-1, 'n', 1))   
        if y < height - 1:
            results.append((x, y+1, 's', 1)) 
    elif dir == 'w':
        if n_in_row < 4:
            if  x > 0:
                results.append((x-1, y, 'w', n_in_row + 1))
            return results 
        if n_in_row < 10 and x > 0:
            results.append((x-1, y, 'w', n_in_row + 1))     
        if y > 0:
            results.append((x, y-1, 'n', 1))   
        if y < height - 1:
            results.append((x, y+1, 's', 1)) 
    else:
        assert False, f"Unexpected direction"
    return results 

#state = (heat_loss, location, dir, n_in_row)


queue = [(0, (0, 0), 'e', 0, [])]
heapq.heapify(queue)

best_routes = {}

best_so_far = None
while len(queue) > 0 and best_so_far is None:
    (heat_loss, location, dir, n_in_row, path) = heapq.heappop(queue)
    # print(f"loc={location} dir={dir} in_row={n_in_row} hl={heat_loss}")
    x, y = location
    key = (location, dir, n_in_row)
    if key in best_routes:
        assert heat_loss >= best_routes[key]
        continue  
    best_routes[key] = heat_loss
    if x == width - 1 and y == height - 1:
        if 4 <= n_in_row <= 10:
            best_so_far =  heat_loss
        continue 
    for new_x, new_y, new_dir, new_n_in_row in get_directions(x, y, dir, n_in_row):
        new_loc = (new_x, new_y)
        new_heat_loss = int(lines[new_y][new_x]) + heat_loss
        heapq.heappush(queue, (new_heat_loss, new_loc, new_dir, new_n_in_row, path +[new_loc]))
        
print("Part 1", best_so_far)
