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
import antlr3
from KeysymsLexer import KeysymsLexer
from KeysymsParser import KeysymsParser
from KeysymsWalker import KeysymsWalker

filename = "keysymdef.h"
if len(sys.argv) > 1:
    filename = sys.argv[1]

try:    
	file = open(filename, 'r')
except OSError:
	print "Could not open file ", filename, ". Aborting..."
	sys.exit(-1)

file.close

print "Please wait; this process may take about 5s..."

char_stream = antlr3.ANTLRFileStream(filename)
lexer = KeysymsLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = KeysymsParser(tokens)

result = parser.keysym()

nodes = antlr3.tree.CommonTreeNodeStream(result.tree)
nodes.setTokenStream(tokens)
walker = KeysymsWalker(nodes)

KeysymsDB = {}

for n in result.tree.getChildren():
	if n.getText() == "KEYSYM":
		child = tuple(n.getChildren())
		if len(child) != 2:
			print "Error"
			sys.exit(-2)
		KeysymsDB[child[0].getText()[3:]] = child[1].getText()

keys = KeysymsDB.keys()
keys.sort()

outputfile = "../Keysyms.py"

try:
    f = open(outputfile, "w")
except:
    print "Error"
     
f.write("KeysymDB = {\n")
for n in keys:
	f.write("    \"" + n + "\" : " + KeysymsDB[n] + ",\n")

f.write("}\n")
print "Done."
print "The output file is", outputfile