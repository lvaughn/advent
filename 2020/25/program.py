#!/usr/bin/env python3

key1 = 14082811
key2 = 5249543

def get_loop_size(key):
    loops = 0
    val = 7
    while val != key:
        loops += 1
        val = (val * 7) % 20201227
    return loops

def get_key(subject, loops):
    val = subject
    for _ in range(loops):
        val = (subject * val) % 20201227
    return val

loop1 = get_loop_size(key1)
loop2 = get_loop_size(key2)

key = get_key(key1, loop2)
print(key)
