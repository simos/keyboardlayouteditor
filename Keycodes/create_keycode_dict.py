#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 0.9

import sys
import pdb
import antlr3
import re
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

keycodedb = {}
keycodeid = "xfree86"
keycodeidinclude = [keycodeid]
copying = False

for itemKeycodeDoc in result.tree.getChildren():
	listType = getChildrenListByType(itemKeycodeDoc, KEYCODELISTTYPE)
	material = getChildrenListByType(itemKeycodeDoc, KEYCODEMATERIAL)
	if len(listType) != 1:
		print "Requires single node for KEYCODELISTTYPE. Found", len(listType)
		sys.exit(-1)
	if len(material) != 1:
		print "Requires single node for KEYCODEMATERIAL. Found", len(material)
		sys.exit(-1)
			
	for listNameGroup in getChildrenListByType(listType[0], KEYCODELISTNAME):
		for listName in listNameGroup.getChildren():
			if listName.getText()[1:-1] == keycodeid or listName.getText()[1:-1] in keycodeidinclude:
				print "About to process", listName.getText()[1:-1]
				copying = True

	for materialIncludeGroup in getChildrenListByType(material[0], INCLUDE):
		for includeName in materialIncludeGroup.getChildren():
			includeKeycodelist = re.findall('(\w+)\((\w+)\)', includeName.getText()[1:-1])
			if includeKeycodelist[0][1] not in keycodeidinclude:
				print "Added", includeKeycodelist[0][0], includeKeycodelist[0][1]
				keycodeidinclude.append(includeKeycodelist[0][1])

	for keycode in getChildrenListByType(material[0], KEYCODE):
		keycodedb[keycode.getChild(0).getText()] = keycode.getChild(1).getText()

	for alias in getChildrenListByType(material[0], ALIAS):
		keycodedb[alias.getChild(0).getText()] = keycodedb[alias.getChild(1).getText()]

	for indicator in getChildrenListByType(material[0], INDICATOR):
		pass

	copying = False
	
for item in keycodedb.keys():
	print item, keycodedb[item]
