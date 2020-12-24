#!/usr/bin/env python3

import numpy as np


def getNewCoords(move, x, y):
    if move == 'e':
        return x + 1, y
    if move == 'w':
        return x - 1, y
    if move == 'ne':
        if y % 2 == 0:
            return x, y + 1
        else:
            return x + 1, y + 1
    if move == 'nw':
        if y % 2 == 0:
            return x - 1, y + 1
        else:
            return x, y + 1
    if move == 'se':
        if y % 2 ==0:
            return x, y - 1
        else:
            return x+1, y-1
    if move == 'sw':
        if y % 2 == 0:
            return x-1, y-1
        else:
            return x, y-1
    assert(False)


def nBlackNeighbors(board, x, y):
    if y % 2 == 0:
        offsets = [(-1, 0), (1, 0), (-1, 1), (0, 1), (-1, -1), (0, -1)]
    else:
        offsets = [(-1, 0), (1, 0), (1, 1), (0, 1), (1, -1), (0, -1)]
    answer = 0
    for x_off, y_off in offsets:
        if board[x+x_off, y+y_off]:
            answer += 1
    return answer

def print_floor(floor):
    for y in range(floor.shape[1]):
        l = ''
        for x in range(floor.shape[0]):
            if floor[x,y]:
                l += '#'
            else:
                l += '.'
        print(l)

SIZE = 160
floor = np.zeros((SIZE, SIZE), dtype=bool) # White = False, Black = True
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        x, y = SIZE//2, SIZE//2
        while line != '':
            if line.startswith('e') or line.startswith('w'):
                x, y = getNewCoords(line[0], x, y)
                line = line[1:]
            else:
                x, y = getNewCoords(line[0:2], x, y)
                line = line[2:]
        floor[x, y] = not floor[x,y]
print("Starting black", np.count_nonzero(floor))

for i in range(100):
    #print_floor(floor)
    new_floor = np.zeros(floor.shape, dtype=bool)
    for x in range(1, SIZE-1):
        for y in range(1, SIZE-1):
            if floor[x,y]: # Black
                if 1 <= nBlackNeighbors(floor, x, y) <= 2: # It stays black
                    new_floor[x,y] = True
            else: # white
                if nBlackNeighbors(floor, x, y) == 2:
                    new_floor[x,y] = True
    floor = new_floor
    print(i+1, np.count_nonzero(floor))

