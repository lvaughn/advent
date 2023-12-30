#!/usr/bin/env python3

import sys
import numpy as np

add_array_cache = {}
sub_array_cache = {}
def get_add_array(pos, in_len):
    if pos not in add_array_cache:
        arr = []
        for j in range((in_len//(pos*4)) + 1):
            add_start = pos-1 + (4*pos) * j
            for i in range(add_start, add_start + pos):
                if i < in_len:
                    arr.append(i)
        add_array_cache[pos] = np.array(arr, dtype=int)
        print("Calculated add array for {}: len={}".format(pos, len(arr)))
    return add_array_cache[pos]

def get_sub_array(pos, in_len):
    if pos not in sub_array_cache:
        arr = []
        for j in range((in_len//(pos*4)) + 1):
            sub_start = pos-1 + (4*pos) * j + 2 * pos
            for i in range(sub_start, sub_start + pos):
                if i < in_len:
                    arr.append(i)
        sub_array_cache[pos] = np.array(arr, dtype=int)
    return sub_array_cache[pos]

def do_phase(input):
    output = []
    in_len = len(input)
    for i in range(in_len):
        total = sum(input[get_add_array(i+1, in_len)]) - sum(input[get_sub_array(i+1, in_len)])
        output.append(abs(total) % 10)
    return np.array(output, dtype=int)



with open(sys.argv[1]) as f:
    line = f.read()

offset = int(line[:7])
print("Offset: {}".format(offset))

numbers = np.array([int(i) for i in line.strip()]*10000, dtype=int)
#print(numbers)
for i in range(100):
    print(i)
    numbers = do_phase(numbers)
    #print(numbers)

#print([3, 4, 6, 9, 4, 6, 1, 6])
#print([2, 4, 1, 7, 6, 1, 7, 6])
print(numbers[offset:offset+8])

