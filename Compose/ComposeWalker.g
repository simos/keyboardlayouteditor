// Compose Grammar (X.org)
// Written by Simos Xenitellis <simos.lists@googlemail.com>, 2008.
// Version 0.1

tree grammar ComposeWalker;

options
{
        language = Python;
        tokenVocab = Compose;
        ASTLabelType = CommonTree;
}

compose	: ^(COMPOSE sequence+) ;
sequence: ^(SEQUENCe sym+ ^(CODEPOINT DQSTRING NAME?)) ;
sym	: ^(SYM NAME) ; 
