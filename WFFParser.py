import ply.yacc as yacc
from WFFLexer import tokens


def p_starter(p):
    'starter : wff'
    p[0] = p[1]


def p_wff_1(p):
    'wff : NUMBER'
    p[0] = ['num', p[1]]


def p_wff_2(p):
    'wff : STRING'
    p[0] = ['string', p[1]]


def p_wff_3(p):
    'wff : ID'
    p[0] = ['id', p[1]]


def p_wff_4(p):
    'wff : NUMBER'
    p[0] = ['num', p[1]]

#primary priority

def p_wff_5(p):
    'wff : wff OR wff'
    p[0] = ['or', p[1], p[3]]


def p_wff_6(p):
    'wff : wff AND wff'
    p[0] = ['and', p[1], p[3]]


#secondary priority


def p_expression_1(p):
    'expression : wff'
    p[0] = [p[1]]


def p_expression_2(p):
    'expression : NOT expression'
    p[0] = ['not', p[2]]


def p_wff_7(p):
    'wff : expression'
    p[0] = [p[1]]
    