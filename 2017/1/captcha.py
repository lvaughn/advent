#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    digits = [int(a) for a in f.read().strip()]

total = 0
for i in range(len(digits)):
    if digits[i] == digits[(i+1)%len(digits)]:
        total += digits[i]
print("Part 1", total)

total = 0
skip = len(digits)//2
for i in range(len(digits)):
    if digits[i] == digits[(i+skip)%len(digits)]:
        total += digits[i]
print("Part 1", total)