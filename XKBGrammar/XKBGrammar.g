// XKB Grammar (X.org)
// Written by Simos Xenitellis <simos.lists@googlemail.com>, 2008.
// Version 0.8

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
	TOKEN_TYPE;
	TOKEN_MODIFIER_MAP;
	TOKEN_SYMBOL;
	TOKEN_VIRTUAL_MODIFIERS;

	// Tokens for tree.
	LAYOUT;
	SYMBOLS;
	MAPTYPE;
	MAPNAME;
	MAPOPTIONS;
	MAPMATERIAL;
	KEYCODE;
	KEYCODEX;
	VALUE;
	STATE;
	ELEM_KEYSYMGROUP;
	ELEM_KEYSYMS;
	ELEM_VIRTUALMODS;
	KEYELEMENTS;
	OVERRIDE;
	OVERLAY;
}

// We cover XKB symbol files that look like
//
// // comments can appear here.
// one of more modifiers "mysymbolsname"
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
// // can have several symbol sections as above.

layout 		
	: symbols+ EOF
	-> ^(LAYOUT symbols+)
	;
	
symbols 
	: mapType '{' mapMaterial+ '}' ';'
	-> ^(SYMBOLS mapType ^(MAPMATERIAL mapMaterial+))
 	;

mapType
	: MAPOPTS+ DQSTRING
	-> ^(MAPTYPE ^(MAPOPTIONS MAPOPTS+) ^(MAPNAME DQSTRING))
	;

mapMaterial 
	: line_include 
	| line_name ';'!
	| line_keytype ';'!
	| line_key ';'!
	| line_modifier_map ';'!
	| line_virtual_modifiers ';'!
	;

line_include
	: 'include' DQSTRING
	-> ^(TOKEN_INCLUDE DQSTRING)
	;

line_name
	: 'name' '[' NAME ']' '=' DQSTRING
	-> ^(TOKEN_NAME DQSTRING)
	;

line_keytype
	: 'key.type' ('[' NAME ']')? '=' DQSTRING
	-> ^(TOKEN_KEY_TYPE DQSTRING)
	;

line_key
	: OVERRIDE? 'key' keycode '{' keyelements (',' keyelements)* '}'
	-> ^(TOKEN_KEY OVERRIDE? keycode keyelements+)
	;

line_modifier_map
	: 'modifier_map' STATE '{' keycode (',' keycode)* '}'
	-> ^(TOKEN_MODIFIER_MAP STATE keycode+)
	;

line_virtual_modifiers
	: 'virtual_modifiers' NAME (',' NAME)*
	-> ^(TOKEN_VIRTUAL_MODIFIERS NAME+)
	;

keycode	
	: '<' NAME '>' -> ^(KEYCODE NAME)
	;

override
	: 'override'
	;

keyelements
	: elem_keysyms 
	| elem_keysymgroup
	| elem_virtualmods
	| elem_overlay
	;

elem_keysyms
	: 'type' ('[' NAME ']')? '=' DQSTRING
	-> ^(ELEM_KEYSYMS DQSTRING)
	;

elem_keysymgroup
	: ('symbols' '[' NAME ']' '=')? '[' keysym+=NAME (',' keysym+=NAME)* ']'
	-> ^(ELEM_KEYSYMGROUP ^(VALUE $keysym+ ))
	;

elem_virtualmods
	: ('virtualMods' '=' NAME)
	-> ^(ELEM_VIRTUALMODS NAME)
	;

elem_overlay
	: NAME '=' keycode
	-> ^(OVERLAY NAME keycode)
	;

MAPOPTS
	: 'default'
	| 'hidden'
	| 'partial' 
	| 'alphanumeric_keys'
	| 'keypad_keys'
	| 'function_keys'
	| 'modifier_keys'
	| 'alternate_group'
	| 'xkb_symbols'
	;

STATE
	: 'Shift'
	| 'Control'
	| 'Lock'
	| 'Mod1'
	| 'Mod2'
	| 'Mod3'
	| 'Mod4'
	| 'Mod5'
        ;

OVERRIDE
	: 'override'
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

