#!/usr/bin/env python

RANGE_START = 172851
RANGE_END = 675869

n_found = 0
for password in xrange(RANGE_START, RANGE_END+1):
    digits = [int(a) for a in str(password)]
    found_double = False
    decrease = False
    for i in xrange(len(digits)-1):
        if digits[i] == digits[i+1]:
            found_double = True
        if digits[i] > digits[i+1]:
            decrease = True
    if found_double and not decrease:
        #print(digits)
        n_found += 1

print n_found
