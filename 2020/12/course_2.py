#!/usr/bin/env python3

with open('input.txt') as infile:
    directions = [a.strip() for a in infile]

ship_x = 0
ship_y = 0
wp_x = 10
wp_y = 1
direction = 0 # 0 == east, 90 == north, 180 == west, 270 == south

for dir in directions:
    inst = dir[0]
    arg = int(dir[1:])
    if inst == 'N':
        wp_y += arg
    elif inst == 'S':
        wp_y -= arg
    elif inst == 'E':
        wp_x += arg
    elif inst == 'W':
        wp_x -= arg
    elif inst == 'L':
        for _ in range(arg//90):
            wp_x, wp_y = -wp_y, wp_x
    elif inst == 'R':
        for _ in range(arg // 90):
            wp_x, wp_y = wp_y, -wp_x
    elif inst == 'F':
        ship_x += arg * wp_x
        ship_y += arg * wp_y
    else:
        print("UNKNOWN INSTRUCTION", dir)

print((ship_x, ship_y), abs(ship_x)+abs(ship_y))
