#!/usr/bin/env python3

seats = [False] * (8 * 128)

with open('input.txt') as infile:
    for line in infile:
        row = 0
        col = 0
        for c in line:
            if c == 'B':
                row = 2*row + 1
            if c == 'F':
                row *= 2
            if c == 'R':
                col = 2*col + 1
            if c == 'L':
                col *= 2
        seat_id = row * 8 + col
        seats[seat_id] = True

for i in range(1, len(seats) - 1):
    if not seats[i] and seats[i-1] and seats[i+1]:
        print(i)