#!/usr/bin/env python3

paper_needed = 0
ribbon_needed = 0
with open('input.txt', 'r') as f:
    for line in f:
        [h,w,l] = [int(a) for a in line.split('x')]
        side_a = h*w
        side_b = h*l
        side_c = w*l
        paper_needed += min(side_a, side_b, side_c) + 2*side_a + 2*side_b + 2*side_c
        smallest_perimiter = 2*(h+w+l-max(h,w,l))
        ribbon_needed += h*w*l + smallest_perimiter

print("Paper", paper_needed)
print("Ribbon", ribbon_needed)