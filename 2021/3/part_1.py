#!/usr/bin/env python3


with open("input.txt", "r") as infile:
    starting = [l.strip() for l in infile]


def binary_to_int(s):
    result = 0
    for ch in s:
        result *= 2
        if ch == '1':
            result += 1
    return result


def find_o2_rating(numbers):
    loc = 0
    while len(numbers) > 1:
        n_ones = len([n for n in numbers if n[loc] == '1'])
        n_zeros = len(numbers) - n_ones
        if n_ones >= n_zeros:
            numbers = [n for n in numbers if n[loc] == '1']
        else:
            numbers = [n for n in numbers if n[loc] == '0']
        loc += 1
    return binary_to_int(numbers[0])


def find_co2_rating(numbers):
    loc = 0
    while len(numbers) > 1:
        n_ones = len([n for n in numbers if n[loc] == '1'])
        n_zeros = len(numbers) - n_ones
        if n_ones < n_zeros:
            numbers = [n for n in numbers if n[loc] == '1']
        else:
            numbers = [n for n in numbers if n[loc] == '0']
        loc += 1
    return binary_to_int(numbers[0])


print(find_co2_rating(starting), find_o2_rating(starting), find_o2_rating(starting) * find_co2_rating(starting))
