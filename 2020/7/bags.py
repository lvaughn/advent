#!/usr/bin/env python3

from collections import defaultdict
import re

contained_by = defaultdict(list)

# TODO: make lex/yacc version
LINE_RE = re.compile(r'(\w+\s+\w+) bags? contain (.*)')
BAG_SPEC_RE = re.compile(r'\s*\d+\s+((\w+\s+\w+)) bags?')


def process_line(l):
    outer_bag_match = LINE_RE.match(l)
    assert outer_bag_match
    outer_bag_name = outer_bag_match[1]
    inner_bags = outer_bag_match[2]
    if inner_bags == "no other bags.":
        return
    for inner_bag in inner_bags.split(','):
        bag_match = BAG_SPEC_RE.match(inner_bag)
        assert bag_match
        contained_by[bag_match[1]].append(outer_bag_name)


with open('input.txt') as infile:
    for line in infile:
        process_line(line)


def find_all_contains(bag_type, seen):
    for b in contained_by[bag_type]:
        if b not in seen:
            seen.add(b)
            find_all_contains(b, seen)
    return seen


print(len(find_all_contains('shiny gold', set())))
