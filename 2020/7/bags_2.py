#!/usr/bin/env python3

from collections import defaultdict, namedtuple
import re

BagReq = namedtuple('BagReq', ['name', 'number'])
contains = defaultdict(list)

# TODO: make lex/yacc version
LINE_RE = re.compile(r'(\w+\s+\w+) bags? contain (.*)')
BAG_SPEC_RE = re.compile(r'\s*(\d+)\s+((\w+\s+\w+)) bags?')


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
        contains[outer_bag_name].append(BagReq(bag_match[2], int(bag_match[1])))


with open('input.txt') as infile:
    for line in infile:
        process_line(line)


def find_all_contains(bag_type):
    if bag_type not in contains:
        return 0
    answer = 0
    for inner_bag in contains[bag_type]:
        # all of the bags it contains, plus the bags themselves
        answer += inner_bag.number * (find_all_contains(inner_bag.name) + 1)
    return answer


print(find_all_contains('shiny gold'))
