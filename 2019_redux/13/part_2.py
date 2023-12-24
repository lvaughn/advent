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
from pynput import keyboard

class IntCodeComputer:
    def __init__(self, program: list) -> None:
        self.ram = program[:]
        self.output_queue = Queue()
        self.input_queue = Queue()
        self.state = 'INITIALIZED'
        self.relative_base = 0
        self.reading = False 
    
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
        if addr in [386, 435]:
            return True 
        return False 
        
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
    
    def is_reading(self):
        return self.reading 
        
    def run(self):
        pc = 0
        self.state = 'RUNNING'
        while self.ram[pc] != 99:
            op, modes = self.decode(self.ram[pc])
            self.op = op
            self.pc = pc 
            if op == 1:
                val = self.get_parameter(pc+1, modes[0]) + self.get_parameter(pc+2, modes[1])
                special = self.set_memory(pc+3, modes[2], val)
                if special:
                    with open("score_changes.txt", "a") as f:
                        f.write(f"{pc:4}:{val}({modes[2]}),a1=({self.ram[pc+1]}, {modes[0]}), a2=({self.ram[pc+2]}, {modes[1]}) base={self.relative_base}\n")
                pc += 4
            elif op == 2:
                val = self.get_parameter(pc+1, modes[0]) * self.get_parameter(pc+2, modes[1])
                self.set_memory(pc+3, modes[2], val)
                pc += 4
            elif op == 3:
                self.is_reading = True 
                self.set_memory(pc+1, modes[0], self.input_queue.get())
                self.is_reading = False 
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

int_to_block = {
    0: ' ',
    1: '#',
    2: '-',
    3: '_',
    4: 'o'
}

def display_board(b, score, c):
    width, height = b.shape
    print(score)
    for y in range(height):
        line = ''
        for x in range(width):
            line += int_to_block[b[x, y]]
        print(line)
    # Paddle location 392, score 386
    print(f"RAM[392]={c.ram[392]} ball_x={c.ball_x} paddle_x={c.paddle_x}")
  
def thread_runner(computer: IntCodeComputer):
    computer.run()
 
answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
program = [int(i) for i in lines[0].split(',')]
program[0] = 2 # Add the quarters 
compy = IntCodeComputer(program)

thread = threading.Thread(target=thread_runner, args=(compy,))
thread.start()

def make_listener(c):
    def on_press(key):
        if key == keyboard.Key.space:
            c.add_input(0)
        elif key == keyboard.Key.left:
            c.add_input(-1)
        elif key == keyboard.Key.right:
            c.add_input(1)
        elif key == keyboard.Key.up or key == keyboard.Key.down:
            c.add_input(0)
        elif key.char == 'w':
            c.ram[392] = c.ball_x
        elif key.char == 'a':
            c.add_input(-1)
        elif key.char == 'l':
            c.add_input(1)
        else:
            print(f"Unexpected key '{key}'")
    return on_press
        
listener = keyboard.Listener(on_press=make_listener(compy))
listener.start()

board = np.zeros((45, 25), dtype=int)
score = 0
print('About to do event loops')

score_file = open('scores.csv', 'w')
compy.ball_x = compy.paddle_x = 20
while True:
    while compy.has_output():
        x, y, b = get_disp(compy)
        if x == -1 and y == 0:
            score = b 
        else: 
            if b == 0:
                if board[x, y] == 2:
                   score_file.write(f"{x},{y},{score}\n")
                   score_file.flush()
            if b == 3:
                print("Paddle y", y)
                compy.paddle_x = x 
            if b == 4:
                compy.ball_x = x 
            board[x, y] = b 
        display_board(board, score, compy)


print("Part 2", score)
