#!/usr/bin/env python3

def sum_of_divisors(n):
    total = 0
    for i in range(1, n+1):
        if n % i == 0:
            total += i
    return total

print("Part 1:", sum_of_divisors(947))
print("Part 2:", sum_of_divisors(10551347))