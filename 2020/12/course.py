#!/usr/bin/env python3

with open('input.txt') as infile:
    directions = [a.strip() for a in infile]

x = 0
y = 0
direction = 0 # 0 == east, 90 == north, 180 == west, 270 == south

for dir in directions:
    inst = dir[0]
    arg = int(dir[1:])
    if inst == 'N':
        y += arg
    elif inst == 'S':
        y -= arg
    elif inst == 'E':
        x += arg
    elif inst == 'W':
        x -= arg
    elif inst == 'L':
        direction = (direction + arg) % 360
    elif inst == 'R':
        direction = (direction - arg) % 360
    elif inst == 'F':
        if direction == 0:
            x += arg
        elif direction == 90:
            y += arg
        elif direction == 180:
            x -= arg
        elif direction == 270:
            y -= arg
        else:
            print("UNKNOWN DIRECTION", direction)
    else:
        print("UNKNOWN INSTRUCTION", dir)

print((x, y), abs(x)+abs(y))
