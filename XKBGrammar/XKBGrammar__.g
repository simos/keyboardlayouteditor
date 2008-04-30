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

// $ANTLR src "XKBGrammar.g" 123
NAME
	: ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'_'|'0'..'9')*
        ;

// $ANTLR src "XKBGrammar.g" 127
NAME_INCLUDE
	: ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'_'|'('|')'|'0'..'9')*
        ;

// $ANTLR src "XKBGrammar.g" 131
NAME_KEYSYM
	: ('0'..'9'|'a'..'z'|'A'..'Z')('a'..'z'|'A'..'Z'|'_'|'0'..'9')*
        ;

// $ANTLR src "XKBGrammar.g" 135
NAME_GROUP
	: ('0'..'9'|'a'..'z'|'A'..'Z')('a'..'z'|'A'..'Z'|'_'|'-'|'.'|'0'..'9')*
        ;

// $ANTLR src "XKBGrammar.g" 139
COMMENT	: '//' (~('\n'|'\r'))* 
	{ $channel = HIDDEN; }
	;

// $ANTLR src "XKBGrammar.g" 143
WS      :       ('\t'|' '|NEWLINE)+ 
	{ $channel=HIDDEN; }
	;

// $ANTLR src "XKBGrammar.g" 147
fragment NEWLINE
        :       '\r'|'\n'
	;

