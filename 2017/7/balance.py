#!/usr/bin/env python3

import re
from collections import namedtuple, Counter

Node = namedtuple('Node', ['name', 'weight', 'children'])

nodes = {}

def calc_weight(node_name):
    node = nodes[node_name]
    weight = node.weight
    for child in node.children:
        weight += calc_weight(child)
    return weight

def all_equal(numbers):
    for n in numbers[1:]:
        if n != numbers[0]:
            return False
    return True

def find_new_weight(node_name, supposed_to_weigh):
    # see if we're balanced, if so, adjust our weight, if not, recurse on the right child
    node = nodes[node_name]

    if len(node.children) == 0:
        return supposed_to_weigh
    # See if we're balanced
    child_weights = [calc_weight(c) for c in node.children]
    if all_equal(child_weights):
        # This node must be wrong
        return supposed_to_weigh - sum(child_weights)

    # Find out which child is wrong
    child_should_weigh = (supposed_to_weigh - node.weight)//len(node.children)
    for i, child in enumerate(node.children):
        if child_weights[i] != child_should_weigh:
            return find_new_weight(child, child_should_weigh)
    assert False


root = 'gynfwly' # From part 1
with open('input.txt', 'r') as f:
    line_re = re.compile(r'(\w+)\s+\((\d+)\)\s*(->)?(.*)')
    for line in f:
        m = line_re.match(line)
        name = m[1]
        weight = int(m[2])
        if len(m[4].strip()) > 0:
            children = [a.strip() for a in m[4].split(',')]
        else:
            children = []
        nodes[name] = Node(name, weight, children)

print(find_new_weight(root, calc_weight(root)))