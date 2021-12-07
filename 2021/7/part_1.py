#!/usr/bin/env python3

import numpy as np
import sys

def triangle(n):
    n = abs(n)
    return (n*(n+1))//2

with open("input.txt", "r") as infile:
    positions = np.array([int(l) for l in infile.readline().split(',')], dtype=int)

start = min(positions)
stop = max(positions)

min_fuel = 100000000000
for location in range(start, stop + 1):
    fuel = sum(abs(positions - location))
    min_fuel = min(min_fuel, fuel)

print(f"Part 1: {min_fuel}")

min_fuel = 1000000000000
for location in range(start, stop + 1):
    fuel = sum(triangle(positions - location))
    min_fuel = min(min_fuel, fuel)

print(f"Part 2: {min_fuel}")


