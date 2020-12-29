#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    values = [int(a) for a in f]

total = sum(values)
target = total // 4

def find_subsets(target, position):
    if target == 0:
        yield []
    else:
        if position < len(values):
            for ls in find_subsets(target, position + 1):
                yield ls
            if values[position] <= target:
                for ls in find_subsets(target - values[position], position + 1):
                    yield [values[position]] + ls


best_length = len(values)
best_qe = 100000000000000
for subset in find_subsets(target, 0):
    if len(subset) <= best_length:
        qe = 1
        for s in subset:
            qe *= s
        if len(subset) < best_length:
            best_length = len(subset)
            best_qe = qe
            print(subset)
        else: # same length
            if qe < best_qe:
                best_qe = qe
                print(subset)

print(best_length, best_qe)