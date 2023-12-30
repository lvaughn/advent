#!/usr/bin/env python

def read_input(filename):
    with open(filename) as i:
        return [int(x) for x in i.readline().split(',')]

ram = read_input('input.txt')
pc = 0

ram[1] = 12
ram[2] = 2

while ram[pc] != 99:
    #print(pc, ram)
    if ram[pc] == 1:
        ram[ram[pc+3]] = ram[ram[pc+1]]+ram[ram[pc+2]]
        pc += 4
    elif ram[pc] == 2:
        ram[ram[pc+3]] = ram[ram[pc+1]]*ram[ram[pc+2]]
        pc += 4
    else:
        print("Unknown instruction %d at %d" % (ram[pc], pc))
        exit(-1)
print(ram[0])
