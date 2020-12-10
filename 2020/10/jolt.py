#!/usr/bin/env python3

with open('input.txt') as infile:
    adaptors = [int(n) for n in infile]

ordered = [0] + sorted(adaptors)
ordered.append(ordered[-1]+3)

ones = 0
threes = 0

for i in range(len(ordered) - 1):
    diff = ordered[i+1] - ordered[i]
    if diff == 1:
        ones += 1
    elif diff == 3:
        threes += 1
    else:
        print("Strange Diff", diff)

print(ones, threes, ones*threes)