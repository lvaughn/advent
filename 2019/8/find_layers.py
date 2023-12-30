#!/usr/bin/env python

def count_char(c, st):
    count = 0
    for a in st:
        if a == c:
            count += 1
    return count

with open('input.txt') as i:
    digits = i.readline().strip()

frames = []
while len(digits) > 0:
    frames.append(digits[:150])
    digits = digits[150:]

lowest_zeros = 151
best_frame = None
for frame in frames:
    n_zeros = count_char('0', frame)
    if n_zeros < lowest_zeros:
        lowest_zeros = n_zeros
        best_frame = frame

print count_char('1', best_frame) * count_char('2', best_frame)
