lexer grammar XKBGrammar;
options {
  language=Python;

}

TOKEN_DEFAULT : 'default' ;
TOKEN_HIDDEN : 'hidden' ;
TOKEN_PARTIAL : 'partial' ;
TOKEN_ALPHANUMERIC_KEYS : 'alphanumeric_keys' ;
TOKEN_MODIFIER_KEYS : 'modifier_keys' ;
TOKEN_ALTERNATE_GROUP : 'alternate_group' ;
TOKEN_XKB_SYMBOLS : 'xkb_symbols' ;
TOKEN_INCLUDE : 'include' ;
TOKEN_KEY_TYPE : 'key.type' ;
TOKEN_NAME : 'name' ;
TOKEN_KEY : 'key' ;
LBRACKET : '[' ;
RBRACKET : ']' ;
LCURLY : '{' ;
RCURLY : '}' ;
COMMA : ',' ;
DQUOTE : '"' ;
MINUS : '-' ;
PLUS : '+' ;
SEMICOLON : ';' ;
EQUAL : '=' ;
LOWERTHAN : '<' ;
GREATERTHAN : '>' ;
DOT : '.' ;

// $ANTLR src "XKBGrammar.g" 164
fragment GENERIC_NAME
	: ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'_'|'0'..'9')
        ;

// $ANTLR src "XKBGrammar.g" 168
NAME
	: ('a'..'z'|'A'..'Z'|'_'|'('|')'|'0'..'9')*
        ;

// Comments are currently ignored.
// $ANTLR src "XKBGrammar.g" 173
COMMENT	
	: '//' (~('\n'|'\r'))* 
	{ $channel = HIDDEN; }
	;

// $ANTLR src "XKBGrammar.g" 178
WS      :       ('\t'|' '|NEWLINE)+ 
	{ $channel=HIDDEN; }
	;

// $ANTLR src "XKBGrammar.g" 182
fragment NEWLINE
        :       '\r'|'\n'
	;

