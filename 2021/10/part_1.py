#!/usr/bin/env python3

import numpy as np
import re

POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

OPENINGS = {'(', '[', '{', '<'}
CLOSINGS = {')', ']', '}', '>'}
MAPPING = {'(': ')', '[': ']', '{': '}', '<': '>'}

COMPLETE_POINTS = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}


def find_bad_character(s):
    stack = []
    for ch in s:
        if ch in OPENINGS:
            stack.append(ch)
        else:
            assert (ch in CLOSINGS)
            if len(stack) == 0 or MAPPING[stack[-1]] != ch:
                return ch
            stack.pop()
    return stack


def find_score(s):
    result = 0
    for ch in reversed(s):
        result *= 5
        result += COMPLETE_POINTS[ch]
    return result


with open("input.txt", "r") as infile:
    lines = [line.strip() for line in infile]

incomplete = []
total = 0
for line in lines:
    c = find_bad_character(line)
    if type(c) != list:
        total += POINTS[c]
    else:
        incomplete.append(c)

print(f"Part 1: {total}")

scores = [find_score(s) for s in incomplete]
scores.sort()
print(f"Part 2: {scores[len(scores) // 2]}")
