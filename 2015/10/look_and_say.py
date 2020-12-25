#!/usr/bin/env python3

start = '1113222113'

def run_length_encode(arr):
    values = []
    lengths = []
    current = None
    length = 0
    for val in arr:
        if val == current:
            length += 1
        else:
            if current is not None:
                lengths.append(length)
                values.append(current)
            current = val
            length = 1
    lengths.append(length)
    values.append(current)
    return values, lengths

ls = [int(i) for i in start]
for i in range(50):
    values, lengths = run_length_encode(ls)
    ls = []
    for v, l in zip(values, lengths):
        ls.append(l)
        ls.append(v)
    #print(ls)
#print(''.join([str(i) for i in ls]))
print(len(ls))