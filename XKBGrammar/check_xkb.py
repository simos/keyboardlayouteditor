#!/usr/bin/env python

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
    formula = sys.argv[1]

try:    
	xkbfile = open(xkbfilename, 'r')
except OSError:
	print "Could not open file ", xkbfilename, ". Aborting..."
	sys.exit(-1)

xkbcontents = xkbfile.read()
xkbfile.close

print "Creating character stream...",
char_stream = antlr3.ANTLRStringStream(xkbcontents)
print " done."
print "Performing the lexer...",
lexer = XKBGrammarLexer(char_stream)
print " done."
print "Extracting tokens...",
tokens = antlr3.CommonTokenStream(lexer)
print " done."
print "Performing the parser...",
parser = XKBGrammarParser(tokens)
print " done."

print "Executing the function...",
result = parser.layout()
print "done."

# Get all of the SPECIES children
for attribute in getChildrenByType(result.tree, INCLUDE):
    print "attribute: ", attribute,
    value = attribute.getFirstChildWithType(NAME).getText()
    print "value: ", value
