from code_generator import CodeGenerator
from parser import BinOpNode, NumberNode
from assembly_writter import generate_assembly

# Create an instance of CodeGenerator
generator = CodeGenerator()

# Step 1: Create the main function
generator.create_main_function()

# Step 2: Generate an expression (e.g., 3 + 5)
result = generator.generate(BinOpNode(NumberNode(3), '+', NumberNode(5)))

# Step 3: Finish the function
generator.finish_function()

# Print the generated LLVM IR
print(generator.module)

# Save LLVM IR to a file
with open("output.ll", "w") as f:
    f.write(str(generator.module))

print("LLVM IR saved to output.ll")


llvm_ir_file = "output.ll"  # Example LLVM IR file
output_asm_file = "output.asm"

generate_assembly(llvm_ir_file, output_asm_file)
