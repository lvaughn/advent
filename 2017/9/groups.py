#!/usr/bin/env python3

import re

with open('input.txt', 'r') as f:
    text = f.read()

# Get rid of characters after !'s
text = re.sub(r'!.', '', text)

# Get rid of the garbage
new_text = ''
garbage_removed = 0
while text != '':
    if text.startswith('<'):
        idx = text.index('>')
        garbage_removed += idx - 1
        text = text[idx+1:]
    else:
        idx = text.find('<')
        if idx < 0:
            new_text += text
            text = ''
        else:
            new_text += text[:idx]
            text = text[idx:]

# process what's left
depth = 0
score = 0
for ch in new_text:
    if ch == '{':
        depth += 1
        score += depth
    elif ch == '}':
        depth -= 1
    else:
        pass
print("Score", score)
print("Garbage removed", garbage_removed)
