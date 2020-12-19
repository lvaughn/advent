#!/usr/bin/env python3
rules = {}

def evaluate_rule_string(rules, str):
    if len(rules) == 0:
        return True, [str]
    match, remainders = evaluate_rule(rules[0], str)
    if match:
        matches = []
        for remainder in remainders:
            inner_match, inner_rem = evaluate_rule_string(rules[1:], remainder)
            if inner_match:
                matches.extend(inner_rem)
        if len(matches) > 0:
            return True, matches
    return False, []


def evaluate_rule(n, str):
    # print("Evaluating rule {} for '{}' ({})".format(n, str, rules[n]))
    rule_str = rules[n]
    if rule_str.startswith('"'):
        if len(str) == 0 or str[0] != rule_str[1]:
            return False, []
        else:
            return True, [str[1:]]
    elif '|' in rule_str:
        idx = rule_str.index('|')
        remainders = []
        _, r = evaluate_rule_string(rule_str[:idx].strip().split(" "), str)
        remainders.extend(r)
        _, r = evaluate_rule_string(rule_str[idx + 1:].strip().split(" "), str)
        remainders.extend(r)
        if len(remainders) > 0:
            return True, remainders
        return False, []
    else:
        return evaluate_rule_string(rule_str.strip().split(" "), str)


with open('input_a.txt', 'r') as infile:
    l = infile.readline().strip()
    while l != "":
        if l.startswith('#'):
            continue
        idx = l.index(':')
        rules[l[:idx]] = l[idx + 1:].strip()
        l = infile.readline().strip()

    matches = 0
    for l in infile:
        l = l.strip()
        passed, remainders = evaluate_rule('0', l)
        if passed and '' in remainders:
            matches += 1
    print(matches)
