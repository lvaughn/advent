#!/usr/bin/env python3
from collections import deque
import sys


class IntCodeComputer:
    def __init__(self, program: list) -> None:
        self.ram = program[:]
        self.output_queue = deque()
        self.input_queue = deque()
    
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


with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
program = [int(a) for a in lines[0].split(',')]
compy = IntCodeComputer(program)
compy.add_input(1)
compy.run()
answer = 0
while answer == 0 and compy.has_output():
    answer = compy.read_output()

print("Part 1", answer)

compy = IntCodeComputer(program)
compy.add_input(5)
compy.run()
answer = compy.read_output()
print("Part 2", answer)
