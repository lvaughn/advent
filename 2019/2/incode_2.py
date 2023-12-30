#!/usr/bin/env python

def read_input(filename):
    with open(filename) as i:
        return [int(x) for x in i.readline().split(',')]

def test_nums(noun, verb):
    ram = read_input('input.txt')
    pc = 0

    ram[1] = noun
    ram[2] = verb

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
    return ram[0]

for n in range(100):
    for v in range(100):
        if test_nums(n, v) == 19690720:
            print(100*n+v)
            exit()
