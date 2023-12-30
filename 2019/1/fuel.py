#!/usr/bin/env python

total = 0
with open('input.txt') as i:
    for line in i:
        total += int(line)/3-2

print total
