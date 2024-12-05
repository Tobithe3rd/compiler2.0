# tests/test_lexer.py

import pytest
from frontend.lexer import Lexer, Token
from utilities.error_handling import LexerError

def test_lexer_basic():
    code = "x = 10 + 5;"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    assert len(tokens) == 7  # IDENTIFIER, ASSIGN, NUMBER, PLUS, NUMBER, SEMI

    expected_types = ['IDENTIFIER', 'ASSIGN', 'NUMBER', 'PLUS', 'NUMBER', 'SEMI']
    for token, expected in zip(tokens, expected_types):
        assert token.type == expected

def test_lexer_invalid_character():
    code = "x = 10 @;"
    lexer = Lexer(code)
    with pytest.raises(LexerError) as excinfo:
        lexer.tokenize()
    assert "@' at line 1" in str(excinfo.value)
