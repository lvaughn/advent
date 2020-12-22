#!/usr/bin/env python3

def is_nice(s):
    skip_letter = False
    for i in range(len(s) - 2):
        if s[i] == s[i+2]:
            skip_letter = True
            break
    if not skip_letter:
        return False

    for i in range(len(s)-4):
        if s[i:i+2] in s[i+2:]:
            return True
    return False

n_nice = 0
with open('input.txt', 'r') as f:
    for line in f:
        if is_nice(line):
            n_nice += 1

print(n_nice)
