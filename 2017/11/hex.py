#!/usr/bin/env python3

from collections import deque

with open('input.txt', 'r') as f:
    moves = f.readline().strip()


distances = {(0, 0): 0}
seen = {(0, 0)}
queue = deque([(0, 0, 0)])

def test(row, col, n_moves):
    if (row, col) not in distances:
        distances[(row, col)] = n_moves
        queue.append((row, col, n_moves))

while len(queue) != 0:
    row, col, n_moves = queue.popleft()
    if n_moves > 1600:
        break
    # Add all 6 neighbors
    test(row+1, col, n_moves+1)
    test(row-1, col, n_moves+1)
    if col % 2 == 0:
        test(row, col+1, n_moves+1)
        test(row-1, col+1, n_moves+1)
        test(row-1, col-1, n_moves+1)
        test(row, col-1, n_moves+1)
    else:
        test(row+1, col+1, n_moves+1)
        test(row, col + 1, n_moves + 1)
        test(row, col - 1, n_moves + 1)
        test(row + 1, col - 1, n_moves + 1)

max_distance = -1
row = 0
col = 0
for move in moves.split(','):
    max_distance = max(max_distance, distances[(row, col)])
    if move == 'n':
        row += 1
    elif move == 's':
        row -= 1
    elif move == 'ne':
        if col % 2 == 1:
            row += 1
        col += 1
    elif move == 'se':
        if col % 2 == 0:
            row -=1
        col += 1
    elif move == 'sw':
        if col % 2 == 0:
            row -=1
        col -=1
    elif move == 'nw':
        if col % 2 == 1:
            row += 1
        col -= 1
    else:
        print("Unknown move", move)

print(row, col)
print("dist:", distances[(row, col)])
print("Max:", max_distance)

