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

class IntCodeComputer:
    def __init__(self, program: list) -> None:
        self.ram = program[:]
        self.output_queue = Queue()
        self.input_queue = Queue()
        self.state = 'INITIALIZED'
        self.relative_base = 0
    
    def set_memory(self, loc, mode, value):
        if mode == 0:
            addr = self.ram[loc]
        elif mode == 1:
            raise Exception("Wrote called with immediate mode")
        elif mode == 2:
            addr = self.relative_base + self.ram[loc]
        else: 
            raise Exception(f"Bad address mode {mode} (address={loc})")
        
        if len(self.ram) <= addr:
            self.ram.extend([0] * (addr - len(self.ram) + 1))  
        self.ram[addr] = value    
        
    def get_parameter(self, address, mode):
        addr = None
        if mode == 0:
            addr = self.ram[address]
        elif mode == 1:
            return self.ram[address]
        elif mode == 2:
            addr = self.relative_base + self.ram[address]
        else: 
            raise Exception(f"Bad address mode {mode} (address={address})")
        
        if addr >= len(self.ram):
            self.ram.extend([0] * (addr - len(self.ram) + 1))
        return self.ram[addr]
    
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
    
    def add_input(self, value: int):
        self.input_queue.put(value)
        
    def has_output(self) -> bool:
        return not self.output_queue.empty()
        
    def read_output(self) -> int:
        return self.output_queue.get()
    
    def is_running(self):
        return self.state == 'RUNNING'
        
    def run(self):
        pc = 0
        self.state = 'RUNNING'
        while self.ram[pc] != 99:
            op, modes = self.decode(self.ram[pc])
            if op == 1:
                val = self.get_parameter(pc+1, modes[0]) + self.get_parameter(pc+2, modes[1])
                self.set_memory(pc+3, modes[2], val)
                pc += 4
            elif op == 2:
                val = self.get_parameter(pc+1, modes[0]) * self.get_parameter(pc+2, modes[1])
                self.set_memory(pc+3, modes[2], val)
                pc += 4
            elif op == 3:
                self.set_memory(pc+1, modes[0], self.input_queue.get())
                pc += 2
            elif op == 4:
                self.output_queue.put(self.get_parameter(pc+1, modes[0]))
                pc += 2
            elif op == 5:
                if self.get_parameter(pc+1, modes[0]) != 0:
                    pc = self.get_parameter(pc+2, modes[1])
                else:
                    pc += 3
            elif op == 6:
                if self.get_parameter(pc+1, modes[0]) == 0:
                    pc = self.get_parameter(pc+2, modes[1])
                else:
                    pc += 3
            elif op == 7:
                a = self.get_parameter(pc+1, modes[0])
                b = self.get_parameter(pc+2, modes[1])
                if a < b:
                    self.set_memory(pc+3, modes[2], 1)
                else:
                    self.set_memory(pc+3, modes[2], 0)
                pc += 4
            elif op == 8:
                a = self.get_parameter(pc+1, modes[0])
                b = self.get_parameter(pc+2, modes[1])
                if a == b:
                    self.set_memory(pc+3, modes[2], 1)
                else:
                    self.set_memory(pc+3, modes[2], 0)
                pc += 4
            elif op == 9:
                self.relative_base += self.get_parameter(pc+1, modes[0])
                pc += 2
            else:
                print(f"Unexpected op code {op}, pc={pc}")
                exit(-1)
        self.state = 'HALTED'

def get_disp(c: IntCodeComputer):
    x = c.read_output()
    y = c.read_output()
    b = c.read_output()
    
    return x, y, b       
  
def thread_runner(computer: IntCodeComputer):
    computer.run()
 
answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
program = [int(i) for i in lines[0].split(',')]
compy = IntCodeComputer(program)

thread = threading.Thread(target=thread_runner, args=(compy,))
thread.start()

while compy.is_running():
    x, y, b = get_disp(compy)
    if b == 2:
        answer += 1


print("Part 1", answer)
