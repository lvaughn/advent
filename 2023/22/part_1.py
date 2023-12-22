#!/usr/bin/env python3
from collections import Counter, defaultdict, deque, namedtuple
import numpy as np
import sys

def parse_line(l):
    first, second = l.split('~')
    first = [int(i) for i in first.split(',')]
    second = [int(i) for i in second.split(',')]
    return first, second 

def is_x(a, b):
    return b[1] == a[1] and a[2] == b[2]

def is_y(a, b):
    return b[0] == a[0] and a[2] == b[2]

def is_z(a, b):
    return b[0] == a[0] and a[1] == b[1]

def get_xy_pairs(block_no):
    global original_pts, directions
    a, b = original_pts[block_no]
    dir = directions[block_no]
    if dir == 'x':
        x_min = min(a[0], b[0])
        x_max = max(a[0], b[0])
        return [(x, a[1]) for x in range(x_min, x_max+1)]
    elif dir == 'y':
        y_min = min(a[1], b[1])
        y_max = max(a[1], b[1])
        return [(a[0], y) for y in range(y_min, y_max+1)]   
    else:
        assert dir == 'z'
        return[(a[0], a[1])]
    
def clear_below(block_no, z, cells):
    global directions
    # print(f"Checking block={block_no} on level {z}")
    if z == 1:
        return False 
    return all(cells[x, y, z-1] == 0 for (x, y) in get_xy_pairs(block_no))

def move_down(block_no, z, cells):
    global directions, original_pts
    if directions[block_no] in ('x', 'y'):
        for x, y in get_xy_pairs(block_no):
            assert cells[x, y, z-1] == 0
            cells[x, y, z-1] = block_no
            cells[x, y, z] = 0
    else:
        assert directions[block_no] == 'z'
        a, b = original_pts[block_no]
        length = abs(a[2]-b[2]) + 1
        assert cells[a[0], a[1], z-1] == 0
        assert cells[a[0], a[1], z+length-1] == block_no, f"a={a} z={z} l={length} cell={cells[a[0], a[1], z+length-1]}"
        assert cells[a[0], a[1], z+length] != block_no
        cells[a[0], a[1], z-1] = block_no
        cells[a[0], a[1], z+length-1] = 0
        
def supported_by(block_no, z, cells):
    global original_pts
    if z == 1:
        return []
    answer = set()
    for x,y in get_xy_pairs(block_no):
        under = cells[x, y, z-1]
        if under == block_no or under == 0:
            continue 
        answer.add(under)
    return list(answer)
    
    
answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

max_x = max_y = max_z = -1000000
bricks = []
for line in lines:
    a, b = parse_line(line)
    max_x = max(max_x, a[0], b[0])
    max_y = max(max_y, a[1], b[1])
    max_z = max(max_z, a[2], b[2])
    bricks.append((a, b))
    
cells = np.zeros((max_x + 1, max_y + 1, max_z + 2), dtype=int)

cells[:, :, 0] = -1 # Floor

directions = {}
original_pts = {}
for n, brick in enumerate(bricks):
    a, b = brick
    original_pts[n+1] = [a, b]
    if is_x(a, b):
        start = min(a[0], b[0])
        end = max(a[0], b[0]) + 1
        cells[start:end, a[1], a[2]] = n+1
        directions[n+1] = 'x'
    elif is_y(a, b):
        start = min(a[1], b[1])
        end = max(a[1], b[1]) + 1
        cells[a[0], start:end, a[2]] = n+1
        directions[n+1] = 'y'
    else:
        assert is_z(a, b)
        start = min(a[2], b[2])
        end = max(a[2], b[2]) + 1
        cells[a[0], a[1], start:end] = n+1
        directions[n+1] = 'z'

# Settle everything to the bottom 
for z in range(1, max_z+1):
    on_level = np.unique(cells[:, :, z])
    for block_no in on_level:
        if block_no == 0:
            continue 
        this_z = z
        while(clear_below(block_no, this_z, cells)):
            move_down(block_no, this_z, cells)
            this_z -= 1
            
# See what is betting supported
on_prev_level = []
is_supported_by = defaultdict(set)
needs = defaultdict(set)
for z in range(1, max_z+1):
    on_level = np.unique(cells[:, :, z])
    for block_no in on_level:
        if block_no == 0:
            continue 
        # See if we're the top level of a stacked on
        if directions[block_no] == 'z':
            a, b = original_pts[block_no]
            if cells[a[0], a[1], z+1] == block_no: # continue # only look at the top one
                continue 
        # Look above
        can_delete = True 
        for blk in np.unique(cells[:, :, z+1]):
            if blk != 0:
                supports = supported_by(blk, z+1, cells)
                for s in supports:
                    is_supported_by[s].add(blk)
                    needs[blk].add(s)
                if len(supports) == 1 and supports[0] == block_no:
                    can_delete = False 
        # print(f"Block {block_no} can_delete:{can_delete}")
        if can_delete:
            answer += 1
    on_prev_level = on_level
        
# print(is_supported_by)
# print(needs)
            
print("Part 1", answer)

def find_collapse(block_no, needs):
    last_count = 0
    currently_deleted = set([block_no])
    while len(currently_deleted) != last_count:
        last_count = len(currently_deleted)
        for blk in needs:
            if len(needs[blk] - currently_deleted) == 0:
                currently_deleted.add(blk)
                
    return last_count - 1

answer = 0
for block_no in original_pts: 
    answer += find_collapse(block_no, needs)
    
print("Part 2", answer)
