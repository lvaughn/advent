#!/usr/bin/env python3


ones = [0] * 12
zeros = [0] * 12
with open("input.txt", "r") as infile:
    for line in infile:
        for i in range(12):
            if line[i] == '1':
                ones[i] += 1
            else:
                zeros[i] += 1

gamma = 0
epsilon = 0

for i in range(12):
    gamma *= 2
    epsilon *= 2
    if ones[i] > zeros[i]:
        gamma += 1
    else:
        epsilon += 1

print(gamma, epsilon, gamma*epsilon)