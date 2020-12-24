#!/usr/bin/env python3

starting_pattern = '123487596'
#starting_pattern = '389125467'
size = 1000000
n_rounds = 10000000

starting_pattern = [int(n) for n in starting_pattern]
ls = [0] * (size + 1)
start = starting_pattern[0]
for i in range(len(starting_pattern)-1):
    ls[starting_pattern[i]] = starting_pattern[i+1]
last = starting_pattern[-1]
for i in range(len(starting_pattern)+1, size+1):
    ls[last] = i
    last = i
ls[last] = start

for _ in range(n_rounds):
    a = ls[start]
    b = ls[a]
    c = ls[b]
    new_start = ls[c]
    ls[start] = new_start
    insert_at = start - 1
    if insert_at == 0:
        insert_at = size
    while insert_at in [a,b,c]:
        insert_at -= 1
        if insert_at == 0:
            insert_at = size

    # Insert what we clipped
    next = ls[insert_at]
    ls[c] = next
    ls[insert_at] = a
    start = new_start

# Prepare the outputs
output = ''
pos = 1
for _ in range(len(starting_pattern)-1):
    pos = ls[pos]
    output += str(pos)

print(output)
next = ls[1]
print(next*ls[next])


