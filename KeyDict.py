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

import Key
import Common

class KeyDictClass:
    def __init__(self):
        self.Keys = {} 

	self.IgnoreKeys = [ "ESC", "FK01", "FK02", "FK03", "FK04", "FK05", "FK06", 
                        "FK07", "FK08", "FK09", "FK10", "FK11", "FK12",
		                "BKSP", "TAB", "CAPS", "RTRN", "LFSH", "RTSH", "LCTL", 
                        "LWIN", "LALT", "SPCE", "RALT", "RWIN", "MENU", "RCTL" ]

    def set(self):
        self.Keys = {
                "ESC" : Key.Key(1, "ESC",  False, Common.keytypes.SPECIAL,'Esc'),
                "FK01": Key.Key(1, "FK01", False, Common.keytypes.SIMPLE, 'F1'),
                "FK02": Key.Key(1, "FK02", False, Common.keytypes.SIMPLE, 'F2'),
                "FK03": Key.Key(1, "FK03", False, Common.keytypes.SIMPLE, 'F3'),
                "FK04": Key.Key(1, "FK04", False, Common.keytypes.SIMPLE, 'F4'),
                "FK05": Key.Key(1, "FK05", False, Common.keytypes.SIMPLE, 'F5'),
                "FK06": Key.Key(1, "FK06", False, Common.keytypes.SIMPLE, 'F6'),
                "FK07": Key.Key(1, "FK07", False, Common.keytypes.SIMPLE, 'F7'),
                "FK08": Key.Key(1, "FK08", False, Common.keytypes.SIMPLE, 'F8'),
                "FK09": Key.Key(1, "FK09", False, Common.keytypes.SIMPLE, 'F9'),
                "FK10": Key.Key(1, "FK10", False, Common.keytypes.SIMPLE, 'F10'),
                "FK11": Key.Key(1, "FK11", False, Common.keytypes.SIMPLE, 'F11'),
                "FK12": Key.Key(1, "FK12", False, Common.keytypes.SIMPLE, 'F12'),

                "TLDE": Key.Key(1, "TLDE", False, Common.keytypes.SIMPLE),
                "AE01": Key.Key(1, "AE01", False, Common.keytypes.SIMPLE),
                "AE02": Key.Key(1, "AE02", False, Common.keytypes.SIMPLE),
                "AE03": Key.Key(1, "AE03", False, Common.keytypes.SIMPLE),
                "AE04": Key.Key(1, "AE04", False, Common.keytypes.SIMPLE),
                "AE05": Key.Key(1, "AE05", False, Common.keytypes.SIMPLE),
                "AE06": Key.Key(1, "AE06", False, Common.keytypes.SIMPLE),
                "AE07": Key.Key(1, "AE07", False, Common.keytypes.SIMPLE),
                "AE08": Key.Key(1, "AE08", False, Common.keytypes.SIMPLE),
                "AE09": Key.Key(1, "AE09", False, Common.keytypes.SIMPLE),
                "AE10": Key.Key(1, "AE10", False, Common.keytypes.SIMPLE),
                "AE11": Key.Key(1, "AE11", False, Common.keytypes.SIMPLE),
                "AE12": Key.Key(1, "AE12", False, Common.keytypes.SIMPLE),
                "BKSP": Key.Key(2, "BKSP", False, Common.keytypes.SPECIAL,'Backspace ⌫'),

                "TAB" : Key.Key(1.8, "TAB", False, Common.keytypes.SPECIAL, 'Tab ↹', 'ISO_Left'),
                "AD01": Key.Key(1, "AD01", False, Common.keytypes.SIMPLE),
                "AD02": Key.Key(1, "AD02", False, Common.keytypes.SIMPLE),
                "AD03": Key.Key(1, "AD03", False, Common.keytypes.SIMPLE),
                "AD04": Key.Key(1, "AD04", False, Common.keytypes.SIMPLE),
                "AD05": Key.Key(1, "AD05", False, Common.keytypes.SIMPLE),
                "AD06": Key.Key(1, "AD06", False, Common.keytypes.SIMPLE),
                "AD07": Key.Key(1, "AD07", False, Common.keytypes.SIMPLE),
                "AD08": Key.Key(1, "AD08", False, Common.keytypes.SIMPLE),
                "AD09": Key.Key(1, "AD09", False, Common.keytypes.SIMPLE),
                "AD10": Key.Key(1, "AD10", False, Common.keytypes.SIMPLE),
                "AD11": Key.Key(1, "AD11", False, Common.keytypes.SIMPLE),
                "AD12": Key.Key(1, "AD12", False, Common.keytypes.SIMPLE),
                "BKSL": Key.Key(1, "BKSL", False, Common.keytypes.SIMPLE),

                "CAPS": Key.Key(2, "CAPS", False, Common.keytypes.SPECIAL, 'Caps Lock ⇩'),
                "AC01": Key.Key(1, "AC01", False, Common.keytypes.SIMPLE),
                "AC02": Key.Key(1, "AC02", False, Common.keytypes.SIMPLE),
                "AC03": Key.Key(1, "AC03", False, Common.keytypes.SIMPLE),
                "AC04": Key.Key(1, "AC04", False, Common.keytypes.SIMPLE),
                "AC05": Key.Key(1, "AC05", False, Common.keytypes.SIMPLE),
                "AC06": Key.Key(1, "AC06", False, Common.keytypes.SIMPLE),
                "AC07": Key.Key(1, "AC07", False, Common.keytypes.SIMPLE),
                "AC08": Key.Key(1, "AC08", False, Common.keytypes.SIMPLE),
                "AC09": Key.Key(1, "AC09", False, Common.keytypes.SIMPLE),
                "AC10": Key.Key(1, "AC10", False, Common.keytypes.SIMPLE),
                "AC11": Key.Key(1, "AC11", False,Common.keytypes.SIMPLE),
                "RTRN": Key.Key(2, "RTRN", False, Common.keytypes.SPECIAL, 'Return ↵'),

                "LFSH": Key.Key(1,   "LFSH", False, Common.keytypes.SPECIAL,'Shift L ⇧', 'ISO Prev'),
                "LSGT": Key.Key(1,   "LSGT", False, Common.keytypes.SIMPLE),
                "AB01": Key.Key(1,   "AB01", False, Common.keytypes.SIMPLE),
                "AB02": Key.Key(1,   "AB02", False, Common.keytypes.SIMPLE),
                "AB03": Key.Key(1,   "AB03", False, Common.keytypes.SIMPLE),
                "AB04": Key.Key(1,   "AB04", False, Common.keytypes.SIMPLE),
                "AB05": Key.Key(1,   "AB05", False, Common.keytypes.SIMPLE),
                "AB06": Key.Key(1,   "AB06", False, Common.keytypes.SIMPLE),
                "AB07": Key.Key(1,   "AB07", False, Common.keytypes.SIMPLE),
                "AB08": Key.Key(1,   "AB08", False, Common.keytypes.SIMPLE),
                "AB09": Key.Key(1,   "AB09", False, Common.keytypes.SIMPLE),
                "AB10": Key.Key(1,   "AB10", False, Common.keytypes.SIMPLE),
                "RTSH": Key.Key(2.5, "RTSH", False, Common.keytypes.SPECIAL, 'Shift R ⇧', 'ISO Next'),

                "LCTL": Key.Key(1.8, "LCTL", False, Common.keytypes.SPECIAL, 'Control L'),
                "LWIN": Key.Key(1.5, "LWIN", False, Common.keytypes.SPECIAL, 'Super L'),
                "LALT": Key.Key(1.5, "LALT", False, Common.keytypes.SPECIAL, 'Alt L'),
                "SPCE": Key.Key(9.0, "SPCE", False, Common.keytypes.SIMPLE, 'Spacebar'),
                "RALT": Key.Key(1.3, "RALT", False, Common.keytypes.SPECIAL, 'AltGr'),
                "RWIN": Key.Key(1.3, "RWIN", False, Common.keytypes.SPECIAL, 'Super R'),
                "MENU": Key.Key(1.3, "MENU", False, Common.keytypes.SPECIAL, 'Compose'),
                "RCTL": Key.Key(1.5, "RCTL", False, Common.keytypes.SPECIAL, 'Control R')
            }

# The dict keeps the current variants that are selected.
# For example, { "latin": {"basic": parsed1, "east": parsed2}, 
#                 "kpdl": {"one": parsed3, "two":parsed4} }
activated_variants = {}
        
# This dict keeps track of included files
# For example, included_files["latin"] = { "file": "/tmp/latin", 
#    "variants": variants_list, "xml": xml_layout }
included_files = {}

KeyDict = KeyDictClass()

if __name__ == "__main__":
    for k in KeyDict.Keys.keys():
        print k, KeyDict.Keys[k] 
