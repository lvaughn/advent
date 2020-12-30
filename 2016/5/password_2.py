#!/usr/bin/env python3

from hashlib import md5

door_id = 'cxdnnyjw'

password = '________'
i = 0
while '_' in password:
    hash = md5('{}{}'.format(door_id, i).encode('ascii')).hexdigest()
    if hash.startswith('00000'):
        loc = int(hash[5], base=16)
        if loc < 8 and password[loc] == '_':
            password = password[:loc] + hash[6] + password[loc+1:]
            print(password)
    i += 1

print(password)