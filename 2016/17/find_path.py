#!/usr/bin/env python3

from hashlib import md5
from collections import deque

passcode = 'ioramepc'
may_pass = set('bcdef')


def getDirections(path):
    to_hash = passcode + path
    hash = md5(to_hash.encode('ascii')).hexdigest()
    directions = []
    if hash[0] in may_pass:
        directions.append('U')
    if hash[1] in may_pass:
        directions.append('D')
    if hash[2] in may_pass:
        directions.append('L')
    if hash[3] in may_pass:
        directions.append('R')
    return directions


queue = deque([(0, 0, '')])
while len(queue) > 0:
    (x, y, path) = queue.popleft()
    if x == 3 and y == 3:
        print("Success!!", path)
        break
    for d in getDirections(path):
        if d == 'U' and y > 0:
            queue.append((x, y - 1, path + d))
        elif d == 'D' and y < 3:
            queue.append((x, y + 1, path + d))
        elif d == 'L' and x > 0:
            queue.append((x - 1, y, path + d))
        elif d == 'R' and x < 3:
            queue.append((x + 1, y, path + d))
