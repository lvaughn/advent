#!/usr/bin/env python3

traps = set(['^^.', '.^^', '^..', '..^'])

with open('input.txt', 'r') as f:
    first_row = f.readline().strip()

rows = [first_row]

while len(rows) < 400000:
    row = rows[-1]
    new_row = []
    for i in range(len(row)):
        if i == 0:
            if '.' + row[:2] in traps:
                new_row.append("^")
            else:
                new_row.append('.')
        elif i == len(row) - 1:
            if row[-2:] + '.' in traps:
                new_row.append("^")
            else:
                new_row.append('.')
        else:
            if row[i-1:i+2] in traps:
                new_row.append('^')
            else:
                new_row.append('.')
    rows.append(''.join(new_row))

n_safe = sum(r.count('.') for r in rows)
print("Number of safe tiles", n_safe)

