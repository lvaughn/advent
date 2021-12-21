#!/usr/bin/env python

import numpy as np

EXTRA = 5

def decode_char(ch):
    if ch == '#':
        return 1
    return 0


def decode_line(line):
    return [decode_char(ch) for ch in line]


def enhance_image(img, decode_array):
    result = np.zeros(img.shape, dtype=int)
    scratch = np.zeros((img.shape[0] + 2, img.shape[1] + 2), dtype=int)
    scratch += img[0,0]
    scratch[1:-1, 1:-1] = img
    for r in range(result.shape[0]):
        for c in range(result.shape[1]):
            value = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    value *= 2
                    value += scratch[r + dr, c + dc]
            result[r, c] = decode_array[value]
    return result

def print_image(img):
    for r in range(img.shape[0]):
        line = ''
        for c in range(img.shape[1]):
            if img[r, c] == 1:
                line += '#'
            else:
                line += '.'
        print(line)

with open("input.txt", "r") as infile:
    lines = [l.strip() for l in infile]

decoder = decode_line(lines[0])
assert(len(decoder) == 512)
input_image = np.array([decode_line(line) for line in lines[2:]], dtype=int)
image = np.zeros([a + 2 * EXTRA for a in input_image.shape], dtype=int)
image[EXTRA: -EXTRA, EXTRA: -EXTRA] = input_image

image_2 = enhance_image(image, decoder)
image_3 = enhance_image(image_2, decoder)
print("Final Image")
print_image(image_3[:, :])
print("Part 1:", sum(sum(image_3[:, :])))
