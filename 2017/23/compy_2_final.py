#!/usr/bin/env python3

h = 0
a = 1
b = 99
c = b
if a != 0:
    b = b * 100
    b -= -100000
    c = b
    c -= -17000

g = 1
while g != 0:
    d = 2
    f = 1
    while d*d <= b:
        if b % d == 0:
            f = 0
        d += 1
    if f == 0:
        h += 1
    g = c-b
    b += 17

print(h)