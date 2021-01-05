#!/usr/bin/env python3

import re


def rotate_pw(pw, steps):
    if steps < 0:  # left rotate
        return pw[-steps:] + pw[:-steps]
    # Right rotation
    start_point = len(pw) - steps
    return pw[start_point:] + pw[:start_point]


password = [c for c in 'fbgdceah']

lines = []
with open('input.txt', 'r') as f:
    lines = [a.strip() for a in f]

swap_re = re.compile(r'swap (letter|position) (\w+) with (letter|position) (\w)')
rotate_re = re.compile(r'rotate (right|left) (\d+) step')
reverse_re = re.compile(r'reverse positions (\d+) through (\d+)')
move_re = re.compile(r'move position (\d+) to position (\d+)')
for line in reversed(lines):
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
        rotate = None
        if 'based' in line:
            letter = line.strip()[-1]
            for i in range(len(password)):
                new_pw = rotate_pw(password, i)
                idx = new_pw.index(letter)
                move_by = idx + 1
                if idx >= 4:
                    move_by += 1
                attempt = rotate_pw(new_pw, move_by)
                if attempt[0] == password[0]:
                    password = new_pw
                    break
        else:
            m = rotate_re.match(line)
            mult = 1
            if m[1] == 'right':
                mult = -1
            rotate = mult * int(m[2])
            password = rotate_pw(password, rotate)
    elif line.startswith('reverse'):
        m = reverse_re.match(line)
        start = int(m[1])
        end = int(m[2])
        password = password[:start] + list(reversed(password[start:end + 1])) + password[end + 1:]
    elif line.startswith('move'):
        m = move_re.match(line)
        dest = int(m[1])
        src = int(m[2])
        moved = password[src]
        password = password[:src] + password[src + 1:]
        password.insert(dest, moved)
    else:
        print("Unexepected instruction:", line)
        assert False

print(''.join(password))
