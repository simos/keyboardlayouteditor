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
import antlr3
from lxml import etree

import Common
import KeyValue

def __recurse_tree__(node, fout):
    if node.tag == "layout":
        #print "Parsing", node.attrib["layoutname"]
        for n in node:
            __recurse_tree__(n, fout)
    elif node.tag == "symbols":
        for k in node:
            if k.tag == "mapoption":
                fout.write(k.text)
                fout.write(" ")
            elif k.tag == "mapname":
                fout.write("\"%(s)s\"\n{\n" % { "s": k.text })
            elif k.tag == "mapmaterial":
                keycodedict_lines = {}
                for t in k:
                    if t.tag == "tokenname":
                        fout.write("\tname[Group1] = \"%(s)s\";\n" % { "s": t.attrib["name"] })
                    elif t.tag == "tokeninclude":
                        fout.write("\tinclude \"%(s)s\"\n" % { "s": t.text })
                    elif t.tag == "tokentype":
                        fout.write("\tkey.type = \"%(s)s\";\n" % { "s": t.text })
                    elif t.tag == "tokenmodifiermap":
                        fout.write("\tmodifier_map %(s)s { " % { "s": t.attrib['state'] })
                        count_mm = len(t)
                        for mm in t:
                            if mm.tag == "keycodex":
                                fout.write("<%(s)s>" % { "s": mm.attrib["value"] })
                            elif mm.tag == "keycode":
                                fout.write("%(s)s" % { "s": mm.attrib["value"] })
                            if count_mm > 1:
                                fout.write(", ")
                            count_mm -= 1
                        fout.write(' };\n')
                    elif t.tag == "tokenkey":
                        # We attempt to sort the keycode lines by keycode value.
                        keycodelinelist = [] 
                        keycodelinecomment = []
                        keycodelinelist.append("\t")
                        keycodelinecomment.append(" // ")
                        if t.attrib["override"] == "True":
                            keycodelinelist.append("override ")
                        for tk in t:
                            if tk.tag == "keycodename":
                                keycodelinelist.append("key <%(s)s> { " % { "s": tk.text })
                                keycodelinekeycode = tk.text
                            elif tk.tag == "keysymgroup":
                                gotitem = False
                                for ks in tk:
                                    if ks.tag == "typegroup":
                                        if gotitem:
                                            keycodelinelist.append(", ")
                                        keycodelinelist.append("type = \"%(s)s\" " % { "s": ks.attrib["value"] })
                                        gotitem = True
                                    elif ks.tag == "tokenvirtualmodifiers":
                                        if gotitem:
                                            keycodelinelist.append(", ")
                                        keycodelinelist.append("virtualMods = %(s)s " % { "s": ks.attrib["value"] })
                                    elif ks.tag == "symbolsgroup":
                                        if gotitem:
                                            keycodelinelist.append(', ')
                                        gotitem = True
                                        keycodelinelist.append('[ ')
                                        count_sg = len(ks)
                                        for sg in ks:
                                            if sg.tag == 'symbol':
                                                if count_sg > 1:
                                                    keycodelinelist.append("%(s)14s, " % { "s": sg.text })
                                                else:
                                                    keycodelinelist.append("%(s)14s " % { "s": sg.text })
                                                count_sg -= 1
                                                kval = KeyValue.KeyValue(sg.text)
                                                keycodelinecomment.append(kval.getPValue())
                                                keycodelinecomment.append(' ')
                                            else:
                                                print 'ERROR'
                                                sys.exit(-1)
                                        for spaces_count in range(Common.LEVELMAX - len(ks)):
                                            keycodelinelist.append('%(s)15s ' % { 's': ' ' })
                                        keycodelinelist.append(']')
                                keycodelinelist.append(' };')
                                keycodelinecomment.append('\n')
                                keycodedict_lines[keycodelinekeycode] = "".join(keycodelinelist) \
                                                                      + "".join(keycodelinecomment)
                keycodeslist = keycodedict_lines.keys()
                keycodeslist.sort()
                for kc in keycodeslist:
                    fout.write(keycodedict_lines[kc])
        fout.write("};\n\n")

def __extract_keycodes__(node, variants, keydict, variant):
    we_are_shooting = False
    variant_verbose_name = ''
    if node.tag == "layout":
        #print "Parsing", node.attrib["layoutname"]
        for n in node:
            result = __extract_keycodes__(n, variants, keydict, variant)
            if result != None:
                if result['done'] == True:
                    return result
            
    if node.tag == "symbols":
        for k in node:
            if k.tag == "mapoption":
                pass
            elif k.tag == "mapname":
                # If we are not processing the correct variant,
                if k.text != variant:
                    break
                else:
                    we_are_shooting = True
            elif k.tag == "mapmaterial":
                for t in k:
                    if t.tag == "tokenname":
                        variant_verbose_name = t.attrib["name"]
                    elif t.tag == "tokeninclude":
                        variants.append(t.text)
                    elif t.tag == "tokentype":
                        # t.text
                        pass
                    elif t.tag == "tokenmodifiermap":
                        pass                                
                    elif t.tag == "tokenkey": 
                        if t.attrib["override"] == "True":
                            pass
                        for tk in t:
                            if tk.tag == "keycodename":
                                keycodename = tk.text
                                keydict[keycodename] = {}
                            elif tk.tag == "keysymgroup":
                                for ks in tk:
                                    if ks.tag == "typegroup":
                                        # ks.attrib["value"]
                                        pass
                                    elif ks.tag == "tokenvirtualmodifiers":
                                        # ks.attrib["value"]
                                        pass
                                    elif ks.tag == "symbolsgroup":
                                        key_index = Common.keysegments.ONE
                                        keyvalues = {}
                                        for sg in ks:
                                            if sg.tag == "symbol":
                                                newkeyvalue = KeyValue.KeyValue(sg.text)
                                                keyvalues[key_index] = newkeyvalue
                                                key_index += 1
                                        keydict[keycodename] = keyvalues
        if we_are_shooting:
            return { 'done' : True, 'variants': variants, 'keydict': keydict, 'variant_name': variant_verbose_name }

def ParseXML(xmllayoutroot, fout):
    return __recurse_tree__(xmllayoutroot, fout)

def ExtractVariantsKeycodes(xmllayoutroot, variant):
    VariantsNew = []
    KeyDictNew = {}
    return __extract_keycodes__(xmllayoutroot, VariantsNew, KeyDictNew, variant)
    
if __name__ == "__main__":
    sourcefile = "/home/user/WORK/KEYBOARDLAYOUTEDITOR/keyboardlayouteditor/XKBGrammar/demo.xml"
    sourcefile = "/home/user/WORK/KEYBOARDLAYOUTEDITOR/keyboardlayouteditor/XKBGrammar/us.xml"
    doc = etree.parse(sourcefile)
    #print doc
    #print etree.tounicode(doc, pretty_print=True)
    #ParseXML(doc.getroot(), sys.stdout)
    print ExtractVariantsKeycodes(doc.getroot(), "euro")