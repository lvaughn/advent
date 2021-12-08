#!/usr/bin/env python3

import numpy as np
import re

with open("input.txt", "r") as infile:
    lines = [l for l in infile]

easy_nums = 0
for line in lines:
    (seq, output) = line.split('|')
    words = output.split()
    easy_nums += len([w for w in words if len(w) in [2,3,4,7]])

print(easy_nums)