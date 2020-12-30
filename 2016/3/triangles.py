#!/usr/bin/env python

import re

valid_triangles = 0
with open('input.txt', 'r') as f:
    for line in f:
        values = sorted([int(x) for x in re.split(r'\s+', line.strip())])
        assert len(values) == 3
        if values[0] + values[1] > values[2]:
            valid_triangles += 1

print(valid_triangles)