#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pdb
import antlr3
from XKBGrammarLexer import XKBGrammarLexer
from XKBGrammarParser import XKBGrammarParser
from XKBGrammarWalker import XKBGrammarWalker

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

# pdb.set_trace()
result = parser.layout()

print "tree =", result.tree.toStringTree()

nodes = antlr3.tree.CommonTreeNodeStream(result.tree)
nodes.setTokenStream(tokens)
walker = XKBGrammarWalker(nodes)
# walker.layout()

