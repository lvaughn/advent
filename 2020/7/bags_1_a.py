#!/usr/bin/env python3

# The first problem of Advent of Code for Dec 7, 2020, but done with lex/yacc

import ply.lex as lex
import ply.yacc as yacc
from collections import defaultdict

# Not for lex/yacc
contained_by = defaultdict(list)

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
            contained_by[ls[0][0]].append(color)
            ls = ls[1]  # AKA cdr :now_there_a_name...gif:


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


def find_all_contains(bag_type, seen):
    for b in contained_by[bag_type]:
        if b not in seen:
            seen.add(b)
            find_all_contains(b, seen)
    return seen


print(len(find_all_contains('shiny gold', set())))

