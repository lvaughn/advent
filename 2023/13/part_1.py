#!/usr/bin/env python3
import numpy as np
import sys


def make_array(rows):
    height = len(rows)
    width = len(rows[0])
    arr = np.zeros((height, width), dtype=int)
    for r in range(height):
        for c in range(width):
            if rows[r][c] == '#':
                arr[r, c] = 1
    return arr 

def find_vert_sym(arr):
    width = arr.shape[0]
    for i in range(width - 1):
        # Try splitting after i 
        h = min(i+1, width - i -1)
        top = arr[(i+1)-h:i+1, :]
        bottom = arr[i+1:i+h+1, :]
        top_flipped = np.flipud(top)
        if np.array_equal(bottom, top_flipped):
            return i + 1
    return None 
        
def find_hor_sym(arr):
    height = arr.shape[1]
    for i in range(height - 1):
        # Try splitting after i 
        w = min(i+1, height - i -1)
        left = arr[:, (i+1)-w:i+1]
        bottom = arr[:, i+1:i+w+1]
        left_flipped = np.fliplr(left)
        if np.array_equal(bottom, left_flipped):
            return i + 1
    return None 

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

first_row = 0
hor_total = 0
vert_total = 0
for row in range(len(lines)):   
    if lines[row] == '':
        rows = lines[first_row:row]
        arr = make_array(rows)
        v = find_vert_sym(arr)
        h = find_hor_sym(arr)
        if v is not None:
            vert_total += v 
        if h is not None:
            hor_total += h 
        first_row = row +1
rows = lines[first_row:row+1]
arr = make_array(rows)
v = find_vert_sym(arr)
h = find_hor_sym(arr)
# print(h, v)
if v is not None:
    vert_total += v 
if h is not None:
    hor_total += h 
            
print("Part 1", vert_total*100 + hor_total)
