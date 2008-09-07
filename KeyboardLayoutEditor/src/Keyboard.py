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
import gtk
import gobject
import cairo
from lxml import etree

import Common
import Key
import GenericLayout
from ParseXML import ParseXML
from KeyDict import KeyDict, included_files, activated_variants

class Keyboard(gtk.Frame):
    __gtype_name__ = 'Keyboard'
    
    SPACING = 5

    def __init__(self, layout):
        gtk.Frame.__init__(self)
        self.connect("expose_event", self.expose)

        # This is a GenericLayout object, created in KeyboardLayoutEditor.
        self.xmllayout = layout
        
        self.layoutcode = ""
        self.layoutvariant = ""
        self.layoutname = ""

        KeyDict.set()

        # Fill in the KeyDict structure with xml branches
        for key in KeyDict.Keys.keys():
            if self.xmllayout.exists_tokenkey(key):
                print "Key", key, "already exists in xmllayout."
                if KeyDict.Keys[key].xmlbranch == None:
                    print "Key", key, "was not set, setting now"
                elif KeyDict.Keys[key].xmlbranch != xmllayout.return_tokenkey(key):
                    print "Key", key, "already set to something..."
                else:
                    KeyDict.Keys[key].xmlbranch = xmllayout.create_tokenkey(key)
            elif self.xmllayout.create_tokenkey(key) != None:
                pass
                #print "Added", key
            else:
                SystemError("Unable to add " + key)
            
        #print self.xmllayout.tostring()
        
        self.set_label("")
        self.set_shadow_type(gtk.SHADOW_NONE)

        __row1 = ("ESC" , "FK01", "FK02", "FK03", "FK04", "FK05", "FK06", "FK07", "FK08", "FK09", "FK10", "FK11", "FK12")
        __row1_esc = ("ESC",)
        __row1_f14 = ("FK01", "FK02", "FK03", "FK04")
        __row1_f58 = ("FK05", "FK06", "FK07", "FK08")
        __row1_f92 = ("FK09", "FK10", "FK11", "FK12")

        __row2 = ("TLDE", "AE01", "AE02", "AE03", "AE04", "AE05", "AE06", "AE07", "AE08", "AE09", "AE10", "AE11", "AE12", "BKSP")
        __row3 = ("TAB" , "AD01", "AD02", "AD03", "AD04", "AD05", "AD06", "AD07", "AD08", "AD09", "AD10", "AD11", "AD12", "BKSL")
        __row4 = ("CAPS", "AC01", "AC02", "AC03", "AC04", "AC05", "AC06", "AC07", "AC08", "AC09", "AC10", "AC11", "RTRN")
        __row5 = ("LFSH", "LSGT", "AB01", "AB02", "AB03", "AB04", "AB05", "AB06", "AB07", "AB08", "AB09", "AB10", "RTSH")
        __row6 = ("LCTL", "LWIN", "LALT", "SPCE", "RALT", "RWIN", "MENU", "RCTL")

        vbox = gtk.VBox(False,  Keyboard.SPACING)
        
        hbox1 = gtk.HBox(False, Keyboard.SPACING)
        hbox2 = gtk.HBox(False, Keyboard.SPACING)
        hbox3 = gtk.HBox(False, Keyboard.SPACING)
        hbox4 = gtk.HBox(False, Keyboard.SPACING)
        hbox5 = gtk.HBox(False, Keyboard.SPACING)
        hbox6 = gtk.HBox(False, Keyboard.SPACING)

        hboxtop_esc = gtk.HBox(False, Keyboard.SPACING)
        hboxtop_f14 = gtk.HBox(False, Keyboard.SPACING)
        hboxtop_f58 = gtk.HBox(False, Keyboard.SPACING)
        hboxtop_f92 = gtk.HBox(False, Keyboard.SPACING)
        aligntop_esc = gtk.Alignment( 0, 0, .1, 1)
        aligntop_f14 = gtk.Alignment(.1, 0, .5, 1)
        aligntop_f58 = gtk.Alignment(.8, 0, .5, 1)
        aligntop_f92 = gtk.Alignment( 1, 0, .4, 1)
        aligntop_esc.add(hboxtop_esc)
        aligntop_f14.add(hboxtop_f14)
        aligntop_f58.add(hboxtop_f58)
        aligntop_f92.add(hboxtop_f92)
        hbox1.pack_start(aligntop_esc, expand=True, fill=True)        
        hbox1.pack_start(aligntop_f14, expand=True, fill=True)        
        hbox1.pack_start(aligntop_f58, expand=True, fill=True)        
        hbox1.pack_start(aligntop_f92, expand=True, fill=True)        

        vbox.pack_start(hbox1, expand=True, fill=True)
        vbox.pack_start(hbox2, expand=True, fill=True)
        vbox.pack_start(hbox3, expand=True, fill=True)
        vbox.pack_start(hbox4, expand=True, fill=True)
        vbox.pack_start(hbox5, expand=True, fill=True)
        vbox.pack_start(hbox6, expand=True, fill=True)

        for item in __row1_esc:
            hboxtop_esc.pack_start(KeyDict.Keys[item], expand=True, fill=True)
        for item in __row1_f14:
            hboxtop_f14.pack_start(KeyDict.Keys[item], expand=True, fill=True)
        for item in __row1_f58:
            hboxtop_f58.pack_start(KeyDict.Keys[item], expand=True, fill=True)
        for item in __row1_f92:
            hboxtop_f92.pack_start(KeyDict.Keys[item], expand=True, fill=True)

        for item in __row2:
            hbox2.pack_start(KeyDict.Keys[item],  expand=True, fill=True)
        for item in __row3:
            hbox3.pack_start(KeyDict.Keys[item],  expand=True, fill=True)
        for item in __row4:
            hbox4.pack_start(KeyDict.Keys[item],  expand=True, fill=True)
        for item in __row5:
            hbox5.pack_start(KeyDict.Keys[item],  expand=True, fill=True)
        for item in __row6:
            hbox6.pack_start(KeyDict.Keys[item],  expand=True, fill=True)
            
        self.add(vbox)

    def draw(self, context):
        pass    

    def expose(self, widget, event):
        self.context = widget.window.cairo_create()

        # set a clip region for the expose event
        self.context.rectangle(event.area.x, event.area.y,
                                       event.area.width, event.area.height)
        self.context.clip()
        self.draw(self.context)

        return False
    
    def receiveCallback(widget, context, x, y, selection, targetType, time):
        print "Keyboard: Received a callback for", selection, "at", x, y, "at", time

    def redraw(self):
        for keycode in KeyDict.Keys.keys():
            KeyDict.Keys[keycode].key.extract_display_keyvalues()
            KeyDict.Keys[keycode].key.redraw()

    def save(self, layout_file):
        try:
            fout = open(layout_file, "w")
        except IOError, e:
            return False

        self.gl_layout = GenericLayout.GenericLayout()
        newxml = self.gl_layout.create_layout(self.layoutcode, 
                                              self.layoutvariant, 
                                              self.layoutname, 
                                              KeyDict.Keys)
        fout.write(Common.layout_preamble)
        ParseXML(newxml, fout)
        fout.close()
        
        return True

