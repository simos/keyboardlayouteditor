// XKB Grammar (X.org)
// Written by Simos Xenitellis <simos.lists@googlemail.com>, 2008.
// Version 0.4

grammar XKBGrammar;

options
{
	language = Python;
	output = AST;
}

tokens
{
	// Map options
	TOKEN_DEFAULT;
	TOKEN_HIDDEN;
	TOKEN_PARTIAL;
	TOKEN_ALPHANUMERIC_KEYS;
	TOKEN_MODIFIER_KEYS;
	TOKEN_ALTERNATE_GROUP;
	TOKEN_XKB_SYMBOLS;

	// Keywords
	TOKEN_INCLUDE;
	TOKEN_KEY_TYPE;
	TOKEN_NAME;
	TOKEN_KEY;

	// Tokens for tree.
	MAPTYPE;
	MAPNAME;
	MAPOPTIONS;
	MAPMATERIAL;
	SECTION;
	KEYCODE;
	KEYSYMS;
	VALUE;
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
	: section+ EOF!
	;
	
section 
	: mapType mapMaterial
	-> ^(SECTION mapType mapMaterial)
 	;

mapType
	: mapOptions+ '"' NAME '"'
	-> ^(MAPTYPE ^(MAPOPTIONS mapOptions+) ^(MAPNAME NAME))
	;

mapMaterial 
	: '{'
	( line_include 
	| line_name ';'!
	| line_keytype ';'!
	| line_key ';'!
	)+ '}' ';'!
	;

line_include
	: 'include' '"' NAME '"'
	-> ^(TOKEN_INCLUDE NAME)
	;

line_name
	: 'name' '[' n1=NAME ']' '=' '"' n2=NAME '"'
	-> ^(TOKEN_NAME $n1 ^(VALUE $n2))
	;

line_keytype
	: 'key.type' '[' n1=NAME ']' '=' '"' n2=NAME '"'
	-> ^(TOKEN_KEY_TYPE $n1 ^(VALUE $n2))
	;
	
line_key
	: 'key' keycode keysyms
	-> ^(TOKEN_KEY keycode keysyms)
	;
	
keycode	
	: '<' NAME '>'
	-> ^(KEYCODE NAME)
	;

keysyms
	: '{' '[' keysym+=NAME (',' keysym+=NAME)* ']' '}'
	-> ^(KEYSYMS $keysym+)
	;

mapOptions
	: 'default'
	| 'hidden'
	| 'partial' 
	| 'alphanumeric_keys'
	| 'alternate_group'
	| 'xkb_symbols'
	;

NAME
	: ('a'..'z' | 'A'..'Z' | '_' | '-' | '(' | ')' | '0'..'9')*
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
	'//' ~('\n' | '\r')* '\r'? '\n' 
	{ $channel=HIDDEN; }
    	;

