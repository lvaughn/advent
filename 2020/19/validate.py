#!/usr/bin/env python3

import re

rules = {}
cache = {}

def get_rule(n):
    if n in cache:
        return cache[n]
    rule_str = rules[n]
    if rule_str.startswith('"'):
        answer = rule_str[1]
    elif '|' in rule_str:
        idx = rule_str.index('|')
        first = "".join([get_rule(r) for r in rule_str[:idx].strip().split(" ")])
        second = "".join([get_rule(r) for r in rule_str[idx+1:].strip().split(" ")])
        answer = '({}|{})'.format(first, second)
    else:
        answer = ''.join([get_rule(r) for r in rule_str.split(" ")])
    cache[n] = answer
    return answer


with open('input_3.txt', 'r') as infile:
    l = infile.readline().strip()
    while l != "":
        idx = l.index(':')
        rules[l[:idx]] = l[idx+1:].strip()
        l = infile.readline().strip()

    re_str = '^{}$'.format(get_rule("0"))
    print(re_str)
    rule_re = re.compile(re_str)
    matches = 0
    for l in infile:
        if rule_re.match(l.strip()) is not None:
            matches += 1
    print(matches)