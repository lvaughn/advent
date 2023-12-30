#!/usr/bin/env python

def count_char(c, st):
    count = 0
    for a in st:
        if a == c:
            count += 1
    return count

with open('input.txt') as i:
    digits = i.readline().strip()

frames = []
while len(digits) > 0:
    frames.append(digits[:150])
    digits = digits[150:]

image = []
for i in range(150):
    found = False
    for f in frames:
        if f[i] != '2':
            image.append(f[i])
            found = True
            break
    if  not found:
        print("One fell through")
        image.append('0')

for r in range(6):
    s = ""
    for c in range(25):
        if image[r*25+c] == '0':
            s += " "
        else:
            s += "*" # image[r*25 + c]
    print(s)
