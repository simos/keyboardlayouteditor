#!/usr/bin/env python
#     -*- encoding: UTF-8 -*-
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

class DeadKeysClass:
    def __init__(self):
        self.dict = {
            'dead_grave': ('Grave', '`'),
            'dead_acute': ('Acute', '´'),
            'dead_circumflex': ('Circumflex', '^'),
            'dead_tilde': ('Tilde', '~'),
            'dead_perispomeni': ('Perispomeni', '῀'),
            'dead_macron': ('Macron', 'ˉ'),
            'dead_breve': ('Breve', '˘'),
            'dead_abovedot': ('Abovedot', '˙'),
            'dead_diaeresis': ('Diaeresis', '¨'),
            'dead_abovering': ('Abovering', '˚'),
            'dead_doubleacute': ('Double Acute', '˝'),
            'dead_caron': ('Caron', 'ˇ'),
            'dead_cedilla': ('Cedilla', '¸'),
            'dead_ogonek': ('Ogonek', '˛'),
            'dead_iota': ('Iota', 'ͺ'),
            'dead_voiced_sound': ('Voiced Sound', 'ﾞ'),  # TODO (maybe)
            'dead_semivoiced_sound': ('Semivoiced Sound', 'ﾟ'),  # TODO (maybe)
            'dead_belowdot': ('Below Dot', '?'),  # TODO
            'dead_hook': ('Hook', '?'),  # TODO
            'dead_horn': ('Horn', '?'),  # TODO
            'dead_stroke': ('Stroke', '?'),  # TODO
            'dead_abovecomma': ('Above Comma', '?'),  # TODO
            'dead_psili': ('Psili', '?'),  # TODO
            'dead_abovereversedcomma': ('Above Reversed Comma', 'ʽ'),
            'dead_dasia': ('Dasia', '῾'),
            'dead_belowring': ('Below Ring', '˳'),
            'dead_belowmacron': ('Below Macron', 'ˍ'),
            'dead_belowcircumflex': ('Below Circumflex', 'ˬ'),
            'dead_belowtilde': ('Below Tilde', '˷'),
            'dead_belowbreve': ('Below Breve', '?'),  # TODO
            'dead_belowdiaeresis': ('Below Diaeresis', '?')}  # TODO


DeadKeys = DeadKeysClass()

if __name__ == "__main__":
    for k in DeadKeys.dict.keys():
        print(k, DeadKeys.dict[k])
