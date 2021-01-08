#!/usr/bin/env python3

import re

rows = []
total = 0
with open('input.txt', 'r') as f:
    for line in f:
        data = [int(a) for a in re.split(r'\s+', line.strip())]
        total += max(data) - min(data)
        rows.append(data)

print("Part 1", total)

total = 0
for row in rows:
    for i in range(len(row) - 1):
        found = False
        for j in range(i+1, len(row)):
            if max(row[i], row[j]) % min(row[i], row[j]) == 0:
                total += max(row[i], row[j]) // min(row[i], row[j])
                found = True
                break
        if found:
            break

print('Part 2', total)
