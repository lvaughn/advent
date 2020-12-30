#!/usr/bin/env python

import re

valid_triangles = 0
data = []
with open('input.txt', 'r') as f:
    for line in f:
        data.append([int(x) for x in re.split(r'\s+', line.strip())])
        # values = sorted([int(x) for x in re.split(r'\s+', line.strip())])
        # assert len(values) == 3
        # if values[0] + values[1] > values[2]:
        #     valid_triangles += 1

for i in range(len(data)//3):
    for c in range(3):
        sides = [data[i*3][c], data[i*3+1][c], data[i*3+2][c]]
        sides.sort()
        if sides[0] + sides[1] > sides[2]:
            valid_triangles += 1

print(valid_triangles)