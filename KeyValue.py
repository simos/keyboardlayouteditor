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
import Keysyms
from DeadKeysDict import DeadKeys
from KeysymsUniByValue import KeysymsUniByValue
from KeysymsUni import KeysymsUni


class KeyValue:
    def __init__(self, value=None, verbatim=False):
        # Any of Common.keyvaluetype.
        self.__type__ = ""
        # String that goes to the XKB file
        self.__value__ = ""
        # String shown in the editor
        self.__presentation_value__ = ""

        if value != None:
            self.add(value, verbatim)

    def getType(self):
        return self.__type__

    def getValue(self):
        return self.__value__

    def getPValue(self):
        """ Accessor to retrieve the PresenationValue """
        return self.__presentation_value__

    def tostring(self):
        return "type: %(type)s, value: %(value)s, pvalue: %(pvalue)s" % \
               {"type": self.getType(), "value": self.getValue(),
                "pvalue": self.getPValue()}

    def copy(self, existing):
        self.__type__ = existing.getType()
        self.__value__ = existing.getValue()
        self.__presentation_value__ = existing.getPValue()

    def reset(self):
        self.add(decode, '')

    def add(self, value, verbatim=False):
        if verbatim:
            if value != '':
                self.__type__ = Common.keyvaluetype.VERBATIM
                self.__value__ = value
                self.__presentation_value__ = value
                return
        try:
            intval = ord(value.decode('utf8'))
        except TypeError as e:
            intval = 0
        if value == '':
            """ If value is empty, we put NoSymbol and inherit from above. """
            self.__type__ = Common.keyvaluetype.NOSYMBOL
            self.__value__ = ''
            self.__presentation_value__ = ''
        elif intval > 0:
            """ If value is a verbatim character, """
            if KeysymsUniByValue.has_key(intval):
                self.__type__ = Common.keyvaluetype.KEYSYM
                self.__value__ = KeysymsUniByValue[intval]
                self.__presentation_value__ = value
            else:
                self.__type__ = Common.keyvaluetype.CODEPOINT
                self.__value__ = 'U' + "%04X" % intval
                self.__presentation_value__ = value
        elif value[0] == 'U':
            """ if value is of the form Uxxxx, where xxxx a hex number, """
            try:
                val = int(value[1:], 16)
            except ValueError as e:
                val = 0
            if val > 0:
                self.__type__ = Common.keyvaluetype.CODEPOINT
                self.__value__ = value
                self.__presentation_value__ = unichr(val)
        elif value[0] == '0':
            """ if value is of the form 0x1000..., a hex number, """
            try:
                val = int(value, 16)
            except ValueError:
                val = 0
            if val > 0:
                if val < 0x1000000:
                    SystemError("Encountered constant that was supposed to be over\
                    0x1000 000. This should not have happened because we\
                    changed this in the code, all over the place.\
                    Sorry, I cannot continue. Error with %(e)s, value %(v)d"
                                % {"e": value, "v": val})
                self.__type__ = Common.keyvaluetype.CONSTANT
                self.__value__ = value.lower()
                self.__presentation_value__ = unichr(val - 0x1000000)  # TODO: 0x200E (special)
        elif value[:5] == "dead_":
            self.__type__ = Common.keyvaluetype.DEADKEY
            self.__value__ = value
            self.__presentation_value__ = "D" + DeadKeys.dict[value][1]
        else:
            self.__type__ = Common.keyvaluetype.KEYSYM
            self.__value__ = value
            if KeysymsUni.has_key(value):
                self.__presentation_value__ = unichr(KeysymsUni[value])
            elif value in ["VoidSymbol", "voidsymbol"]:
                """ If value is empty, we put VoidSymbol and inherit from above. """
                self.__type__ = Common.keyvaluetype.VOIDSYMBOL
                self.__value__ = ''
                self.__presentation_value__ = ''
            elif value in ["NoSymbol", "noSymbol", "Nosymbol"]:
                """ If value is empty, we put NoSymbol and inherit from above. """
                self.__type__ = Common.keyvaluetype.NOSYMBOL
                self.__value__ = ''
                self.__presentation_value__ = ''
            elif value == "NoAction":
                """ If value is empty, we put NoAction and inherit from above. """
                self.__type__ = Common.keyvaluetype.NOACTION
                self.__value__ = ''
                self.__presentation_value__ = ''
            else:
                self.__presentation_value__ = value


if __name__ == "__main__":
    print(KeyValue("U0392").tostring())
    print(KeyValue("U4FE8").tostring())
    print(KeyValue("0x1000389").tostring())
    print(KeyValue("dead_acute").tostring())
    print(KeyValue("0x1000392").tostring())
    print(KeyValue("A").tostring())
    print(KeyValue("'").tostring())
    print(KeyValue("α").tostring())
