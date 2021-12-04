#!/usr/bin/env python3

import numpy as np


class Board:
    def __init__(self, numbers):
        self.numbers = np.array(numbers, dtype=int)

    def __repr__(self):
        return str(self.numbers)

    def is_winner(self, numbers_called):
        for row in range(5):
            if all(n in numbers_called for n in self.numbers[row, :]):
                return True
        for col in range(5):
            if all(n in numbers_called for n in self.numbers[:, col]):
                return True
        return False

    def unmarked_sum(self, numbers_called):
        return sum(n for n in self.numbers.flatten() if n not in numbers_called)


with open("input.txt", "r") as infile:
    lines = [l for l in infile]
    numbers_called = [int(n) for n in lines[0].split(',')]

    boards = []
    for start_line in range(2, len(lines), 6):
        rows = []
        for row in range(5):
            rows.append(lines[start_line + row].split())
        boards.append(Board(rows))

called = set()
is_won = False
for number in numbers_called:
    called.add(number)
    for board in boards:
        if board.is_winner(called):
            print("Got a winner")
            print(board)
            print(board.unmarked_sum(called) * number)
            is_won = True
            break
    if is_won:
        break

# Part 2
print("Part 2")
called = set()
for number in numbers_called:
    called.add(number)
    if len(boards) == 1 and boards[0].is_winner(called):
        print("Got a loser")
        print(boards[0])
        print(boards[0].unmarked_sum(called) * number)
        break
    boards = [b for b in boards if not b.is_winner(called)]


