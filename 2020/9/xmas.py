#!/usr/bin/env python3

def sum_exists(ls, target):
    seen = set()
    for n in ls:
        if target - n in seen:
            return True
        seen.add(n)
    return False


with open('input.txt', 'r') as infile:
    numbers = [int(n) for n in infile]

for i in range(25, len(numbers)):
    if not sum_exists(numbers[i - 25:i], numbers[i]):
        print(numbers[i])
        exit()
print("Not Found")