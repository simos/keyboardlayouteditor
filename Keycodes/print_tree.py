#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 0.8

import sys
import pdb
import antlr3
from KeycodesLexer import KeycodesLexer
from KeycodesParser import KeycodesParser
from KeycodesWalker import KeycodesWalker

# Helper function to iterate through all children of a given type
def getChildrenByType(tree, type_value):
	for i in range(tree.getChildCount()):
		child = tree.getChild(i)
		if child.getType() == type_value:
			yield child

# Helper function to iterate through all children of a given type
def getChildrenListByType(tree, type_value):
	list = []
    	for i in range(tree.getChildCount()):
        	child = tree.getChild(i)
        	if child.getType() == type_value:
        		list.append(child)
	return list

filename = "xfree86"
if len(sys.argv) > 1:
    filename = sys.argv[1]

try:    
	file = open(filename, 'r')
except OSError:
	print "Could not open file ", filename, ". Aborting..."
	sys.exit(-1)

file.close

char_stream = antlr3.ANTLRFileStream(filename)
lexer = KeycodesLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = KeycodesParser(tokens)

result = parser.keycodedoc()

print "XXXXXXXXXXXXXXXXXXXXXXX", filename
print "tree =", result.tree.toStringTree()

nodes = antlr3.tree.CommonTreeNodeStream(result.tree)
nodes.setTokenStream(tokens)
walker = KeycodesWalker(nodes)
walker.keycodedoc()

MAX = 10
TABS = "\t\t\t\t\t\t\t\t\t\t"

def print_tree(node, depth):
	if depth >= MAX:
		return
	for n in node.getChildren():
		print TABS[:depth], "===", n.getText(), "==="
		print_tree(n, depth + 1)
		

print result.tree.getChild(0).getText()
print
print_tree(result.tree, 0)
