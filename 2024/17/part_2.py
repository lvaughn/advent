#!/usr/bin/env python3
import sys
#import numpy as np
import re
# from collections import Counter, defaultdict, deque, namedtuple
# from string import ascii_uppercase, ascii_lowercase, digits
# from itertools import count, product, permutations, combinations, combinations_with_replacement
# from sortedcontainers import SortedSet, SortedDict, SortedList
# from z3 import Solver, BitVec, Distinct
# from networkx import networkx as nx  
# import pprint
# import sympy as sym
# from functools import cache


# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

# directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
height = len(lines)
width = len(lines[0])

pgm_line = lines[-1]
program = pgm_line.split(':')[1].strip()
memory = [int(x) for x in program.split(",")]

def decode_combo(val, a, b, c):
    if val < 4:
        return val
    if val == 4:
        return a 
    if val == 5:
        return b    
    if val == 6:
        return c  
    assert False, f"Bad arg {val}"

def simulate(a): 
    reg_a = a
    reg_b = 0
    reg_c = 0
    output = []
    ip = 0
    while ip < len(memory):
        op_code = memory[ip]
        operand = memory[ip+1]
        match op_code:
            case 0:
                reg_a = reg_a >> decode_combo(operand, reg_a, reg_b, reg_c)
                ip += 2
            case 1:
                reg_b = reg_b ^ operand
                ip += 2
            case 2: 
                reg_b = decode_combo(operand, reg_a, reg_b, reg_c) % 8
                ip += 2
            case 3:
                if reg_a == 0:
                    ip += 2
                else:
                    ip = operand
            case 4:
                reg_b = reg_b ^ reg_c 
                ip += 2
            case 5:
                output.append(decode_combo(operand, reg_a, reg_b, reg_c) % 8)
                ip += 2
            case 6:
                reg_b = reg_a >> decode_combo(operand, reg_a, reg_b, reg_c)
                ip += 2   
            case 7:
                reg_c = reg_a >> decode_combo(operand, reg_a, reg_b, reg_c)
                ip += 2
    return ",".join(str(a) for a in output)

def search_for(value_so_far, instructions):
    if len(instructions) == 0:
        print(value_so_far)
        return 
    for i in range(8):
        new_start = 8 * value_so_far + i
        results = simulate(new_start)
        if results[0] == instructions[0]:
            search_for(new_start, instructions[1:])
    
search_for(0, list(reversed([x for x in program.split(",")])))
            
        

