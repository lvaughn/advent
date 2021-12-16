#!/usr/bin/env python3

import sys


def binary_to_int(s):
    val = 0
    for digit in s:
        val *= 2
        if digit == '1':
            val += 1
    return val


def parse_all_packets(s):
    packets = []
    while s:
        result = read_packet(s)
        if not result:
            break
        s = result[3]
        packets.append(result[:3])
    return packets


def read_packet(s):
    if len(s) < 7:
        return None
    version = binary_to_int(s[:3])
    p_type = binary_to_int(s[3:6])

    if p_type == 4:
        loc = 6
        value = 0
        while s[loc] == '1':
            value *= 16
            value += binary_to_int(s[loc+1:loc + 5])
            loc += 5
        value *= 16
        value += binary_to_int(s[loc+1:loc + 5])
        loc += 5
        return version, p_type, value, s[loc:]

    # Operation packet
    if s[6] == '0':
        packets_len = binary_to_int(s[7:22])
        sub_packets = parse_all_packets(s[22:22 + packets_len])
        return version, p_type, sub_packets, s[22 + packets_len:]
    else:
        n_sub_packets = binary_to_int(s[7:18])
        sub_packets = []
        s = s[18:]
        for _ in range(n_sub_packets):
            packet = read_packet(s)
            sub_packets.append(packet[:3])
            s = packet[3]
        return version, p_type, sub_packets, s


def evaluate(packet):
    _, p_type, data = packet[:3]
    if p_type == 0:
        args = [evaluate(p) for p in data]
        return sum(args)
    elif p_type == 1:
        value = 1
        args = [evaluate(p) for p in data]
        for x in args:
            value *= x
        return value
    elif p_type == 2:
        return min([evaluate(p) for p in data])
    elif p_type == 3:
        return max([evaluate(p) for p in data])
    elif p_type == 4:
        return data
    elif p_type == 5:
        if evaluate(data[0]) > evaluate(data[1]):
            return 1
        return 0
    elif p_type == 6:
        if evaluate(data[0]) < evaluate(data[1]):
            return 1
        return 0
    elif p_type == 7:
        if evaluate(data[0]) == evaluate(data[1]):
            return 1
        return 0
    else:
        assert False


decode = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111',
}

with open(sys.argv[1], "r") as infile:
    bits = ''
    for digit in infile.readline().lower().strip():
        bits += decode[digit]

print(f'Parsing {len(bits)} bits')
global_packet = read_packet(bits)
print(evaluate(global_packet))
