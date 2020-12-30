#!/usr/bin/env python3

def has_abba(s):
    for i in range(len(s)-3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
            return True
    return False

def find_abas(s):
    for i in range(len(s)-2):
        if s[i] == s[i+2] and s[i] != s[i+1]:
            yield s[i:i+3]


def split_addr(s):
    outside = ''
    inside = ''
    while s != '':
        if s[0] == '[':
            idx = s.index(']')
            inside += '|||' + s[1:idx]
            s = s[idx + 1:]
        else:
            idx = s.find('[')
            if idx < 0:
                outside += '|||' + s
                s = ''
            else:
                outside += '|||' + s[:idx]
                s = s[idx:]
    return inside, outside

def supports_tls(s):
    inside, outside = split_addr(s)
    return has_abba(outside) and not has_abba(inside)

def supports_ssl(s):
    inside, outside = split_addr(s)
    for aba in find_abas(inside):
        target = aba[1] + aba[0] + aba[1]
        if target in outside:
            return True

n_tls = 0
n_ssl = 0
with open('input.txt', 'r') as f:
    for line in f:
        if supports_tls(line.strip()):
            n_tls += 1
        if supports_ssl(line.strip()):
            n_ssl += 1

print("tls", n_tls)
print("ssl", n_ssl)