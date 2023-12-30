#!/usr/bin/env python

from collections import namedtuple

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

def get_rval(op, pc, n):
    mode = op.modes[n-1]
    if mode == 0:
        v = ram[ram[pc+n]]
    elif mode == 1:
        v = ram[pc+n]
    else:
        print("Bad mode", mode)
        exit(-1)
    #print "    rval:", pc, n, op.modes[n-1], v
    return v

def set_lval(op, pc, n, value):
    mode = op.modes[n-1]
    #print "    lval:", ram[pc+n], value, pc, n, mode
    if mode == 0:
        ram[ram[pc+n]] = value
    elif mode == 1:
        ram[pc+n] = value
    else:
        print("Bad mode", mode)
        exit(-1)

OP_ARGS = {
    1: 4,
    2: 4,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 4,
    8: 4,
    99: 0}
def get_nargs(op):
    return OP_ARGS[op.opcode]

ram = read_input('input.txt')
pc = 0

op = decode_opcode(ram[pc])
while op.opcode != 99:
    #print("Starting opcode", pc, op, ram[pc:pc+4])
    jump_to = None
    if op.opcode == 1:
        value = get_rval(op, pc, 1) + get_rval(op, pc, 2) 
        set_lval(op, pc, 3, value)
    elif op.opcode == 2:
        value = get_rval(op, pc, 1) * get_rval(op, pc, 2) 
        set_lval(op, pc, 3, value)
    elif op.opcode == 3:
        i = raw_input("> ")
        set_lval(op, pc, 1, int(i))
    elif op.opcode == 4:
        print(get_rval(op, pc, 1))
    elif op.opcode == 5:
        if get_rval(op, pc, 1) != 0:
            jump_to = get_rval(op, pc, 2)
    elif op.opcode == 6:
        if get_rval(op, pc, 1) == 0:
            jump_to = get_rval(op, pc, 2)
    elif op.opcode == 7:
        if get_rval(op, pc, 1) < get_rval(op, pc, 2):
            set_lval(op, pc, 3, 1)
        else:
            set_lval(op, pc, 3, 0)
    elif op.opcode == 8:
        if get_rval(op, pc, 1) == get_rval(op, pc, 2):
            set_lval(op, pc, 3, 1)
        else:
            set_lval(op, pc, 3, 0)
    else:
        print("Unknown instruction %d at %d" % (ram[pc], pc))
        exit(-1)
    #print("New RAM", ram[pc:pc+4])
    if jump_to is None:
        pc = pc + get_nargs(op)
    else:
        pc = jump_to
    op = decode_opcode(ram[pc])
