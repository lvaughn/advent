#!/usr/bin/env python

from collections import namedtuple
from itertools import permutations
from Queue import Queue

def read_input(filename):
    with open(filename) as i:
        return [int(x) for x in i.readline().split(',')]

Opcode = namedtuple('Opcode', ['opcode', 'modes'])
def decode_opcode(n):
    op = n % 100
    n = n /100
    modes = []
    for i in xrange(3):
        modes.append(n%10)
        n = n / 10
    return Opcode(op, modes)

class IntCode:
    op_n_args = {
        1: 4,
        2: 4,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4,
        8: 4,
        99: 0}
        
    def __init__(self, ram):
        self.ram = list(ram)
        self.pc = 0
        self.input_queue = Queue()
        self.output_queue = Queue()
        
    def get_rval(self, op, n):
        mode = op.modes[n-1]
        if mode == 0:
            v = self.ram[self.ram[self.pc+n]]
        elif mode == 1:
            v = self.ram[self.pc+n]
        else:
            print("Bad mode", mode)
            exit(-1)
        #print "    rval:", self.pc, n, op.modes[n-1], v
        return v

    def set_lval(self, op, n, value):
        mode = op.modes[n-1]
        #print "    lval:", self.ram[self.pc+n], value, self.pc, n, mode
        if mode == 0:
            self.ram[self.ram[self.pc+n]] = value
        elif mode == 1:
            self.ram[self.pc+n] = value
        else:
            print("Bad mode", mode)
            exit(-1)

    def send_input(self, value):
        self.input_queue.put(value)

    def get_output(self):
        return self.output_queue.get()
            
    def run(self):
        op = decode_opcode(self.ram[self.pc])
        while op.opcode != 99:
            #print("Starting opcode", pc, op, ram[pc:pc+4])
            jump_to = None
            if op.opcode == 1:
                value = self.get_rval(op, 1) + self.get_rval(op, 2) 
                self.set_lval(op, 3, value)
            elif op.opcode == 2:
                value = self.get_rval(op, 1) * self.get_rval(op, 2) 
                self.set_lval(op, 3, value)
            elif op.opcode == 3:
                #i = raw_input("> ")
                self.set_lval(op, 1, self.input_queue.get())
            elif op.opcode == 4:
                #print(self.get_rval(op, 1))
                self.output_queue.put(self.get_rval(op, 1))
            elif op.opcode == 5:
                if self.get_rval(op, 1) != 0:
                    jump_to = self.get_rval(op, 2)
            elif op.opcode == 6:
                if self.get_rval(op, 1) == 0:
                    jump_to = self.get_rval(op, 2)
            elif op.opcode == 7:
                if self.get_rval(op, 1) < self.get_rval(op, 2):
                    self.set_lval(op, 3, 1)
                else:
                    self.set_lval(op, 3, 0)
            elif op.opcode == 8:
                if self.get_rval(op, 1) == self.get_rval(op, 2):
                    self.set_lval(op, 3, 1)
                else:
                    self.set_lval(op, 3, 0)
            else:
                print("Unknown instruction %d at %d" % (self.ram[self.pc], self.pc))
                exit(-1)
            #print("New RAM", ram[pc:pc+4])
            if jump_to is None:
                self.pc += self.op_n_args[op.opcode]
            else:
                self.pc = jump_to
            op = decode_opcode(self.ram[self.pc])


ram = read_input('program.txt')
def run_permutation(perm):
    computers = []
    for i in perm:
        c = IntCode(ram)
        c.send_input(i)
        computers.append(c)

    input = 0
    for c in computers:
        c.send_input(input)
        c.run()
        output = c.get_output()
        #print(input, output)
        input = output
    return input

best = -999999999
for perm in permutations(range(5)):
    #print "LGV", perm
    val = run_permutation(perm)
    if val > best:
        best = val
        print perm, val
    

    
