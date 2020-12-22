#!/usr/bin/env python3

import hashlib

key = 'iwrupvqb'
i = 1
while True:
    s = '{}{}'.format(key, i)
    h = hashlib.md5(s.encode('ascii')).hexdigest()
    if h.startswith('00000'):
        print("Answer for 5 zeros is {} ({})".format(i, s))
        break
    i += 1

i = 1
while True:
    s = '{}{}'.format(key, i)
    h = hashlib.md5(s.encode('ascii')).hexdigest()
    if h.startswith('000000'):
        print("Answer for six zeros is {} ({})".format(i, s))
        break
    i += 1