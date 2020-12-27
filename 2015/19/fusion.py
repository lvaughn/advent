#!/usr/bin/env python3

from collections import defaultdict

substitions = defaultdict(list)
starting_str = ''
with open('input.txt', 'r') as f:
    for line in f:
        idx = line.find('=>')
        if idx > 0:
            start = line[:idx].strip()
            end = line[idx+2:].strip()
            substitions[start].append(end)
        else:
            striped = line.strip()
            if striped != '':
                starting_str = striped

results = set()
for i in range(len(starting_str)):
    if starting_str[i] in substitions:
        for s in substitions[starting_str[i]]:
            result = starting_str[:i] + s + starting_str[i+1:]
            results.add(result)
    if i < len(starting_str) - 1:
        if starting_str[i:i+2] in substitions:
            for s in substitions[starting_str[i:i+2]]:
                result = starting_str[:i] + s + starting_str[i + 2:]
                results.add(result)
print(len(results))
