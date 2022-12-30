#!/usr/bin/env python3
import re
import sys

NUMBER_RE = re.compile(r'(\w+):\s+(\d+)')
OP_RE = re.compile(r'(\w+):\s+(\w+)\s+([+-/*])\s+(\w+)')
answer = 0
number_lookup = {}
op_lookup = {}
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

for l in lines:
    m = NUMBER_RE.match(l)
    if m is not None:
        number_lookup[m[1]] = m[2]
        continue
    m = OP_RE.match(l)
    if m is not None:
        if m[1] == 'root':
            op_lookup[m[1]] = ('=', m[2], m[4])
        else:
            op_lookup[m[1]] = (m[3], m[2], m[4])
    else:
        print(l)
        assert (False)

cache = {}


def make_function(s):
    if s == 'humn':
        return s
    if s in cache:
        return cache[s]
    if s in number_lookup:
        return number_lookup[s]
    assert s in op_lookup
    op, val_a, val_b = op_lookup[s]
    a = make_function(val_a)
    b = make_function(val_b)
    if op == '+':
        result = f"({a} + {b})"
    elif op == '-':
        result = f"({a} - {b})"
    elif op == '*':
        result = f"({a} * {b})"
    elif op == '/':
        result = f"({a} // {b})"
    elif op == '=':
        assert False
        # if a == b:
        #     return "Done"
        # else:
        #     return "Fail"
    else:
        print(s, op_lookup[s])
        assert False
    cache[s] = result
    return result


def has_humn(s):
    if s == 'humn':
        return True
    if s in number_lookup:
        return False
    op, a, b = op_lookup[s]
    return has_humn(a) or has_humn(b)


def solve(s, val):
    if s == 'humn':
        return val
    assert s not in number_lookup
    op, a, b = op_lookup[s]
    if has_humn(a):
        b_val = eval(make_function(b))
        if op == '+':
            return solve(a, val - b_val)
        if op == '-':
            return solve(a, val + b_val)
        if op == '*':
            return solve(a, val // b_val)
        if op == '/':
            return solve(a, val * b_val)
        print(s)
        assert False
    else:
        a_val = eval(make_function(a))
        if op == '+':
            return solve(b, val - a_val)
        if op == '-':
            return solve(b, -(val - a_val))
        if op == '*':
            return solve(b, val // a_val)
        if op == '/':
            return solve(b, a_val // val)


_, left, right = op_lookup['root']
right_fn = make_function(right)
right_val = eval(right_fn)

res = solve(left, right_val)
print("Part 2", res)
