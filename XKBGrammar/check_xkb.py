#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import antlr3
from XKBGrammarLexer import XKBGrammarLexer
from XKBGrammarParser import XKBGrammarParser, ATTRIBUTES, ATTRIBUTE, INCLUDE, NAME

# Helper function to iterate through all children of a given type
def getChildrenByType(tree, type_value):
    for i in range(tree.getChildCount()):
        child = tree.getChild(i)
        if child.getType() == type_value:
            yield child

xkbfilename = "gr"
if len(sys.argv) > 1:
    xkbfilename = sys.argv[1]

try:    
	xkbfile = open(xkbfilename, 'r')
except OSError:
	print "Could not open file ", xkbfilename, ". Aborting..."
	sys.exit(-1)

xkbfile.close

char_stream = antlr3.ANTLRFileStream(xkbfilename, encoding='utf-8')
lexer = XKBGrammarLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = XKBGrammarParser(tokens)

result = parser.layout()

# Get all of the SPECIES children
for attribute in getChildrenByType(result.tree, INCLUDE):
    print "attribute: ", attribute,
    value = attribute.getFirstChildWithType(NAME).getText()
    print "value: ", value
