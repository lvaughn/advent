#!/usr/bin/env python3
import numpy as np
import sys

def find_digit(a, i):
    block_size = i+1
    loc = i 
    total = 0
    mode = 0
    while loc < len(a):
        if mode == 0:
            total += a[loc:loc+block_size].sum()
        if mode == 2:
            total -= a[loc:loc+block_size].sum()
        mode = (mode + 1) % 4 
        loc += block_size
        
    return abs(total) % 10
        


def fft_cycle(arr):
    answer = np.zeros(arr.shape, dtype=int)
    for i in range(len(arr)):
        answer[i] = find_digit(arr, i)
    return answer 


answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

starting_arr = np.array([int(i) for i in lines[0]], dtype=int)
arr = starting_arr
for _ in range(100):
    arr = fft_cycle(arr)
    # print(arr)
    
print("Part 1", "".join(str(i) for i in arr[:8]))
