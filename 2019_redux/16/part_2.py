#!/usr/bin/env python3
import numpy as np
import sys



def fft_cycle(arr):
    answer = np.zeros(arr.shape, dtype=int)
    total = 0
    for i in range(arr.shape[0]-1, -1, -1):
        total += arr[i]
        answer[i] = total % 10 
    return answer 


answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]


answer_loc = int(lines[0][:7])
starting_arr = np.array([int(i) for i in lines[0] * 10000], dtype=int)

print(len(starting_arr), answer_loc, len(starting_arr) - answer_loc)

arr = starting_arr[answer_loc:]
for step in range(100):
    arr = fft_cycle(arr)
    print(f"Step {step}")
    
print("Part 2", "".join(str(i) for i in arr[:8]))