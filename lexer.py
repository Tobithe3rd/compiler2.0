import ply.lex as lex

# Token types
tokens = [
    'NUMBER', 'IDENTIFIER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LT', 'GT', 'LE', 'GE', 'EQ', 'NE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'ASSIGN', 'SEMICOLON', 'IF', 'ELSE'
]

# Regular expressions for tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ASSIGN = r'='
t_SEMICOLON = r';'

# Keywords
reserved = {
    'if': 'IF',
    'else': 'ELSE',
}

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignore whitespace
t_ignore = ' \t'

# Ignore comments
def t_comment(t):
    r'//.*'
    pass

# Error handling
def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()
