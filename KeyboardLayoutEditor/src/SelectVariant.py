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
import copy

class SelectVariant:
    def __init__(self, window):
        self.dialog = gtk.Dialog("Select Variant", 
                                 window, 
                                 gtk.DIALOG_MODAL,
                                 (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT,
                                  gtk.STOCK_OK, gtk.RESPONSE_ACCEPT)  )
        vbox = gtk.VBox()
        self.dialog.vbox.pack_start(vbox, expand = True, fill = True)
        vbox.show()
        
        # The selection
        self.selection = ''

        # Creation of the actual model
        self.store = gtk.ListStore(gobject.TYPE_STRING, gobject.TYPE_BOOLEAN)
        for i in ([1,2,3,4,5]):
            self.store.append((i, True))

        # Creation of the filter, from the model
        self.filter = self.store.filter_new()
        self.filter.set_visible_column(1)

        # The TreeView gets the filter as model
        self.view = gtk.TreeView(self.filter)

        # Some other gtk stuff
        renderer = gtk.CellRendererText()
        self.view.insert_column_with_attributes(-1,"Variants",renderer,text=0)
        vbox.pack_start(self.view)
        self.view.show()
        self.dialog.connect("response", self.select_row)
        self.dialog.connect("close", self.close)

    def show(self):
        self.dialog.show()
        self.dialog.run()

    def set_list(self, list_items):
        self.store.clear()
        for variant in list_items:
            self.store.append((variant, True))
        self.selection = list_items[0]

    def get_selection(self):
        return self.selection

    def select_row(self, widget, response_id):
        if response_id == gtk.RESPONSE_ACCEPT:
            # Get the selected row
            filter_iter = self.view.get_selection().get_selected()[1]
            # Translate it into a useful iterator
            store_iter = self.filter.convert_iter_to_child_iter(filter_iter)
            # Use it to show the selected row
            self.selection = self.store[store_iter][0]
            print self.selection
        else:
            self.selection = ''
            print "Cancelled"
        self.dialog.hide()
        
    def close(self):
        self.dialog.hide()

if __name__ == '__main__':
    # That's it
    # Prepare the window and other Gtk stuff 
    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_modal(True)
    window.set_default_size(100, 200)
    window.connect("destroy", gtk.main_quit)
    a = SelectVariant(window)
    a.set_list(["one", "two", "three"])
    a.show()
    gtk.main()
