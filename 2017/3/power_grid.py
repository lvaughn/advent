#!/usr/bin/env python3

def find_distance(n):
    x, y = 0, 0
    val = 1
    dir = 'e'
    toMove = 1
    while val <= n:
        if dir == 'e':
            if val + toMove >= n:
                x += n - val
                return abs(x) + abs(y)
            x += toMove
            val += toMove
            dir = 'n'
        elif dir == 'n':
            if val + toMove >= n:
                y += n - val
                return abs(x) + abs(y)
            y += toMove
            dir = 'w'
            val += toMove
            toMove += 1
        elif dir == 'w':
            if val + toMove >= n:
                x -= n - val
                return abs(x) + abs(y)
            x -= toMove
            dir = 's'
            val += toMove
        elif dir == 's':
            if val + toMove >= n:
                y -= n - val
                return abs(x) + abs(y)
            y -= toMove
            dir = 'e'
            val += toMove
            toMove += 1



print(find_distance(361527))