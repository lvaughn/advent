#!/usr/bin/env python3

naughty_substrings = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']
def is_nice(s):
    for ss in naughty_substrings:
        if ss in s:
            return False

    # Check the vowels
    n_vowels = 0
    for vowel in vowels:
        n_vowels += s.count(vowel)
        if n_vowels >= 3:
            break
    if n_vowels < 3:
        return False

    # Check for double letters
    last = s[0]
    for ch in s[1:]:
        if ch == last:
            return True
        last = ch
    # No double letters
    return False

n_nice = 0
with open('input.txt', 'r') as f:
    for line in f:
        if is_nice(line):
            n_nice += 1

print(n_nice)
