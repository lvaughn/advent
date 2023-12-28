#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase, digits
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

def deal(deck, inc):
    loc = 0
    new_deck = [None] * len(deck)
    
    for c in deck:
        new_deck[loc] = c 
        loc = (loc + inc) % len(deck)
        
    assert None not in new_deck
    return new_deck

def deal_in_stack(deck):
    return list(reversed(deck))

def cut(deck, n):
    if n < 0:
        n += len(deck)
    return deck[n:] + deck[:n]


with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]


deck = list(range(10007))

for line in lines:
    if line.startswith('deal into new stack'):
        deck = deal_in_stack(deck)
    elif line.startswith('deal with increment'):
        deck = deal(deck, int(line[20:]))
    elif line.startswith('cut'):
        deck = cut(deck, int(line[4:]))
    else:
        assert False, f"Bad line: {line}"

print("Part 1", deck.index(2019))
