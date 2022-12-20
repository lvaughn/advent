#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase
#from collections import Counter, defaultdict, deque, namedtuple
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
#import numpy as np
#import re
#import pprint
import sys


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

def print_list(hd):
    cur = hd.next
    values = [hd.value]
    while cur != hd:
        values.append(cur.value)
        cur = cur.next
    print(values)

def count_list(hd):
    result = 1
    cur = hd.next
    while cur != hd:
        cur = cur.next
        result += 1
    return result

def find_node(node, n):
    while node.value != n:
        node = node.next
    return node


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f"Node:{self.value}:{self.next.value}:{self.prev.value}"

with open(sys.argv[1], 'r') as infile:
    numbers = [int(l) for l in infile]


head = cur = Node(numbers[0]*811589153)
shortcuts = {numbers[0]: head}
nodes = [head]
for n in numbers[1:]:
    new_node = Node(n*811589153)
    shortcuts[n] = new_node
    cur.next = new_node
    new_node.prev = cur
    cur = new_node
    nodes.append(new_node)
cur.next = head
head.prev = cur

list_len = len(nodes)
for _ in range(10):
    # print_list(head)
    for node in nodes:
        # print(num)
        # print_list(shortcuts[num])
        if node.value == 0:
            continue
        # if node == head:
        #     head = head.next
        num = node.value
        if num < 0:  # move left
            nxt = node.next
            prev = node.prev
            prev.next = nxt
            nxt.prev = prev
            to_move = (num % (list_len-1)) - (list_len-1)
            # print(num, list_len, (num % list_len), to_move)
            # to_move = num
            for _ in range(-to_move):
                prev = prev.prev
            nxt = prev.next
            node.prev = prev
            node.next = nxt
            nxt.prev = node
            prev.next = node
        else:
            assert num > 0
            nxt = node.next
            prev = node.prev
            prev.next = nxt
            nxt.prev = prev
            to_move = (num % (list_len-1))
            # print(num, to_move, num - list_len* (num // list_len))
            # to_move = num
            for _ in range(to_move):
                nxt = nxt.next
            # Insert before
            prev = nxt.prev
            node.prev = prev
            node.next = nxt
            nxt.prev = node
            prev.next = node
    # print_list(shortcuts[0])

curr = shortcuts[0]
# print_list(curr)
for _ in range(1000):
    curr = curr.next
first = curr.value

for _ in range(1000):
    curr = curr.next
second = curr.value

for _ in range(1000):
    curr = curr.next
third = curr.value


# print(count_list(shortcuts[0]))
# print(first, second, third)
print("Part 2", first + second+ third)
# -20863 fail, -15009 fail, 1589 fail
