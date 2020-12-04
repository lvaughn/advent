#!/usr/bin/env python3

from collections import namedtuple
import re

ValidationRule = namedtuple('ValidationRule', ['regex', 'validator'])


def makeYearValidator(low, high):
    def val(s):
        return low <= int(s) <= high

    return val


def validateHeight(s):
    n = int(s[:-2])
    if 'cm' == s[-2:]:
        return 150 <= n <= 193
    return 59 <= n <= 76


YEAR_RE = re.compile(r'^\d{4}$')
FIELDS = {
    'byr': ValidationRule(YEAR_RE, makeYearValidator(1920, 2002)),
    'iyr': ValidationRule(YEAR_RE, makeYearValidator(2010, 2020)),
    'eyr': ValidationRule(YEAR_RE, makeYearValidator(2020, 2030)),
    'hgt': ValidationRule(re.compile(r'^(\d{2,3})(cm|in)$'), validateHeight),
    'hcl': ValidationRule(re.compile(r'^#[a-f0-9]{6}$'), None),
    'ecl': ValidationRule(re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$'), None),
    'pid': ValidationRule(re.compile(r'^\d{9}$'), None)
}


def validate_passport(s):
    record = {}
    for field in s.split():
        record[field[:3]] = field[4:]
    for f, rule in FIELDS.items():
        if f not in record:
            # print("Missed", f)
            return False
        # print("fields[{}]={}".format(f, fields[f]))
        val = record[f]
        # Check the regex
        if not rule.regex.match(val):
            return False
        # If there's a custom validator, run it
        if rule.validator is not None and not rule.validator(val):
            return False
    # print("Passed")
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
