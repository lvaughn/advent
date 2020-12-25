#!/usr/bin/env python3

import json

def sum_numbers(data, ignore_red=False):
    if isinstance(data, list):
        total = 0
        for e in data:
            total += sum_numbers(e, ignore_red)
        return total
    elif isinstance(data, str):
        return 0
    elif isinstance(data, int):
        return data
    elif isinstance(data, dict):
        total = 0
        for key in data:
            if ignore_red and data[key] == 'red':
                return 0
            total += sum_numbers(key, ignore_red)
            total += sum_numbers(data[key], ignore_red)
        return total
    else:
        print("Unknown type", type(data))
    return 0

with open('input.txt', 'r') as f:
    data = json.load(f)

print(sum_numbers(data))
print(sum_numbers(data, True))