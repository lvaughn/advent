#!/usr/bin/env python3

def reduced_length(chain):
    reduced = True
    while reduced:
        reduced = False
        new_chain = ''
        i = 0
        while i < len(chain):
            if i < len(chain) - 1 and chain[i].islower() and chain[i + 1] == chain[i].upper():
                i += 2
                reduced = True
            elif i < len(chain) - 1 and chain[i].isupper() and chain[i + 1] == chain[i].lower():
                i += 2
                reduced = True
            else:
                new_chain += chain[i]
                i += 1
        chain = new_chain
    return len(chain)


with open('input.txt', 'r') as f:
    start = f.read().strip()

letters = set(start.lower())
best_len = len(start) + 1
for l in letters:
    length = reduced_length(start.replace(l, '').replace(l.upper(), ''))
    if length < best_len:
        best_len = length
print("Part 2:", best_len)