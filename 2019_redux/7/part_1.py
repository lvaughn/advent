#!/usr/bin/env python3
from collections import Counter, defaultdict, deque, namedtuple
from itertools import count, product, permutations, combinations, combinations_with_replacement
import sys


class IntCodeComputer:
    def __init__(self, program: list) -> None:
        self.ram = program[:]
        self.output_queue = deque()
        self.input_queue = deque()
        self.state = 'RUNNING'
    
    def set_memory(self, loc, mode, value):
        if mode == 0:
            physical_address = self.ram[loc]
        elif mode == 1:
            raise Exception("Wrote called with immediate mode")
        else: 
            raise Exception(f"Bad address mode {mode} (address={loc})")
        
        if len(self.ram) <= physical_address:
            self.ram.extend([None] * (physical_address - len(self.ram) + 1))  
        self.ram[physical_address] = value    
        
    def get_parameter(self, address, mode):
        if mode == 0:
            return self.ram[self.ram[address]]
        elif mode == 1:
            return self.ram[address] 
        else: 
            raise Exception(f"Bad address mode {mode} (address={address})")
    
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
        self.input_queue.append(value)
        
    def has_output(self) -> bool:
        return len(self.output_queue) > 0
        
    def read_output(self) -> int:
        return self.output_queue.popleft()
    
    def is_running(self):
        return self.state == 'RUNNING'
        
    def run(self):
        pc = 0
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
                self.set_memory(pc+1, modes[0], self.input_queue.popleft())
                pc += 2
            elif op == 4:
                self.output_queue.append(self.get_parameter(pc+1, modes[0]))
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
            else:
                print(f"Unexpected op code {op}, pc={pc}")
                exit(-1)
        self.state = 'HALTED'



with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
answer =  -9999999999
    
program = [int(i) for i in lines[0].split(',')]
for perm in permutations([0,1,2,3,4], 5):
    computers = [IntCodeComputer(program) for _ in range(5)]
    for c, phase in zip(computers, perm):
        c.add_input(phase)
    value = 0
    for c in computers:
        c.add_input(value)
        c.run()
        value = c.read_output()
    answer = max(answer, value)

print("Part 1", answer)
