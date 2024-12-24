#!/usr/bin/env python3
import sys
#import numpy as np
import re
from collections import Counter, defaultdict, deque, namedtuple
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

class Gate:
    def __init__(self, func, id, a, b):
        self.a = a
        self.b = b 
        self.id = id 
        self.func = func 
        
    def eval(self, vars):
        if vars[self.a] is None or vars[self.b] is None:
            return None 
        if self.func == 'OR':
            return vars[self.a] or vars[self.b] 
        if self.func == 'XOR': 
            return vars[self.a] ^ vars[self.b]
        if self.func == 'AND':
            return vars[self.a] and vars[self.b]
        assert False, f"Bad func {self.func}"
        
    def __str__(self):
        return f"{self.a} {self.func} {self.b} -> {self.id}"
    
    def __repr__(self):
        return self.__str__()
        
def process_bitslice(x_in, y_in, c_in, output, gates):
    # need to find, input_xor, input_and, carry_or, carry_and
    # output bit = (x^y)^c
    # carry bit = (x&y) | (c&(x^y))
    #                      ------- = carry_and
    #             ----------------- = carry_or (AKA carry bit)
    print(f"  Processing x={x_in}, y={y_in}, c={c_in} to {output}")
    
    # Find input xor and input and
    input_gates = all_gates_with_input(gates, x_in)
    input_xors = [g for g in input_gates if g.func == 'XOR']
    input_ands = [g for g in input_gates if g.func == 'AND']
    assert len(input_xors) == 1
    assert len(input_ands) == 1
    input_xor = input_xors[0]
    input_and = input_ands[0]
    assert input_xor.a in [x_in, y_in]
    assert input_xor.b in [x_in, y_in]
    assert input_and.a in [x_in, y_in]
    assert input_and.b in [x_in, y_in]
    print(f"  input_xor={input_xor.id}, input_and={input_and.id}")
    
    # find the output bit
    output_gate = gates[output]
    print(f"  Known output gate {output_gate}")
    # carry_gate = gates[c_in]
    uses_carry = all_gates_with_input(gates, c_in)
    assert output_gate in uses_carry
    assert output_gate.a == input_xor.id or output_gate.b == input_xor.id
    assert output_gate.a == c_in or output_gate.b == c_in
    
    # find the carry and
    in_xor = input_xor.id
    possible_carry_ands = [g for g in uses_carry if g.func == 'AND' and (g.a == in_xor or g.b == in_xor)]
    assert len(possible_carry_ands) == 1, possible_carry_ands
    carry_and = possible_carry_ands[0]
    
    # Find the carry or
    possible_carry_ors = all_gates_with_input(gates, input_and.id)
    assert len(possible_carry_ors) == 1
    carry_or = possible_carry_ors[0]
    assert carry_or.func == 'OR'
    assert carry_or.a == carry_and.id or carry_or.b == carry_and.id 
    
    carry_bit = carry_or.id
    print(f"  Calculated output={output_gate.id}, carry={carry_bit}")
    return output_gate.id, carry_bit, input_xor.id, input_and.id, carry_and.id


def all_gates_with_input(gates, input):
    return [gates[g] for g in gates if gates[g].a == input or gates[g].b == input]

with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
# Find the start
for no, l in enumerate(lines):
    if l == '':
        funcs_start = no+1
        break 
    
# Swaps needed (determined by running a lot and fixing the asserts)
swaps = {
    'z11': 'vkq',
    'vkq': 'z11', 
    'mmk': 'z24', 
    'z24': 'mmk', 
    'pvb': 'qdq',
    'qdq': 'pvb',
    'hqh': 'z38',
    'z38': 'hqh'
}

# Load up the gates
func_re = re.compile(r'(\S+) (\S+) (\S+) -> (\S+)')
gates = {}
for l in lines[funcs_start:]:
    m = func_re.match(l)
    # Swap if needed
    id = m[4]
    if id in swaps:
        id = swaps[id]
        
    f = Gate(m[2], id, m[1], m[3])
    gates[id] = f 

# Set up the loop
bitslice = 1
carry_bit = 'rnv' # Found by inspecting the input 
while bitslice < 45:
    print(f"Doing bitslice {bitslice}")
    x_in = f"x{bitslice:02}"
    y_in = f"y{bitslice:02}"
    z_out = f"z{bitslice:02}"
    
    new_gates = process_bitslice(x_in, y_in, carry_bit, z_out, gates)
    new_out, new_carry, in_xor, in_and, c_and = new_gates 
    assert new_out == z_out 
    carry_bit = new_carry
    
    bitslice += 1
assert carry_bit == 'z45', carry_bit 

# Actually find the answer
print("Part 2:", ",".join(sorted(swaps.keys())))