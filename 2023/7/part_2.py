#!/usr/bin/env python3
from collections import Counter
import sys
from functools import cmp_to_key

ranks = {c: i for i, c in enumerate(reversed("AKQT98765432J"))}

def is_5_of_a_kind(cards):
    return cards.most_common(1)[0][1] == 5

def is_4_of_a_kind(cards):
    return cards.most_common(1)[0][1] == 4

def is_full_house(cards):
    common = cards.most_common(5)
    return common[0][1] == 3 and common[1][1] == 2

def is_3_of_a_kind(cards):
    common = cards.most_common(5)
    return len(common) == 3 and common[0][1] == 3

def is_2_pairs(cards):
    common = cards.most_common(5)
    return len(common) == 3 and common[0][1] == 2 and common[1][1] == 2

def is_pair(cards):
    common = cards.most_common(5)
    return len(common) == 4 and common[0][1] == 2

def is_greater(a, b):
    for x, y in zip(a, b):
        if ranks[x] > ranks[y]:
            return True
        elif ranks[x] < ranks[y]:
            return False
    assert False
    
def get_best_combo(hand):
    if 'J' not in hand:
        return Counter(hand)
    
    no_js = hand.replace('J', '')
    if len(no_js) == 0:
        return Counter('AAAAA')
    cnt = Counter(no_js)
    common = cnt.most_common(5)
    return Counter(no_js + (common[0][0] * (5 - len(no_js))))
        
    
    
def hand_compare(a_hand, b_hand):
    assert a_hand != b_hand
    a = get_best_combo(a_hand)
    b = get_best_combo(b_hand)
    
    if is_5_of_a_kind(a):
        if is_5_of_a_kind(b):
            if is_greater(a_hand, b_hand): 
                return 1
            else: 
                return -1
        else:
            return 1
    if is_5_of_a_kind(b):
        return -1
        
    if is_4_of_a_kind(a):
        if is_4_of_a_kind(b):
            if is_greater(a_hand, b_hand):
                return 1
            else:
                return -1
        else:
            return 1
    if is_4_of_a_kind(b):
        return -1
    
    if is_full_house(a):
        if is_full_house(b):
            if is_greater(a_hand, b_hand):
                return 1
            else:
                return -1
        else:
            return 1
    if is_full_house(b):
        return -1
    
    if is_3_of_a_kind(a):
        if is_3_of_a_kind(b):
            if is_greater(a_hand, b_hand):
                return 1
            else:
                return -1
        else:
            return 1
    if is_3_of_a_kind(b):
        return -1
    
    if is_2_pairs(a):
        if is_2_pairs(b):
            if is_greater(a_hand, b_hand):
                return 1
            else:
                return -1
        else:
            return 1
    if is_2_pairs(b):
        return -1
        
    if is_pair(a):
        if is_pair(b):
            if is_greater(a_hand, b_hand):
                return 1
            else:
                return -1
        else:
            return 1
    if is_pair(b):
        return -1
    
    if is_greater(a_hand, b_hand):
        return 1
    return -1
    

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
bids = []
for line in lines:
    hand = line[:5]
    bid = int(line[6:])
    bids.append((hand, bid))
    
def sort_func(a, b):
    return hand_compare(a[0], b[0])

bids.sort(key=cmp_to_key(sort_func))

answer = 0
for i, (hand, bid) in enumerate(bids):
    answer += (i+1) * bid

print("Part 2", answer)
