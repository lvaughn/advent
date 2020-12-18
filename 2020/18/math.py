#!/usr/bin/env python3
import ply.lex as lex
import ply.yacc as yacc

# Note: Basics of lex/yacc cribbed from David Beazly (https://www.dabeaz.com/ply/ply.html)
tokens = (
    'NUMBER',
    'PLUS',
    'TIMES',
    'LPAREN',
    'RPAREN',
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_TIMES = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

    # Error handling rule


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


t_ignore = ' \t'

lexer = lex.lex()


def p_expression_plus(p):
    'expression : expression PLUS factor'
    # print("Plus", p[1], p[3])
    p[0] = p[1] + p[3]


def p_term_times(p):
    'expression : expression TIMES factor'
    p[0] = p[1] * p[3]


def p_expression_term(p):
    'expression : factor'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


# Build the parser
parser = yacc.yacc()


def eval_line(l):
    return parser.parse(l)


# print(eval_line('1 + 2 * 3 + 4 * 5 + 6'))
# print(eval_line('1 + (2 * 3) + (4 * (5 + 6))'))

with open('input.txt', 'r') as infile:
    total = 0
    for line in infile:
        total += eval_line(line.strip())
    print(total)
