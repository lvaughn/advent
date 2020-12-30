#!/usr/bin/env python3

pad = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
row = 1
col = 1

combo = []
with open('input.txt', 'r') as f:
    for line in f:
        for c in line.strip():
            if c == 'U':
                row = max(0, row - 1)
            elif c == 'D':
                row = min(2, row + 1)
            elif c == 'L':
                col = max(0, col - 1)
            elif c == 'R':
                col = min(2, col + 1)
        combo.append(pad[row][col])

print(''.join(str(x) for x in combo))
