#!/usr/bin/env python3
from collections import Counter, defaultdict, deque, namedtuple
import numpy as np
import sys
from queue import Queue 

import threading

class IntCodeComputer:
    def __init__(self, program: list) -> None:
        self.ram = program[:]
        self.output_queue = Queue()
        self.input_queue = Queue()
        self.state = 'INITIALIZED'
        self.relative_base = 0
        self.killed = False
    
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
        while self.ram[pc] != 99 and not self.killed:
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
        
def thread_runner(computer: IntCodeComputer):
    computer.run()

ox_loc = None 
def make_map(compy: IntCodeComputer, grid: np.ndarray):
    start_loc = (grid.shape[0]//2, grid.shape[1]//2)
    
    def helper(r, c):
        global ox_loc 
        if grid[r-1, c] == -1:
            compy.add_input(1)
            result = compy.read_output()
            if result == 2:
                ox_loc = (r-1, c)
                result = 1
            grid[r-1, c] = result 
            if result > 0:
                helper(r-1, c)
                compy.add_input(2) # Undo the move
                compy.read_output()
        if grid[r+1, c] == -1:
            compy.add_input(2)
            result = compy.read_output()
            if result == 2:
                ox_loc = (r+1, c)
                result = 1
            grid[r+1, c] = result 
            if result > 0:
                helper(r+1, c)
                compy.add_input(1) # Undo the move
                compy.read_output()
        if grid[r, c+1] == -1:
            compy.add_input(4)
            result = compy.read_output()
            if result == 2:
                ox_loc = (r, c+1)
                result = 1
            grid[r, c+1] = result 
            if result > 0:
                helper(r, c+1)
                compy.add_input(3) # Undo the move       
                compy.read_output() 
        if grid[r, c-1] == -1:
            compy.add_input(3)
            result = compy.read_output()
            if result == 2:
                ox_loc = (r, c-1)
                result = 1
            grid[r, c-1] = result 
            if result > 0:
                helper(r, c-1)
                compy.add_input(4) # Undo the move  
                compy.read_output()     
    helper(start_loc[0], start_loc[1])
    return ox_loc 
            

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
program = [int(n) for n in lines[0].split(',')]

computer = IntCodeComputer(program)
thread = threading.Thread(target=thread_runner, args=(computer,))
thread.start()

board = np.ones((50,50), dtype=int) * -1
make_map(computer, board)
# print(ox_loc)
# print(board)

# Shut it down
computer.killed = True 
computer.add_input(0)

board[ox_loc[0], ox_loc[1]] = 3
steps = 0
while np.count_nonzero(board==1) > 0:
    steps += 1
    new_board = board.copy()
    for r in range(board.shape[0]):
        for c in range(board.shape[1]):
            if board[r, c] == 3:
                if board[r, c+1] == 1:
                    new_board[r, c+1] = 3
                if board[r, c-1] == 1:
                    new_board[r, c-1] = 3 
                if board[r+1, c] == 1:
                    new_board[r+1, c] = 3                  
                if board[r-1, c] == 1:
                    new_board[r-1, c] = 3  
    board = new_board     
               
print("Part 2", steps)             
