#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 0.8

import sys
import os.path
import pdb
import antlr3
from lxml import etree

xkbfilename = "xkbsample.xml"
if len(sys.argv) > 1:
    xkbfilename = sys.argv[1]

try:    
	xkbfile = open(xkbfilename, 'r')
	xkbfile.close
except OSError:
	print "Could not open file ", xkbfilename, ". Aborting..."
	sys.exit(-1)


doc = etree.parse(xkbfilename)

# for elem in doc.getiterator():
#	print elem.tag, "has", len(elem), "children", elem.attrib, elem.text

TABS="\t\t\t\t\t\t\t\t\t\t\t\t"

def recurse_tree(node, depth):
	if node.tag == "layout":
		print "Filename: ", node.attrib["layoutname"]
		for n in node:
			recurse_tree(n, depth+1)
	elif node.tag == "symbols":
		for k in node:
			if k.tag == "mapoption":
				print k.text,
			elif k.tag == "mapname":
				print "\"%(s)s\"\n{" % { "s": k.text }
			elif k.tag == "mapmaterial":
				for t in k:
					if t.tag == "tokenname":
						print "\tname = \"%(s)s\";" % { "s": t.attrib["name"] }
					elif t.tag == "tokeninclude":
						print "\tinclude \"%(s)s\"" % { "s": t.text }
					elif t.tag == "tokentype":
						print "\tkey.type = \"%(s)s\";" % { "s": t.text }
					elif t.tag == "tokenmodifiermap":
						print "\tmodifier_map %(s)s {" % { "s": t.attrib['state'] },
						count_mm = len(t)
						for mm in t:
							if mm.tag == "keycodex":
								print "<%(s)s>" % { "s": mm.attrib["value"] },
							elif mm.tag == "keycode":
								print "%(s)s" % { "s": mm.attrib["value"] },
							if count_mm > 1:
								sys.stdout.write(", ")
							count_mm -= 1
						print "};"
								
					elif t.tag == "tokenkey": 
						print "\t",
						if t.attrib["override"] == "True":
							print "override",	
						for tk in t:
							if tk.tag == "keycodename":
								print "key <%(s)s> {" % { "s": tk.text },
							elif tk.tag == "keysymgroup":
								gotitem = False
								for ks in tk:
									if ks.tag == "typegroup":
										if gotitem:
											sys.stdout.write(", ")
										print "type = \"%(s)s\"" % { "s": ks.attrib["value"] },
										gotitem = True
									elif ks.tag == "tokenvirtualmodifiers":
										if gotitem:
											sys.stdout.write(", ")
										print "virtualMods = %(s)s" % { "s": ks.attrib["value"] },
									elif ks.tag == "symbolsgroup":
										if gotitem:
											sys.stdout.write(", ")
										gotitem = True
										print "[",
										count_sg = len(ks)
										for sg in ks:
											if sg.tag == "symbol":
												if count_sg > 1:
													print "%(s)s," % { "s": sg.text },
												else:
													print "%(s)s" % { "s": sg.text },
												count_sg -= 1
											else:
												print "ERROR"
												sys.exit(-1)
										print "]",
								print "};"
		print "};\n"

recurse_tree(doc.getroot(), 0)
