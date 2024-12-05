from parser import AssignNode, BinOpNode, NumberNode, VariableNode, IfNode
class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, node):
        if isinstance(node, AssignNode):
            self.symbol_table[node.var.name] = self.analyze(node.expr)
        elif isinstance(node, BinOpNode):
            left_type = self.analyze(node.left)
            right_type = self.analyze(node.right)
            if left_type != right_type:
                raise TypeError("Type mismatch")
            return left_type
        elif isinstance(node, NumberNode):
            return 'int'
        elif isinstance(node, VariableNode):
            if node.name not in self.symbol_table:
                raise NameError(f"Variable {node.name} not defined")
            return self.symbol_table[node.name]
        elif isinstance(node, IfNode):
            cond_type = self.analyze(node.condition)
            if cond_type != 'int':
                raise TypeError("Condition must be an integer")
            for stmt in node.then_body.statements:
                self.analyze(stmt)
            if node.else_body:
                for stmt in node.else_body.statements:
                    self.analyze(stmt)
