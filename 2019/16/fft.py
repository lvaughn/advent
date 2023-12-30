#!/usr/bin/env python3

import sys
import numpy as np

def do_phase(input):
    output = []
    in_len = len(input)
    for i in range(in_len):
        acc = 0
        pos = i+1
        ## for j in range((in_len//(pos*4)) + 1):
        ##     add_start = i + (4*pos) * j
        ##     sub_start = add_start + 2 * pos
        ##     if add_start < in_len:
        ##         add_end = min(add_start + pos, in_len)
        ##         #print("{}:Adding input[{}:{}]".format(pos, add_start, add_end))
        ##         acc += sum(input[add_start:add_end])
        ##     if sub_start < in_len:
        ##         sub_end = min(sub_start+pos, in_len)
        ##         #print("{}:Subing input[{}:{}]".format(pos, sub_start, sub_end))
        ##         acc -= sum(input[sub_start:sub_end])
        ## #print("{0} summed to {1}".format(pos, acc))
        for j in range(pos):
            add_start = i+j
            if add_start < in_len:
                acc += sum(input[add_start::4*pos])
            sub_start = i+(pos*2)+j
            if sub_start < in_len:
                acc -= sum(input[sub_start::4*pos])
        output.append(abs(acc) % 10)
    return np.array(output, dtype=int)



with open(sys.argv[1]) as f:
    line = f.read()

numbers = np.array([int(i) for i in line.strip()], dtype=int)
#print(numbers)
for i in range(100):
    numbers = do_phase(numbers)
    #print(numbers)

print([3, 4, 6, 9, 4, 6, 1, 6])
print([2, 4, 1, 7, 6, 1, 7, 6])
print(numbers[:8])

