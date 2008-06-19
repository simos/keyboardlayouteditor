#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 0.8

import sys
import os.path
import pdb
import antlr3
from lxml import etree
from XKBGrammarLexer import XKBGrammarLexer 
from XKBGrammarParser import XKBGrammarParser
from XKBGrammarWalker import XKBGrammarWalker, LAYOUT, SYMBOLS, MAPMATERIAL, MAPTYPE, MAPOPTIONS, MAPOPTS, MAPNAME, TOKEN_INCLUDE, TOKEN_NAME, TOKEN_KEY_TYPE, TOKEN_KEY, TOKEN_TYPE, TOKEN_MODIFIER_MAP, TOKEN_VIRTUAL_MODIFIERS, KEYCODE, KEYCODEX, ELEM_KEYSYMS, ELEM_KEYSYMGROUP, ELEM_VIRTUALMODS, OVERLAY, VALUE, STATE, NAME, DQSTRING, OVERRIDE

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

# print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", sys.argv[1]

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

# print "tree =", result.tree.toStringTree()

nodes = antlr3.tree.CommonTreeNodeStream(result.tree)
nodes.setTokenStream(tokens)
walker = XKBGrammarWalker(nodes)
# walker.layout()

layout = etree.Element('layout')

doc = etree.ElementTree(layout)

layout.attrib['layoutname'] = os.path.basename(xkbfilename)

for symbols in result.tree.getChildren():
	eSymbol = etree.SubElement(layout, 'symbols')
	for mapobject in symbols.getChildren():
		if mapobject.getType() == MAPTYPE:
			for maptypesect in mapobject.getChildren():
				if maptypesect.getType() == MAPOPTIONS:
					for mapoption in maptypesect.getChildren():
						if mapoption.getText() == 'xkb_symbols':
							eMapOption = etree.SubElement(eSymbol, 'mapoption')
							eMapOption.text = mapoption.getText()
				elif maptypesect.getType() == MAPNAME:
					if maptypesect.getChildCount() == 1:
						eMapName = etree.SubElement(eSymbol, 'mapname')
						eMapName.text = maptypesect.getChildren()[0].getText()[1:-1]
					else:
						print "\t\t\tInternal error in mapoption"
				else:
					print "\t\tInternal error in maptypesect"
					sys.exit(-2)
		elif mapobject.getType() == MAPMATERIAL:
			eMapMaterial = etree.SubElement(eSymbol, 'mapmaterial')
			for name in getChildrenByType(mapobject, TOKEN_NAME):
				nameText = name.getChild(0).getText()[1:-1]
				eTokenName = etree.SubElement(eMapMaterial, 'tokenname', name=nameText ) 
			for include in getChildrenByType(mapobject, TOKEN_INCLUDE):
				eInclude = etree.SubElement(eMapMaterial, 'tokeninclude')
				eInclude.text = include.getChild(0).getText()[1:-1]
			for keytype in getChildrenByType(mapobject, TOKEN_KEY_TYPE):
				keytypeText = keytype.getChild(0).getText()
				for i in keytype.getChildren():
					if i.getType() == VALUE:
						eKeyType = etree.SubElement(eMapMaterial, 'tokentype')
						eKeyType.attrib['name'] = keytypeText
						eKeyType.text = i.getChild(0).getText()[1:-1]
			for keyset in getChildrenByType(mapobject, TOKEN_KEY):
				keycode = getChildrenListByType(keyset, KEYCODE)
				keycodex = getChildrenListByType(keyset, KEYCODEX)
				elem_keysymgroup = getChildrenByType(keyset, ELEM_KEYSYMGROUP)
				elem_virtualmods = getChildrenByType(keyset, ELEM_VIRTUALMODS)
				elem_overlay = getChildrenByType(keyset, OVERLAY)
				override = getChildrenListByType(keyset, OVERRIDE)
				eTokenKey = etree.SubElement(eMapMaterial, 'tokenkey')
				if len(override) == 1:
					eTokenKey.attrib['override'] = "True"
				else:
					eTokenKey.attrib['override'] = "False"
				if len(keycode) == 1:
					eKeyCodeName = etree.SubElement(eTokenKey, 'keycodename', value=keycode[0].getChild(0).getText())
				elif len(keycodex) == 1:
					eKeyCodeNameX = etree.SubElement(eTokenKey, 'keycodenamex', value=keycode[0].getChild(0).getText())
				else:
					print "\tInternal error keycode/keycodex:", len(keycode), len(keycodex)
					sys.exit(-1)
				if len(getChildrenListByType(keyset, ELEM_KEYSYMGROUP)):
					elem_keysyms = getChildrenListByType(keyset, ELEM_KEYSYMS)
					eKeySymGroup = etree.SubElement(eTokenKey, 'keysymgroup')
					keysymgroup_counter = len(getChildrenListByType(keyset, ELEM_KEYSYMGROUP))
					for elem in elem_keysymgroup:
						eSymbolsGroup = etree.SubElement(eKeySymGroup, 'symbolsgroup')
						for elem2 in elem.getChildren():
							for elem3 in elem2.getChildren():
								eSymbol = etree.SubElement(eSymbolsGroup, 'symbol')
								eSymbol.text = elem3.getText()	
					if len(elem_keysyms) > 0:
						if len(elem_keysyms) == 1:
							ksname = elem_keysyms[0].getChild(0).getText()
							eKeySyms = etree.SubElement(eKeySymGroup, 'typegroup', value=ksname[1:-1])
						else:
							print "Unexpected error!"
							sys.exit(-2)
				if len(getChildrenListByType(keyset, ELEM_VIRTUALMODS)):
					eVirtualMods = etree.SubElement(eTokenKey, 'tokenvirtualmodifiers', value=elem.getChild(0).getText())
				if len(getChildrenListByType(keyset, OVERLAY)):
					for elem in elem_overlay:
						for elem2 in getChildrenByType(elem, KEYCODEX):
							pass
		else:
			print "\tInternal error at map level,", mapobject.getText()
			# sys.exit(-2)

print etree.tostring(layout, pretty_print=True)

#pdb.set_trace()
