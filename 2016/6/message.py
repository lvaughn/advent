#!/usr/bin/env python3

from collections import Counter

characters = []
with open('input.txt', 'r') as f:
    for line in f:
        for i, ch in enumerate(line.strip()):
            while len(characters) < i+1:
                characters.append(list())
            characters[i].append(ch)

msg = ''
decoded_msg = ''
for ls in characters:
    count = Counter(ls)
    msg += count.most_common(1)[0][0]
    decoded_msg += count.most_common()[-1][0]

print(msg)
print(decoded_msg)

