grammar XKBGrammar;

options
{
	language = Python;
	output = AST;
}

tokens
{
	// attributes
	TOKEN_DEFAULT 			= 'default';
	TOKEN_HIDDEN 			= 'hidden';
	TOKEN_PARTIAL 			= 'partial';
	TOKEN_ALPHANUMERIC_KEYS 	= 'alphanumeric_keys';
	TOKEN_MODIFIER_KEYS 		= 'modifier_keys';
	TOKEN_ALTERNATE_GROUP 		= 'alternate_group';
	TOKEN_XKB_SYMBOLS 		= 'xkb_symbols';

	// Keywords
	TOKEN_INCLUDE 			= 'include';
	TOKEN_KEY_TYPE			= 'key.type';
	TOKEN_NAME 			= 'name';		
	TOKEN_KEY 			= 'key';

	// Punctuators
	LBRACKET			= '[';
	RBRACKET			= ']';
	LCURLY				= '{';
	RCURLY				= '}';
	COMMA				= ',';
	DQUOTE				= '"';
	MINUS				= '-';
	PLUS				= '+';
	SEMICOLON			= ';';
	EQUAL				= '=';
	LOWERTHAN			= '<';
	GREATERTHAN			= '>';
	// HYPHEN			= '-';
	// SPACE			= ' ';
	// UNDERSCORE			= '_';
	DOT				= '.';
	
	ATTRIBUTES;
	ATTRIBUTE;
	KEYCODE;
	INCLUDE;
	NAME;
	KEY;
	KEYTYPE;
	SECTION;
	SECTIONNAME;
}

layout 	: section* EOF!
	;
	
section
	: preamble quotedstring LCURLY sectionmaterial+ RCURLY SEMICOLON -> ^(SECTION)
 	;

preamble:	attribute_xkb+;

quotedstring
	: DQUOTE sectionname+=~(DQUOTE)+ DQUOTE -> ^(SECTIONNAME $sectionname)
	;

sectionmaterial
	: line_include 
	| line_name 
	| line_keytype 
	| line_key 
	;

// line_comment
//	:	COMMENT;

line_include
	//: KEYWORD_INCLUDE DQUOTE NAME_INCLUDE DQUOTE COMMENT*
	: TOKEN_INCLUDE quotedstring
	;

line_name
	: TOKEN_NAME LBRACKET name=NAME RBRACKET EQUAL quotedstring SEMICOLON
	;

line_keytype
	: TOKEN_KEY_TYPE LBRACKET keytype=NAME RBRACKET EQUAL DQUOTE keytypevalue=NAME DQUOTE SEMICOLON
	;
	
line_key
	: TOKEN_KEY keycode keysyms SEMICOLON
	;
	
keycode	
	: LOWERTHAN NAME GREATERTHAN -> ^(INCLUDE NAME)
	;

keysyms	
	: LCURLY LBRACKET (NAME|NAME_KEYSYM) (COMMA (NAME|NAME_KEYSYM))* RBRACKET RCURLY  
	;

attribute_xkb
	: TOKEN_DEFAULT
	| TOKEN_HIDDEN 			
	| TOKEN_PARTIAL 			
	| TOKEN_ALPHANUMERIC_KEYS 	
	| TOKEN_MODIFIER_KEYS 		
	| TOKEN_ALTERNATE_GROUP 	
	| TOKEN_XKB_SYMBOLS -> ^(ATTRIBUTES ATTRIBUTE)
	;

/*
ATTRIBUTE_XKB
	: 'default' 
	| 'hidden'
	| 'partial' 
	| 'alphanumeric_keys'
	| 'modifier_keys'
	| 'alternate_group' 
	| 'xkb_symbols'
	;
*/

NAME
	: ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'_'|'0'..'9')*
        ;

NAME_INCLUDE
	: ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'_'|'('|')'|'0'..'9')*
        ;

NAME_KEYSYM
	: ('0'..'9'|'a'..'z'|'A'..'Z')('a'..'z'|'A'..'Z'|'_'|'0'..'9')*
        ;

NAME_GROUP
	: ('0'..'9'|'a'..'z'|'A'..'Z')('a'..'z'|'A'..'Z'|'_'|'-'|'.'|'0'..'9')*
        ;

COMMENT	: '//' (~('\n'|'\r'))* 
	{ $channel = HIDDEN; }
	;

WS      :       ('\t'|' '|NEWLINE)+ 
	{ $channel=HIDDEN; }
	;

fragment NEWLINE
        :       '\r'|'\n'
	;

