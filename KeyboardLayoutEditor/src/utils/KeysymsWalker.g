// Keysyms Grammar (X.org)
// Written by Simos Xenitellis <simos.lists@googlemail.com>, 2008.
// Version 0.1

tree grammar KeysymsWalker;

options
{
	language = Python;
        tokenVocab = Keysyms;
        ASTLabelType = CommonTree;
}

keysym
	: ^(ENTRY line+)
	;

line
	: ^(KEYSYM NAME NAME)
	;
