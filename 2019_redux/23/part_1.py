#!/usr/bin/env python3
from queue import Queue 
import sys
import threading
import time 

class IntCodeComputer:
    def __init__(self, program: list, address: int) -> None:
        self.ram = program[:]
        self.output_queue = Queue()
        self.input_queue = Queue()
        self.state = 'INITIALIZED'
        self.relative_base = 0
        self.address = address # Only read once
        self.y = None
    
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
    
    # def add_input(self, value: int):
    #     self.input_queue.put(value)
        
    def receive_packet(self, x: int, y: int):
        self.input_queue.put((x, y))
        
    def has_output(self) -> bool:
        return not self.output_queue.empty()
        
    def read_output(self) -> int:
        return self.output_queue.get()
    
    def check_and_send_packet(self):
        if self.output_queue.qsize() >= 3:
            dest = self.output_queue.get()
            x =  self.output_queue.get()
            y = self.output_queue.get()
            
            send_packet(dest, x, y)
    
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
                if self.address is not None:
                    self.set_memory(pc+1, modes[0], self.address)
                    self.address = None 
                elif self.y is not None:
                    self.set_memory(pc+1, modes[0], self.y)
                    self.y = None 
                elif self.input_queue.empty():
                    self.set_memory(pc+1, modes[0], -1)
                else: # Read a new packet, save y for the next read 
                    x, self.y = self.input_queue.get()
                    self.set_memory(pc+1, modes[0], x)
                pc += 2
            elif op == 4:
                self.output_queue.put(self.get_parameter(pc+1, modes[0]))
                self.check_and_send_packet()
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
        
def thread_runner(computer: IntCodeComputer, computer_number: int):
    time.sleep(0.2)
    computer.run()
    print(f"Computer {computer_number} done")

computer_registry = {}
def send_packet(dest: int, x: int, y: int):
    print(f"Packet sent ({x},{y}) to {dest}")
    if dest == 255:
        print(f"Part 1 x={x} y={y}")
        exit()
    
    compy = computer_registry[dest]
    compy.receive_packet(x, y)


answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
program = [int(i) for i in lines[0].split(",")]


threads = []
for i in range(50):
    compy = IntCodeComputer(program, i)
    computer_registry[i] = compy 
    thread = threading.Thread(target=thread_runner, args=(compy, i))
    threads.append(thread)
    
for t in threads:
    t.start()

print("Computers started")
