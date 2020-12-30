#!/usr/bin/env python3

from hashlib import md5

door_id = 'cxdnnyjw'

password = ''
i = 0
while len(password) < 8:
    hash = md5('{}{}'.format(door_id, i).encode('ascii')).hexdigest()
    if hash.startswith('00000'):
        password += hash[5]
    i += 1

print(password)