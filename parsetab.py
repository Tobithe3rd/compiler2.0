
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN DIVIDE ELSE EQ GE GT IDENTIFIER IF LBRACE LE LPAREN LT MINUS NE NUMBER PLUS RBRACE RPAREN SEMICOLON TIMESprogram : blockblock : LBRACE statements RBRACEstatements : statements statement\n                  | statementstatement : IDENTIFIER ASSIGN expression SEMICOLONstatement : IF LPAREN expression RPAREN block ELSE block\n                 | IF LPAREN expression RPAREN blockexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression LT expression\n                  | expression GT expression\n                  | expression LE expression\n                  | expression GE expression\n                  | expression EQ expression\n                  | expression NE expressionexpression : NUMBERexpression : IDENTIFIER'
    
_lr_action_items = {'LBRACE':([0,27,39,],[3,3,3,]),'$end':([1,2,8,],[0,-1,-2,]),'IDENTIFIER':([3,4,5,8,9,10,11,16,17,18,19,20,21,22,23,24,25,26,38,40,],[6,6,-4,-2,-3,12,12,-5,12,12,12,12,12,12,12,12,12,12,-7,-6,]),'IF':([3,4,5,8,9,16,38,40,],[7,7,-4,-2,-3,-5,-7,-6,]),'RBRACE':([4,5,8,9,16,38,40,],[8,-4,-2,-3,-5,-7,-6,]),'ASSIGN':([6,],[10,]),'LPAREN':([7,],[11,]),'ELSE':([8,38,],[-2,39,]),'NUMBER':([10,11,17,18,19,20,21,22,23,24,25,26,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'SEMICOLON':([12,13,14,28,29,30,31,32,33,34,35,36,37,],[-19,16,-18,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,]),'PLUS':([12,13,14,15,28,29,30,31,32,33,34,35,36,37,],[-19,17,-18,17,17,17,17,17,17,17,17,17,17,17,]),'MINUS':([12,13,14,15,28,29,30,31,32,33,34,35,36,37,],[-19,18,-18,18,18,18,18,18,18,18,18,18,18,18,]),'TIMES':([12,13,14,15,28,29,30,31,32,33,34,35,36,37,],[-19,19,-18,19,19,19,19,19,19,19,19,19,19,19,]),'DIVIDE':([12,13,14,15,28,29,30,31,32,33,34,35,36,37,],[-19,20,-18,20,20,20,20,20,20,20,20,20,20,20,]),'LT':([12,13,14,15,28,29,30,31,32,33,34,35,36,37,],[-19,21,-18,21,21,21,21,21,21,21,21,21,21,21,]),'GT':([12,13,14,15,28,29,30,31,32,33,34,35,36,37,],[-19,22,-18,22,22,22,22,22,22,22,22,22,22,22,]),'LE':([12,13,14,15,28,29,30,31,32,33,34,35,36,37,],[-19,23,-18,23,23,23,23,23,23,23,23,23,23,23,]),'GE':([12,13,14,15,28,29,30,31,32,33,34,35,36,37,],[-19,24,-18,24,24,24,24,24,24,24,24,24,24,24,]),'EQ':([12,13,14,15,28,29,30,31,32,33,34,35,36,37,],[-19,25,-18,25,25,25,25,25,25,25,25,25,25,25,]),'NE':([12,13,14,15,28,29,30,31,32,33,34,35,36,37,],[-19,26,-18,26,26,26,26,26,26,26,26,26,26,26,]),'RPAREN':([12,14,15,28,29,30,31,32,33,34,35,36,37,],[-19,-18,27,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'block':([0,27,39,],[2,38,40,]),'statements':([3,],[4,]),'statement':([3,4,],[5,9,]),'expression':([10,11,17,18,19,20,21,22,23,24,25,26,],[13,15,28,29,30,31,32,33,34,35,36,37,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> block','program',1,'p_program','parser.py',35),
  ('block -> LBRACE statements RBRACE','block',3,'p_block','parser.py',39),
  ('statements -> statements statement','statements',2,'p_statements','parser.py',43),
  ('statements -> statement','statements',1,'p_statements','parser.py',44),
  ('statement -> IDENTIFIER ASSIGN expression SEMICOLON','statement',4,'p_statement_assign','parser.py',51),
  ('statement -> IF LPAREN expression RPAREN block ELSE block','statement',7,'p_statement_if','parser.py',55),
  ('statement -> IF LPAREN expression RPAREN block','statement',5,'p_statement_if','parser.py',56),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',63),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',64),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',65),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',66),
  ('expression -> expression LT expression','expression',3,'p_expression_binop','parser.py',67),
  ('expression -> expression GT expression','expression',3,'p_expression_binop','parser.py',68),
  ('expression -> expression LE expression','expression',3,'p_expression_binop','parser.py',69),
  ('expression -> expression GE expression','expression',3,'p_expression_binop','parser.py',70),
  ('expression -> expression EQ expression','expression',3,'p_expression_binop','parser.py',71),
  ('expression -> expression NE expression','expression',3,'p_expression_binop','parser.py',72),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',76),
  ('expression -> IDENTIFIER','expression',1,'p_expression_variable','parser.py',80),
]
