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

for i in range(len(numbers) - 1):
    s = numbers[i] + numbers[i + 1]
    j = i + 1
    while s < weak_point and j < len(numbers):
        j += 1
        s += numbers[j]
    if s == weak_point:
        sub_range = numbers[i:j + 1]
        print(max(sub_range) + min(sub_range))
        exit()
