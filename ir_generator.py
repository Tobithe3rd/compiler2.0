from llvmlite import ir
from parser import NumberNode, BinOpNode

class CodeGenerator:
    def __init__(self):
        self.module = ir.Module(name="main")
        self.module.triple = "x86_64-pc-windows-msvc"
        self.builder = None
        self.function = None
    
    def create_main_function(self):
        # Define the main function
        func_type = ir.FunctionType(ir.IntType(32), [])
        self.function = ir.Function(self.module, func_type, name="main")
        block = self.function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

    def finish_function(self):
        # Return 0 at the end of the main function
        self.builder.ret(ir.Constant(ir.IntType(32), 0))

    def generate_number(self, value):
        return ir.Constant(ir.IntType(32), value)

    def generate_binop(self, left, op, right):
        if op == '+':
            return self.builder.add(left, right, name="addtmp")
        elif op == '-':
            return self.builder.sub(left, right, name="subtmp")
        elif op == '*':
            return self.builder.mul(left, right, name="multmp")
        elif op == '/':
            return self.builder.sdiv(left, right, name="divtmp")

    def generate(self, node):
        if isinstance(node, NumberNode):
            return self.generate_number(node.value)
        elif isinstance(node, BinOpNode):
            left = self.generate(node.left)
            right = self.generate(node.right)
            return self.generate_binop(left, node.op, right)

# Example: Create LLVM IR
generator = CodeGenerator()
generator.create_main_function()
# Example expression: 3 + 5
result = generator.generate(BinOpNode(NumberNode(3), '+', NumberNode(5)))
generator.finish_function()

print(generator.module)
