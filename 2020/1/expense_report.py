#!/usr/bin/env python3

with open('input', 'r') as infile:
    seen = set()
    for line in infile:
        n = int(line)
        if (2020-n) in seen:
            print(n * (2020-n))
            exit()
        seen.add(n)
print("None Found")