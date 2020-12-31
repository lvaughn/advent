#!/usr/bin/env python3

def decompress(s, recurse):

    answer = ''
    while s != '':
        if s[0] == '(':
            idx = s.index(')')
            (n_chars, reps) = s[1:idx].split('x')
            to_repeat = s[idx + 1:idx + 1 + int(n_chars)]
            if recurse:
                to_repeat = decompress(to_repeat, True)
            answer += to_repeat * int(reps)
            s = s[idx + 1 + int(n_chars):]
        else:
            idx = s.find('(')
            if idx < 0:
                answer += s
                s = ''
            else:
                answer += s[:idx]
                s = s[idx:]
    return answer


with open('input.txt', 'r') as f:
    total_len = 0
    recurse_len = 0
    for line in f:
        total_len += len(decompress(line.strip(), False))
        recurse_len += len(decompress(line.strip(), True))
    print("V1", total_len)
    print("V2", recurse_len)
