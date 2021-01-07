#!/usr/bin/env python3

import re
from collections import namedtuple
import numpy as np

Node = namedtuple('Node', ['name', 'x', 'y', 'size', 'used', 'avail'])

nodes = []
node_lookup = {}
max_x = -1
max_y = -1
empty = None
with open('input.txt', 'r') as f:
    f.readline() # Shell command
    f.readline() # Headers
    line_re = re.compile(r'([a-z0-9/-]+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+')
    name_re = re.compile(r'[^-]+-x(\d+)-y(\d+)')
    for line in f:
        m = line_re.match(line)
        name_m = name_re.match(m[1])
        x = int(name_m[1])
        y = int(name_m[2])
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        node = Node(m[1], x, y, int(m[2]), int(m[3]), int(m[4]))
        node_lookup[(x, y)] = node
        if node.used == 0:
            empty = node

print("Grid: {}*{}={} ({})".format(max_x+1, max_y+1, (max_x+1)*(max_y+1), len(node_lookup)))
print("Target is", node_lookup[(0, max_y)])
print("Empty", empty)

needed = node_lookup[(0, max_y)].used

def swap(x1, y1, x2, y2):
    global board, moves
    tmp = board[x1, y1]
    board[x1, y1] = board[x2, y2]
    board[x2, y2] = tmp
    moves += 1

board = np.zeros((max_x+1, max_y+1), dtype=int)
for x in range(max_x+1):
    for y in range(max_y+1):
        node = node_lookup[x, y]
        print(empty.avail, node.used, x, y)
        if x == 0 and y == 0:
            board[0, 0] = 1
        elif x == max_x and y == 0:
            board[x, y] = 2
        elif node.used == 0:
            board[x, y] = 4
        elif node.used > empty.avail:
            board[x, y] = 3
        else:
            pass
chars = ['.', 'O', 'G', '#', '_']
# for x in range(max_x + 1):
#     line = ''
#     for y in range(max_y + 1):
#         line += chars[board[x,y]]
#     print(line)

loc = [empty.x, empty.y]
moves = 0
# Not proud of this, but sometimes visual inspection is the way to go
while loc[0] != 1: # Up
    swap(loc[0], loc[1], loc[0] - 1, loc[1])
    loc = [loc[0]-1, loc[1]]

while loc[1] > 0: # Over
    swap(loc[0], loc[1], loc[0], loc[1]-1)
    loc = [loc[0], loc[1]-1]

while loc[0] < max_x - 1: # Down
    swap(loc[0], loc[1], loc[0] + 1, loc[1])
    loc = [loc[0]+1, loc[1]]

while loc[0] != 0: # Shimmy to the top
    x, y = loc
    swap(x, y, x+1, y)
    swap (x+1, y, x+1, y+1)
    swap(x+1, y+1, x, y+1)
    swap(x, y+1, x-1, y+1)
    swap(x-1, y+1, x-1, y)
    loc = [x-1, y]
#
# print("After {} moves".format(moves))
# for x in range(max_x + 1):
#     line = ''
#     for y in range(max_y + 1):
#         line += chars[board[x,y]]
#     print(line)
print("Moves:", moves+1)
