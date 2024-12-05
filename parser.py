import ply.yacc as yacc
from lexer import tokens

class IfNode:
    def __init__(self, condition, then_body, else_body=None):
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class NumberNode:
    def __init__(self, value):
        self.value = value

class VariableNode:
    def __init__(self, name):
        self.name = name

class AssignNode:
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr

class BlockNode:
    def __init__(self, statements):
        self.statements = statements

# Grammar rules
def p_program(p):
    '''program : block'''
    p[0] = p[1]

def p_block(p):
    '''block : LBRACE statements RBRACE'''
    p[0] = BlockNode(p[2])

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement_assign(p):
    '''statement : IDENTIFIER ASSIGN expression SEMICOLON'''
    p[0] = AssignNode(VariableNode(p[1]), p[3])

def p_statement_if(p):
    '''statement : IF LPAREN expression RPAREN block ELSE block
                 | IF LPAREN expression RPAREN block'''
    if len(p) == 8:
        p[0] = IfNode(p[3], p[5], p[7])
    else:
        p[0] = IfNode(p[3], p[5])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression'''
    p[0] = BinOpNode(p[1], p[2], p[3])

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = NumberNode(p[1])

def p_expression_variable(p):
    '''expression : IDENTIFIER'''
    p[0] = VariableNode(p[1])

def p_error(p):
    print(f"Syntax error at {p.value}")

# Build parser
parser = yacc.yacc()
