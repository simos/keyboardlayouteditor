// XKB Grammar (X.org)
// Written by Simos Xenitellis <simos.lists@googlemail.com>, 2008.
// Version 0.3

tree grammar XKBGrammarWalker;

options
{
    tokenVocab=XKBGrammar;
    ASTLabelType=CommonTree;
    language=Python;
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
	: ^(SECTION mapType mapMaterial)
 	;

mapType
	: ^(MAPTYPE mapOptions+ NAME)
	;

mapMaterial 
 	: ^(MAPMATERIAL line_include line_name line_keytype line_key)
	;
//	: ^(MAPMATERIAL TOKEN_INCLUDE TOKEN_NAME TOKEN_KEY_TYPE TOKEY_KEY)
//	;

line_include
	: ^(TOKEN_INCLUDE NAME)
	;

line_name
	: ^(TOKEN_NAME NAME+)
	;

line_keytype
	: ^(TOKEN_KEY_TYPE NAME+)
	;
	
line_key
	: ^(TOKEN_KEY keycode keysyms)
	;
	
keycode	
	: ^(KEYCODE NAME)
	;

keysyms
	: ^(KEYSYMS NAME+)
	;

mapOptions
	: 'default'
	| 'hidden'
	| 'partial' 
	| 'alphanumeric_keys'
	| 'alternate_group'
	| 'xkb_symbols'
	;
