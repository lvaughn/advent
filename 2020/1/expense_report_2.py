#!/usr/bin/env python3

numbers = []
with open('input', 'r') as infile:
    for line in infile:
        numbers.append(int(line))

for i in range(len(numbers) - 2):
    a = numbers[i]
    seen = set()
    missing = 2020 - a
    for b in numbers[i+1:]:
        c = missing - b
        if c > 0 and c in seen:
            print(a*b*c)
            exit()
        seen.add(b)


print("None Found")