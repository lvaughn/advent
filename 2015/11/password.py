#!/usr/bin/env python3

from string import ascii_lowercase

start = 'vzbxkghb'
#start = 'abcdefgh'

nextLetters = {}
allowedNextLetter = {}
for i in range(25):
    nextLetters[ascii_lowercase[i]] = ascii_lowercase[i+1]
nextLetters['z'] = 'INVALID'
allowed_next = 'abcdefghjkmnpqrstuvwxyz'
for i in range(23):
    allowedNextLetter[allowed_next[i]] = allowed_next[(i + 1) % 23]

def hasRepeats(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True, s[i+2:]
    return False, ''

def isValid(pw):
    # forbidden letters
    for ch in ['i', 'o', 'l']:
        if ch in pw:
            return False

    # Repeated letters
    rep, rest = hasRepeats(pw)
    if not rep:
        return False
    rep, _ = hasRepeats(rest)
    if not rep:
        return False

    # Look for three in a row
    for i in range(len(pw)-2):
        if pw[i+1] == nextLetters[pw[i]] and pw[i+2] == nextLetters[pw[i+1]]:
            return True
    return False

def increment(pw):
    if pw == '':
        return ''
    if pw[-1] == 'z':
        return increment(pw[:-1]) + 'a'
    return pw[:-1] + allowedNextLetter[pw[-1]]

pw = increment(start)
while not isValid(pw):
    pw = increment(pw)
print(pw)
pw = increment(pw)
while not isValid(pw):
    pw = increment(pw)
print(pw)