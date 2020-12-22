#!/usr/bin/env python3

visited = set()
visited.add((0, 0))

turn = 0  # Santa = 0, Robo-Santa = 1
locations = [[0, 0], [0, 0]]
with open('input.txt', 'r') as f:
    for line in f:
         for ch in line:
            pos = locations[turn]
            turn = (turn + 1) % 2
            if ch == '^':
                pos[0] += 1
            elif ch == 'v':
                pos[0] -= 1
            elif ch == '<':
                pos[1] -= 1
            elif ch == '>':
                pos[1] += 1
            visited.add(tuple(pos))

print("Total houses", len(visited))
