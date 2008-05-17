#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 0.7

import sys
import pdb
import antlr3
from XKBGrammarLexer import XKBGrammarLexer, SECTION, MAPTYPE, MAPNAME, MAPOPTIONS, MAPMATERIAL, TOKEN_INCLUDE, TOKEN_NAME, TOKEN_KEY_TYPE, TOKEN_KEY, VALUE, KEYCODE, KEYCODEX, KEYSYMS
from XKBGrammarParser import XKBGrammarParser
from XKBGrammarWalker import XKBGrammarWalker

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

print "tree =", result.tree.toStringTree()

nodes = antlr3.tree.CommonTreeNodeStream(result.tree)
nodes.setTokenStream(tokens)
walker = XKBGrammarWalker(nodes)
walker.layout()

print "Layout has", result.tree.getChildCount(), "sections"
for section in result.tree.getChildren():
	print "// Section"
	for mapobject in section.getChildren():
		if mapobject.getType() == MAPTYPE:
			for maptypesect in mapobject.getChildren():
				if maptypesect.getType() == MAPOPTIONS:
					for mapoption in maptypesect.getChildren():
						print mapoption.getText(),
				elif maptypesect.getType() == MAPNAME:
					if maptypesect.getChildCount() == 1:
						print '%(opt)s {' % { "opt": maptypesect.getChildren()[0].getText() }
					else:
						print "\t\t\tInternal error in mapoption"
				else:
					print "\t\tInternal error in maptypesect"
					sys.exit(-2)
		elif mapobject.getType() == MAPMATERIAL:
			for name in getChildrenByType(mapobject, TOKEN_NAME):
				nameText = name.getChild(0).getText()
				for i in name.getChildren():
					if i.getType() == VALUE:
						print '\tname[%(name)s] = %(val)s;' % { "name": nameText, "val": i.getChild(0).getText()}
			for include in getChildrenByType(mapobject, TOKEN_INCLUDE):
				print "\tinclude", include.getChild(0).getText()
			for keytype in getChildrenByType(mapobject, TOKEN_KEY_TYPE):
				keytypeText = keytype.getChild(0).getText()
				for i in keytype.getChildren():
					if i.getType() == VALUE:
						print '\tkey.type[%(kt)s] = %(val)s;' % { "kt": keytypeText, "val": i.getChild(0).getText() }
			for keyset in getChildrenByType(mapobject, TOKEN_KEY):
				keycode = getChildrenListByType(keyset, KEYCODE)
				keycodex = getChildrenListByType(keyset, KEYCODEX)
				keysyms = getChildrenListByType(keyset, KEYSYMS)
				if len(keycode) == 1:
					print '\tkey %(kc)s = { [' % { "kc": keycode[0].getChild(0).getText() },
				elif len(keycodex) == 1:
					print '\tkey <%(kc)s> = { [' % { "kc": keycodex[0].getChild(0).getText() },
				else:
					print "\tInternal error keycode/keycodex:", len(keycode), len(keycodex)
					sys.exit(-1)
				first_time = True
				if keysyms[0].getChildCount() == 0:
					print "Internal error"
					sys.exit(-1)
				for ks in keysyms[0].getChildren():
					if first_time:
						first_time = False
					else:
						sys.stdout.write(", ");
					sys.stdout.write(ks.getText())
				print "] };"
		else:
			print "\tInternal error at map level,", mapobject.getText()
			# sys.exit(-2)
	print "};\n"

#pdb.set_trace()
