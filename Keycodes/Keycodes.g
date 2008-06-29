// Keycodes Grammar (X.org)
// Written by Simos Xenitellis <simos.lists@googlemail.com>, 2008.
// Version 0.8

grammar Keycodes;

options
{
	language = Python;
	output = AST;
}

tokens
{
	KEYCODEDOC;
	KEYCODELIST;
	KEYCODELISTTYPE;
	KEYCODELISTOPTIONS;
	KEYCODELISTOPTS;
	KEYCODELISTNAME;
	KEYCODEMATERIAL;
	INCLUDE;
	MINIMUM;
	MAXIMUM;	
	ALIAS;
	INDICATOR;
	KEYCODE;
}

keycodedoc 		
	: keycodelist+ EOF
	-> ^(KEYCODEDOC keycodelist+)
	;
	
keycodelist 
	: keycodelisttype '{' keycodeMaterial+ '}' ';'
	-> ^(KEYCODELIST keycodelisttype ^(KEYCODEMATERIAL keycodeMaterial+))
 	;

keycodelisttype
	: KEYCODELISTOPTS+ DQSTRING
	-> ^(KEYCODELISTTYPE ^(KEYCODELISTOPTIONS KEYCODELISTOPTS+) ^(KEYCODELISTNAME DQSTRING))
	;

keycodeMaterial 
	: line_include 
	| line_minmax ';'!
	| line_alias ';'!
	| line_keycode ';'!
	| line_indicator ';'!
	;

line_include
	: 'include' DQSTRING
	-> ^(INCLUDE DQSTRING)
	;

line_minmax
	: 'minimum' '=' NAME -> ^(MINIMUM NAME)
	| 'maximum' '=' NAME -> ^(MAXIMUM NAME)
	;

line_alias
	: 'alias' '<' val+=NAME '>' '=' '<' val+=NAME '>'
	-> ^(ALIAS $val+)
	;

line_keycode
	: '<' val+=NAME '>' '=' val+=NAME
	-> ^(KEYCODE NAME+)
	;

line_indicator
	: 'indicator' NAME '=' DQSTRING
	-> ^(INDICATOR NAME DQSTRING)
	;

KEYCODELISTOPTS
	: 'default'
	| 'xkb_keycodes'
	;

NAME
	: ( 'a'..'z' | 'A'..'Z' | '_' | '0'..'9' | '+' | '-' )*
        ;

WS  	
	:  
	( ' ' | '\r' | '\t' | '\u000C' | '\n') 
	{ $channel=HIDDEN; }
    	;

COMMENT
    	:   
	'/*' .* '*/' {$channel=HIDDEN;}
    	;

LINE_COMMENT
    	: 
	('//' | '#')  ~('\n' | '\r')* '\r'? '\n' 
	{ $channel=HIDDEN; }
    	;

/** Match various string types.  Note that greedy=false implies '''
 *  should make us exit loop not continue.
 */
DQSTRING
    	:   '"' (options {greedy=false;}:~('"'))* '"'
        ;

