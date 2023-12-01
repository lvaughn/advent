#!/usr/bin/env python3
import sys
from string import digits

numbers = {'one': '1', 
           'two': '2', 
           'three': '3', 
           'four': '4', 
           'five': '5', 
           'six': '6', 
           'seven': '7', 
           'eight': '8', 
           'nine': '9', 
           'zero': '0'}
def get_number(s):
    first = None
    for loc in range(len(s)):
        if s[loc] in digits:
            if first is None:
                first = s[loc]
            last = s[loc]
        else:
            for word, num in numbers.items():
                if s[loc:].startswith(word):
                    if first is None:
                        first = num
                    last = num
                    break
    return int(f"{first}{last}")

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
answer = sum(get_number(l) for l in lines)

print("Part 2", answer)
