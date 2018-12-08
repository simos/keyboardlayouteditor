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

import gtk
import gobject
import cairo
import copy
import pango

import Common
import KeyValue
from KeyDict import KeyDict, included_files, activated_variants

class DumbKey(gtk.DrawingArea):
    def __init__(self, size = 1, keycode = None, vertical = False, 
                 keytype = Common.keytypes.SIMPLE, 
                 level1 = '', level2 = '', 
                 level3 = '', level4 = ''):
        gtk.DrawingArea.__init__(self)
        self.connect("expose_event", self.expose)

        self.__key_width = 50
        self.keyvalues = {}
        self.dvalues = {}
        self.dvalues_inherited = {}

        self.setvalues(size, keycode, vertical, keytype, 
                       level1, level2, level3, level4)

        self.modifier = 1
        self.highlight_x = -1
        self.highlight_y = -1
        self.highlight = False
        self.pending = { "ispending": False, 
                        "keysegment": Common.keysegments.NONE,
                        "value": '', 
                        "coordinates": (-1, -1) }
        self.popup_highlight = 0
        
        self.infowin = gtk.Window()
        self.infowin.set_decorated(False)
                
    def setvalues(self, size = 1, keycode = None, vertical = False, 
                  keytype = Common.keytypes.SIMPLE, 
                  level1 = '', level2 = '', 
                  level3 = '', level4 = ''):
        self.keycode = keycode
        self.size = size
        self.vertical = vertical
        self.keytype = keytype
        if self.keycode in KeyDict.IgnoreKeys:
            self.verbatim = True
        else:
            self.verbatim = False
        self.keyvalues = { 
                        Common.keysegments.ONE:   KeyValue.KeyValue(level1.decode('utf-8'), self.verbatim), 
                        Common.keysegments.TWO:   KeyValue.KeyValue(level2.decode('utf-8'), self.verbatim),
                        Common.keysegments.THREE: KeyValue.KeyValue(level3.decode('utf-8'), self.verbatim),
                        Common.keysegments.FOUR:  KeyValue.KeyValue(level4.decode('utf-8'), self.verbatim)
                      }
        # Fills up the dvalues list with the values to display
        self.extract_display_keyvalues()

    def expose(self, widget, event):
        self.context = widget.window.cairo_create()
        self.layout= self.context.create_layout()
        
        # set a clip region for the expose event
        self.context.rectangle(event.area.x,     event.area.y,
                                       event.area.width, event.area.height)
        self.context.clip()

        self.a = self.parent.get_parent()
        self.b = self.a.parent.get_parent()
        self.set_size_request(int(self.__key_width*self.size), -1)
        self.draw(self.context)

        return False

    def draw(self, context):
        """ Draws the actual key in the widget using Cairo"""
        rect = self.get_allocation()

        """ Draw the rectangle, filling in with color """
        self.context.set_source_rgb(0.0, 0.0, 0.0)
        self.roundedrec(context, 0, 0, rect.width, rect.height, 15, 3)
                           
        if self.keytype == Common.keytypes.SIMPLE:
            context.set_source_rgb(1.0 * self.modifier, 
                                   1.0 * self.modifier, 
                                   0.9 * self.modifier)
        elif self.keytype == Common.keytypes.SPECIAL:
            context.set_source_rgb(.7 * self.modifier,
                                   .7 * self.modifier, 
                                   .5 * self.modifier)
        self.context.fill_preserve()
        self.context.stroke()

        """ Highlight the segment """
        if self.highlight or self.popup_highlight:
            self.context.set_source_rgb(1.0, 1.0, 0.6)
            self.roundedrec_segment(context, self.pending["keysegment"], 
                                    0, 0, rect.width, rect.height, 15, 3)
            self.context.fill_preserve()
            self.context.stroke()

        """ Draw the cross """
        context.set_source_rgb(.1,.1,.1)
        context.set_line_width(0.3)
        if self.dvalues[Common.keysegments.THREE].getPValue() != '' \
                or self.dvalues[Common.keysegments.FOUR].getPValue() != '':
            self.context.move_to(rect.width / 2, 0)
            self.context.line_to(rect.width / 2, rect.height)
        if self.dvalues[Common.keysegments.TWO].getPValue() != '':
            self.context.move_to(0, rect.height / 2)
            self.context.line_to(rect.width, rect.height / 2)
        self.context.stroke()

        """ Draw the four characters on the key """
        self.context.set_source_rgb(0,1,0)
        if self.dvalues[Common.keysegments.ONE].getPValue() == '':
            pass
        if self.dvalues[Common.keysegments.TWO].getPValue() == '' and \
                    self.dvalues[Common.keysegments.THREE].getPValue() == '' and \
                    self.dvalues[Common.keysegments.FOUR].getPValue() == '' \
                    or self.dvalues[Common.keysegments.THREE].getPValue() == '' and \
                    self.dvalues[Common.keysegments.FOUR].getPValue() == '':
            self.draw_character(context, self.dvalues[Common.keysegments.ONE].getPValue(), 
                                Common.alignments.LEFT, 
                                0, rect.height / 2, rect.width, rect.height / 2)
        else:
            self.draw_character(context, self.dvalues[Common.keysegments.ONE].getPValue(), 
                                Common.alignments.CENTRE, 
                                0, rect.height / 2, rect.width / 2, rect.height / 2)

        if self.dvalues[Common.keysegments.THREE].getPValue() == '' and \
                    self.dvalues[Common.keysegments.FOUR].getPValue() == '':
            self.draw_character(context, self.dvalues[Common.keysegments.TWO].getPValue(),  
                                Common.alignments.LEFT, 
                                0, 0, rect.width, rect.height / 2)
        else:
            self.draw_character(context, self.dvalues[Common.keysegments.TWO].getPValue(), 
                                Common.alignments.CENTRE, 
                                0, 0, rect.width / 2, rect.height / 2)
        self.draw_character(context, self.dvalues[Common.keysegments.THREE].getPValue(), 
                                Common.alignments.CENTRE, 
                                rect.width / 2, rect.height / 2, 
                                rect.width / 2, rect.height / 2 )
        self.draw_character(context, self.dvalues[Common.keysegments.FOUR].getPValue(), 
                            Common.alignments.CENTRE, 
                            rect.width / 2, 0, rect.width / 2, rect.height / 2)

    def draw_segment(self, segment):
        pass
    
    def draw_line(self, context, x1, y1, x2, y2):
        self.context.move_to(x1, y1)
        self.context.line_to(x2, y2)
        self.context.stroke()

    def draw_linewh(self, context, x, y, w, h):
        self.context.move_to(x, y)
        self.context.line_to(x+w, y+h)
        self.context.stroke()
            
    def draw_character(self, context, char, align, cx, cy, cwidth, cheight):
        if char == '':
            return

        # set the font and text
        self.layout.set_font_description(Common.font_desc)
        self.layout.set_text(char)

        # now calculate the position for the text based on the fonts metrics
        text_bounds = self.layout.get_pixel_size()
        twidth= text_bounds[0]
        theight= text_bounds[1]
        spacing = theight / 3

        # TODO: The font-size should be adjusted according to the available
        # space. If the rendered text is larger than the available space
        # its font-size should be reduced until it fits

        if align == Common.alignments.CENTRE:
            self.context.move_to(cx + cwidth/2  - twidth/2,
                                 cy + cheight/2 - theight/2)
        elif align == Common.alignments.LEFT:
            self.context.move_to(cx + spacing,
                                 cy + cheight - theight - spacing)
        elif align == Common.alignments.RIGHT:
            self.context.move_to(cx + cwidth  - twidth - spacing,
                                 cy + cheight - theight - spacing)
        else:
            print "Error; unknown alignment"
            sys.exit(-1)

        self.context.set_source_rgb(.30, .30, .30)
        self.context.update_layout(self.layout)
        self.context.show_layout(self.layout)
        
    def redraw(self):
        (x,y,width,height) = self.get_allocation()
        self.queue_draw_area(x, y, width, height)    
    
    def roundedrec(self, context, x, y, w, h, r = 10, line_width=1):
        "Draw a rounded rectangle (source: anonymous/pygtk website)"
        #   A****BQ
        #  H      C
        #  *      *
        #  G      D
        #   F****E

        context.set_line_width(line_width)
        context.move_to(x+r,y)                    # Move to A
        context.line_to(x+w-r,y)                # Straight line to B
        context.curve_to(x+w,y,x+w,y,x+w,y+r)    # Curve to C, Control points are both at Q
        context.line_to(x+w,y+h-r)                # Move to D
        context.curve_to(x+w,y+h,x+w,y+h,x+w-r,y+h) # Curve to E
        context.line_to(x+r,y+h)                # Line to F
        context.curve_to(x,y+h,x,y+h,x,y+h-r)    # Curve to G
        context.line_to(x,y+r)                    # Line to H
        context.curve_to(x,y,x,y,x+r,y)            # Curve to A

    def roundedrec_segment(self,context, which_segment, x, y, w, h, r = 10, 
                           line_width=1):
        "Draw a rounded rectangle (source: anonymous/pygtk website)"
        #   A****BQ
        #  H      C
        #  *      *
        #  G      D
        #   F****E

        context.set_line_width(line_width)
        if which_segment == Common.keysegments.ALL:
            self.roundedrec(context, x, y, w, h, r, line_width)
        elif which_segment == Common.keysegments.ONE:
            context.move_to(x, y + h / 2)                   # Move to GH-middle
            context.line_to(x, y + h - r)                   # Line to G
            context.curve_to(x, y + h, x, y + h, x + r, y+h)# Curve to F
            context.line_to(x + w / 2, y + h)               # Line to FE-middle
            context.line_to(x + w / 2, y + h / 2)           # Line to middle
            context.line_to(x, y + h / 2)                   # Line to GH-middle
        elif which_segment == Common.keysegments.TWO:
            context.move_to(x, y + h / 2)                   # Move to GH-middle
            context.line_to(x, y + r)                       # Line to H
            context.curve_to(x, y, x, y, x + r, y)          # Curve to A
            context.line_to(x + w / 2, y)                   # Line to AB-middle
            context.line_to(x + w / 2, y + h / 2)           # Line to middle
            context.line_to(x, y + h / 2)                   # Line to GH-middle
        elif which_segment == Common.keysegments.THREE:
            context.move_to(x + w / 2, y + h)               # Move to FE-middle
            context.line_to(x + w - r, y + h)               # Line to E
            context.curve_to(x + w, y + h, x + w, y + h, 
                             x + w, y + h - r)              # Curve to D
            context.line_to(x + w, y + h / 2)               # Line to CD-middle
            context.line_to(x + w / 2, y + h / 2)           # Line to middle
            context.line_to(x + w / 2, y + h)               # Line to FE-middle
        elif which_segment == Common.keysegments.FOUR:
            context.move_to(x + w, y + h / 2)               # Move to CD-middle
            context.line_to(x + w, y + r)                   # Line to C
            context.curve_to(x + w, y, x + w, y, 
                             x + w - r, y)                  # Curve to B
            context.line_to(x + w / 2, y)                   # Line to AB-middle
            context.line_to(x + w / 2, y + h / 2)           # Line to middle
            context.line_to(x + w, y + h / 2)               # Line to CD-middle

    def do_highlight(self, do_highlight = Common.keysegments.NONE, x = -1, y = -1):
        self.highlight_x = x
        self.highlight_y = y
        
        #print "do_highlight():", x, y
        if do_highlight:
            self.modifier = .8
        else:
            self.modifier = 1

        self.queue_draw()

    def extract_display_keyvalues(self):
        """ Updates the display values, based on current include files, layout """
        for counter in Common.keysegmentslist:
            self.dvalues[counter] = copy.copy(self.keyvalues[counter])
            if self.keycode in KeyDict.IgnoreKeys:
                continue
            if self.keyvalues[counter].getType() == Common.keyvaluetype.NOSYMBOL:
                for layout in activated_variants.keys():
                    for variant in activated_variants[layout].keys():
                        if activated_variants[layout][variant].has_key(self.keycode):
                            if activated_variants[layout][variant][self.keycode].has_key(counter):
                                self.dvalues_inherited[counter] = True
                                self.dvalues[counter] = copy.copy(activated_variants[layout][variant][self.keycode][counter])
            if self.dvalues[counter].getType() == Common.keyvaluetype.NOSYMBOL:
                self.dvalues_inherited[counter] = False
                self.dvalues[counter] = copy.copy(self.keyvalues[counter])

