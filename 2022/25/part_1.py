#!/usr/bin/env python3
import sys

values = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}


def snafu_to_int(s):
    acc = 0
    power = 1
    for ch in reversed(s):
        acc += power * values[ch]
        power *= 5
    return acc


def int_to_snafu(val):
    result = ""
    while val != 0:
        remainder = val % 5
        if remainder < 3:
            result = str(remainder) + result
            val = val // 5
        else:
            if remainder == 4:
                result = "-" + result
                val = (val + 1) // 5
            elif remainder == 3:
                result = "=" + result
                val = (val + 2) // 5
            else:
                assert False
    return result


with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]

total = sum(snafu_to_int(s) for s in lines)
print("Part 1", total, int_to_snafu(total))
