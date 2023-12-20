#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase, digits
from collections import Counter, defaultdict, deque, namedtuple
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
#import numpy as np
import re
#import pprint
import sys
import math 

class Generation:
    def __init__(self, symbol, amount, inputs):
        self.symbol = symbol
        self.amount = amount
        self.inputs = inputs
        

def get_all_derivitives(ing, single_step):
    if ing not in single_step:
        return set()
    result = set(single_step[ing])
    for s in single_step[ing]:
        result = result | get_all_derivitives(s, single_step)
    return result 

def get_next_move(ing_ls, derive_from):
    for ing in ing_ls:
        neg_inclusions = [i not in derive_from[ing] for i in ing_ls]
        if all(neg_inclusions):
            return ing 
    assert len(ing_ls) == 1 and ing_ls[0] == 'ORE'
    return 'ORE'

def merge_lists(a, b):
    result_dict = defaultdict(int)
    for ing, amt in a:
        result_dict[ing] += amt 
    for ing, amt in b:
        result_dict[ing] += amt 
    return [(ing, result_dict[ing]) for ing in result_dict]
        

def find_upstream(ing, quantity, can_derive, to_create):
    if ing == 'ORE':
        return [(ing, quantity)]
    gen = to_create[ing]
    mult = int(math.ceil(quantity/gen.amount))
    ing_list = [(i[0], mult*i[1]) for i in gen.inputs]
    ### DO NOT RECURSE, Just keep going until we there's one thing left 
    while len(ing_list) > 1:
        ing_names = [i[0] for i in ing_list]
        next_move = get_next_move(ing_names, can_derive)
        quantity = [i[1] for i in ing_list if i[0] == next_move][0]
        needed = to_create[next_move]
        mult =  int(math.ceil(quantity/needed.amount))
        new_ing = [(i[0], mult*i[1]) for i in needed.inputs]
        ing_list = merge_lists(new_ing, [x for x in ing_list if x[0] != next_move])
    return ing_list[0]
    

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
yields_one_gen = defaultdict(list)
to_create = {}
input_re = re.compile(r'(\d+)\s+(\w+)')
for line in lines:
    inputs, output = line.split('=>')
    m = input_re.search(output)
    inputs = [(a[1], int(a[0])) for a in input_re.findall(inputs)]
    gen = Generation(m[2], int(m[1]), inputs)
    to_create[gen.symbol] = gen 
    
    for ing, amt in inputs:
        yields_one_gen[ing].append(gen.symbol)
        
can_derive = {} 
for ing in yields_one_gen:
    can_derive[ing] = get_all_derivitives(ing, yields_one_gen)
    
results = find_upstream('FUEL', 1, can_derive, to_create)

print("Part 1", results[1])
