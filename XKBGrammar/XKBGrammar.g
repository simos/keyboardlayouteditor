// XKB Grammar (X.org)
// Written by Simos Xenitellis <simos.lists@googlemail.com>, 2008.
// Version 0.2

grammar XKBGrammar;

options
{
	language = Python;
	output = AST;
}

tokens
{
	// attributes [TODO: check terminolody]
	TOKEN_DEFAULT 			= 'default';
	TOKEN_HIDDEN 			= 'hidden';
	TOKEN_PARTIAL 			= 'partial';
	TOKEN_ALPHANUMERIC_KEYS 	= 'alphanumeric_keys';
	TOKEN_MODIFIER_KEYS 		= 'modifier_keys';
	TOKEN_ALTERNATE_GROUP 		= 'alternate_group';
	TOKEN_XKB_SYMBOLS 		= 'xkb_symbols';

	// Keywords [TODO: check terminology]
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
	DOT				= '.';
	// HYPHEN			= '-';
	// SPACE				= ' ';
	// UNDERSCORE			= '_';
	
	// Tokens for tree.
	ATTRIBUTES;
	ATTRIBUTE;
	INCLUDE;
	KEY;
	KEYTYPE;
	SECTION;
	SECTIONNAME;
}

// We cover XKB files that look like
//
// // comments can appear here.
// one of more modifiers "mysectionname"
// {
//   // comments can appear here.
//   include "somename"                 // comments can also appear here.
//   name[somestring] = "sometext";
//   key.type[someotherstring] = "someothertext";
//   key <someotherstring> { [ somesymbol, someothersymbol, ... uptoEightSymbols ] };
//   modifier_map someothertext { somesymbol, someothersymbol, ... uptoEightSymbols };
//   // can also have multiples of the above.
// };
//
// // can have several sections as above.

layout 		: section* EOF! 
		;
	
section 	: preamble sectionmaterial 
		{ print '}' }
		-> ^(SECTION)
 		;

preamble 	: attribute_xkb+ sectionname=quotedstring
		{ print '\%(sectionname)s {' \% { "sectionname": $sectionname.text } }
		;

quotedstring returns [value]
        	: DQUOTE sectionname+=~(DQUOTE)+ DQUOTE 
                {       
                        qstring = ['"']
                        for elem in $sectionname:
                                qstring.append(elem.getText())
                        qstring.append('"')
                        $value = "".join(qstring)
                }
        	;

sectionmaterial : LCURLY (line_include 
		| line_name 
		| line_keytype 
		| line_key 
		)+ RCURLY SEMICOLON
		;

line_include
	: TOKEN_INCLUDE include=quotedstring 
	{ print '\tinclude \%(inc)s' \% { "inc": $include.text } }
	;

line_name
	: TOKEN_NAME LBRACKET name=NAME RBRACKET EQUAL nameval=quotedstring SEMICOLON
	{ print '\tname[\%(name)s] = \%(nameval)s;' \% {  "name": $name.text, "nameval": $nameval.text } }
	;

line_keytype
	: TOKEN_KEY_TYPE LBRACKET keytype=NAME RBRACKET EQUAL DQUOTE keytypevalue=NAME DQUOTE SEMICOLON
	{ print '\tkey.type[\%(kt)s] = \"\%(ktv)s\";' \% {  "kt": $keytype.text, "ktv": $keytypevalue.text } }
	;
	
line_key
	: TOKEN_KEY keycode keysyms SEMICOLON
	{ print "\tkey \%(keycode)s \%(keysyms)s ;" \% {  "keycode": $keycode.text, "keysyms": $keysyms.text } }
	;
	
keycode	
	: LOWERTHAN NAME GREATERTHAN 
	-> ^(INCLUDE NAME)
	;

keysyms	
	: LCURLY LBRACKET NAME (COMMA NAME)* RBRACKET RCURLY  
	;

// mapsyms	
//	: LCURLY LBRACKET (NAME|keycode) (COMMA (NAME|keycode))* RBRACKET RCURLY  
//	;

attribute_xkb
	: TOKEN_DEFAULT 	{ print "default", }
	| TOKEN_HIDDEN 		{ print "hidden", }
	| TOKEN_PARTIAL 	{ print "partial", }	
	| TOKEN_ALPHANUMERIC_KEYS { print "alphanumeric_keys", } 	
	| TOKEN_ALTERNATE_GROUP { print "alternate_group", }
	| TOKEN_XKB_SYMBOLS     { print "xkb_symbols", }
	-> ^(ATTRIBUTES ATTRIBUTE)
	;

fragment GENERIC_NAME
	: ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'_'|'0'..'9')
        ;

NAME
	: ('a'..'z'|'A'..'Z'|'_'|'('|')'|'0'..'9')*
        ;

// Comments are currently ignored.
COMMENT	: '//' (~('\n'|'\r'))* 
	{ $channel = HIDDEN; }
	;

WS      :       ('\t'|' '|NEWLINE)+ 
	{ $channel=HIDDEN; }
	;

fragment NEWLINE
        :       '\r'|'\n'
	;

