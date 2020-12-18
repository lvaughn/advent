#!/usr/bin/env python3
import numpy as np


def run_round(seats):
    new_seats = np.zeros(seats.shape, dtype=int)
    for row in range(seats.shape[0]):
        for col in range(seats.shape[1]):
            # Zeros stay the same
            if seats[row, col] != 0:
                n_occupied = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        if 0 <= row + i < seats.shape[0] and \
                                0 <= col + j < seats.shape[1] and \
                                seats[row + i, col + j] == 2:
                            n_occupied += 1
                if seats[row, col] == 1:
                    if n_occupied == 0:
                        new_seats[row, col] = 2
                    else:
                        new_seats[row, col] = 1
                elif seats[row, col] == 2:
                    if n_occupied >= 4:
                        new_seats[row, col] = 1
                    else:
                        new_seats[row, col] = 2
    return new_seats


with open('input.txt') as infile:
    seats = [a.strip() for a in infile]

# 0 == No seat
# 1 == Empty Seat
# 2 == Occupied Seat

base_seats = np.zeros((len(seats[0]), len(seats)), dtype=int)
for row in range(len(seats)):
    for col, ch in enumerate(seats[row]):
        if ch == 'L':
            base_seats[row, col] = 1
        elif ch == '#':
            base_seats[row, col] = 2

new_seats = run_round(base_seats)

while not np.array_equal(new_seats, base_seats):
    base_seats = new_seats
    new_seats = run_round(base_seats)

print(np.count_nonzero(new_seats == 2))
