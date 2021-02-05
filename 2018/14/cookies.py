#!/usr/bin/env python3

target = 236021

pos_1 = 0
pos_2 = 1

values = [3, 7]
while len(values) < target + 10:
    new_values = [int(d) for d in str(values[pos_1] + values[pos_2])]
    values.extend(new_values)
    pos_1 = (pos_1 + 1 + values[pos_1]) % len(values)
    pos_2 = (pos_2 + 1 + values[pos_2]) % len(values)

print(''.join(str(d) for d in values[target:target+10]))