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
    results = []
    width = arr.shape[0]
    for i in range(width - 1):
        # Try splitting after i 
        h = min(i+1, width - i -1)
        # print(f"i={i}, h={h}")
        top = arr[(i+1)-h:i+1, :]
        bottom = arr[i+1:i+h+1, :]
        # print(top)
        # print(bottom)
        top_flipped = np.flipud(top)
        # print(top_flipped)
        # print("LGV", np.array_equal(bottom, top_flipped))
        if np.array_equal(bottom, top_flipped):
            results.append(i + 1)
    return results 
        
def find_hor_sym(arr):
    results = []
    height = arr.shape[1]
    for i in range(height - 1):
        # Try splitting after i 
        w = min(i+1, height - i -1)
        # print(f"i={i}, h={h}")
        left = arr[:, (i+1)-w:i+1]
        bottom = arr[:, i+1:i+w+1]
        # print(bottom)
        left_flipped = np.fliplr(left)
        # print(top_flipped)
        # print("LGV", np.array_equal(bottom, top_flipped))
        if np.array_equal(bottom, left_flipped):
            results.append(i + 1)
    return results 

def mutate_wrapper(arr, f):
    # print(arr)
    results = []
    for r in range(arr.shape[0]):
        for c in range(arr.shape[1]):
            value = arr[r, c]
            arr[r, c] = 1 - arr[r, c]
            # print(r, c, value)
            # print(arr)
            v = f(arr)
            arr[r, c] = value
            if v:
                # print("LGV: Returning", v)
                results.append(v)
            
    return results 

def dedup(ls):
    results = set()
    for l in ls:
        if isinstance(l, list):
            l = dedup(l)
            for n in l:
                results.add(n)
        else:
            results.add(l)
        
    return results

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
        v = mutate_wrapper(arr, find_vert_sym)
        h = mutate_wrapper(arr, find_hor_sym)
        orig_v = find_vert_sym(arr)
        orig_h = find_hor_sym(arr)
        v = dedup(v)
        if v is not None:
            for n in [x for x in v if x not in orig_v]:
                vert_total += n 
        h = dedup(h)
        if h is not None:
            for n in [x for x in h if x not in orig_h]:
                hor_total += n            
        first_row = row +1
rows = lines[first_row:row+1]
arr = make_array(rows)
v = mutate_wrapper(arr, find_vert_sym)
h = mutate_wrapper(arr, find_hor_sym)
orig_v = find_vert_sym(arr)
orig_h = find_hor_sym(arr)
v = dedup(v)
if v is not None:
    for n in [x for x in v if x not in orig_v]:
        vert_total += n 
h = dedup(h)
if h is not None:
    for n in [x for x in h if x not in orig_h]:
        hor_total += n 
            
print("Part 2", vert_total*100 + hor_total)
