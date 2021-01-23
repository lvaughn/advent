#!/usr/bin/env python3

n_steps = 12523873
tape_size = 10000

tape = [0] * (tape_size * 2)
loc = tape_size # left = -1, right = +1
state = 'A'
for _ in range(n_steps):
    if state == 'A':
        if tape[loc] == 0:
            tape[loc] = 1
            loc += 1
            state = 'B'
        else:
            loc -= 1
            state = 'E'
    elif state == 'B':
        if tape[loc] == 0:
            tape[loc] = 1
            loc += 1
            state = 'C'
        else:
            loc += 1
            state = 'F'
    elif state == 'C':
        if tape[loc] == 0:
            tape[loc] = 1
            loc -= 1
            state = 'D'
        else:
            tape[loc] = 0
            loc += 1
            state = 'B'
    elif state == 'D':
        if tape[loc] == 0:
            tape[loc] = 1
            loc += 1
            state = 'E'
        else:
            tape[loc] = 0
            loc -= 1
            state = 'C'
    elif state == 'E':
        if tape[loc] == 0:
            tape[loc] = 1
            loc -= 1
            state = 'A'
        else:
            tape[loc] = 0
            loc += 1
            state = 'D'
    elif state == 'F':
        if tape[loc] == 0:
            tape[loc] = 1
            loc += 1
            state = 'A'
        else:
            tape[loc] = 1
            loc += 1
            state = 'C'
    else:
        assert False or "Bad state" or state

print("Checksum", sum(tape))