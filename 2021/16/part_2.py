#!/usr/bin/env python3

from pprint import pprint
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
    type = binary_to_int(s[3:6])

    if type == 4:
        loc = 6
        value = 0
        while s[loc] == '1':
            value *= 16
            value += binary_to_int(s[loc+1:loc + 5])
            loc += 5
        value *= 16
        value += binary_to_int(s[loc+1:loc + 5])
        loc += 5
        return version, type, value, s[loc:]

    # Operation packet
    if s[6] == '0':
        packets_len = binary_to_int(s[7:22])
        sub_packets = parse_all_packets(s[22:22 + packets_len])
        return version, type, sub_packets, s[22 + packets_len:]
    else:
        n_sub_packets = binary_to_int(s[7:18])
        sub_packets = []
        s = s[18:]
        for _ in range(n_sub_packets):
            packet = read_packet(s)
            sub_packets.append(packet[:3])
            s = packet[3]
        return version, type, sub_packets, s


def sum_version(packet):
    total = 0
    ver, type, data = packet[:3]
    total += ver
    if type != 4:
        for sub_packet in data:
            total += sum_version(sub_packet)
    return total


def evaluate(packet):
    _, type, data = packet[:3]
    if type == 0:
        args = [evaluate(p) for p in data]
        return sum(args)
    elif type == 1:
        value = 1
        args = [evaluate(p) for p in data]
        for x in args:
            value *= x
        return value
    elif type == 2:
        return min([evaluate(p) for p in data])
    elif type == 3:
        return max([evaluate(p) for p in data])
    elif type == 4:
        return data
    elif type == 5:
        assert (len(data) == 2)
        if evaluate(data[0]) > evaluate(data[1]):
            return 1
        return 0
    elif type == 6:
        assert (len(data) == 2)
        if evaluate(data[0]) < evaluate(data[1]):
            return 1
        return 0
    elif type == 7:
        assert (len(data) == 2)
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
    hex = infile.readline().lower().strip()
    input = ''
    for digit in hex:
        input += decode[digit]

print(f'Parsing {len(input)} bits')
packet = read_packet(input)
print(evaluate(packet))
