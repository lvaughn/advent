#!/usr/bin/env python3
import numpy as np
from queue import Queue 
import sys
import threading

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
        
        
def rotate(current_dir, value):
    assert value in (0, 1), f"Bad value {value}"
    if current_dir == 'u':
        if value == 0:
            return 'l'
        return 'r'
    elif current_dir == 'l':
        if value == 0:
            return 'd'
        return 'u'
    elif current_dir == 'd':
        if value == 0:
            return 'r'
        return 'l'
    elif current_dir == 'r':
        if value == 0:
            return 'u'
        return 'd'
    else:
        assert False, f"Bad direction {current_dir} (value = {value})"
        
        
def move(x, y, dir):
    if dir == 'u':
        return x, y+1 
    elif dir == 'l':
        return x-1, y
    elif dir == 'd':
        return x, y-1
    elif dir == 'r':
        return x+1, y 
    else:
        assert False, f"Bad direction {dir}"

def thread_runner(computer: IntCodeComputer):
    computer.run()


SIZE=1000

dir = 'u'

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

program = [int(a) for a in lines[0].split(',')]

has_updated = np.zeros((SIZE, SIZE), dtype=bool)
hull = np.zeros((SIZE, SIZE), dtype=int)

x = SIZE // 2
y = SIZE // 2
dir = 'u'

compy = IntCodeComputer(program)
thread = threading.Thread(target=thread_runner, args=(compy,))
thread.start()

while compy.is_running():
    compy.add_input(hull[x, y])
    new_color = compy.read_output()
    turn = compy.read_output()
    has_updated[x, y] = True
    hull[x, y] = new_color
    dir = rotate(dir, turn)
    x, y = move(x, y, dir)

answer = np.sum(has_updated)
print("Part 1", answer)

compy = IntCodeComputer(program)
thread = threading.Thread(target=thread_runner, args=(compy,))
thread.start()
hull = np.zeros((SIZE, SIZE), dtype=int)

x = SIZE // 2
y = SIZE // 2
dir = 'u'
hull[x, y] = 1
while compy.is_running():
    compy.add_input(hull[x, y])
    new_color = compy.read_output()
    turn = compy.read_output()
    hull[x, y] = new_color
    dir = rotate(dir, turn)
    x, y = move(x, y, dir)
    
# find the bounding box
columns, rows = np.nonzero(hull)
min_row = np.min(rows)
max_row = np.max(rows)
min_col = np.min(columns)
max_col = np.max(columns)

for row in range(max_row, min_row-1, -1):
    s = ""
    for col in range(min_col, max_col+1):
        if hull[col, row] == 1:
            s += "*"
        else:
            s += " "
    print(s)