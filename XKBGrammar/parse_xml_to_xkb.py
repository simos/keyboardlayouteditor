#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 0.8

import sys
import os.path
import pdb
import antlr3
from lxml import etree

xmlfilename = "xkbsample.xml"
if len(sys.argv) > 1:
    xmlfilename = sys.argv[1]

try:    
	xmlfile = open(xmlfilename, 'r')
	xmlfile.close
except OSError:
	print "Could not open file ", xmlfilename, ". Aborting..."
	sys.exit(-1)


doc = etree.parse(xmlfilename)

# for elem in doc.getiterator():
#	print elem.tag, "has", len(elem), "children", elem.attrib, elem.text

TABS="\t\t\t\t\t\t\t\t\t\t\t\t"

xkbfilename = os.path.basename(xmlfilename)[:-4]
fout = open(xkbfilename, "w")

def recurse_tree(node, depth):
	if node.tag == "layout":
		print "Parsing", node.attrib["layoutname"]
		for n in node:
			recurse_tree(n, depth+1)
	elif node.tag == "symbols":
		for k in node:
			if k.tag == "mapoption":
				fout.write(k.text)
				fout.write(" ")
			elif k.tag == "mapname":
				fout.write("\"%(s)s\"\n{\n" % { "s": k.text })
			elif k.tag == "mapmaterial":
				for t in k:
					if t.tag == "tokenname":
						fout.write("\tname = \"%(s)s\";\n" % { "s": t.attrib["name"] })
					elif t.tag == "tokeninclude":
						fout.write("\tinclude \"%(s)s\"\n" % { "s": t.text })
					elif t.tag == "tokentype":
						fout.write("\tkey.type = \"%(s)s\";\n" % { "s": t.text })
					elif t.tag == "tokenmodifiermap":
						fout.write("\tmodifier_map %(s)s {" % { "s": t.attrib['state'] })
						count_mm = len(t)
						for mm in t:
							if mm.tag == "keycodex":
								fout.write("<%(s)s>" % { "s": mm.attrib["value"] })
							elif mm.tag == "keycode":
								fout.write("%(s)s" % { "s": mm.attrib["value"] })
							if count_mm > 1:
								fout.write(", ")
							count_mm -= 1
						fout.write("};\n")
								
					elif t.tag == "tokenkey": 
						fout.write("\t")
						if t.attrib["override"] == "True":
							fout.write("override")
						for tk in t:
							if tk.tag == "keycodename":
								fout.write("key <%(s)s> { " % { "s": tk.text })
							elif tk.tag == "keysymgroup":
								gotitem = False
								for ks in tk:
									if ks.tag == "typegroup":
										if gotitem:
											fout.write(", ")
										fout.write("type = \"%(s)s\" " % { "s": ks.attrib["value"] })
										gotitem = True
									elif ks.tag == "tokenvirtualmodifiers":
										if gotitem:
											fout.write(", ")
										fout.write("virtualMods = %(s)s " % { "s": ks.attrib["value"] })
									elif ks.tag == "symbolsgroup":
										if gotitem:
											fout.write(", ")
										gotitem = True
										fout.write("[ ")
										count_sg = len(ks)
										for sg in ks:
											if sg.tag == "symbol":
												if count_sg > 1:
													fout.write("%(s)s, " % { "s": sg.text })
												else:
													fout.write("%(s)s " % { "s": sg.text })
												count_sg -= 1
											else:
												print "ERROR"
												sys.exit(-1)
										fout.write("]")
								fout.write(" };\n")
		fout.write("};\n\n")

recurse_tree(doc.getroot(), 0)
