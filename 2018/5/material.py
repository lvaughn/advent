#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    chain = f.read().strip()

print("Starts as {} chars".format(len(chain)))

reduced = True
while reduced:
    reduced = False
    new_chain = ''
    i = 0
    while i < len(chain):
        if i < len(chain) - 1 and chain[i].islower() and chain[i+1] == chain[i].upper():
            i += 2
            reduced = True
        elif i < len(chain) - 1 and chain[i].isupper() and chain[i+1] == chain[i].lower():
            i += 2
            reduced = True
        else:
            new_chain += chain[i]
            i += 1
    chain = new_chain

print("Part 1:", len(new_chain))