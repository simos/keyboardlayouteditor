// XKB Grammar (X.org)
// Written by Simos Xenitellis <simos.lists@googlemail.com>, 2008.
// Version 0.7

tree grammar XKBGrammarWalker;

options
{
	language = Python;
	tokenVocab = XKBGrammar; 
	ASTLabelType = CommonTree;
}

// We cover XKB symbol files that look like
//
// // comments can appear here.
// one of more modifiers "mysymbolname"
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
	: ^(LAYOUT symbols+)
	;
	
symbols 
        : ^(SYMBOLS mapType ^(MAPMATERIAL mapMaterial+))
 	;

mapType
	: ^(MAPTYPE ^(MAPOPTIONS mapOptions+) ^(MAPNAME DQSTRING))
	;

keycode
        : ^(KEYCODE NAME)
        | ^(KEYCODEX NAME)
        ;

mapOptions
	: 'default'
	| 'hidden'
	| 'partial' 
	| 'alphanumeric_keys'
	| 'keypad_keys'
	| 'alternate_group'
	| 'modifier_keys'
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

mapMaterial
	: ^(TOKEN_INCLUDE DQSTRING)
	| ^(TOKEN_NAME NAME ^(VALUE DQSTRING))
	| ^(TOKEN_KEY_TYPE NAME ^(VALUE DQSTRING))
	| ^(TOKEN_KEY ^(OVERRIDE 'override') keycode keysyms)
	| ^(TOKEN_MODIFIER_MAP state keycode+)
	| ^(TOKEN_VIRTUAL_MODIFIERS NAME+)
	;

line_type
	:
	^(TOKEN_TYPE NAME ^(VALUE DQSTRING))
	;
	
keysyms
	: ^(KEYSYMS ^(TOKEN_TYPE NAME DQSTRING) keysymgroup+)
	;

keysymgroup
        : ^(KEYSYM_GROUP ^(TOKEN_SYMBOL NAME) NAME+)
	;


