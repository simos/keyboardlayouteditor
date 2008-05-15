// XKB Grammar (X.org)
// Written by Simos Xenitellis <simos.lists@googlemail.com>, 2008.
// Version 0.6

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
        : ^(SECTION mapType ^(MAPMATERIAL mapMaterial+))
 	;

mapType
	: ^(MAPTYPE ^(MAPOPTIONS mapOptions+) ^(MAPNAME DQSTRING))
	;

mapOptions
	: 'default'
	| 'hidden'
	| 'partial' 
	| 'alphanumeric_keys'
	| 'alternate_group'
	| 'xkb_symbols'
	;

mapMaterial
	: ^(TOKEN_INCLUDE DQSTRING)
	| ^(TOKEN_NAME NAME ^(VALUE DQSTRING))
	| ^(TOKEN_KEY_TYPE NAME ^(VALUE DQSTRING))
	| ^(TOKEN_KEY keycode keysyms)
	;
	
keycode	
	: ^(KEYCODE NAME)
	;

keysyms
	: ^(KEYSYMS NAME+)
	;

