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

reg_a = 30878003
reg_b = 0
reg_c = 0
def decode_combo(val):
    if val < 4:
        return val
    if val == 4:
        return reg_a 
    if val == 5:
        return reg_b    
    if val == 6:
        return reg_c  
    assert False, f"Bad arg {val}"
       
program = "2,4,1,2,7,5,0,3,4,7,1,7,5,5,3,0"
memory = [int(x) for x in program.split(",")]
ip = 0

is_halting = False 
output = []
while ip < len(memory):
    op_code = memory[ip]
    operand = memory[ip+1]
    match op_code:
        case 0:
            reg_a = reg_a >> decode_combo(operand)
            ip += 2
        case 1:
            reg_b = reg_b ^ operand
            ip += 2
        case 2: 
            reg_b = decode_combo(operand) % 8
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
            output.append(decode_combo(operand) % 8)
            ip += 2
        case 6:
            reg_b = reg_a >> decode_combo(operand)
            ip += 2   
        case 7:
            reg_c = reg_a >> decode_combo(operand)
            ip += 2
            
            


print("Part 1", ",".join(str(a) for a in output))
