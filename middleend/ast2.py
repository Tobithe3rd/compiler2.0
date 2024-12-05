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
