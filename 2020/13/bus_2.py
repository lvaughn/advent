#!/usr/bin/env python3

from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


with open('input.txt', 'r') as infile:
    _ = int(infile.readline())
    busses = infile.readline().strip().split(",")

bus_gaps = [] # list of busses, with the desired offset from time t to leave
for i, bus in enumerate(busses):
    if bus == 'x':
        continue
    bus_gaps.append((int(bus), i))

print(bus_gaps)

base = 0
skip = bus_gaps[0][0]

# OK, this is "fun"
# after each run of the loop, the following hold:
#   base: the smallest time t that satisfies problem's condition for all busses we've processed so far
#   skip: the number of minutes we can increment is and still have all the leaving conditions hold
for bus, gap in bus_gaps[1:]:
    # check each of the values that satisfies the previous busses util we find one that works for this as well
    while base % bus != (bus - gap)%bus:
        base += skip
    # Once we know that, we need a "skip" that will work for all the old busses and this one
    skip = lcm(skip, bus)

print(base)
