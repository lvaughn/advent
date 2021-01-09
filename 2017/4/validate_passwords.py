#!/usr/bin/env python3

from collections import Counter

with open('input.txt', 'r') as f:
    n_valid = 0
    n_valid_ana = 0
    for line in f:
        words = line.strip().split()
        c = Counter(words)
        if c.most_common(1)[0][1] == 1:
            n_valid += 1
        sorted_words = [''.join(sorted(a for a in w)) for w in words]
        c = Counter(sorted_words)
        if c.most_common(1)[0][1] == 1:
            n_valid_ana += 1


print("part 1", n_valid)
print("part 2", n_valid_ana)

