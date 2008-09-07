// Keycodes Grammar (X.org)
// Written by Simos Xenitellis <simos.lists@googlemail.com>, 2008.
// Version 0.8

tree grammar KeycodesWalker;

options
{
        language = Python;
        tokenVocab = Keycodes;
        ASTLabelType = CommonTree;
}


keycodedoc 		
	: ^(KEYCODEDOC keycodelist+)
	;
	
keycodelist 
	: ^(KEYCODELIST keycodelisttype ^(KEYCODEMATERIAL keycodeMaterial+))
 	;

keycodelisttype
	: ^(KEYCODELISTTYPE ^(KEYCODELISTOPTIONS KEYCODELISTOPTS+) ^(KEYCODELISTNAME DQSTRING))
	;

keycodeMaterial 
	: ^(INCLUDE DQSTRING)
	| ^(MINIMUM NAME)
	| ^(MAXIMUM NAME)
	| ^(ALIAS NAME+)
	| ^(KEYCODE NAME+)
	| ^(INDICATOR NAME DQSTRING)
	;
