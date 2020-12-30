#!/usr/bin/env python3

def has_abba(s):
    for i in range(len(s)-3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
            return True
    return False

def valid_address(s):
    abba = False
    while s != '':
        if s[0] == '[':
            idx = s.index(']')
            if has_abba(s[1:idx]):
                return False
            s = s[idx+1:]
        else:
            idx = s.find('[')
            if idx < 0:
                if has_abba(s):
                    abba = True
                s = ''
            else :
                if has_abba(s[:idx]):
                    abba = True
                s = s[idx:]
    return abba


n_good = 0
with open('input.txt', 'r') as f:
    for line in f:
        if valid_address(line.strip()):
            n_good += 1

print(n_good)