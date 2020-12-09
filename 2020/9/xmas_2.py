#!/usr/bin/env python3

INPUT_FILE = 'input.txt'
WINDOW = 25


def sum_exists(ls, target):
    seen = set()
    for n in ls:
        if target - n in seen:
            return True
        seen.add(n)
    return False


with open(INPUT_FILE, 'r') as infile:
    numbers = [int(n) for n in infile]

for i in range(WINDOW, len(numbers)):
    if not sum_exists(numbers[i - WINDOW:i], numbers[i]):
        weak_point = numbers[i]
        break

i = 0
j = 1
s = numbers[0] + numbers[1]
while True:
    if s == weak_point:
        rng = numbers[i:j + 1]
        print(max(rng) + min(rng))
        exit()
    elif s < weak_point:
        j += 1
        s += numbers[j]
    else:  # s > weak_point
        s -= numbers[i]
        i += 1
