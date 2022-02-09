import ply.lex as lex

reserved = {'exists': 'EXISTS', 'forall': 'FORALL'}

tokens = ['NUMBER', 'STRING', 'VARIABLE', 'LPAR', 'RPAR', 'AND', 'OR', 'NOT',  'PLUS', 'MINUS', 'MULT', 'DIV', 'LESS', 'GREAT',
'LOEQ', 'GOEQ', 'EQUAL', 'NEQUAL', 'TRUE', "FALSE"] + list(reserved.values())

t_LPAR = r'\('
t_RPAR = r'\)'
t_OR = r'[oO][rR]'
t_AND = r'[aA][nN][dD]'
t_NOT = r'[nN][oO][tT]'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_LESS = r'\<'
t_GREAT = r'\>'
t_GOEQ = r'\>\='
t_LOEQ = r'\<\='
t_EQUAL = r'\='
t_NEQUAL = r'\<\>'
t_TRUE = r'[tT][rR][uU][eE]'
t_FALSE = r'[fF][aA][lL][sS][eE]'
t_ignore = " \r\n\t,"

def t_NUMBER(t):
    r'[-+]?[0-9]+(\.([0-9]+)?)?'
    t.value = float(t.value)
    t.type = 'NUMBER'
    return t


def t_STRING(t):
    r'\'[_a-zA-Z0-9]*\''
    t.type = 'STRING'
    t.value = t.value[1:int(len(t.value))-1]
    return t


def t_VARIABLE(t):
    r'[a-z][_a-zA-Z0-9]*'
    t.type = 'VARIABLE'
    return t


def t_error(t):
    print("error: ")
    print(t.value[0])
    raise Exception('LEX ERROR')


lexer = lex.lex()
