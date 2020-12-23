#!/usr/bin/env python3

def processString(s):
    answer = ''
    if s.startswith('"'):
        s = s[1:]
    if s.endswith('"'):
        s = s[:-1]
    while len(s) > 0:
        idx = s.find('\\')
        if idx == -1:
            answer += s
            s = ''
        else:
            answer += s[:idx]
            if s[idx + 1] == '"' or s[idx + 1] == '\\':
                answer += s[idx + 1]
                s = s[idx + 2:]
            elif s[idx + 1] == 'x':
                answer += 'X'
                s = s[idx + 4:]
    return answer


def encodeString(s):
    answer = '"'
    for c in s:
        if c == '"':
            answer += '\\"'
        elif c == '\\':
            answer += '\\\\'
        else:
            answer += c
    return answer + '"'


with open('input.txt', 'r') as f:
    raw_total = 0
    net_total = 0
    encoded_total = 0
    for line in f:
        line = line.strip()
        raw_total += len(line)
        net_total += len(processString(line))
        encoded_total += len(encodeString(line))
    print(raw_total - net_total)
    print(encoded_total - raw_total)
