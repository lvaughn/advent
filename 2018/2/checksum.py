#!/usr/bin/env python3

from collections import Counter

twos = 0
threes = 0

ids = []
with open('input.txt', 'r') as f:
    for id in f:
        id = id.strip()
        ids.append(id)
        c = Counter(id)
        if 2 in c.values():
            twos += 1
        if 3 in c.values():
            threes += 1

print("Part 1:", twos * threes)

for i in range(len(ids)):
    done = False
    for j in range(i+1, len(ids)):
        n_different = len([a for a in zip(ids[i], ids[j]) if a[0] != a[1]])
        if n_different == 1:
            print("Part 2:", ''.join(a[0] for a in zip(ids[i], ids[j]) if a[0] == a[1]))
            done = True
            break
    if done:
        break
