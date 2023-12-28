#!/usr/bin/env python3

import sys

def deal(deck, inc):
    loc = 0
    new_deck = [None] * len(deck)
    
    for c in deck:
        new_deck[loc] = c 
        loc = (loc + inc) % len(deck)
        
    assert None not in new_deck
    return new_deck
    
def inv_deal(deck_len, n, dest):
    return pow(n, -1, deck_len) * dest % deck_len 

def deal_in_stack(deck):
    return list(reversed(deck))

def inv_deal_in_stack(deck_len, dest):
    return deck_len - dest - 1

def cut(deck, n):
    if n < 0:
        n += len(deck)
    return deck[n:] + deck[:n]

def inv_cut(deck_len, n, dest):
    if n < 0:
        n += deck_len
    if dest >= deck_len - n:
        return dest + n - deck_len
    else:
        return dest + n 


with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
deck_len = 119315717514047
iterations = 101741582076661

ending_pos = 2020
pos_ls = [ending_pos]
pos = ending_pos
while len(pos_ls) < 5:
    for line in reversed(lines):
        if line.startswith('deal into new stack'):
            pos = inv_deal_in_stack(deck_len, pos)
        elif line.startswith('deal with increment'):
            pos = inv_deal(deck_len, int(line[20:]), pos)
        elif line.startswith('cut'):
            pos = inv_cut(deck_len, int(line[4:]), pos)
        else:
            assert False, f"Bad line: {line}"
    pos_ls.append(pos)
    
X = pos_ls[0]
Y = pos_ls[1]
Z = pos_ls[2]
    
A = (Y-Z) * pow(X-Y+deck_len, -1, deck_len) % deck_len
B = (Y-A*X) % deck_len
# print(A, B)

print("Part 2", (pow(A, iterations, deck_len)*X + (pow(A, iterations, deck_len)-1) * pow(A-1, -1, deck_len) * B) % deck_len)


deck = list(range(10007))

# foo = deal_in_stack(deck)

# for i, value in enumerate(foo):
#     assert value == inv_deal_in_stack(len(deck), i)
    
# short_deck = list(range(10))
# foo = cut(short_deck, 3)
# for i, value in enumerate(foo):
#     assert value == inv_cut(len(short_deck), 3, i)
# foo = cut(short_deck, -4)
# for i, value in enumerate(foo):
#     assert value == inv_cut(len(short_deck), -4, i)
    
# for cut_depth in [-100, -5, 5, 1234]:
#     foo = cut(deck, cut_depth)
#     for i, value in enumerate(foo):
#         assert value == inv_cut(len(deck), cut_depth, i), f"Bad inverse i={i} value={value} cut={cut_depth} got {inv_cut(len(deck), cut_depth, i)}"

# foo = deal(short_deck, 3)
# for i, value in enumerate(foo):
#     assert value == inv_deal(10, 3, i)
    
# foo = deal(deck, 59)
# for i, value in enumerate(foo):
#     assert value == inv_deal(len(deck), 59, i)

# for line in lines:
#     if line.startswith('deal into new stack'):
#         deck = deal_in_stack(deck)
#     elif line.startswith('deal with increment'):
#         deck = deal(deck, int(line[20:]))
#     elif line.startswith('cut'):
#         deck = cut(deck, int(line[4:]))
#     else:
#         assert False, f"Bad line: {line}"

