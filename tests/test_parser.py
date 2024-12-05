from frontend.lexer import Lexer
from frontend.parser import Parser

# Initialize the lexer and parser
lexer = Lexer()
parser = Parser()

# Define a test input (source code) string
source_code = """
print("Hello, World!")
x = 5 + 3 * 2
if x > 10:
    print("Greater than 10")
else:
    print("Less than or equal to 10")
"""

# Tokenize the source code
tokens = lexer.tokenize(source_code)

# Print the tokens to ensure correct tokenization
print("Tokens:")
for token in tokens:
    print(f"{token.type}: {token.value}")

# Parse the source code
ast = parser.parse(source_code)

# Print the resulting Abstract Syntax Tree (AST)
print("\nAbstract Syntax Tree (AST):")
print(ast)
