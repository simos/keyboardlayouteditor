#!/usr/bin/env python
# -*- encoding: UTF-8 -*-
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#   
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#   
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>

import sys
import os.path
import string
import antlr3
import re
import copy
from lxml import etree
from XKBGrammarLexer import XKBGrammarLexer 
from XKBGrammarParser import XKBGrammarParser
from XKBGrammarWalker import XKBGrammarWalker, LAYOUT, SYMBOLS, MAPMATERIAL, MAPTYPE, MAPOPTIONS, MAPOPTS, MAPNAME, TOKEN_INCLUDE, TOKEN_NAME, TOKEN_KEY_TYPE, TOKEN_KEY, TOKEN_TYPE, TOKEN_MODIFIER_MAP, TOKEN_VIRTUAL_MODIFIERS, KEYCODE, KEYCODEX, ELEM_KEYSYMS, ELEM_KEYSYMGROUP, ELEM_VIRTUALMODS, OVERLAY, VALUE, STATE, NAME, DQSTRING, OVERRIDE
import KeycodesReader
import KeysymsUni

import Common
from ParseXML import ExtractVariantsKeycodes

class ParseXKB:
    def __init__(self):
        KeycodesReader.initialise()

    # Sorts a dictionary by value, produces a sorted list of values.
    def sortDict(self, adict, cmp_function = None):
        keys = adict.keys()
        keys.sort(cmp_function)
        return map(adict.get, keys)

    # Helper function to iterate through all children of a given type
    def getChildrenByType(self, tree, type_value):
        for i in range(tree.getChildCount()):
            child = tree.getChild(i)
            if child.getType() == type_value:
                yield child

    # Helper function to iterate through all children of a given type
    def getChildrenByTypes(self, tree, type_value1, type_value2):
        for i in range(tree.getChildCount()):
            child = tree.getChild(i)
            if child.getType() == type_value1 or child.getType() == type_value2:
                yield child

    # Helper function to iterate through all children of a given type
    def getChildrenListByType(self, tree, type_value):
        list = []
        for i in range(tree.getChildCount()):
            child = tree.getChild(i)
            if child.getType() == type_value:
                list.append(child)
        return list

    # Helper function to iterate through all children of a given type
    def getChildrenListByTypes(self, tree, type_value1, type_value2):
        list = []
        for i in range(tree.getChildCount()):
                child = tree.getChild(i)
                if child.getType() == type_value1 or child.getType() == type_value2:
                    list.append(child)
        return list

    def hasChildByType(self, tree, type_value):
        has = False
        for i in range(tree.getChildCount()):
                child = tree.getChild(i)
                if child.getType() == type_value:
                    has = True
                    break
        return has

    def parse(self, xkbfilename):
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

        #print "Processing", os.path.basename(xkbfilename), "...",
        for symbols in result.tree.getChildren():
            eSymbol = etree.SubElement(layout, 'symbols')
            for mapobject in symbols.getChildren():
                if mapobject.getType() == MAPTYPE:
                    for maptypesect in mapobject.getChildren():
                        if maptypesect.getType() == MAPOPTIONS:
                            for mapoption in maptypesect.getChildren():
                                if mapoption.getText() == 'xkb_symbols' or mapoption.getText() == 'hidden':
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
                    for name in self.getChildrenByType(mapobject, TOKEN_NAME):
                        nameText = name.getChild(0).getText()[1:-1]
                        eTokenName = etree.SubElement(eMapMaterial, 'tokenname', name=nameText ) 
                    for include in self.getChildrenByType(mapobject, TOKEN_INCLUDE):
                        eInclude = etree.SubElement(eMapMaterial, 'tokeninclude')
                        eInclude.text = include.getChild(0).getText()[1:-1]
                    for keytype in self.getChildrenByType(mapobject, TOKEN_KEY_TYPE):
                        keytypeText = keytype.getChild(0).getText()
                        eKeyType = etree.SubElement(eMapMaterial, 'tokentype')
                        eKeyType.text = keytypeText[1:-1]
                    for modmap in self.getChildrenByType(mapobject, TOKEN_MODIFIER_MAP):
                        eModMap = etree.SubElement(eMapMaterial, 'tokenmodifiermap', state=modmap.getChild(0).getText())
                        for modstate in self.getChildrenByTypes(modmap, KEYCODE, KEYCODEX):
                            if modstate.getType() == KEYCODE:
                                  eModState = etree.SubElement(eModMap, "keycode", value=modstate.getChild(0).getText())
                            elif modstate.getType() == KEYCODEX:
                                eModState = etree.SubElement(eModMap, "keycodex", value=modstate.getChild(0).getText())
                            else:
                                print "Unexpected token encountered. Aborting...", modstate.getText()
                                sys.exit(-1)
                    allkeysymgroups = {}
                    for keyset in self.getChildrenByType(mapobject, TOKEN_KEY):
                        allkeysymgroups[keyset.getChild(0).getChild(0).getText()] = keyset
                    sortedkeysymgroups = self.sortDict(allkeysymgroups, KeycodesReader.compare_keycode)
                    for keyset in sortedkeysymgroups:
                        elem_keysymgroup = self.getChildrenByType(keyset, ELEM_KEYSYMGROUP)
                        elem_virtualmods = self.getChildrenByType(keyset, ELEM_VIRTUALMODS)
                        elem_overlay = self.getChildrenByType(keyset, OVERLAY)
                        override = self.getChildrenListByType(keyset, OVERRIDE)
                        eTokenKey = etree.SubElement(eMapMaterial, 'tokenkey')
                        eKeyCodeName = etree.SubElement(eTokenKey, 'keycodename')
                        keycodex = self.getChildrenListByType(keyset, KEYCODEX)
                        if len(keycodex) == 1:
                            eKeyCodeName.text = keycodex[0].getChild(0).getText()
                        else:
                            print "Could not retrieve keycode name"
                            exit(-1)
                        if len(override) == 1:
                            eTokenKey.attrib['override'] = "True"
                        else:
                            eTokenKey.attrib['override'] = "False"
                        if len(self.getChildrenListByType(keyset, ELEM_KEYSYMGROUP)):
                            elem_keysyms = self.getChildrenListByType(keyset, ELEM_KEYSYMS)
                            eKeySymGroup = etree.SubElement(eTokenKey, 'keysymgroup')
                            keysymgroup_counter = len(self.getChildrenListByType(keyset, ELEM_KEYSYMGROUP))
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
                                    """ We are probably processing level3; we keep first item """
                                    ksname = elem_keysyms[0].getChild(0).getText()
                                    eKeySyms = etree.SubElement(eKeySymGroup, 'typegroup', value=ksname[1:-1])
                                    #print "Possibly processing level3"
                        if len(self.getChildrenListByType(keyset, ELEM_VIRTUALMODS)):
                            for vmods in elem_virtualmods:
                                etree.SubElement(eKeySymGroup, 'tokenvirtualmodifiers', value=vmods.getChild(0).getText())
                        if len(self.getChildrenListByType(keyset, OVERLAY)):
                            for elem in elem_overlay:
                                for elem2 in self.getChildrenByType(elem, KEYCODEX):
                                    pass
                else:
                    print "\tInternal error at map level,", mapobject.getText()
                    # sys.exit(-2)
                    
        return layout


    def parse_layout(self, xkbfilename, variant = None):
        char_stream = antlr3.ANTLRFileStream(xkbfilename, encoding='utf-8')
        lexer = XKBGrammarLexer(char_stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = XKBGrammarParser(tokens)

        result = parser.layout()
        variants = []

        layout = etree.Element('layout')
        layout.attrib['layoutname'] = os.path.basename(xkbfilename)

        #print "Processing", os.path.basename(xkbfilename), "...",
        for symbols in result.tree.getChildren():
            eSymbol = etree.SubElement(layout, 'symbols')
            for mapobject in symbols.getChildren():
                if mapobject.getType() == MAPTYPE:
                    for maptypesect in mapobject.getChildren():
                        if maptypesect.getType() == MAPOPTIONS:
                            for mapoption in maptypesect.getChildren():
                                if mapoption.getText() == 'xkb_symbols' or mapoption.getText() == 'hidden':
                                    eMapOption = etree.SubElement(eSymbol, 'mapoption')
                                    eMapOption.text = mapoption.getText()
                        elif maptypesect.getType() == MAPNAME:
                            if maptypesect.getChildCount() == 1:
                                eMapName = etree.SubElement(eSymbol, 'mapname')
                                eMapName.text = maptypesect.getChildren()[0].getText()[1:-1]
                                variants.append(maptypesect.getChildren()[0].getText()[1:-1])
                            else:
                                return { "success": False }
                                #print "\t\t\tInternal error in mapoption"
                        else:
                            return { "success": False }
                            #print "\t\tInternal error in maptypesect"
                            #sys.exit(-2)
                elif mapobject.getType() == MAPMATERIAL:
                    eMapMaterial = etree.SubElement(eSymbol, 'mapmaterial')
                    for name in self.getChildrenByType(mapobject, TOKEN_NAME):
                        nameText = name.getChild(0).getText()[1:-1]
                        eTokenName = etree.SubElement(eMapMaterial, 'tokenname', name=nameText ) 
                    for include in self.getChildrenByType(mapobject, TOKEN_INCLUDE):
                        eInclude = etree.SubElement(eMapMaterial, 'tokeninclude')
                        eInclude.text = include.getChild(0).getText()[1:-1]
                    for keytype in self.getChildrenByType(mapobject, TOKEN_KEY_TYPE):
                        keytypeText = keytype.getChild(0).getText()
                        eKeyType = etree.SubElement(eMapMaterial, 'tokentype')
                        eKeyType.text = keytypeText[1:-1]
                    for modmap in self.getChildrenByType(mapobject, TOKEN_MODIFIER_MAP):
                        eModMap = etree.SubElement(eMapMaterial, 'tokenmodifiermap', state=modmap.getChild(0).getText())
                        for modstate in self.getChildrenByTypes(modmap, KEYCODE, KEYCODEX):
                            if modstate.getType() == KEYCODE:
                                  eModState = etree.SubElement(eModMap, "keycode", value=modstate.getChild(0).getText())
                            elif modstate.getType() == KEYCODEX:
                                eModState = etree.SubElement(eModMap, "keycodex", value=modstate.getChild(0).getText())
                            else:
                                return { "success": False }
                                # print "Unexpected token encountered. Aborting...", modstate.getText()
                                # sys.exit(-1)
                    allkeysymgroups = {}
                    for keyset in self.getChildrenByType(mapobject, TOKEN_KEY):
                        try:
                            allkeysymgroups[keyset.getChild(0).getChild(0).getText()] = keyset
                        except AttributeError:
                            print "Error setting keyset:", keyset
                    sortedkeysymgroups = self.sortDict(allkeysymgroups, KeycodesReader.compare_keycode)
                    for keyset in sortedkeysymgroups:
                        elem_keysymgroup = self.getChildrenByType(keyset, ELEM_KEYSYMGROUP)
                        elem_virtualmods = self.getChildrenByType(keyset, ELEM_VIRTUALMODS)
                        elem_overlay = self.getChildrenByType(keyset, OVERLAY)
                        override = self.getChildrenListByType(keyset, OVERRIDE)
                        eTokenKey = etree.SubElement(eMapMaterial, 'tokenkey')
                        eKeyCodeName = etree.SubElement(eTokenKey, 'keycodename')
                        keycodex = self.getChildrenListByType(keyset, KEYCODEX)
                        if len(keycodex) == 1:
                            eKeyCodeName.text = keycodex[0].getChild(0).getText()
                        else:
                            return { "success": False }
                            #print "Could not retrieve keycode name"
                            #exit(-1)
                        if len(override) == 1:
                            eTokenKey.attrib['override'] = "True"
                        else:
                            eTokenKey.attrib['override'] = "False"
                        if len(self.getChildrenListByType(keyset, ELEM_KEYSYMGROUP)):
                            elem_keysyms = self.getChildrenListByType(keyset, ELEM_KEYSYMS)
                            eKeySymGroup = etree.SubElement(eTokenKey, 'keysymgroup')
                            keysymgroup_counter = len(self.getChildrenListByType(keyset, ELEM_KEYSYMGROUP))
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
                                    """ We are probably processing level3; we keep first item """
                                    ksname = elem_keysyms[0].getChild(0).getText()
                                    eKeySyms = etree.SubElement(eKeySymGroup, 'typegroup', value=ksname[1:-1])
                                    #print "Possibly processing level3"
                        if len(self.getChildrenListByType(keyset, ELEM_VIRTUALMODS)):
                            for vmods in elem_virtualmods:
                                etree.SubElement(eKeySymGroup, 'tokenvirtualmodifiers', value=vmods.getChild(0).getText())
                        if len(self.getChildrenListByType(keyset, OVERLAY)):
                            for elem in elem_overlay:
                                for elem2 in self.getChildrenByType(elem, KEYCODEX):
                                    pass
                else:
                    return { "success": False }
                    #print "\tInternal error at map level,", mapobject.getText()
                    # sys.exit(-2)
                    
        return { "success": True, "variants": variants, "layout": layout }



################################################################################
# xkb_symbols "basic" {
#    name[Group1]= "USA";
#    include "latin"
#    include "kpdl(comma)
#    include "level3(ralt_switch)"
#
#    // Alphanumeric section
#    key <TLDE> {        [     grave,    asciitilde      ]       };
#    key <AE01> {        [         1,    exclam          ]       };
#    key <AE02> {        [         2,    at              ]       };
# };

# Algorigth
#   1. Collect include statements
#   2. Parse include files
#
    def parse_layout_controller(self, store_keydict, xkbfilename, variantname = None):
        self.parse_layout_recursive(store_keydict, xkbfilename, variantname, start = True)
        return store_keydict
    
    def parse_layout_recursive(self, store_keydict, xkbfilename, variantname = None, start = True):
        #print "Processing", os.path.basename(xkbfilename), "..."
        parsed_layout = self.parse_layout_slave(xkbfilename, variantname)
        
        #print "############# ", xkbfilename, variantname, "Looping for", parsed_layout['variants']
        for includefile in parsed_layout['variants']:
            #print "  Doing includefile:", includefile
            include_components = Common.parseIncludeString(includefile)
            if include_components['variant'] == '':
                #print "    variant was empty", 
                include_parse_result = self.parse_layout(xkbfilename)
                include_components['variant'] = include_parse_result["variants"][0]
                #print "    we fix to", include_components

            #print "  Calling ourselves", Common.symbolsdir + include_components['filename'], include_components['variant']
            new_parsed_layout = self.parse_layout_recursive(store_keydict, 
                                        Common.symbolsdir + include_components['filename'], 
                                        include_components['variant'],
                                        True)
            #print "  new_parsed_result for variantname", include_components['variant'], " is ", new_parsed_layout
            if new_parsed_layout.has_key('keydict'):
                #print "    LINES:", len(new_parsed_layout['keydict'].keys())
                for k in new_parsed_layout['keydict'].keys():
                    for i in parsed_layout['keydict'][k].keys():
                        #print parsed_layout['keydict'][k][i].getPValue(),
                        if store_keydict.has_key(k) == False:
                            store_keydict[k] = {}
                        store_keydict[k][i] = copy.copy(new_parsed_layout['keydict'][k][i])
                            #print

        #extraction_result = ExtractVariantsKeycodes(parsed_layout['layout'], variantname)
        if start == True:
            #print "parsed_result for variantname", variantname, " is ", parsed_layout
            if parsed_layout.has_key('keydict'):
                #print "    LINES:", len(parsed_layout['keydict'].keys())
                for k in parsed_layout['keydict'].keys():
                    #print k,
                    for i in parsed_layout['keydict'][k].keys():
                        #print parsed_layout['keydict'][k][i].getPValue(),
                        if store_keydict.has_key(k) == False:
                            store_keydict[k] = {}
                        store_keydict[k][i] = copy.copy(parsed_layout['keydict'][k][i])
                            #print
                
        return { 'success': True, 'layout': parsed_layout['layout'], 'variants': parsed_layout['variants'] }
    
    def parse_layout_slave(self, xkbfilename, variantname = None):
        #print "+++++We are recursive, called with", xkbfilename, variantname
        char_stream = antlr3.ANTLRFileStream(xkbfilename, encoding='utf-8')
        lexer = XKBGrammarLexer(char_stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = XKBGrammarParser(tokens)

        parser_layout = parser.layout()
        variants = []

        xml_layout = etree.Element('layout')
        xml_layout.attrib['layoutname'] = os.path.basename(xkbfilename)
        
        includes = []

        for symbols in parser_layout.tree.getChildren():
            eSymbol = etree.SubElement(xml_layout, 'symbols')
            for mapobject in symbols.getChildren():
                if mapobject.getType() == MAPTYPE:
                    for maptypesect in mapobject.getChildren():
                        if maptypesect.getType() == MAPOPTIONS:
                            for mapoption in maptypesect.getChildren():
                                if mapoption.getText() == 'xkb_symbols' or mapoption.getText() == 'hidden':
                                    eMapOption = etree.SubElement(eSymbol, 'mapoption')
                                    eMapOption.text = mapoption.getText()
                        elif maptypesect.getType() == MAPNAME:
                            if maptypesect.getChildCount() == 1:
                                eMapName = etree.SubElement(eSymbol, 'mapname')
                                eMapName.text = maptypesect.getChildren()[0].getText()[1:-1]
                                variants.append(maptypesect.getChildren()[0].getText()[1:-1])
                            else:
                                return { "success": False }
                        else:
                            return { "success": False }
                elif mapobject.getType() == MAPMATERIAL:
                    eMapMaterial = etree.SubElement(eSymbol, 'mapmaterial')
                    for name in self.getChildrenByType(mapobject, TOKEN_NAME):
                        nameText = name.getChild(0).getText()[1:-1]
                        eTokenName = etree.SubElement(eMapMaterial, 'tokenname', name=nameText ) 
                    for include in self.getChildrenByType(mapobject, TOKEN_INCLUDE):
                        eInclude = etree.SubElement(eMapMaterial, 'tokeninclude')
                        eInclude.text = include.getChild(0).getText()[1:-1]
                        includes.append(eInclude.text)
                    for keytype in self.getChildrenByType(mapobject, TOKEN_KEY_TYPE):
                        keytypeText = keytype.getChild(0).getText()
                        eKeyType = etree.SubElement(eMapMaterial, 'tokentype')
                        eKeyType.text = keytypeText[1:-1]
                    for modmap in self.getChildrenByType(mapobject, TOKEN_MODIFIER_MAP):
                        eModMap = etree.SubElement(eMapMaterial, 'tokenmodifiermap', state=modmap.getChild(0).getText())
                        for modstate in self.getChildrenByTypes(modmap, KEYCODE, KEYCODEX):
                            if modstate.getType() == KEYCODE:
                                  eModState = etree.SubElement(eModMap, "keycode", value=modstate.getChild(0).getText())
                            elif modstate.getType() == KEYCODEX:
                                eModState = etree.SubElement(eModMap, "keycodex", value=modstate.getChild(0).getText())
                            else:
                                return { "success": False }
                                # print "Unexpected token encountered. Aborting...", modstate.getText()
                                # sys.exit(-1)
                    allkeysymgroups = {}
                    for keyset in self.getChildrenByType(mapobject, TOKEN_KEY):
                        allkeysymgroups[keyset.getChild(0).getChild(0).getText()] = keyset
                    sortedkeysymgroups = self.sortDict(allkeysymgroups, KeycodesReader.compare_keycode)
                    for keyset in sortedkeysymgroups:
                        elem_keysymgroup = self.getChildrenByType(keyset, ELEM_KEYSYMGROUP)
                        elem_virtualmods = self.getChildrenByType(keyset, ELEM_VIRTUALMODS)
                        elem_overlay = self.getChildrenByType(keyset, OVERLAY)
                        override = self.getChildrenListByType(keyset, OVERRIDE)
                        eTokenKey = etree.SubElement(eMapMaterial, 'tokenkey')
                        eKeyCodeName = etree.SubElement(eTokenKey, 'keycodename')
                        keycodex = self.getChildrenListByType(keyset, KEYCODEX)
                        if len(keycodex) == 1:
                            eKeyCodeName.text = keycodex[0].getChild(0).getText()
                        else:
                            return { "success": False }
                            #print "Could not retrieve keycode name"
                            #exit(-1)
                        if len(override) == 1:
                            eTokenKey.attrib['override'] = "True"
                        else:
                            eTokenKey.attrib['override'] = "False"
                        if len(self.getChildrenListByType(keyset, ELEM_KEYSYMGROUP)):
                            elem_keysyms = self.getChildrenListByType(keyset, ELEM_KEYSYMS)
                            eKeySymGroup = etree.SubElement(eTokenKey, 'keysymgroup')
                            keysymgroup_counter = len(self.getChildrenListByType(keyset, ELEM_KEYSYMGROUP))
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
                                    """ We are probably processing level3; we keep first item """
                                    ksname = elem_keysyms[0].getChild(0).getText()
                                    eKeySyms = etree.SubElement(eKeySymGroup, 'typegroup', value=ksname[1:-1])
                                    #print "Possibly processing level3"
                        if len(self.getChildrenListByType(keyset, ELEM_VIRTUALMODS)):
                            for vmods in elem_virtualmods:
                                etree.SubElement(eKeySymGroup, 'tokenvirtualmodifiers', value=vmods.getChild(0).getText())
                        if len(self.getChildrenListByType(keyset, OVERLAY)):
                            for elem in elem_overlay:
                                for elem2 in self.getChildrenByType(elem, KEYCODEX):
                                    pass
                else:
                    return { "success": False }
                    
        extraction_result = ExtractVariantsKeycodes(xml_layout, variantname)
        return { 'success': True, 
                 'all_variants': variants,
                 'variants': extraction_result['variants'], 
                 'layout': xml_layout, 
                 'keydict': extraction_result['keydict']
             }

if __name__ == '__main__':
    px = ParseXKB()

    store_keydict = {}
    px.parse_layout_controller(store_keydict, '/usr/share/X11/xkb/symbols/gr', 'polytonic')
    print "About to print"
    for k in store_keydict.keys():
        print k,
        for i in store_keydict[k].keys():
            print store_keydict[k][i].getValue(),
        print
