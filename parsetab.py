
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN B END GOTO ID INT LET NUMBER OP PRINT SEP STRING VARc : svalue : VAR\n                 | INTterm : OP value\n                | term term \n                | emptyexpr : value \n                | value terms : NUMBER LET VAR ASSIGN expr\n             | NUMBER GOTO INTs : NUMBER PRINT STRINGempty :varprint : VAR SEP VAR\n                    | varprint SEP VARs : NUMBER PRINT VAR\n             | NUMBER PRINT varprint'
    
_lr_action_items = {'NUMBER':([0,],[3,]),'$end':([1,2,8,9,10,11,15,16,17,18,19,20,21,23,24,25,],[0,-1,-10,-11,-15,-16,-2,-9,-7,-3,-13,-14,-8,-6,-5,-4,]),'LET':([3,],[4,]),'GOTO':([3,],[5,]),'PRINT':([3,],[6,]),'VAR':([4,6,12,13,14,22,],[7,10,15,19,20,15,]),'INT':([5,12,22,],[8,18,18,]),'STRING':([6,],[9,]),'ASSIGN':([7,],[12,]),'SEP':([10,11,19,20,],[13,14,-13,-14,]),'OP':([15,17,18,21,23,24,25,],[-2,22,-3,22,-6,22,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'c':([0,],[1,]),'s':([0,],[2,]),'varprint':([6,],[11,]),'expr':([12,],[16,]),'value':([12,22,],[17,25,]),'term':([17,21,24,],[21,24,24,]),'empty':([17,21,24,],[23,23,23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> c","S'",1,None,None,None),
  ('c -> s','c',1,'p_program','BasicParser.py',25),
  ('value -> VAR','value',1,'p_value','BasicParser.py',31),
  ('value -> INT','value',1,'p_value','BasicParser.py',32),
  ('term -> OP value','term',2,'p_term','BasicParser.py',40),
  ('term -> term term','term',2,'p_term','BasicParser.py',41),
  ('term -> empty','term',1,'p_term','BasicParser.py',42),
  ('expr -> value','expr',1,'p_expr','BasicParser.py',57),
  ('expr -> value term','expr',2,'p_expr','BasicParser.py',58),
  ('s -> NUMBER LET VAR ASSIGN expr','s',5,'p_statement','BasicParser.py',66),
  ('s -> NUMBER GOTO INT','s',3,'p_statement','BasicParser.py',67),
  ('s -> NUMBER PRINT STRING','s',3,'p_print_string','BasicParser.py',75),
  ('empty -> <empty>','empty',0,'p_empty','BasicParser.py',83),
  ('varprint -> VAR SEP VAR','varprint',3,'p_varprint','BasicParser.py',88),
  ('varprint -> varprint SEP VAR','varprint',3,'p_varprint','BasicParser.py',89),
  ('s -> NUMBER PRINT VAR','s',3,'p_print','BasicParser.py',103),
  ('s -> NUMBER PRINT varprint','s',3,'p_print','BasicParser.py',104),
]
