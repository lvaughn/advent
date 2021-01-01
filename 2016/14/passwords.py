#!/usr/bin/env python3

from hashlib import md5

salt = 'ihaygndm'

md5_cache = {}


def get_md5(idx):
    if idx not in md5_cache:
        md5_cache[idx] = md5('{}{}'.format(salt, idx).encode('ascii')).hexdigest()
    return md5_cache[idx]


def triple_digit(digest):
    for i in range(len(digest) - 2):
        if digest[i] == digest[i + 1] and digest[i] == digest[i + 2]:
            return digest[i]
    return None


index = 0
keys = []
while len(keys) <= 64:
    digest = get_md5(index)
    trip = triple_digit(digest)
    if trip is not None:
        looking_for = trip * 5
        for i in range(1, 1001):
            if looking_for in get_md5(index + i):
                keys.append((index, digest))
                break
    index += 1

print(keys[63])
