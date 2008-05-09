// XKB Grammar (X.org)
// Written by Simos Xenitellis <simos.lists@googlemail.com>, 2008.
// Version 0.3

grammar XKBGrammar;

options
{
	language = Python;
	output = AST;
}

tokens
{
	// Map options
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
	MAPTYPE;
	ATTRIBUTES;
	ATTRIBUTE;
	INCLUDE;
	KEY;
	KEYTYPE;
	KEYCODE;
	SECTION;
	SECTIONNAME;
}

// We cover XKB symbol files that look like
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

layout 		
	: section+
	;
	
section 
	: mapType sectionmaterial 
	{ print '}' }
 	;

mapType
	: mapOptions+ sectionname=quotedstring
	{ print '\%(sectionname)s {' \% { "sectionname": $sectionname.text } }
	-> ^(MAPTYPE mapOptions+ $sectionname)
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

sectionmaterial 
	: lc=LCURLY (line_include 
	| line_name 
	| line_keytype 
	| line_key 
	)+ RCURLY SEMICOLON
	-> ^(SECTION)
	;

line_include
	: TOKEN_INCLUDE include=quotedstring 
	{ print '\tinclude \%(inc)s' \% { "inc": $include.text } }
	-> ^(TOKEN_INCLUDE $include)
	;

line_name
	: TOKEN_NAME LBRACKET name=NAME RBRACKET EQUAL nameval=quotedstring SEMICOLON
	{ print '\tname[\%(name)s] = \%(nameval)s;' \% {  "name": $name.text, "nameval": $nameval.text } }
	-> ^(TOKEN_NAME $name $nameval)
	;

line_keytype
	: TOKEN_KEY_TYPE LBRACKET keytype=NAME RBRACKET EQUAL DQUOTE keytypevalue=NAME DQUOTE SEMICOLON
	{ print '\tkey.type[\%(kt)s] = \"\%(ktv)s\";' \% {  "kt": $keytype.text, "ktv": $keytypevalue.text } }
	-> ^(TOKEN_KEY_TYPE $keytype $keytypevalue)
	;
	
line_key
	: TOKEN_KEY keycode keysyms SEMICOLON
	{ print '\tkey \%(keycode)s \%(keysyms)s;' \% {  "keycode": $keycode.text, "keysyms": $keysyms.value } }
	-> ^(TOKEN_KEY keycode keysyms)
	;
	
keycode	
	: LOWERTHAN NAME GREATERTHAN 
	-> ^(KEYCODE NAME)
	;

keysyms	returns [value]
	: LCURLY LBRACKET keysym+=NAME (COMMA keysym+=NAME)* RBRACKET RCURLY
        {       
                qstring = ["{ [ "]
                first_elem = $keysym[0].getText()
                qstring.append(first_elem)
                for elem in $keysym:
                        if first_elem != "":
                                first_elem = ""
                                continue
                        qstring.append(", ")
                        qstring.append(elem.getText())
                qstring.append(" ] }")
                $value = "".join(qstring)
        }
	;

// mapsyms	
//	: LCURLY LBRACKET (NAME|keycode) (COMMA (NAME|keycode))* RBRACKET RCURLY  
//	;

mapOptions
	: TOKEN_DEFAULT 	{ print "default", }
	| TOKEN_HIDDEN 		{ print "hidden", }
	| TOKEN_PARTIAL 	{ print "partial", }	
	| TOKEN_ALPHANUMERIC_KEYS { print "alphanumeric_keys", } 	
	| TOKEN_ALTERNATE_GROUP { print "alternate_group", }
	| TOKEN_XKB_SYMBOLS     { print "xkb_symbols", }
	;

fragment GENERIC_NAME
	: ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'_'|'0'..'9')
        ;

NAME
	: ('a'..'z'|'A'..'Z'|'_'|'('|')'|'0'..'9')*
        ;

// Comments are currently ignored.
WS  	
	:  
	(' '|'\r'|'\t'|'\u000C'|'\n') 
	{$channel=HIDDEN;}
    	;

COMMENT
    	:   
	'/*' .* '*/' {$channel=HIDDEN;}
    	;

LINE_COMMENT
    	: 
	'//' ~('\n'|'\r')* '\r'? '\n' 
	{$channel=HIDDEN;}
    	;

