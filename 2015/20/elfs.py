#!/usr/bin/env python3

import math

TARGET = 29000000


def factors(n):
    answer = set()
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            answer.add(i)
            answer.add(n // i)
    return answer


num = 1
while True:
    s = sum(i * 10 for i in factors(num))
    if s >= TARGET:
        print("Found it! (part 1)", num)
        break
    num += 1

num = 1
while True:
    s = sum(i * 11 for i in factors(num) if num <= i * 50)
    if s >= TARGET:
        print("Found it! (part 2)", num)
        break
    num += 1
