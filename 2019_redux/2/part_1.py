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

class IntCodeComputer:
    def __init__(self, program: list) -> None:
        self.ram = program[:]
    
    def set_memory(self, address, value):
        if len(self.ram) <= address:
            self.ram.extend([None] * (address - len(self.ram) + 1))  
        self.ram[address] = value
        
    def get_memory(self, address):
        return self.ram[address]
        
    def run(self):
        pc = 0
        while self.ram[pc] != 99:
            if self.ram[pc] == 1:
                val = self.get_memory(self.ram[pc+1]) + self.get_memory(self.ram[pc+2])
                self.set_memory(self.ram[pc+3], val)
                pc += 4
            elif self.ram[pc] == 2:
                val = self.get_memory(self.ram[pc+1]) * self.get_memory(self.ram[pc+2])
                self.set_memory(self.ram[pc+3], val)
                pc += 4
            else:
                print(f"Unexpected op code {self.ram[pc]}, pc={pc}")
                exit(-1)


answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
ram = [int(i) for i in lines[0].split(',')]


compy = IntCodeComputer(ram)
compy.ram[1] = 12
compy.ram[2] = 2

compy.run()


print("Part 1", compy.ram[0])

for noun in range(100):
    for verb in range(100):
        compy = IntCodeComputer(ram)
        compy.ram[1] = noun
        compy.ram[2] = verb 
        
        compy.run()
        
        if compy.ram[0] == 19690720:
            print("Part 2: ", 100*noun + verb)
            exit(0)
