#!/usr/bin/env python3

# west->east increasing x
# south->north increasing y

import sys
from collections import defaultdict, deque


def move(dir, x, y):
    if dir == 'E':
        next_x, next_y = x + 1, y
    elif dir == 'W':
        next_x, next_y = x - 1, y
    elif dir == 'N':
        next_x, next_y = x, y + 1
    elif dir == 'S':
        next_x, next_y = x, y - 1
    else:
        assert False
    rooms[(x, y)].add((next_x, next_y))
    rooms[(next_x, next_y)].add((x, y))
    return next_x, next_y


def debug(depth, str):
    if False:
        print(" " * (2*depth) + str)

visited = set()
def process_regex(s, x, y, depth=0):
    debug(depth, "process_regex:{}:{}:".format((x, y), s))
    key = (x, y, s)
    if key in visited:
        return
    visited.add(key)
    if len(s) == 0:
        yield x, y
    else:
        if s[0] == '(':
            # Scan to other end, recurse on those
            pieces = []
            loc = 1
            level = 1
            piece = ''
            while level > 0:
                if s[loc] == '|':
                    if level == 1:
                        pieces.append(piece)
                        piece = ''
                    else:
                        piece += '|'
                elif s[loc] == '(':
                    level += 1
                    piece += '('
                elif s[loc] == ')':
                    level -= 1
                    if level == 0:
                        pieces.append(piece)
                    else:
                        piece += ')'
                else:
                    piece += s[loc]
                loc += 1
            debug(depth, "Recursing on {}".format(pieces))
            for piece in pieces:
                for new_x, new_y in process_regex(piece, x, y, depth + 1):
                    debug(depth, "From piece '{}'".format(piece))
                    for newer_x, newer_y in process_regex(s[loc:], new_x, new_y, depth + 1):
                        yield newer_x, newer_y
        else:
            # Do moves until we're out of string or until we hit a '('
            loc = 0
            while loc < len(s) and s[loc] != '(':
                x, y = move(s[loc], x, y)
                loc += 1
            if loc == len(s):
                yield x, y
            else:
                for new_x, new_y in process_regex(s[loc:], x, y, depth + 1):
                    yield new_x, new_y


with open(sys.argv[1], 'r') as f:
    directions = f.read()

start_x = 100
start_y = 100

rooms = defaultdict(set)  # map from (x, y) to a list of adjacent rooms from that room
for end_x, end_y in process_regex(directions[1:-2], start_x, start_y):
    pass

distances = {(start_x, start_y): 0}
queue = deque([(start_x, start_y)])
while len(queue) > 0:
    x, y = queue.popleft()
    dist = distances[(x, y)]
    for other_room in rooms[(x, y)]:
        if other_room not in distances:
            distances[other_room] = dist + 1
            queue.append(other_room)

print("Total rooms:", len(distances))
print("Part 1:", max(distances.values()))
print("Part 2:", len([d for d in distances.values() if d >= 1000]))
