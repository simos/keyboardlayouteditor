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

import gtk
import gobject

import Common
import DumbKey
import KeyValue
from KeyDict import KeyDict

class Key(gtk.EventBox):                                                                          
    TARGET_TYPE_TEXT = 80
    __toKey__ = [ ( "text/plain", 0, TARGET_TYPE_TEXT ) ]
    
    def __init__(self, size = 1, keycode = None, vertical = False, 
                 keytype = Common.keytypes.SIMPLE, 
                 level1 = '', level2 = '', level3 = '', level4 = ''):
        gtk.EventBox.__init__(self)

        self.keycode = keycode
        #print "Key: Invoked __init__(), level1:", level1

        self.key = DumbKey.DumbKey(size, keycode, vertical, keytype, 
                                   level1, level2, level3, level4)
        self.add(self.key)
        self.set_events(gtk.gdk.BUTTON_PRESS_MASK)
        self.connect("button_press_event", self.button_press_event_callback)
        self.connect("button_release_event", self.button_release_event_callback)

        # Initialise the context menu
        self.context_menu = gtk.Menu()
        self.context_menu_item = gtk.MenuItem("Remove")
        self.context_menu.add(self.context_menu_item)
        self.context_menu_item.connect("activate", self.menu_item_activate_callback, 
                                       "remove")
        self.context_menu.connect("selection-done", self.menu_selection_done_callback)
        self.context_menu.show_all()
        
        # Adding DnD support
        if self.keycode not in KeyDict.IgnoreKeys:
            self.connect("drag_data_received", self.drag_data_get_callback)
            self.drag_dest_set(gtk.DEST_DEFAULT_MOTION |
                           gtk.DEST_DEFAULT_HIGHLIGHT |
                           gtk.DEST_DEFAULT_DROP,
                           self.__toKey__, gtk.gdk.ACTION_COPY)
        
            self.add_events(self.get_events() | gtk.gdk.EXPOSURE_MASK
                                | gtk.gdk.BUTTON1_MOTION_MASK | gtk.gdk.BUTTON_PRESS_MASK
                                | gtk.gdk.POINTER_MOTION_MASK | gtk.gdk.DRAG_MOTION
                                | gtk.gdk.DROP_FINISHED | gtk.gdk.DRAG_STATUS | gtk.gdk.ENTER_NOTIFY
                                | gtk.gdk.DRAG_ENTER)
            # self.connect("motion-notify-event", self.mouse_move_signal)
            self.connect("enter_notify_event", self.enter_notify_callback)
            self.connect("leave_notify_event", self.leave_notify_callback)
            self.connect("drag_drop", self.drag_drop_callback)
            self.connect("drag_motion", self.drag_motion_callback)
            self.connect("drag_leave", self.drag_leave_callback)
        self.tooltips = gtk.Tooltips()
        self.tooltips.set_tip(self, "Keycode: " + self.keycode)
        
    def drag_data_get_callback(self, widget, context, x, y, selection, targetType, time):
        #print "Callback drag_data_get: Received a callback for '%(str)s', segment: %(s)d at %(x)d, %(y)d" % \
        #                  { "s": self.key.pending["keysegment"], "str": selection.data.decode('utf-8'), "x": x, "y": y }
        if selection.data[0] == '\\' and \
              (selection.data[1] == 'u' or selection.data[1] == 'U'):
            newval = selection.data.decode('unicode-escape')
        else:
            newval = selection.data
        self.key.pending["ispending"] = True
        self.key.pending["value"] = newval
        #print "drag_data_get"
        #print "self.key.pending[\"keysegment\"]:", self.key.pending["keysegment"]
        self.key.keyvalues[self.key.pending["keysegment"]].add(newval)
        self.key.extract_display_keyvalues()
        self.key.redraw()
        self.set_tooltip()
        Common.addtostatusbar('Added ' + newval + ' to key ' + self.keycode + \
                              ', at level ' + str(self.key.pending["keysegment"]))
        
    def mouse_move_callback(self, widget, event):
        pass
    
    def enter_notify_callback(self, widget, event):
        #print "enter_notify"
        self.key.do_highlight(True)
        self.set_tooltip()

    def leave_notify_callback(self, widget, event):
        #self.key.infowin.hide()
        #print "leave_notify"
        self.key.do_highlight(False, event.x, event.y)

    def drag_drop_callback(self, widget, drag_context, x, y, timestamp):
        # print "drag_drop"
        pass

    def drag_motion_callback(self, widget, drag_context, x, y, timestamp):
        #print "drag_motion"
        self.key.highlight = True
        self.key.do_highlight(True, x, y)
        self.key.pending["keysegment"] = self.find_highlighted_segment(x, y)
        
    def drag_leave_callback(self, widget, drag_context, timestamp):
        #print "drag_leave"
        self.key.highlight = False
        self.key.do_highlight(False)

    def button_press_event_callback(self, widget, event):
        if self.keycode not in KeyDict.IgnoreKeys:
            if (event.button == 3):
                self.key.popup_highlight = True
                self.context_menu.popup(None, None, None, event.button, event.time)
                self.key.pending["keysegment"] = self.find_highlighted_segment(event.x, event.y)
                # Tell calling code that we have handled this event.
                return True
        
        # Tell calling code we have not handled this code; pass it on
        return False

    def button_release_event_callback(self, widget, event):
        self.key.popup_highlight = False

    def menu_selection_done_callback(self, menushell):
        """ Dehighlight highlighted segment """
        self.key.popup_highlight = False
        self.key.redraw()

    def menu_item_activate_callback(self, menuitem, action):
        if action == "remove":
            self.key.keyvalues[self.key.pending["keysegment"]].add('')
            self.key.extract_display_keyvalues()
            self.set_tooltip()
            self.key.redraw()
        
    def myname(self):
        return "[%(k1)s, %(k2)s, %(k3)s, %(k4)s]" % \
               { "k1": self.key.keyvalues[Common.keysegments.ONE].getValue(), 
                 "k2": self.key.keyvalues[Common.keysegments.TWO].getValue(), 
                 "k3": self.key.keyvalues[Common.keysegments.THREE].getValue(), 
                 "k4": self.key.keyvalues[Common.keysegments.FOUR].getValue()
               }
            
    def find_highlighted_segment(self, x, y):
        dummy, dummy, width, height = self.get_allocation()
        #print "find:", width, height, x, y
        if x != -1 and y != -1:
            if x <= width/2:
                if y <= height/2:
                    return Common.keysegments.TWO
                else:
                    return Common.keysegments.ONE
            elif y <= height/2:
                    return Common.keysegments.FOUR
            else:
                    return Common.keysegments.THREE
        else:
            return Common.keysegments.NONE

    def set_tooltip(self):
        tooltip_string = 'Keycode: ' + self.keycode
        counter_empty = 0
        for counter in Common.keysegmentslist:
            if self.key.dvalues[counter].getType() == Common.keyvaluetype.NOSYMBOL:
                counter_empty +=1
        if counter_empty < len(Common.keysegmentslist):
            for counter in Common.keysegmentslist:
                tooltip_string += '\n' + str(counter) + '. ' +\
                            str(self.key.dvalues[counter].getValue()) + '  ' +\
                            self.key.dvalues[counter].getPValue()
        self.tooltips.set_tip(self, tooltip_string)
