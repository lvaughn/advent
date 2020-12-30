#!/usr/bin/env python3

target_row = 3010
target_col = 3019

row = 1
col = 1
value = 20151125
while (row != target_row) or (col != target_col):
    row -= 1
    if row == 0:
        row = col + 1
        col = 1
    else:
        col += 1
    value = (value * 252533) % 33554393

print(row, col, value)