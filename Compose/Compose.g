// Compose Grammar (X.org)
// Written by Simos Xenitellis <simos.lists@googlemail.com>, 2008.
// Version 0.1

grammar Compose;

options
{
	language = Python;
	output = AST;
}

tokens
{
	COMPOSE;
	CODEPOINT;
	SEQUENCE;
	SYM;
}

compose
	: sequence+ EOF
	-> ^(COMPOSE sequence+)
	;

sequence
	: sym+ ':' DQSTRING NAME?
	-> ^(SEQUENCE sym+ ^(CODEPOINT DQSTRING NAME?))
	;

sym	
	: '<' NAME '>'
	-> ^(SYM NAME)
	;

NAME 
	: ( 'a'..'z' | 'A'..'Z' | '_' | '0'..'9' )*
        ;

WS  	
	:  
	( ' ' | '\r' | '\t' | '\u000C' | '\n') 
	{ $channel=HIDDEN; }
    	;

LINE_COMMENT
    	: 
	'#'  ~('\n' | '\r')* '\r'? '\n' 
	{ $channel=HIDDEN; }
    	;

/** Match various string types.  Note that greedy=false implies '''
 *  should make us exit loop not continue.
 */
DQSTRING
    	:   '"' str=('\\\"' | (options {greedy=false;}:~('"'))*) '"'
	;

