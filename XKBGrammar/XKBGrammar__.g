lexer grammar XKBGrammar;
options {
  language=Python;

}

T31 : '"' ;
T32 : '{' ;
T33 : ';' ;
T34 : '}' ;
T35 : 'include' ;
T36 : 'name' ;
T37 : '[' ;
T38 : ']' ;
T39 : '=' ;
T40 : 'key.type' ;
T41 : 'key' ;
T42 : '<' ;
T43 : '>' ;
T44 : ',' ;
T45 : 'default' ;
T46 : 'hidden' ;
T47 : 'partial' ;
T48 : 'alphanumeric_keys' ;
T49 : 'alternate_group' ;
T50 : 'xkb_symbols' ;

// $ANTLR src "XKBGrammar.g" 123
NAME
	: ('a'..'z' | 'A'..'Z' | '_' | '-' | '(' | ')' | '0'..'9')*
        ;

// Comments are currently ignored.
// $ANTLR src "XKBGrammar.g" 128
WS  	
	:  
	( ' ' | '\r' | '\t' | '\u000C' | '\n') 
	{ $channel=HIDDEN; }
    	;

// $ANTLR src "XKBGrammar.g" 134
COMMENT
    	:   
	'/*' .* '*/' {$channel=HIDDEN;}
    	;

// $ANTLR src "XKBGrammar.g" 139
LINE_COMMENT
    	: 
	'//' ~('\n' | '\r')* '\r'? '\n' 
	{ $channel=HIDDEN; }
    	;

