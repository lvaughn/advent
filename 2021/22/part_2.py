#!/usr/bin/env python3

import numpy as np
import re

def line_intersection(a, b):
    if a[0] > b[1] or b[0] > a[1]:
        return None
    if a[0] <= b[0] and a[1] >= b[1]: # A contains B
        return b
    if b[0] <= a[0] and b[1] >= a[1]: # b contains a
        return a
    if a[0] <= b[0]:
        return b[0], a[1]
    if b[0] <= a[0]:
        return a[0], b[1]
    assert False

def remove_block(orig, remove):
    intersection = get_intersection(orig, remove)
    if intersection is None:
        return [orig]

    blocks = []
    xo, yo, zo = orig
    xi, yi, zi = intersection

    # Remove the left and right (x-axis)
    if xo[1] > xi[1]:
        blk = ((xi[1] + 1, xo[1]), yo, zo)
        blocks.append(blk)

    if xo[0] < xi[0]:
        x = xo[0], xi[0] - 1
        blocks.append((x, yo, zo))

    # front and back (y-axis)
    if yo[1] > yi[1]:
        blocks.append((xi, (yi[1]+1, yo[1]), zo))
    if yo[0] < yi[0]:
        blocks.append((xi, (yo[0], yi[0]-1), zo))

    # The top and bottom (z-axis)
    if zo[1] > zi[1]:
        blocks.append((xi, yi, (zi[1]+1, zo[1])))
    if zo[0] < zi[0]:
        blocks.append((xi, yi, (zo[0], zi[0]-1)))
    return blocks

def get_intersection(a, b):
    ax, ay, az = a
    bx, by, bz = b

    rx = line_intersection(ax, bx)
    if rx is None:
        return None
    ry = line_intersection(ay, by)
    if ry is None:
        return None
    rz = line_intersection(az, bz)
    if rz is None:
        return None
    return (rx, ry, rz)

line_re = re.compile(r'(\S+)\s(.*)')
var_re = re.compile(r'=(-?\d+)..(-?\d+)')

def parse_var(s):
    m = var_re.search(s)
    val = (int(m[1]), int(m[2]))
    assert val[0] <= val[1]
    return val

commands = []
with open("input.txt", "r") as infile:
    for line in infile:
        m = line_re.match(line)
        cmd = m[1]
        x, y, z = m[2].split(',')
        command = (cmd, parse_var(x), parse_var(y), parse_var(z))
        commands.append(command)

blocks = []
for state, x, y, z in commands:
    new_block = (x, y, z)
    new_blocks = []
    for block in blocks:
        new_blocks.extend(remove_block(block, new_block))
    if state == 'on':
        new_blocks.append(new_block)
    blocks = new_blocks

print(len(blocks))
lights_on = 0
for block in blocks:
    x, y, z = block
    lights_on += (x[1]-x[0]+1) * (y[1]-y[0]+1) * (z[1]-z[0]+1)

print("Part 2", lights_on)

