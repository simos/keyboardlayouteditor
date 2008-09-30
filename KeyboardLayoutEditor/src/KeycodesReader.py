#!/usr/bin/env python
# -*- encoding: UTF-8 -*-
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#   
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#   
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import sys
import re
import antlr3

from KeycodesLexer import KeycodesLexer, KEYCODELISTTYPE, KEYCODEMATERIAL, \
                                        KEYCODELISTOPTIONS, KEYCODELISTNAME, \
                                        INCLUDE, MINIMUM, MAXIMUM, KEYCODE, \
                                        ALIAS, INDICATOR
from KeycodesParser import KeycodesParser
from KeycodesWalker import KeycodesWalker

# Global variable, we use global so that the compare function does not have to create the dictionary on every invocation.
KEYCODEDB = {}

# Helper function to iterate through all children of a given type
def getChildrenListByType(tree, type_value):
    list = []
    for i in range(tree.getChildCount()):
        child = tree.getChild(i)
        if child.getType() == type_value:
            list.append(child)
    return list


def parseFile(fileandvariant = "/usr/share/X11/xkb/keycodes/xfree86|xfree86", *morefilesandvariants):
    keycodedb = {}
    for eachfileandvariant in (fileandvariant,) + morefilesandvariants:
        filename, pipe, variant = eachfileandvariant.partition('|')

        try:    
            file = open(filename, 'r')
        except OSError:
            print "Could not open file ", filename, " Aborting..."
            sys.exit(-1)
        file.close
    
        char_stream = antlr3.ANTLRFileStream(filename)
        lexer = KeycodesLexer(char_stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = KeycodesParser(tokens)
    
        result = parser.keycodedoc()
    
        nodes = antlr3.tree.CommonTreeNodeStream(result.tree)
        nodes.setTokenStream(tokens)
        walker = KeycodesWalker(nodes)
        # walker.keycodedoc()
    
        keycodeidinclude = [variant]
    
        for itemKeycodeDoc in result.tree.getChildren():
            copying = False
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
                    if listName.getText()[1:-1] == variant or listName.getText()[1:-1] in keycodeidinclude:
                        copying = True
        
            if not copying:
                break

            for materialIncludeGroup in getChildrenListByType(material[0], INCLUDE):
                for includeName in materialIncludeGroup.getChildren():
                    includeKeycodelist = re.findall('(\w+)\((\w+)\)', includeName.getText()[1:-1])
                    if includeKeycodelist[0][1] not in keycodeidinclude:
                        keycodeidinclude.append(includeKeycodelist[0][1])
        
            for keycode in getChildrenListByType(material[0], KEYCODE):
                keycodedb[keycode.getChild(0).getText()] = keycode.getChild(1).getText()
        
            for alias in getChildrenListByType(material[0], ALIAS):
                keycodedb[alias.getChild(0).getText()] = keycodedb[alias.getChild(1).getText()]
        
            for indicator in getChildrenListByType(material[0], INDICATOR):
                pass

    return keycodedb
    
def compare_keycode(a, b):
    global KEYCODEDB
    if not KEYCODEDB.has_key(a):
        if not KEYCODEDB.has_key(b):
            return 0
        else:
            return 1
    else:
        return -1
    if KEYCODEDB[a] > KEYCODEDB[b]:
        return 1
    elif KEYCODEDB[a] < KEYCODEDB[b]:
        return -1
    else:
        return 0

def initialise():
    global KEYCODEDB

    KEYCODEDB = parseFile("/usr/share/X11/xkb/keycodes/xfree86|xfree86", 
                          "/usr/share/X11/xkb/keycodes/aliases|qwerty", 
                          "/usr/share/X11/xkb/keycodes/evdev|evdev")
    #KEYCODEDB = parseFile("evdev|evdev", "aliases|qwerty")

if __name__ == "__main__":
    KEYCODEDB = parseFile("/usr/share/X11/xkb/keycodes/xfree86|xfree86", "/usr/share/X11/xkb/keycodes/aliases|qwerty")
