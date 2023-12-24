#!/usr/bin/env python3
#from string import ascii_uppercase, ascii_lowercase, digits
#from collections import Counter, defaultdict, deque, namedtuple
#from itertools import count, product, permutations, combinations, combinations_with_replacement
#from sortedcontainers import SortedSet, SortedDict, SortedList
import numpy as np
#import re
#import pprint
import sys
import threading
from queue import Queue

class IntCodeDissasembler:
    def __init__(self, program: list) -> None:
        self.ram = program[:]
        self.relative_base = 0
    
    def decode(self, opcode: int) -> (int, [int]):
        op = opcode % 100
        addresses = opcode // 100
        modes = []
        while addresses > 0:
            modes.append(addresses % 10)
            addresses = addresses // 10
        if len(modes) <  3:
            modes.extend([0] * (3 - len(modes)))
        return op, modes 
    
    def param_to_string(self, offset: int, mode:int) -> str:
        addr = self.ram[offset]
        if mode == 0:
            return f"@{addr}"
        elif mode == 1:
            return f"{addr}"
        elif mode == 2:
            return f".{addr}"
        else:
            return "_"
    
    def output(self):
        for pc in range(len(self.ram) - 3):
            op, modes = self.decode(self.ram[pc])
            start = f"{pc:5}  [{self.ram[pc]:3}]  : "
            valid_modes = (0 <= modes[0] <= 2) and (0 <= modes[1] <= 2) and (0 <= modes[2] <= 2)
            if op == 1 and valid_modes:
                rest = f"{pc:5} ADD  {self.param_to_string(pc+1, modes[0])} {self.param_to_string(pc+2, modes[1])} -> {self.param_to_string(pc+3, modes[2])}"
            elif op == 2 and valid_modes:
                rest = f"{pc:5} MUL  {self.param_to_string(pc+1, modes[0])} {self.param_to_string(pc+2, modes[1])} -> {self.param_to_string(pc+3, modes[2])}"
            elif op == 3 and valid_modes:
                rest = f"{pc:5} READ {self.param_to_string(pc+1, modes[0])}"
            elif op == 4 and valid_modes:
                rest = f"{pc:5} WRT  {self.param_to_string(pc+1, modes[0])}"
            elif op == 5 and valid_modes:
                rest = f"{pc:5} JNZ  {self.param_to_string(pc+1, modes[0])} -> {self.param_to_string(pc+2, modes[1])}"
            elif op == 6 and valid_modes:
                rest = f"{pc:5} JZ   {self.param_to_string(pc+1, modes[0])} -> {self.param_to_string(pc+2, modes[1])}"
            elif op == 7 and valid_modes:
                rest = f"{pc:5} LT   {self.param_to_string(pc+1, modes[0])} {self.param_to_string(pc+2, modes[1])} ->{self.param_to_string(pc+3, modes[2])}"
            elif op == 8 and valid_modes:
                rest = f"{pc:5} EQ   {self.param_to_string(pc+1, modes[0])} {self.param_to_string(pc+2, modes[1])} ->{self.param_to_string(pc+3, modes[2])}"
            elif op == 9 and valid_modes:
                rest = f"{pc:5} SREL {self.param_to_string(pc+1, modes[0])}"
            elif op == 99:
                rest = f"{pc:5} HALT"
            else:
                rest = ''
            print(start, rest)
        for pc in range(len(self.ram) - 3, len(self.ram)):
            start = f"{pc:5}  [{self.ram[pc]:3}]  : "
            print(start)

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
program = [int(i) for i in lines[0].split(',')]
compy = IntCodeDissasembler(program)
compy.output()