#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 0.8

import sys
import pdb
import antlr3
from XKBGrammarLexer import XKBGrammarLexer 
from XKBGrammarParser import XKBGrammarParser
from XKBGrammarWalker import XKBGrammarWalker, LAYOUT, SYMBOLS, MAPMATERIAL, MAPTYPE, MAPOPTIONS, MAPOPTS, MAPNAME, TOKEN_INCLUDE, TOKEN_NAME, TOKEN_KEY_TYPE, TOKEN_KEY, TOKEN_TYPE, TOKEN_MODIFIER_MAP, TOKEN_VIRTUAL_MODIFIERS, KEYCODE, KEYCODEX, ELEM_KEYSYMS, ELEM_KEYSYMGROUP, ELEM_VIRTUALMODS, ELEM_ACTIONS, OVERLAY, ACTIONS_SETMODS, VALUE, STATE, NAME, DQSTRING, OVERRIDE

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

def hasChildByType(tree, type_value):
	has = False
	for i in range(tree.getChildCount()):
		child = tree.getChild(i)
		if child.getType() == type_value:
			has = True
			break
	return has

xkbfilename = "gr"
if len(sys.argv) > 1:
    xkbfilename = sys.argv[1]

print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", sys.argv[1]

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
# walker.layout()

for symbols in result.tree.getChildren():
	for mapobject in symbols.getChildren():
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
				elem_keysyms = getChildrenByType(keyset, ELEM_KEYSYMS)
				elem_keysymgroup = getChildrenByType(keyset, ELEM_KEYSYMGROUP)
				elem_virtualmods = getChildrenByType(keyset, ELEM_VIRTUALMODS)
				elem_actions = getChildrenByType(keyset, ELEM_ACTIONS)
				elem_overlay = getChildrenByType(keyset, OVERLAY)
				override = getChildrenListByType(keyset, OVERRIDE)
				print '\t',
				if len(override) == 1:
					print 'override',
				if len(keycode) == 1:
					print 'key %(kc)s = {' % { "kc": keycode[0].getChild(0).getText() },
				elif len(keycodex) == 1:
					print 'key <%(kc)s> = {' % { "kc": keycodex[0].getChild(0).getText() },
				else:
					print "\tInternal error keycode/keycodex:", len(keycode), len(keycodex)
					sys.exit(-1)
				gotitem = False
				if len(getChildrenListByType(keyset, ELEM_KEYSYMGROUP)):
					gotitem = True
					print "[",
					keysymgroup_counter = len(getChildrenListByType(keyset, ELEM_KEYSYMGROUP))
					for elem in elem_keysymgroup:
						for elem2 in elem.getChildren():
							repeat_visit = False
							for elem3 in elem2.getChildren():
								if repeat_visit:
									sys.stdout.write(', ')
								else:
									repeat_visit = True
								print "%(elem)s" % { "elem": elem3.getText() },
						if keysymgroup_counter > 1:
							print "], [",
							keysymgroup_counter -= 1
					print "]",
				if len(getChildrenListByType(keyset, ELEM_VIRTUALMODS)):
					if gotitem:
						sys.stdout.write(",\n\t\t\t"),
					else:
						gotitem = True
					for elem in elem_virtualmods:
						print "virtualMods =", elem.getChild(0).getText(),
				if len(getChildrenListByType(keyset, ELEM_ACTIONS)):
					if gotitem:
						sys.stdout.write(", "),
					else:
						gotitem = True
					repeat_visit = False
					for elem in elem_actions:
						print "actions[%(s)s] = [ " % { "s": elem.getChild(0).getText() },
						sys.stdout.write("SetMods(modifiers=")
						for elem2 in getChildrenByType(elem, ACTIONS_SETMODS):
							if repeat_visit:
								sys.stdout.write(", "),
							else:
								repeat_visit = True
							print "%(s)s" % { "s": elem2.getChild(0).getText() },
						sys.stdout.write(") ]")
				if len(getChildrenListByType(keyset, OVERLAY)):
					if gotitem:
						sys.stdout.write(", "),
					else:
						gotitem = True
					for elem in elem_overlay:
						print elem.getChild(0).getText(), "=",
						for elem2 in getChildrenByType(elem, KEYCODEX):
							print "<%(s)s>" % { "s": elem2.getChild(0).getText() },
				print " };"
		else:
			print "\tInternal error at map level,", mapobject.getText()
			# sys.exit(-2)
	print "};\n"

#pdb.set_trace()
