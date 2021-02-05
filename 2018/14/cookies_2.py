#!/usr/bin/env python3

target = '236021'
last_digit = int(target[-1])

pos_1 = 0
pos_2 = 1

values = [3, 7]
while True:
    new_values = [int(d) for d in str(values[pos_1] + values[pos_2])]
    values.extend(new_values)
    pos_1 = (pos_1 + 1 + values[pos_1]) % len(values)
    pos_2 = (pos_2 + 1 + values[pos_2]) % len(values)

    if last_digit in values[-3:]:
        s = ''.join(str(d) for d in values[-8:])
        if target in s:
            print("Number before:", ''.join(str(d) for d in values).index(target))
            break
