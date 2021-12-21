#!/usr/bin/env python3

import sys


def add(a, b):
    return ['['] + a + [','] + b + [']']

def reduce(num):
    changed = True
    while changed:
        changed, num = do_explode(num)
        if not changed:
            changed, num = do_split(num)
    return num

def do_explode(num):
    # returns (changed, value)
    depth = 0
    loc = 0
    for loc in range(len(num)):
        if num[loc] == '[':
            depth += 1
            if depth > 4:
                # Boom
                left_part = list(num[:loc])
                left = num[loc + 1]
                right = num[loc + 3]
                right_part = num[loc + 5:]
                # Fix left
                i = len(left_part) - 1
                changed = False
                while i >= 0 and not changed:
                    if type(left_part[i]) is int:
                        left_part[i] += left
                        changed = True
                    i -= 1
                # Fix right
                i = 0
                changed = False
                while i < len(right_part) and not changed:
                    if type(right_part[i]) is int:
                        right_part[i] += right
                        changed = True
                    i += 1

                # return the value
                return True, left_part + [0] + right_part
        elif num[loc] == ']':
            depth -= 1
        loc += 1
    return False, num

def do_split(num):
    for loc in range(len(num)):
        val = num[loc]
        if type(val) is int and val >= 10:
            return True, num[:loc] + ['[', val // 2, ',', val//2 + val % 2, ']'] + num[loc+1:]
    return False, num

def magnitude(num):
    if type(num) != list:
        return num
    return magnitude(num[0]) * 3 + magnitude(num[1]) * 2

def nested_to_array(num):
    if type(num) == list:
        return ['['] + nested_to_array(num[0]) + [','] + nested_to_array(num[1]) + [']']
    return [num]

def array_to_nested(ls):
    return eval(''.join(str(a) for a in ls))

numbers = []
with open(sys.argv[1], "r") as infile:
    for line in infile:
        numbers.append(nested_to_array(eval(line)))

total = numbers[0]
for n in numbers[1:]:
    total = reduce(add(total, n))


mag = magnitude(array_to_nested(total))
print(f"Part 1: {mag}")

max_mag = -1
for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        s = magnitude(array_to_nested(reduce(add(numbers[i], numbers[j]))))
        max_mag = max(max_mag, s)

        s = magnitude(array_to_nested(reduce(add(numbers[j], numbers[i]))))
        max_mag = max(max_mag, s)

print(f"Part 2: {max_mag}")

