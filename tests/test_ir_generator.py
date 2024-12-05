from middleend.ir_generator import IRGenerator
from frontend.symbol_table import SymbolTable
from middleend.ast import Assignment, Identifier, Number

# Example AST for: x := 5
assign_node = Assignment('Assignment')
identifier_node = Identifier('Identifier', 'x')
number_node = Number('Number', 5)
assign_node.add_child(identifier_node)
assign_node.add_child(number_node)

# Symbol table (just for the sake of completeness)
symbol_table = SymbolTable()

# Generate IR
ir_generator = IRGenerator(symbol_table)
ir = ir_generator.generate(assign_node)
print(ir)
