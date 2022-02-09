from ast import Subscript
import ply.yacc as yacc
from WFFLexer import tokens


def p_wffstart(p):
    'wffstart : start'
    p[0] = p[1]


def p_start_1(p):
    'start : wff'
    p[0] = ['wff', p[1]]


def p_start_2(p):
    'start : list'
    p[0] = ['list', p[1]]


def p_start_3(p):
    'start : bool'
    p[0] = ['bool', p[1]]

# wffs

def p_wff_1(p):
    'wff : NUMBER'
    p[0] = ['num', float(str(p[1]))]


def p_wff_2(p):
    'wff : LPAR PLUS wff wff RPAR'
    p[0] = ['+', p[3], p[4]]


def p_wff_3(p):
    'wff : LPAR MINUS wff wff RPAR'
    p[0] = ['-', p[3], p[4]]


def p_wff_4(p):
    'wff : LPAR MULT wff wff RPAR'
    p[0] = ['*', p[3], p[4]]


def p_wff_5(p):
    'wff : LPAR DIV wff wff RPAR'
    p[0] = ['/', p[3], p[4]]


def p_wff_6(p):
    'wff : STRING'
    p[0] = ['string', p[1]]


def p_wff_7(p):
    'wff : VARIABLE'
    p[0] = ['variable', p[1]]
# booleans

def p_bool_1(p):
    'bool : LPAR LESS wff wff RPAR'
    p[0] = ['<', p[3], p[4]]


def p_bool_2(p):
    'bool : LPAR OR bool bool RPAR'
    p[0] = ['or', p[3], p[4]]


def p_bool_3(p):
    'bool : LPAR AND bool bool RPAR'
    p[0] = ['and', p[3], p[4]]


def p_bool_4(p):
    'bool : LPAR GREAT wff wff RPAR'
    p[0] = ['>', p[3], p[4]]


def p_bool_5(p):
    'bool : LPAR GOEQ wff wff RPAR'
    p[0] = ['>=', p[3], p[4]]


def p_bool_6(p):
    'bool : LPAR LOEQ wff wff RPAR'
    p[0] = ['<=', p[3], p[4]]

def p_bool_7(p):
    'bool : LPAR NEQUAL wff wff RPAR'
    p[0] = ['<>', p[3], p[4]]

def p_bool_8(p):
    'bool : LPAR NOT bool RPAR'
    p[0] = ['not', p[3]]


def p_bool_9(p):
    'bool : TRUE'
    p[0] = ['true']


def p_bool_10(p):
    'bool : FALSE'
    p[0] = ['false']


def p_list_1(p):
  'list : LPAR array RPAR'
  p[0] = ['array', p[2]]


#array definition
def p_array_1(p):
  'array :'
  p[0] = []

def p_array_2(p):
  'array : array wff'
  p[0] = p[1] + [p[2]]

#
# def p_array_3(p):
#   'array : array STRING'
#   p[0] = p[1] + [p[2]]
#
#
# def p_array_4(p):
#   'array : array VARIABLE'
#   p[0] = p[1] + [p[2]]
#
# def p_variable_1(p):
#     'variable : VARIABLE'
#     print(1)
#     p[0] = ['variable', p[1]]

def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()
