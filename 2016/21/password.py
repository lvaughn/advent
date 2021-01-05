#!/usr/bin/env python3

import re


def rotate_pw(pw, steps):
    if steps < 0:  # left rotate
        return pw[-steps:] + pw[:-steps]
    # Right rotation
    start_point = len(pw) - steps
    return pw[start_point:] + pw[:start_point]


password = [c for c in 'abcdefgh']

with open('input.txt', 'r') as f:
    swap_re = re.compile(r'swap (letter|position) (\w+) with (letter|position) (\w)')
    rotate_re = re.compile(r'rotate (right|left) (\d+) step')
    reverse_re = re.compile(r'reverse positions (\d+) through (\d+)')
    move_re = re.compile(r'move position (\d+) to position (\d+)')
    for line in f:
        if line.startswith('swap'):
            m = swap_re.match(line)
            if m[1] == 'position':
                a = int(m[2])
                b = int(m[4])
                tmp = password[a]
                password[a] = password[b]
                password[b] = tmp
            else:
                for i in range(len(password)):
                    a = m[2]
                    b = m[4]
                    if password[i] == a:
                        password[i] = b
                    elif password[i] == b:
                        password[i] = a
        elif line.startswith('rotate'):
            rotate = 0
            if 'based' in line:
                letter = line.strip()[-1]
                idx = password.index(letter)
                if idx >= 4:
                    idx += 1
                rotate = idx + 1
            else:
                m = rotate_re.match(line)
                mult = 1
                if m[1] == 'left':
                    mult = -1
                rotate = mult * int(m[2])
            password = rotate_pw(password, rotate)
        elif line.startswith('reverse'):
            m = reverse_re.match(line)
            start = int(m[1])
            end = int(m[2])
            password = password[:start] + list(reversed(password[start:end+1])) + password[end+1:]
        elif line.startswith('move'):
            m = move_re.match(line)
            src = int(m[1])
            dest = int(m[2])
            moved = password[src]
            password = password[:src] + password[src+1:]
            password.insert(dest, moved)
        else:
            print("Unexepected instruction:", line)
            assert False


print(''.join(password))
