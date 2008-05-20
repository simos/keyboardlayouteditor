// XKB Grammar (X.org)
// Written by Simos Xenitellis <simos.lists@googlemail.com>, 2008.
// Version 0.7

grammar XKBGrammar;

options
{
	language = Python;
	output = AST;
}

tokens
{
	// Keywords
	TOKEN_INCLUDE;
	TOKEN_KEY_TYPE;
	TOKEN_NAME;
	TOKEN_KEY;
	TOKEN_MODIFIER_MAP;

	// Tokens for tree.
	LAYOUT;
	MAPTYPE;
	MAPNAME;
	MAPOPTIONS;
	MAPMATERIAL;
	SECTION;
	KEYCODE;
	KEYCODEX;
	KEYSYMS;
	VALUE;
	STATE;
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
	: section+ EOF
	-> ^(LAYOUT section+)
	;
	
section 
	: mapType '{' mapMaterial+ '}' ';'
	-> ^(SECTION mapType ^(MAPMATERIAL mapMaterial+))
 	;

mapType
	: mapOptions+ DQSTRING
	-> ^(MAPTYPE ^(MAPOPTIONS mapOptions+) ^(MAPNAME DQSTRING))
	;

mapMaterial 
	: line_include 
	| line_name ';'!
	| line_keytype ';'!
	| line_key ';'!
	| line_modifier_map ';'!
	;

line_include
	: 'include' DQSTRING
	-> ^(TOKEN_INCLUDE DQSTRING)
	;

line_name
	: 'name' '[' n1=NAME ']' '=' n2=DQSTRING
	-> ^(TOKEN_NAME $n1 ^(VALUE $n2))
	;

line_keytype
	: 'key.type' '[' n1=NAME ']' '=' n2=DQSTRING
	-> ^(TOKEN_KEY_TYPE $n1 ^(VALUE $n2))
	;
	
line_key
	: 'key' keycode keysyms
	-> ^(TOKEN_KEY keycode keysyms)
	;

line_modifier_map
	: 'modifier_map' state '{' keycode (',' keycode)* '}'
	-> ^(TOKEN_MODIFIER_MAP state keycode+)
	;

// segment_type
//	: 'type' '[' NAME ']' '=' DQSTRING ','
//	-> ^(TOKEN_SEGMENT_TYPE NAME DQSTRING)

keycode	
	: NAME -> ^(KEYCODE NAME)
	| '<' NAME '>' -> ^(KEYCODEX NAME)
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
	| 'modifier_keys'
	| 'alternate_group'
	| 'xkb_symbols'
	;

state
	: 'Shift'
	| 'Control'
	| 'Lock'
	| 'Mod1'
	| 'Mod2'
	| 'Mod3'
	| 'Mod4'
	| 'Mod5'
        ;

NAME
	: ( 'a'..'z' | 'A'..'Z' | '_' | '(' | ')' | '0'..'9' | '+' | '-' )*
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

/** Match various string types.  Note that greedy=false implies '''
 *  should make us exit loop not continue.
 */
DQSTRING
    	:   '"' (options {greedy=false;}:~('"'))* '"'
        ;

