#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 0.9

import sys
import pdb
import antlr3
from KeycodesLexer import KeycodesLexer, KEYCODELISTTYPE, KEYCODEMATERIAL, KEYCODELISTOPTIONS, KEYCODELISTNAME, INCLUDE, MINIMUM, MAXIMUM, KEYCODE, ALIAS, INDICATOR
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

# Helper function to iterate through all children of a given type
def getChildrenListValuesByType(tree, type_value):
	list = []
    	for i in range(tree.getChildCount()):
        	child = tree.getChild(i)
        	if child.getType() == type_value:
        		list.append(child.getChild(0).getText())
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

#print "XXXXXXXXXXXXXXXXXXXXXXX", filename
#print "tree =", result.tree.toStringTree()

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
		

#print result.tree.getChild(0).getText()
#print
#print_tree(result.tree, 0)

for itemKeycodeDoc in result.tree.getChildren():
	listType = getChildrenListByType(itemKeycodeDoc, KEYCODELISTTYPE)
	material = getChildrenListByType(itemKeycodeDoc, KEYCODEMATERIAL)
	if len(listType) != 1:
		print "Requires single node for KEYCODELISTTYPE. Found", len(listType)
		sys.exit(-1)
	if len(material) != 1:
		print "Requires single node for KEYCODEMATERIAL. Found", len(material)
		sys.exit(-1)
			
	for listOptionsGroup in getChildrenListByType(listType[0], KEYCODELISTOPTIONS):
		for listOptions in listOptionsGroup.getChildren():
			print listOptions.getText(),
	for listNameGroup in getChildrenListByType(listType[0], KEYCODELISTNAME):
		for listName in listNameGroup.getChildren():
			print listName.getText(),
	print "{"

	for materialIncludeGroup in getChildrenListByType(material[0], INCLUDE):
		for includeName in materialIncludeGroup.getChildren():
			print "\tinclude", includeName.getText()

	if len(getChildrenListByType(material[0], MINIMUM)) not in [0, 1]:
		print "More than one Minimum entries found. Aborting..."
		sys.exit(-1)
	if len(getChildrenListByType(material[0], MAXIMUM)) not in [0, 1]:
		print "More than one Maximym entries found. Aborting..."
		sys.exit(-1)
	if len(getChildrenListByType(material[0], MINIMUM)) == 1:
		print "\tminimum %(v)s;" % { "v": getChildrenListByType(material[0], MINIMUM)[0].getChild(0).getText() }
	if len(getChildrenListByType(material[0], MAXIMUM)) == 1:
		print "\tmaximum %(v)s;" % { "v": getChildrenListByType(material[0], MAXIMUM)[0].getChild(0).getText() }

	for keycode in getChildrenListByType(material[0], KEYCODE):
		print "\tkeycode <%(k)s> = %(v)s;" % { "k": keycode.getChild(0).getText(), "v": keycode.getChild(1).getText()}			

	for alias in getChildrenListByType(material[0], ALIAS):
		print "\talias <%(k1)s> = <%(k2)s>;" % { "k1": alias.getChild(0).getText(), "k2": alias.getChild(1).getText()}			

	for indicator in getChildrenListByType(material[0], INDICATOR):
		print "\tindicator %(id)s = %(val)s;" % { "id": indicator.getChild(0).getText(), "val": indicator.getChild(1).getText()}			

	print '};\n'
	
