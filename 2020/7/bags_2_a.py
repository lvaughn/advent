#!/usr/bin/env python3

# The second problem of Advent of Code for Dec 7, 2020, but done with lex/yacc

import ply.lex as lex
import ply.yacc as yacc
from collections import defaultdict, namedtuple

# Not for lex/yacc
BagReq = namedtuple('BagReq', ['name', 'number'])
contains = defaultdict(list)

reserved = {
    'no': 'NO',
    'contain': 'CONTAIN',
    'bags': 'BAGS',
}

tokens = list(reserved.values()) + \
         [
             'NUMBER',
             'ID',
             'COMMA',
             'PERIOD',
         ]

t_COMMA = r','
t_PERIOD = r'\.'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-z]+'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    if t.value == 'bag':
        t.type = 'BAGS' # HACK
    return t


t_ignore = ' \t\n'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])


def p_rule(p):
    '''
    rule : color BAGS CONTAIN NO ID BAGS PERIOD
         | color BAGS CONTAIN bag_list PERIOD
    '''
    if p[4] != 'no':
        ls = p[4]
        color = p[1]
        while ls is not None:
            contains[color].append(BagReq(ls[0][0], ls[0][1]))
            ls = ls[1]


def p_bag_list(p):
    '''
    bag_list : bag_spec COMMA bag_list
             | bag_spec
    '''
    if len(p) == 2:
        p[0] = (p[1], None)
    else:
        p[0] = (p[1], p[3])


def p_bag_spec(p):
    '''
    bag_spec : NUMBER color BAGS
    '''
    p[0] = (p[2], p[1])


def p_color(p):
    '''
    color : ID ID
    '''
    p[0] = '{} {}'.format(p[1], p[2])


lexer = lex.lex()
parser = yacc.yacc()

with open('input.txt') as infile:
    for line in infile:
        parser.parse(line)


def find_all_contains(bag_type):
    if bag_type not in contains:
        return 0
    answer = 0
    for inner_bag in contains[bag_type]:
        # all of the bags it contains, plus the bags themselves
        answer += inner_bag.number * (find_all_contains(inner_bag.name) + 1)
    return answer


print(find_all_contains('shiny gold'))
