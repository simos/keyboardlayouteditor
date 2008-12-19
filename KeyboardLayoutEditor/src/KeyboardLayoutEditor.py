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

__author__      = "Simos Xenitellis <simos.lists@googlemail.com>"
__version__     = "1.1"
__date__        = "Date: 2008/09/07"
__copyright__   = "Copyright (c) 2008 Simos Xenitellis"
__license__     = "GPLv3"

# Hidden: *Lexer.py, *Parser.py, *Walker.py, evdev, aliases, *.tokens, *.g, KeysymsUni.py, print_tree.py, parse_*.py

try:
    import os
    import sys
    import copy
    import string
    import gtk
    import gobject
    import pango
except ImportError, e:
    raise SystemExit("Import error, Keyboard Layout Editor: " + str(e))

if gtk.pygtk_version < (2, 12):
    print "PyGtk 2.12 or later required for this application"
    print "You have pyGTK", gtk.pygtk_version
    raise SystemExit

try:
    import cairo
except ImportError, e:
    raise SystemExit("The Python bindings for Cairo are required \
                        for this application: " + str(e))

try:
    from lxml import etree
except ImportError, e:
    raise SystemExit("The Python bindings for libxml2 were not found: " + str(e))

try:
    import Enum
    import Key
    import Keyboard
    import ParseXKB
    import GenericLayout
    import Common
    import SelectVariant
    from KeyDict import KeyDict, included_files, activated_variants
    from ParseXML import ExtractVariantsKeycodes
    from DeadKeysDict import DeadKeys
except ImportError, e:
    raise SystemExit("Import error, Keyboard Layout Editor: " + str(e))

class Controller_KeyboardLayoutEditor:
    """ The keyboard layout editor controller """

    def __init__(self):
        # Set the home directory of the application
        Common.HOMEDIR = os.path.split( os.path.realpath( sys.argv[0] ) )[0] + '/'
        
        # This is the parser for XKB files, creates an lxml.etree object.
        self.parse_xkb = ParseXKB.ParseXKB()
        
        # Here we create an lxml.etree object that holds the current layout.
        self.xmllayout = GenericLayout.GenericLayout()

        # Include files: the selected model and paths, as dict ("model", "paths") 
        self.include_layout_selected = {}

        # This is the window object.
        self.window = gtk.Window()

        # This variable holds the state of the layout; where modifications took place.
        #self.layout_not_empty = False

        # Capture keyboard events (key presses), and highlight the relevant keys.
        self.root_window = gtk.gdk.get_default_root_window()
        self.root_window.set_events(gtk.gdk.KEY_PRESS_MASK)
        gtk.gdk.event_handler_set(self.keypress_filter_callback, None)

        # Set initial size
        (width, height) = self.window.get_size()
        self.window.resize(800, 550)
        
        self.window.connect("check_resize", self.check_resize)
        
        self.icon_pixbuf = gtk.gdk.pixbuf_new_from_file(Common.HOMEDIR + 'kle-icon4.svg')
        self.window.set_icon(self.icon_pixbuf)

        self.TARGET_TYPE_TEXT = 80

        self.select_variant = SelectVariant.SelectVariant(self.window)

        # Set window title
        self.window.set_title("Keyboard Layout Editor")
        
        # Fill in the dead key section
        deadkey_frame = gtk.Frame("Dead keys")
        deadkey_vbox = gtk.VBox()
        deadkey_info_label = gtk.Label("Drag the dead key (coloured text)"
                " and drop to the keyboard below. Click on button for more options.")
        deadkey_info_label.set_line_wrap(True)
        deadkey_combobox = gtk.ComboBox()
        deadkey_liststore = gtk.ListStore(str)
        deadkey_cell = gtk.CellRendererText()
        deadkey_combobox.pack_start(deadkey_cell)
        deadkey_combobox.add_attribute(deadkey_cell, 'text', 0)
        self.deadkey_label = gtk.Label("No dead key")
        
        PLIST = pango.AttrList()
        BOLD = pango.AttrWeight(pango.WEIGHT_HEAVY, 0, -1)
        GRAYBG = pango.AttrBackground(45000, 40000, 55000, 0, -1)
        PLIST.insert(BOLD)
        PLIST.insert(GRAYBG)
        self.deadkey_label.set_property("attributes", PLIST)
                
        deadkey_eventboxlabel = gtk.EventBox()
        deadkey_eventboxlabel.add(self.deadkey_label)
        deadkey_eventboxlabel.connect("drag_data_get", 
                                      self.deadkey_drag_data_get_callback)
        deadkey_eventboxlabel.drag_source_set(gtk.gdk.BUTTON1_MASK, 
                                [ ( "text/plain", 0, self.TARGET_TYPE_TEXT )],
                                gtk.gdk.ACTION_COPY)
        
        deadkey_vbox.pack_start(deadkey_info_label, expand=False, fill=False)
        deadkey_vbox.pack_start(deadkey_eventboxlabel, expand=False, fill=False)
        deadkey_vbox.pack_start(deadkey_combobox, expand=False, fill=False)
        deadkey_frame.add(deadkey_vbox)
        
        self.deadkey_tooltips = gtk.Tooltips()
        self.set_deadkey_tooltip()

        deadkey_combobox.set_wrap_width(4)
        deadkey_allnames = []
        for deadkey in DeadKeys.dict.keys():
            deadkey_allnames.append([DeadKeys.dict[deadkey][0]])
        deadkey_allnames.sort()
        for deadkeyname in deadkey_allnames: 
            deadkey_liststore.append(deadkeyname)
        deadkey_combobox.set_model(deadkey_liststore)
        deadkey_combobox.connect('changed', self.changed_deadkey_combobox_callback)
        deadkey_combobox.set_active(4)

        deadkey_unicodechars_vbox = gtk.VBox()
        unicodechars_frame = gtk.Frame("Unicode characters")
        unicodechars_vbox = gtk.VBox()
        unicodechars_label = gtk.Label("Start Character Map, and then drag \
and drop characters from there to the keyboard below")
        unicodechars_label.set_line_wrap(True)
        unicodechars_button = gtk.Button("Start Character map")
        unicodechars_button.connect("clicked", self.unicodechars_clicked_callback)
        unicodechars_vbox.pack_start(unicodechars_label, expand = False, fill = False)
        unicodechars_vbox.pack_start(unicodechars_button, expand = False, fill = False)
        unicodechars_frame.add(unicodechars_vbox)
        deadkey_unicodechars_vbox.pack_start(unicodechars_frame, 
                                             expand = False, 
                                             fill = False)
        deadkey_unicodechars_vbox.pack_start(deadkey_frame, 
                                             expand = False, 
                                             fill = False)
        
        includefile_frame = gtk.Frame("Include files")
        includefile_hbox = gtk.HBox()
        includefile_button_load = gtk.Button("Load file...")
        includefile_button_remove = gtk.Button("Remove layout")
        includefile_button_load.connect("clicked", self.clicked_loadincludefile_callback)
        includefile_button_remove.connect("clicked", self.clicked_removeentry_callback)
        includefile_button_remove.set_sensitive(False)
        includefile_frame.add(includefile_hbox)
        includefile_vbox = gtk.VBox()
        includefile_hbox.add(self.doincludes(includefile_button_remove))
        includefile_hbox.add(includefile_vbox)
        includefile_vbox.pack_end(includefile_button_load, expand = False)
        includefile_vbox.pack_end(includefile_button_remove, expand = False)

        addtolayout_frame = gtk.Frame("Add to layout")
        addtolayout_hbox = gtk.HBox()
        addtolayout_frame.add(addtolayout_hbox)
        addtolayout_hbox.pack_start(includefile_frame, expand=True, fill=True)
        addtolayout_hbox.pack_start(deadkey_unicodechars_vbox, expand=False, fill=False)

        layoutdetails_frame = gtk.Frame("Layout details")

        layoutdetails_vbox = gtk.VBox()
        layoutdetails_hbox_code = gtk.HBox()
        layoutdetails_label_code = gtk.Label("Layout code")
        self.layoutdetails_entry_code = gtk.Entry()
        self.layoutdetails_entry_code.set_max_length(24)
        self.layoutdetails_entry_code.connect("key_release_event", self.entry_callback, self.layoutdetails_entry_code)
        layoutdetails_code_tooltip = gtk.Tooltips()
        layoutdetails_code_tooltip_text = "Enter the layout code.\nTypically \
this is the relevant ISO 3166\ncountry code, \
or in special cases,\nthe ISO 639 language code. \
This is two \nor three letters long, lowercase."
        layoutdetails_code_tooltip.set_tip(self.layoutdetails_entry_code, layoutdetails_code_tooltip_text)
        layoutdetails_hbox_code.pack_start(layoutdetails_label_code, expand=False, fill=False)
        layoutdetails_hbox_code.pack_start(self.layoutdetails_entry_code, expand=True, fill=True)
        layoutdetails_vbox.pack_start(layoutdetails_hbox_code, expand=False, fill=False)

        layoutdetails_hbox_variant = gtk.HBox()
        layoutdetails_label_variant = gtk.Label("Variant")
        self.layoutdetails_entry_variant = gtk.Entry()
        self.layoutdetails_entry_variant.set_max_length(24)
        self.layoutdetails_entry_variant.connect("key_release_event", self.entry_callback, self.layoutdetails_entry_variant)
        layoutdetails_variant_tooltip = gtk.Tooltips()
        layoutdetails_variant_tooltip_text = "Enter the variant name.\nThis is one \
or more alphanumeric characters,\nall lowercase."
        layoutdetails_variant_tooltip.set_tip(self.layoutdetails_entry_variant, layoutdetails_variant_tooltip_text)
        layoutdetails_hbox_variant.pack_start(layoutdetails_label_variant, expand=False, fill=False)
        layoutdetails_hbox_variant.pack_start(self.layoutdetails_entry_variant, expand=True, fill=True)
        layoutdetails_vbox.pack_start(layoutdetails_hbox_variant, expand=False, fill=False)

        layoutdetails_hbox_country = gtk.HBox()
        layoutdetails_label_country = gtk.Label("Country name")
        self.layoutdetails_entry_country = gtk.Entry()
        self.layoutdetails_entry_country.set_max_length(48)
        self.layoutdetails_entry_country.connect("key_release_event", self.entry_callback, self.layoutdetails_entry_country)
        layoutdetails_country_tooltip = gtk.Tooltips()
        layoutdetails_country_tooltip_text = "Enter the relevant country name for the layout.\n\
You put something like France or Germany.\n\
In very special cases where no country is relevant,\n\
you may put a language name (for example, Arabic).\n\
This information is used when submitting the layout to\n\
the xkeyboard-config project\n\
Please do not put punctuation marks."
        layoutdetails_country_tooltip.set_tip(self.layoutdetails_entry_country, layoutdetails_country_tooltip_text)
        layoutdetails_hbox_country.pack_start(layoutdetails_label_country, expand=False, fill=False)
        layoutdetails_hbox_country.pack_start(self.layoutdetails_entry_country, expand=True, fill=True)
        layoutdetails_vbox.pack_start(layoutdetails_hbox_country, expand=False, fill=False)

        layoutdetails_hbox_name = gtk.HBox()
        layoutdetails_label_name = gtk.Label("Layout name")
        self.layoutdetails_entry_name = gtk.Entry()
        self.layoutdetails_entry_name.set_max_length(48)
        self.layoutdetails_entry_name.connect("key_release_event", self.entry_callback, self.layoutdetails_entry_name)
        layoutdetails_name_tooltip = gtk.Tooltips()
        layoutdetails_name_tooltip_text = "Enter the layout name.\nIt is \
the name to describe this variant.\n\
This is a free-form description.\n\
Please do not put punctuation marks."
        layoutdetails_name_tooltip.set_tip(self.layoutdetails_entry_name, layoutdetails_name_tooltip_text)
        layoutdetails_hbox_name.pack_start(layoutdetails_label_name, expand=False, fill=False)
        layoutdetails_hbox_name.pack_start(self.layoutdetails_entry_name, expand=True, fill=True)
        layoutdetails_vbox.pack_start(layoutdetails_hbox_name, expand=False, fill=False)
        
        preferences_frame = gtk.Frame("Preferences")
        preferences_vbox = gtk.VBox()
        preferences_frame.add(preferences_vbox)

        basedir_vbox = gtk.VBox()
        basedir_label = gtk.Label('Select a new basedir')
        basedir_vbox.pack_start(basedir_label, expand=False, fill=False)
        basedirbutton = gtk.Button(Common.basedir)
        basedirbutton.connect('clicked', self.basedir_set_callback)
        basedir_vbox.pack_start(basedirbutton, expand=False, fill=False)
        
        fontbutton_vbox = gtk.VBox()
        fontbutton_label = gtk.Label("Select a font")
        fontbutton_vbox.pack_start(fontbutton_label, expand=False, fill=False)
        fontbutton = gtk.FontButton(fontname=Common.fontname + " " + str(Common.fontsize))
        fontbutton.set_title('Select a font')
        fontbutton.connect('font-set', self.font_set_callback)
        fontbutton_vbox.pack_start(fontbutton, expand=False, fill=False)

        preferences_vbox.pack_start(fontbutton_vbox, expand=True, fill=True)
        preferences_vbox.pack_start(basedir_vbox, expand=True, fill=True)

        #layoutdetails_vbox.pack_start(preferences_frame, expand=False, fill=False)
        
        layoutdetails_frame.add(layoutdetails_vbox)

        layoutdetails_and_preferences_vbox = gtk.VBox()
        layoutdetails_and_preferences_vbox.pack_start(layoutdetails_frame, expand=True, fill=True)
        layoutdetails_and_preferences_vbox.pack_start(preferences_frame, expand=True, fill=True)
        
        layoutdetails_and_addtoframe = gtk.HBox()
        layoutdetails_and_addtoframe.pack_start(layoutdetails_and_preferences_vbox, expand=False, fill=False)
        layoutdetails_and_addtoframe.pack_start(addtolayout_frame, expand=True, fill=True)

        # Create an accelerator group
        accelgroup = gtk.AccelGroup()
        # Add the accelerator group to the toplevel window
        self.window.add_accel_group(accelgroup)

        # Create an action for starting with a new layout using a stock item
        action_new = gtk.Action('New', '_New...', 'New layout', gtk.STOCK_NEW)
        action_new.set_property('short-label', '_New')
        # Connect a callback to the action
        action_new.connect('activate', self.new_layout)

        # Create an action for opening an existing layout using a stock item
        action_open = gtk.Action('Open', '_Open', 
                                 'Open an existing layout', gtk.STOCK_OPEN)
        action_open.set_property('short-label', '_Open')
        # Connect a callback to the action
        action_open.connect('activate', self.open_layout)

        # Create an action for saving the layout using a stock item
        action_save = gtk.Action('Save', '_Save', 'Save the Layout', 
                                 gtk.STOCK_SAVE)
        action_save.set_property('short-label', '_Save')
        # Connect a callback to the action
        action_save.connect('activate', self.save_layout)

        # Create an action for saving the layout with a new name, using a stock item
        action_save_as = gtk.Action('SaveAs', 'Save _As', 
                                    'Save the layout with a different filename', 
                                    gtk.STOCK_SAVE_AS)
        action_save_as.set_property('short-label', '_Save As')
        # Connect a callback to the action
        action_save_as.connect('activate', self.save_as_layout)

        # Create an action for quitting the program using a stock item
        action_quit = gtk.Action('Quit', '_Quit', 'Quit the Program', 
                                 gtk.STOCK_QUIT)
        action_quit.set_property('short-label', '_Quit')
        # Connect a callback to the action
        action_quit.connect('activate', self.quit_application)

        # Create an ActionGroup named BasicAction
        actiongroup = gtk.ActionGroup('BasicAction')
        # Add the action to the actiongroup with an accelerator
        # None means use the stock item accelerator
        actiongroup.add_action_with_accel(action_new, None)
        actiongroup.add_action_with_accel(action_open, None)
        actiongroup.add_action_with_accel(action_save, None)
        actiongroup.add_action_with_accel(action_save_as, None)
        actiongroup.add_action_with_accel(action_quit, None)

        # Have the action use accelgroup
        action_new.set_accel_group(accelgroup)
        action_open.set_accel_group(accelgroup)
        action_save.set_accel_group(accelgroup)
        action_save_as.set_accel_group(accelgroup)
        action_quit.set_accel_group(accelgroup)

        # Create a MenuBar
        menubar = gtk.MenuBar()

        # Create the File Action and MenuItem
        file_action = gtk.Action('File', '_File', None, None)
        actiongroup.add_action(file_action)
        file_menuitem = file_action.create_menu_item()
        menubar.append(file_menuitem)

        # Create the File Menu
        file_menu = gtk.Menu()
        file_menuitem.set_submenu(file_menu)

        # Create a proxy MenuItem
        menuitem_new = action_new.create_menu_item()
        menuitem_open = action_open.create_menu_item()
        menuitem_save = action_save.create_menu_item()
        menuitem_save_as = action_save_as.create_menu_item()
        menuitem_quit = action_quit.create_menu_item()
        file_menu.append(menuitem_new)
        file_menu.append(menuitem_open)
        file_menu.append(menuitem_save)
        file_menu.append(menuitem_save_as)
        file_menu.append(menuitem_quit)

        self.mainvbox = gtk.VBox(False)
        
        # Here we create the Keyboard object.
        self.mykeyboard = Keyboard.Keyboard(self.xmllayout)

        # Status bar object
        Common.statusbar = gtk.Statusbar()
        Common.statusbar.console_context = Common.statusbar.get_context_id('statusbar')
        
        self.window.add(self.mainvbox)

        self.mykeyboard.add_events(gtk.gdk.KEY_PRESS_MASK |
                    gtk.gdk.POINTER_MOTION_MASK |
                    gtk.gdk.BUTTON_PRESS_MASK | 
                    gtk.gdk.SCROLL_MASK)

        self.mainvbox.pack_start(menubar, expand=False, fill=True)
        self.mainvbox.pack_start(layoutdetails_and_addtoframe, expand=False, 
                                 fill=False)
        self.mainvbox.pack_start(self.mykeyboard, expand=True, fill=True)
        self.mainvbox.pack_start(Common.statusbar, expand=False, fill=True)

        self.window.connect("destroy", gtk.main_quit)
        self.window.show_all()

    def doincludes(self, button_remove):
        # create a TreeStore with one string column to use as the model
        self.treestore_includes = gtk.TreeStore(str, 'gboolean', 'gboolean')

        self.treestore_includes_iters = {}

        # create the TreeView using treestore
        self.treeview_includes = gtk.TreeView(self.treestore_includes)

        # get a TreeViewSelection object
        self.treeview_includes_selection = self.treeview_includes.get_selection()
        self.treeview_includes_selection.connect('changed', 
                            self.on_selection_changed_callback, button_remove)

        # create the TreeViewColumn to display the data
        self.cells0 = gtk.CellRendererText()
        self.treeview_includes.insert_column_with_attributes(-1, "Layout", self.cells0, text=0)

        # create the TreeViewColumn to display the data
        self.cells1 = gtk.CellRendererToggle()
        self.cells1.connect( 'toggled', 
                             self.col1_toggled_callback, 
                             self.treestore_includes )
        self.treeview_includes.insert_column_with_attributes(-1, "Included", 
                                                    self.cells1, 
                                                    active=1, 
                                                    visible=2)

        # make it searchable
        self.treeview_includes.set_search_column(0)

        # Allow drag and drop reordering of rows
        self.treeview_includes.set_reorderable(False)
        self.treeview_includes.set_enable_tree_lines(True)
        self.treeview_includes.set_show_expanders(True)

        self.scrolled_window = gtk.ScrolledWindow()
        self.scrolled_window.add_with_viewport(self.treeview_includes)
        self.scrolled_window.set_size_request(300, 200)

        return self.scrolled_window

    def clicked_loadincludefile_callback(self, param):
        chooser = gtk.FileChooserDialog("Load layout file", 
                                        action=gtk.FILE_CHOOSER_ACTION_OPEN, 
                                        buttons=(gtk.STOCK_CANCEL, 
                                                 gtk.RESPONSE_CANCEL, 
                                                 gtk.STOCK_OPEN, 
                                                 gtk.RESPONSE_OK))
        chooser.set_current_folder(Common.symbolsdir)
        chooser.set_default_response(gtk.RESPONSE_OK)
         
        filter = gtk.FileFilter()
        filter.set_name("All files")
        filter.add_pattern("*")
        chooser.add_filter(filter)
         
        response = chooser.run()
        if response == gtk.RESPONSE_OK:
             layout_file = chooser.get_filename()
             layout_name = layout_file.rpartition('/')[2]
             for layout_id in included_files.keys():
                 if included_files[layout_id]["file"] == layout_file:
                    chooser.destroy()    
                    self.error_dialog("The file " + layout_file + 
                        " has already been loaded. Remove first before reloading.")
                    return
             #print layout_file, layout_name
             parse_result = self.parse_xkb.parse_layout(layout_file)
             #print parse_result
             if parse_result["success"] == True:
                # For example, included_files["latin"] = { "file": "/tmp/latin", 
                #    "variants": variants_dict, xml_layout }
                self.add_includefile(layout_file)
                
                chooser.destroy()
                Common.addtostatusbar('Successfully added include file ' + layout_file + '.')
             else:
                 chooser.destroy()    
                 self.error_dialog("An error was encountered while trying to parse " \
                                 + layout_file + ". The file is not loaded.")
        elif response == gtk.RESPONSE_CANCEL:
            chooser.destroy()    

    def add_includefile(self, layout_file, highlight_variant = None):
        """ Adds an include file in the Include file tree. """
        try:
            layout_file.index('/')
            fullfilename = True
        except ValueError:
            fullfilename = False
            
        if fullfilename:
            include_parse_result = self.parse_xkb.parse_layout(layout_file)
            layout_name = layout_file.rpartition('/')[2]
        else:
            include_parse_result = self.parse_xkb.parse_layout(Common.symbolsdir + layout_file)
            layout_name = layout_file
            
        #print "ADD++Include_parse_result (after parse_xkb.parse_layout):", include_parse_result
        if include_parse_result["success"] == True:
            include_parsed_variants = copy.deepcopy(include_parse_result["variants"])
            include_parsed_layout = include_parse_result["layout"]

        # For example, included_files["latin"] = { "file": "/tmp/latin", 
        #    "variants": variants_dict, xml_layout }
        included_files[layout_name] = { 'file': layout_name,
                                                  'variants' : include_parsed_variants, 
                                                  'xml' : include_parsed_layout}
        #print "+++included files for", layout_name, included_files[layout_name]

        self.treestore_includes_iters[layout_name] = \
                self.treestore_includes.append(None, [layout_name, False, False])
        for variant in include_parsed_variants:
            #print "ADD_INCLUDE, doing variant", variant
            if highlight_variant != None and variant == highlight_variant:
                #print "HIGHLIGHT", variant
                self.treestore_includes.append(self.treestore_includes_iters[layout_name],
                                           [variant, True, True])
            else:
                self.treestore_includes.append(self.treestore_includes_iters[layout_name],
                                           [variant, False, True])

    def basedir_set_callback(self, button):
        """ Signal, emitted when the user presses the basedir button. """
        chooser = gtk.FileChooserDialog("Select new basedir", 
                                        action=gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER, 
                                        buttons=(gtk.STOCK_CANCEL, 
                                                 gtk.RESPONSE_CANCEL, 
                                                 gtk.STOCK_OPEN, 
                                                 gtk.RESPONSE_OK))
        chooser.set_current_folder(Common.basedir)
        chooser.set_default_response(gtk.RESPONSE_OK)
         
        filter = gtk.FileFilter()
        filter.set_name("All files")
        filter.add_pattern("*")
        chooser.add_filter(filter)
         
        response = chooser.run()
        if response == gtk.RESPONSE_OK:
            symbols_temp = chooser.get_filename() + '/symbols/'
            if os.path.isdir(symbols_temp):
                Common.basedir = chooser.get_filename()
                Common.symbolsdir = Common.basedir + '/symbols/'
                button.set_label(Common.basedir)
            else:
                chooser.destroy()    
                self.error_dialog('Invalid basedir ' + symbols_temp + '.\n' \
                                 'symbols/ subdirectory not found.')
                return
        elif response == gtk.RESPONSE_CANCEL:
            pass
        chooser.destroy()    
                              
    def new_layout(self, something):
        """ Invoked when the user clicks File/New... """
        if self.layout_not_empty():
            if self.ask_to_save_first() == False:
                Common.addtostatusbar('Canceled the new layout.')
                return
        self.reset_layout()
        Common.addtostatusbar('Created new layout.')

    def reset_layout(self):
        activated_variants.clear()
        included_files.clear()
        Common.currentlayoutfile = ''
        self.mykeyboard.layoutcode = ''
        self.mykeyboard.layoutvariant = ''
        self.mykeyboard.layoutcountry = ''
        self.mykeyboard.layoutname = ''
        self.layoutdetails_entry_code.set_text(self.mykeyboard.layoutcode)
        self.layoutdetails_entry_variant.set_text(self.mykeyboard.layoutvariant)
        self.layoutdetails_entry_country.set_text(self.mykeyboard.layoutcountry)
        self.layoutdetails_entry_name.set_text(self.mykeyboard.layoutname)
        for keycode in KeyDict.Keys.keys():
            if keycode not in KeyDict.IgnoreKeys:
                for segment in Common.keysegmentslist:
                    KeyDict.Keys[keycode].key.keyvalues[segment].reset()

        self.treestore_includes.clear()
        self.mykeyboard.redraw()

    def ask_to_save_first(self):
        """ Asks the user if to save. On cancel, we return False. """
        shallsave_message = "Would you like to save the existing layout?"
        shallsave_box = gtk.MessageDialog(parent=self.window, 
                                          flags=gtk.DIALOG_MODAL, 
                                          type=gtk.MESSAGE_QUESTION, 
                                          buttons=gtk.BUTTONS_YES_NO,
                                          message_format = shallsave_message)
        shallsave_box.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
        shallsave_box.set_default_response(gtk.RESPONSE_CANCEL)
        response = shallsave_box.run()
        shallsave_box.destroy()
        if response == gtk.RESPONSE_CANCEL:
            return False
        elif response == gtk.RESPONSE_YES:
            if self.save_layout(None):
                return True
            else:
                return False
        elif response == gtk.RESPONSE_NO:
            return True
        return False
                
    def open_layout(self, something):
        """ Invoked when the user clicks File/Open... """
        if self.layout_not_empty():
            if self.ask_to_save_first() == False:
                Common.addtostatusbar('Canceled opening a layout.')
                return

        chooser = gtk.FileChooserDialog("Open layout file", 
                                        action=gtk.FILE_CHOOSER_ACTION_OPEN, 
                                        buttons=(gtk.STOCK_CANCEL, 
                                                 gtk.RESPONSE_CANCEL, 
                                                 gtk.STOCK_OPEN, 
                                                 gtk.RESPONSE_OK))
        chooser.set_current_folder(Common.symbolsdir)
        chooser.set_default_response(gtk.RESPONSE_OK)
         
        filter = gtk.FileFilter()
        filter.set_name("All files")
        filter.add_pattern("*")
        chooser.add_filter(filter)
         
        response = chooser.run()
        if response == gtk.RESPONSE_OK:
             layout_file = chooser.get_filename()
             chooser.destroy()
             layout_name = layout_file.rpartition('/')[2]
             #print "We are about to open a file"
             #print "+We have layout file", layout_file
             parse_result = self.parse_xkb.parse_layout(layout_file)
             if parse_result["success"] == True:
                # For example, included_files["latin"] = { "file": "/tmp/latin", 
                #    "variants": variants_dict, xml_layout }
                
                # Clear the layout constructs
                #print "+Parse was success", parse_result
                
                self.select_variant.set_list(parse_result['variants'])
                self.select_variant.show()
                # If the user did not select a variant, we cancel the opening of the file.
                if self.select_variant.get_selection() == '':
                    Common.addtostatusbar('Canceled opening layout file.')
                    return        
                self.reset_layout()
                variant_verbose_name = ''
                self.mykeyboard.layoutvariant = self.select_variant.get_selection()
                Common.currentlayoutfile = layout_file
                #print "Selected:", self.mykeyboard.layoutvariant
                result_extract = ExtractVariantsKeycodes(parse_result['layout'], 
                                                self.mykeyboard.layoutvariant)
                #print "+Extracting variants from layout", parse_result['layout'], "variant", self.mykeyboard.layoutvariant
                newkeydict = result_extract['keydict']
                newvariants = result_extract['variants']
                #print "+Keycodes (newkeydict):", newkeydict
                #print "+Variants (newvariants):", newvariants

                for keycode in KeyDict.Keys.keys():
                    if keycode not in KeyDict.IgnoreKeys:
                        if newkeydict.has_key(keycode):
                            for segment in Common.keysegmentslist:
                                if newkeydict[keycode].has_key(segment):
                                    KeyDict.Keys[keycode].key.keyvalues[segment].copy(newkeydict[keycode][segment])

                self.mykeyboard.layoutcode = layout_name
                self.mykeyboard.layoutname = result_extract['variant_name']
                self.layoutdetails_entry_code.set_text(self.mykeyboard.layoutcode)
                self.layoutdetails_entry_variant.set_text(self.mykeyboard.layoutvariant)
                self.layoutdetails_entry_name.set_text(self.mykeyboard.layoutname)

                for variant in result_extract['variants']:
                    #print "++Parsed include strings:", Common.parseIncludeString(variant)
                    parsed_variant = Common.parseIncludeString(variant)
                    
                    include_parse_result = self.parse_xkb.parse_layout(Common.symbolsdir 
                                                               + parsed_variant['filename'])
                    #print "++Include_parse_result (after parse_xkb.parse_layout):", include_parse_result
                    if include_parse_result["success"] == True:
                        include_parsed_layout = include_parse_result["layout"]
                        if parsed_variant['variant'] == '':
                            """ If not variant is supplied, we select the first one. """
                            parsed_variant['variant'] = include_parse_result["variants"][0]
                            #print "+++fixed", include_parse_result["variants"][0]

                        # For example, included_files["latin"] = { "file": "/tmp/latin", 
                        #    "variants": variants_dict, xml_layout }
                        included_files[parsed_variant['variant']] = { 
                                                    "file": parsed_variant['filename'],
                                                    "variants" : copy.deepcopy(include_parse_result["variants"]), 
                                                    "xml" : include_parsed_layout}
                        #print "+++included files for", layout_name, included_files[parsed_variant['variant']]
                        self.add_includefile(parsed_variant['filename'], 
                                             parsed_variant['variant'])
                        self.select_include_variant(parsed_variant['filename'], 
                                                    parsed_variant['variant'], 
                                                    included_files[parsed_variant['filename']]["xml"])

                if result_extract['variants'] == []:
                    parsed_variant = []
                
                self.mykeyboard.redraw()
                Common.addtostatusbar('Successfully opened layout file ' + layout_file + ', ' + 
                                      'selected variant ' + self.mykeyboard.layoutname + '.')
             else:
                chooser.destroy()    
                self.error_dialog('An error was encountered while trying to parse ' \
                                 + layout_file + '. The file is not opened.')
                Common.addtostatusbar('Failed at parsing layout file ' + layout_file + '.')
        elif response == gtk.RESPONSE_CANCEL:
            chooser.destroy()    
            Common.addtostatusbar('Canceled opening layout file.')
        else:
            # Should not be reached
            chooser.destroy()
        
    def save_layout(self, something):
        """ Invoked when the user clicks File/Save """
        if self.save_perform_checks_notifications() == False:
            return False

        if Common.currentlayoutfile == '':
            return self.save_as_layout(None)
        else:
            if os.access(Common.currentlayoutfile, os.W_OK):
                result = self.mykeyboard.save(Common.currentlayoutfile)
                if result == True:
                    Common.addtostatusbar('Layout saved to ' + Common.currentlayoutfile + '.')
                    return True
                else:
                    return False
            else:
                self.error_dialog('Cannot write to file ' + Common.currentlayoutfile + '. Please select to Save As.')
                Common.addtostatusbar('File save cancelled because file is not writable; please select Save As.')
                return False
            
    def save_as_layout(self, arg):
        """ Invoked when the user clicks File/Save As..."""
        if self.save_perform_checks_notifications() == False:
            return False
        chooser = gtk.FileChooserDialog("Save layout file as...", 
                                        action=gtk.FILE_CHOOSER_ACTION_SAVE, 
                                        buttons=(gtk.STOCK_CANCEL, 
                                                 gtk.RESPONSE_CANCEL, 
                                                 gtk.STOCK_SAVE_AS, 
                                                 gtk.RESPONSE_OK))
        chooser.set_current_folder(".")
        chooser.set_default_response(gtk.RESPONSE_OK)
        chooser.set_filename(self.mykeyboard.layoutcode)
         
        filter = gtk.FileFilter()
        filter.set_name("All files")
        filter.add_pattern("*")
        chooser.add_filter(filter)
         
        response = chooser.run()
        if response == gtk.RESPONSE_OK:
            temp_filename = chooser.get_filename()
            chooser.destroy()
            if os.access(os.path.dirname(temp_filename), os.W_OK):
                Common.currentlayoutfile = temp_filename
                self.mykeyboard.save(Common.currentlayoutfile)
                Common.addtostatusbar('Layout saved to ' + Common.currentlayoutfile + '.')
                return True
            else:
                #print "temp_filename:", temp_filename
                self.error_dialog('File save cancelled; cannot save to ' + temp_filename + '.')
                Common.addtostatusbar('File save cancelled; cannot save to ' + temp_filename + '.')
                return False
        else:
            chooser.destroy()
            return False

    def save_perform_checks_notifications(self):
        if self.layout_not_empty() == False:
            self.error_dialog("The layout is empty. Not saving.")
            return False
        if self.mykeyboard.layoutcode == '':
            self.error_dialog("Cannot save layout; please add a layout code.")
            return False
        if self.mykeyboard.layoutvariant == '':
            self.error_dialog("Cannot save layout; please add a layout variant.")
            return False
        if self.mykeyboard.layoutname == '':
            self.error_dialog("Cannot save layout; please add a layout name.")
            return False
        return True
    
    def clicked_removeentry_callback(self, button):
        model = self.include_layout_selected["model"]
        path = str(self.include_layout_selected["paths"][0][0])
        iter_layout = model.get_iter_from_string(path.partition(':')[0])
        selected_layout = model.get_value(iter_layout, 0)

        if activated_variants.has_key(selected_layout):
            del activated_variants[selected_layout]
        print "clicked_removeentry_callback:", included_files
        del included_files[selected_layout]
        del self.include_layout_selected["model"][self.include_layout_selected["paths"][0]]
        self.mykeyboard.redraw()
        Common.addtostatusbar('Removed layout ' + selected_layout)
        button.set_sensitive(False)
          
    def col1_toggled_callback( self, cell, path, model ):
        """ Sets the toggled state on the toggle button to true or false. """
        model[path][1] = not model[path][1]

        iter_variant = model.get_iter_from_string(path)
        iter_layout = model.get_iter_from_string(path.partition(':')[0])
        toggle_layout = model.get_value(iter_layout, 0)
        toggle_variant = model.get_value(iter_variant, 0)

        # If the variant is toggled **ON**,
        #print "toggling",
        if model[path][1]:
            #print "on"
            if not activated_variants.has_key(toggle_layout):
                activated_variants[toggle_layout] = {}

            self.select_include_variant(toggle_layout, toggle_variant, 
                                        included_files[toggle_layout]["xml"])
        else:   # If the variant is toggled **OFF**
            #print "off"
            del activated_variants[toggle_layout][toggle_variant]
            if len(activated_variants[toggle_layout]) == 0:
                del activated_variants[toggle_layout]
            for keycode in KeyDict.Keys.keys():
                    KeyDict.Keys[keycode].key.extract_display_keyvalues()
                    KeyDict.Keys[keycode].key.redraw()

    def select_include_variant(self, layout, variant, xml_layout):
        if not activated_variants.has_key(layout):
            activated_variants[layout] = {}
            if not activated_variants[layout].has_key(variant):
                activated_variants[layout][variant] = {}
        if activated_variants[layout].has_key(variant):
            activated_variants[layout][variant].clear()
            activated_variants[layout][variant] = {}
        store_keydict = {}
        self.parse_xkb.parse_layout_controller(store_keydict, 
                                               Common.symbolsdir + layout, 
                                               variant)
        activated_variants[layout][variant] = copy.deepcopy(store_keydict)
        for keycode in activated_variants[layout][variant].keys():
            if KeyDict.Keys.has_key(keycode):
                KeyDict.Keys[keycode].key.extract_display_keyvalues()
                KeyDict.Keys[keycode].key.redraw()

    def changed_deadkey_combobox_callback(self, combobox):
        model = combobox.get_model()
        index = combobox.get_active()
        if index > -1:
            self.deadkey_label.set_text(model[index][0])
            for dk in DeadKeys.dict.keys():
                if DeadKeys.dict[dk][0] == model[index][0]:
                    Common.deadkey = dk
                    break
        self.set_deadkey_tooltip()

    def deadkey_drag_data_get_callback(self, widget, context, selection, 
                                       targetType, eventTime):
        if targetType == self.TARGET_TYPE_TEXT:
            label = widget.get_children()[0]
            deadkey_value = ''
            for deadkey in DeadKeys.dict.keys():
                if DeadKeys.dict[deadkey][0] == label.get_text():
                    deadkey_value = deadkey
            selection.set(selection.target, 8, deadkey_value)
        
    def on_selection_changed_callback(self, selection, button):
        model, paths = selection.get_selected_rows()
        self.include_layout_selected = { "model": model, "paths": paths }
        if self.include_layout_selected["paths"]:
            if len(paths[0]) == 1:
                button.set_sensitive(True)
            else:
                button.set_sensitive(False)

    def entry_callback(self, widget, event, entry):
        if entry == self.layoutdetails_entry_code:
            self.mykeyboard.layoutcode = entry.get_text()
        elif entry == self.layoutdetails_entry_variant:
            self.mykeyboard.layoutvariant = entry.get_text()
        elif entry == self.layoutdetails_entry_country:
            self.mykeyboard.layoutcountry = entry.get_text()
        elif entry == self.layoutdetails_entry_name:
            self.mykeyboard.layoutname = entry.get_text()
        else:
            SystemError("Internal error at entry boxes")

    def font_set_callback(self, fontbutton):
        newfont = fontbutton.get_font_name()
        context = self.window.create_pango_context()
        for family in context.list_families():
            if newfont.find(family.get_name()) == 0:
                face = family.list_faces()[0]
                Common.fontname = family.get_name()
                Common.fontsize = string.atoi(newfont.rpartition(' ')[-1], 10)
                Common.fontstyle = cairo.FONT_SLANT_NORMAL
                Common.fontweight = cairo.FONT_WEIGHT_NORMAL
                if face.get_face_name() == "Regular":
                    Common.fontstyle = cairo.FONT_SLANT_NORMAL
                if face.get_face_name() == "Bold":
                    Common.fontweight = cairo.FONT_SLANT_BOLD
                if face.get_face_name() == "Italic":
                    Common.fontstyle = cairo.FONT_SLANT_ITALIC
                if face.get_face_name() == "Oblique":
                    Common.fontstyle = cairo.FONT_SLANT_OBLIQUE
                break
        for keycode in KeyDict.Keys.keys():
            KeyDict.Keys[keycode].key.redraw()
        Common.addtostatusbar('Font set to ' + newfont + '.')

    def set_deadkey_tooltip(self):
        tooltip_string  = "Dead key: " + DeadKeys.dict[Common.deadkey][0] + "\n"
        tooltip_string += "Keysym: " + Common.deadkey + "\n"
        tooltip_string += "Representation: " + DeadKeys.dict[Common.deadkey][1]
        self.deadkey_tooltips.set_tip(self.deadkey_label, tooltip_string)
        
    def quit_application(self, arg):
        if self.layout_not_empty():
            if self.ask_to_save_first() == True:
                gtk.main_quit()

    def layout_not_empty(self):
        if activated_variants != {}:
            return True
        if self.mykeyboard.layoutcode != "" or \
                self.mykeyboard.layoutvariant != "" or \
                self.mykeyboard.layoutname != "":
            return True
        for keycode in KeyDict.Keys.keys():
            if keycode not in KeyDict.IgnoreKeys:
                for segment in Common.keysegmentslist:
                    if KeyDict.Keys[keycode].key.keyvalues[segment].getType() !=\
                                Common.keyvaluetype.NOSYMBOL:
                        return True
        return False
    
    def unicodechars_clicked_callback(self, button):
        os.spawnl(os.P_NOWAIT, Common.gucharmappath)

    def check_resize(self, container):
        pass    # TODO: Make sure the keyboard does not get too small.

    def error_dialog(self, message):
        notification_box = gtk.MessageDialog(parent=self.window, 
                                    flags=gtk.DIALOG_MODAL, 
                                    type=gtk.MESSAGE_INFO, 
                                    buttons=gtk.BUTTONS_OK, 
                                    message_format = message)
        notification_box.run()
        notification_box.destroy()
        
    def keypress_filter_callback(self, event, data = None):
        if event.type == gtk.gdk.KEY_PRESS:
            #print event.keyval, event.string
		pass
        gtk.main_do_event(event)

if __name__ == "__main__":
    myeditor = Controller_KeyboardLayoutEditor()

    gtk.main()
