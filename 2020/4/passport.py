#!/usr/bin/env python3

def validate_passport(s):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] #, 'cid']
    seen = set()
    for field in s.split():
        seen.add(field[:3])
    for f in fields:
        if f not in seen:
            return False
    return True

n_valid = 0
acc = ""
with open('input.txt', 'r') as infile:
    for l in infile:
        l = l.strip()
        if len(l) == 0:
            if validate_passport(acc):
                n_valid += 1
            acc = ""
        else:
            acc = "{} {}".format(acc, l)

# get the last one
if validate_passport(acc):
    n_valid += 1

print(n_valid)