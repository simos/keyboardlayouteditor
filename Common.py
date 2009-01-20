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

import cairo
import Enum

keytypes = Enum.Enum("SIMPLE SPECIAL").vals(illegal=255)
alignments = Enum.Enum("LEFT CENTRE RIGHT").vals(illegal=255)
keysegments = Enum.Enum("ALL ONE TWO THREE FOUR NONE").vals(illegal=255)
keyvaluetype = Enum.Enum("UNICHAR CODEPOINT KEYSYM CONSTANT DEADKEY ANY VOIDSYMBOL NOSYMBOL NOACTION VERBATIM").vals(illegal=255)

keysegmentslist = [keysegments.ONE, keysegments.TWO, 
                   keysegments.THREE, keysegments.FOUR]
keysegmentslistreverse = list(keysegmentslist)
keysegmentslistreverse.reverse()

fontname = "Sans"
fontstyle = cairo.FONT_SLANT_NORMAL
fontweight = cairo.FONT_WEIGHT_NORMAL
fontsize = 12

gucharmappath = "/usr/bin/gucharmap"

# The Xkeyboard-Config path
xkcpath = "/etc/X11/xkb"
xkcsymbols = xkcpath + "/symbols"

# The program icon
KLEiconfile = "kleiconfile.ico"

# Max levels, currently 4. May go 8 in future.
LEVELMAX = 4

# The application home directory
HOMEDIR = ''

# The application's official full name.
applicationname="Keyboard Layout Editor"

# Holds the current filename.
currentlayoutfile=''

# The directory to the xkeyboard-config base directory.
basedir = '/etc/X11/xkb/'

# The directory to the xkeyboard-config symbols directory.
symbolsdir = basedir + 'symbols/'

# A gtk.Statusbar object, shared, so that all can write to.
statusbar = None

# Default dead key.
deadkey = "dead_acute"

# Text that appears when saving a keyboard layout (appears in text file, at start
layout_preamble = """/////////////////////////////////////////////////////////////////////////////////
//
// Generated keyboard layout file with the Keyboard Layout Editor.
// For more about the software, see http://code.google.com/p/keyboardlayouteditor
//

"""

# Sorts a dictionary by value, produces a sorted list of values.
def sortDict(adict, cmp_function = None):
    keys = adict.keys()
    keys.sort(cmp_function)
    return map(adict.get, keys)

def addtostatusbar(message):
    statusbar.push(statusbar.console_context, message)

def parseIncludeString(include):
    """ 
    Parses strings of the form 'us(intl)', 'us', and produces
    { 'filename': 'us', 'variant': 'intl' }, { 'filename': 'us', 'variant': 'basic' }
    """
    if include.partition('(')[1] == '(':
        return { 'filename': include.partition('(')[0], 'variant': include.partition('(')[2].partition(')')[0] }
    else:
        return { 'filename': include.partition('(')[0], 'variant': '' }

if __name__ == '__main__':
    print parseIncludeString('us')
    print parseIncludeString('us(level1)')
    
    
