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

import Common
from lxml import etree
from KeyDict import KeyDict, included_files, activated_variants

# <layout layoutname="CHANGEME">
#  <symbols>
#    <mapoption/>
#    <mapname/>
#    <mapmaterial>
#      <tokenname name="CHANGEME"/>
#      <tokeninclude/>
#      <tokenkey override="CHANGEME">
#        <keycodename/>
#        <keysymgroup/>
#        <symbolsgroup>
#          <symbol/>
#          <symbol/>
#          <symbol/>
#          <symbol/>
#        </symbolsgroup>
#      </tokenkey>
#    </mapmaterial>
#  </symbols>
#</layout>


class GenericLayout:
    def __init__(self): 
        self.generic_layout = etree.Element("layout", layoutname = "CHANGEME")

        self.symbols = etree.SubElement(self.generic_layout, "symbols")

        self.mapoption = etree.SubElement(self.symbols, "mapoption")
        self.mapname = etree.SubElement(self.symbols, "mapname")
        self.mapmaterial = etree.SubElement(self.symbols, "mapmaterial")

        self.tokenname = etree.SubElement(self.mapmaterial, "tokenname")
        self.tokenname.attrib["name"] = "CHANGEME"
        self.tokinclude = etree.SubElement(self.mapmaterial, "tokeninclude")

        """for keycodename in KeyDict.Keys.keys():
            self.tokenkey = etree.SubElement(self.mapmaterial, "tokenkey")
            self.tokenkey.attrib["override"] = "False"

            self.keycodename = etree.SubElement(self.tokenkey, "keycodename")
            self.keycodename.text = keycodename
            self.keysymgroup = etree.SubElement(self.tokenkey, "keysymgroup")

            self.symbolsgroup = etree.SubElement(self.tokenkey, "symbolsgroup")

            for counter in range(Common.LEVELS):
                etree.SubElement(self.symbolsgroup, "symbol")
        """
        
    def create_layout(self, layoutcode, layoutvariant, layoutname, layoutkeys):
        """ 
        Creates an lxml construct with the layout. 
        Makes use of KeyDict.included_files, KeyDict.activated_variants 
        """
        self.new_layout = etree.Element("layout", layoutname = layoutcode)

        self.symbols = etree.SubElement(self.new_layout, "symbols")

        self.mapoption = etree.SubElement(self.symbols, "mapoption")
        self.mapoption.text = "xkb_symbols"
        self.mapname = etree.SubElement(self.symbols, "mapname")
        self.mapname.text = layoutvariant
        self.mapmaterial = etree.SubElement(self.symbols, "mapmaterial")

        self.tokenname = etree.SubElement(self.mapmaterial, "tokenname")
        self.tokenname.attrib["name"] = layoutname
        for includefile in activated_variants.keys():
            for variant in activated_variants[includefile].keys():
                self.tokinclude = etree.SubElement(self.mapmaterial, "tokeninclude")
                self.tokinclude.text = includefile + '(' + variant + ')'

        for keycodename in layoutkeys.keys():
            if keycodename in KeyDict.IgnoreKeys:
                #print "keycodename", keycodename, "is in ignorekeys"
                continue
            votes_empty = 0
            for counter in Common.keysegmentslist:
                if layoutkeys[keycodename].key.keyvalues[counter].getType() == Common.keyvaluetype.NOSYMBOL:
                    votes_empty += 1
            if votes_empty == len(Common.keysegmentslist):
                # print "Keycode", keycodename, "is empty, skipping"
                continue
            else: 
                # print keycodename, "we only had", votes_empty, "votes,"
                for counter in Common.keysegmentslist:
                    pass
                    #print layoutkeys[keycodename].key.keyvalues[counter].getValue(),
                #print
            #print layoutkeys[keycodename].key.keyvalues[Common.keysegments.ONE].getValue()
            self.tokenkey = etree.SubElement(self.mapmaterial, "tokenkey")
            self.tokenkey.attrib["override"] = "False"

            self.keycodename = etree.SubElement(self.tokenkey, "keycodename")
            self.keycodename.text = keycodename
            self.keysymgroup = etree.SubElement(self.tokenkey, "keysymgroup")

            self.symbolsgroup = etree.SubElement(self.keysymgroup, "symbolsgroup")

            # print "Counting elems in key:",
            for counter in Common.keysegmentslistreverse:
                max_index = counter
                if layoutkeys[keycodename].key.keyvalues[counter].getType() == Common.keyvaluetype.NOSYMBOL:
                    #print "O",
                    continue
                else:
                    break
            #print
            #print "Doing look between", Common.keysegments.ONE, "and", max_index
            for counter in range(Common.keysegments.ONE, max_index + 1):
                sym = etree.SubElement(self.symbolsgroup, "symbol")
                sym.text = layoutkeys[keycodename].key.keyvalues[counter].getValue()
                if sym.text == "":
                    sym.text = "NoSymbol"

                # print "sym.text", sym.text
        return self.new_layout
    
    def create_tokenkey(self, keycodenametext):
        if not self.exists_tokenkey(keycodenametext):
            tokenkey = etree.SubElement(self.mapmaterial, "tokenkey")
            tokenkey.attrib["override"] = "False"

            keycodename = etree.SubElement(tokenkey, "keycodename")
            keycodename.text = keycodenametext
            keysymgroup = etree.SubElement(tokenkey, "keysymgroup")

            symbolsgroup = etree.SubElement(tokenkey, "symbolsgroup")

            for counter in Common.keysegmentslist:
                etree.SubElement(symbolsgroup, "symbol")
            return tokenkey
        else:
            return None

    def return_tokenkey(self, keycode):
        all_tokenkeys = self.generic_layout.findall(".//tokenkey")
        if all_tokenkeys == []:
            return None
        for tk in all_tokenkeys:
            keycodenames = tk.findall(".//keycodename")
            if keycodenames == []:  
                SystemError("Internal error, expecting a keycodename")
            if len(keycodenames) > 1:
                SystemError("Internal error, expecting only one keycodename")
            if keycodenames[0].text == keycode:
                return tk

    def exists_tokenkey(self, keycode):
        all_tokenkeys = self.generic_layout.findall(".//tokenkey")
        if all_tokenkeys == []:
            return False
        for tk in all_tokenkeys:
            keycodenames = tk.findall(".//keycodename")
            if keycodenames == []:  
                SystemError("Internal error, expecting a keycodename")
            if len(keycodenames) > 1:
                SystemError("Internal error, expecting only one keycodename")
            if keycodenames[0].text == keycode:
                return True
            else:
                return False
                
    def tostring(self):
        return etree.tostring(self.generic_layout, pretty_print = True)
    
if __name__ == "__main__":
    gl = GenericLayout()
    print gl.tostring()
