import ply.lex as lex

reserved = {'exists': 'EXISTS', 'forall': 'FORALL'}

tokens = ['NUMBER', 'STRING', 'ID', 'LPAR', 'RPAR', 'AND', 'OR', 'NOT'] + list(reserved.values())

t_LPAR = r'\('
t_RPAR = r'\)'
t_OR = r'[oO][rR]'
t_AND = r'[aA][nN][dD]'
t_NOT = r'[nN][oO][tT]'
t_ignore = " \r\n\t,"


def t_NUMBER(t):
    r'[-+]?[0-9]+(\.([0-9]+)?)?'
    t.value = float(t.value)
    t.type = 'NUMBER'
    return t


def t_STRING(t):
    r'\'[_a-zA-Z0-9]*\''
    t.type = 'STRING'
    return t


def t_ID(t):
    r'[a-z][_a-zA-Z0-9]*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t


def t_error(t):
    print("error: ")
    print(t.value[0])
    raise Exception('LEX ERROR')


lexer = lex.lex()
