#!/usr/bin/env python3
import sys
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
            self.op = op 
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

def adjacent(r, c, height, width):
    results = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_r, new_c = r+dr, c+dc
        if 0 <= new_r < height and 0 <= new_c < width:
            results.append((new_r, new_c))
    return results 
    
def next_move(loc, dir, diagram):
    height = len(diagram)
    width = len(diagram[0]) 
    r, c = loc 
    turn = None
    distance = None
    new_dir = None 
    if dir == '^':
        if diagram[r][c-1] == '#':
            turn = 'L'
            new_dir = '<'
            distance = 0
            while c > 0 and diagram[r][c-1] == '#':
                c -= 1
                distance += 1
        elif diagram[r][c+1] == '#':
            turn = 'R'
            new_dir = '>'
            distance = 0
            while c < width-1 and diagram[r][c+1] == '#':
                c += 1
                distance += 1
    elif dir == 'v':
        if diagram[r][c-1] == '#':
            turn = 'R'
            new_dir = '<'
            distance = 0
            while c > 0 and diagram[r][c-1] == '#':
                c -= 1
                distance += 1
        elif diagram[r][c+1] == '#':
            turn = 'L'
            new_dir = '>'
            distance = 0
            while c < width-1 and diagram[r][c+1] == '#':
                c += 1
                distance += 1
    if dir == '<':
        if diagram[r-1][c] == '#':
            turn = 'R'
            new_dir = '^'
            distance = 0
            while r > 0 and diagram[r-1][c] == '#':
                r -= 1
                distance += 1
        elif diagram[r+1][c] == '#':
            turn = 'L'
            new_dir = 'v'
            distance = 0
            while r < height-1 and diagram[r+1][c] == '#':
                r += 1
                distance += 1
    if dir == '>':
        if diagram[r-1][c] == '#':
            turn = 'L'
            new_dir = '^'
            distance = 0
            while r > 0 and diagram[r-1][c] == '#':
                r -= 1
                distance += 1
        elif diagram[r+1][c] == '#':
            turn = 'R'
            new_dir = 'v'
            distance = 0
            while r < height-1 and diagram[r+1][c] == '#':
                r += 1
                distance += 1
    return turn, distance, (r, c), new_dir 
    
def arrays_start_same(a, b):
    l = min(len(a), len(b))
    for x, y in zip(a[:l], b[:l]):
        if x != y:
            return False 
    return True 

def sub_pattern(pat, ls , sub_var):
    if len(ls) < len(pat):
        return ls 
    if arrays_start_same(pat, ls):
        return [sub_var] + sub_pattern(pat, ls[len(pat):], sub_var)
    return [ls[0]] + sub_pattern(pat, ls[1:], sub_var)   

def moves_to_send(move_ls):
    output = []
    for l in move_ls:
        if type(l) is int:
            for ch in str(l):
                output.append(ord(ch))
        else:
            output.append(ord(l))
        output.append(ord(','))
    output[-1] = 10 
    return output 
    
def first_sub_array(move_ls):
    start = 0
    while start < len(move_ls) and move_ls[start] in ('A', 'B', 'C'):
        start += 1
    end = start 
    while end < len(move_ls) and move_ls[end] not in ('A', 'B', 'C'):
        end += 1
    return move_ls[start:end]
     

answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
program = [int(i) for i in lines[0].split(',')]

compy = IntCodeComputer(program)
compy.run()
diagram = []
line = ''
newline = chr(10)
while compy.has_output():
    ch = chr(compy.read_output())
    if ch == newline:
        if line:
            diagram.append(line)
        line = ''
    else:
        line += ch 
        
height = len(diagram)
width = len(diagram[0])
start_loc = None
for r in range(height):
    for c in range(width):
        if diagram[r][c] in ('>', '<', 'v', '^'):
            start_loc = r, c
        if diagram[r][c] == '#':
            neighbors = [diagram[row][col] for row, col in adjacent(r, c, height, width)]
            if len(neighbors) == 4 and all(n == '#' for n in neighbors):
                answer += r*c
    
print("Part 1", answer)
current_dir = diagram[start_loc[0]][start_loc[1]]
loc = start_loc 
moves = []
cont = True
while cont:
    turn, distance, new_loc, new_dir = next_move(loc, current_dir, diagram)
    if turn is not None:
        moves.append(turn)
        moves.append(distance)
        loc = new_loc 
        current_dir = new_dir
    else:
        cont = False 
    
    
print("Original", moves)
top_program = None
A = None
B = None 
C = None 
for i in range(1, 10):
    possible_a = moves[:2*i]
    if len(possible_a) > 10:
        continue
    a_removed = sub_pattern(possible_a, moves, 'A')
    b_start = first_sub_array(a_removed)
    assert len(b_start) % 2 == 0
    for j in range(1, len(b_start) // 2+1):
        possible_b = b_start[:2*j]
        if len(possible_b) > 10:
            continue
        b_removed = sub_pattern(possible_b, a_removed, 'B')
        c_start = first_sub_array(b_removed)
        assert len(c_start) % 2 == 0
        for k in range(1, len(c_start) // 2+1):
            possible_c = c_start[:2*k]
            if len(possible_c) > 10:
                continue    
            c_removed = sub_pattern(possible_c, b_removed, 'C')
            if all(x in ('A', 'B', 'C') for x in c_removed):
                top_program = c_removed
                A = possible_a
                B = possible_b
                C = possible_c

assert program[0] == 1
program[0] = 2
compy = IntCodeComputer(program)
print("Program:", top_program)
print("A", A)
print("B", B)
print("C", C)
for ch in moves_to_send(top_program):
    compy.add_input(ch)
for ch in moves_to_send(A):
    compy.add_input(ch)
for ch in moves_to_send(B):
    compy.add_input(ch)
for ch in moves_to_send(C):
    compy.add_input(ch)
compy.add_input(ord('n'))
compy.add_input(10)
compy.run()
last_output = -1
while compy.has_output():
    last_output = compy.read_output()
print("Part 2", last_output)
