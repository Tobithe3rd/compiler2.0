import unittest
from frontend.parser import Parser, ParserError
from frontend.lexer import tokenize
from frontend.symbol_table import SymbolTable

class TestSymbolTable(unittest.TestCase):

    def test_symbol_redefinition(self):
        code = '''
        def add(a, b):
            return a + b;
        
        def add(a, b):
            return a + b;
        '''
        
        # Tokenize and parse the code
        tokens = tokenize(code)
        parser = Parser(tokens)
        
        with self.assertRaises(ParserError) as context:
            parser.parse()
        
        self.assertTrue("Function 'add' already defined." in str(context.exception))

if __name__ == "__main__":
    unittest.main()
