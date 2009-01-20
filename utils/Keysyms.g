// Keysyms Grammar (X.org)
// Written by Simos Xenitellis <simos.lists@googlemail.com>, 2008.
// Version 0.1

grammar Keysyms;

options
{
	language = Python;
	output = AST;
}

tokens
{
	ENTRY;
	KEYSYM;
	KEYSYMVALUE;
	IFDEF;
	ENDIF;
}

keysym
	: line* EOF
	-> ^(ENTRY line+)
	;

line
	: '#define' NAME NAME 	-> ^(KEYSYM NAME NAME)
	| '#ifdef' NAME		-> ^(IFDEF NAME)
	| '#endif'		-> ^(ENDIF)
	;

NAME 
	: ( 'a'..'z' | 'A'..'Z' | '_' | '0'..'9' )*
        ;

WS  	
	:  
	( ' ' | '\r' | '\t' | '\u000C' | '\n') 
	{ $channel=HIDDEN; }
    	;

ML_COMMENT
	: '/*' (options {greedy=false;} : .)* '*/' 
	{ $channel=HIDDEN; }
	;
