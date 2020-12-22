#!/usr/bin/env python3

visited = set()
visited.add((0,0))

x, y = 0,0
with open('input.txt', 'r') as f:
    for line in f:
        for ch in line:
            if ch == '^':
                x += 1
            elif ch == 'v':
                x -= 1
            elif ch == '<':
                y -= 1
            elif ch == '>':
                y += 1
            visited.add((x, y))

print("Total houses", len(visited))
