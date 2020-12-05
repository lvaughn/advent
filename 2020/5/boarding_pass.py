#!/usr/bin/env python3

max_seat = 0

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
        max_seat = max(max_seat, seat_id)

print(max_seat)