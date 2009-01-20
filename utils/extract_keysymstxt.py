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
import string

keysymdb = {}
keysymdbbyvalue = {}

preamble = """#!/usr/bin/env python
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

"""

insteadofmain = """
if __name__ == "__main__":
    pass
"""

def process_keysymstxt():
    """ Grabs and opens the keysyms.txt file that Markus Kuhn maintains """
    """ This file keeps a record between keysyms <-> unicode chars """
    filename_keysymstxt = "keysyms.txt"
    try:
            keysymstxt = open(filename_keysymstxt, 'r')
    except IOError, (errno, strerror):
            print "I/O error(%s): %s, %s" % (errno, strerror, filename_keysymstxt)
            sys.exit(- 1)
    except:
            print "Unexpected error: ", sys.exc_info()[0]
            sys.exit(- 1)

    """ Parse the keysyms.txt file and place content in  keysymdb """
    linenum_keysymstxt = 0
    for line in keysymstxt.readlines():
            linenum_keysymstxt += 1
            line = line.strip()
            if line == "" or re.match('^#', line):
                    continue
            components = re.split('\s+', line)
            if len(components) < 5:
                    print "Invalid line %(linenum)d in %(filename)s: %(line)s'"\
                    % {'linenum': linenum_keysymstxt, 'filename': filename_keysymstxt, 'line': line}
                    print "Was expecting 5 items in the line"
                    sys.exit(-1)
            if components[1][0] == 'U' and re.match('[0-9a-fA-F]+$', components[1][1:]):
                    unival = string.atoi(components[1][1:], 16)
            if unival == 0:
                    continue
            keysymdb[components[4]] = unival
            keysymdbbyvalue[unival] = components[4]
    keysymstxt.close()

    """ Patch up the keysymdb with some of our own stuff """

    """ This is preferential treatment for Greek """
    """ => we get more savings if used for Greek """
    # keysymdb['dead_tilde'] = 0x342                

def write_files():
    process_keysymstxt()

    keys = keysymdb.keys()
    keys.sort()

    outputfile = "../KeysymsUni.py"

    try:
        f = open(outputfile, "w")
    except:
        print "Error opening file", outputfile
     
    f.write(preamble)
    f.write("KeysymsUni = {\n")
    for n in keys:
        f.write("    \"" + n + "\" : " + "0x%X" % keysymdb[n] + ",\n")

    f.write("}\n")
    print "Done."
    print "The output file is", outputfile

    f.write(insteadofmain)
    f.close()

    codepoints = keysymdbbyvalue.keys()
    codepoints.sort()
    outputfile = "../KeysymsUniByValue.py"

    try:
        f = open(outputfile, "w")
    except:
        print "Error opening file", outputfile

    f.write(preamble)
    f.write("KeysymsUniByValue = {\n")
    for n in codepoints:
        f.write("    0x" + ("%X" % n) + " : \"" + keysymdbbyvalue[n] + "\",\n")

    f.write("}\n")
    f.write(insteadofmain)
    f.close()
    print "Done."
    print "The output file is", outputfile

if __name__ == "__main__":
    write_files()

