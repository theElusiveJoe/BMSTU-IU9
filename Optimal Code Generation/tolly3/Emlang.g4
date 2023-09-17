// emlang.g4
grammar Emlang;

// Tokens
OP : '+' | '-' | '*' ;
NUMBER: [0-9]+ ;
WHITESPACE: [ \r\n\t]+ -> skip ;
IDENT: [A-Za-z][A-Za-z0-9]* ;

// Rules
start : 'main' block EOF ;
block: '{' (part)* '}' ;
part : declaration | assignation | ifElseStmt | returnStmt | lolStmt | whileStmt;

declaration : 'decl' IDENT ';' ;
assignation : 'assign' IDENT expr ';' ;

expr : ident | number | pexp ;
pexp : '(' OP expr expr ')' ;
ident : IDENT ;
number : NUMBER ;

ifElseStmt : 'if' cond block1 'else' block2 ;
cond : expr;
block1 : block;
block2 : block;

whileStmt : 'while' wcond wblock ;
wblock : block ;
wcond : expr ;

returnStmt : 'return' expr ';' ;
lolStmt : 'lol' expr ';' ;