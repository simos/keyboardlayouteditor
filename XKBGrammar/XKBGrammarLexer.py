# $ANTLR 3.1b1 XKBGrammar.g 2008-06-19 21:40:26

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
MAPOPTIONS=16
OVERLAY=27
TOKEN_INCLUDE=4
ELEM_VIRTUALMODS=24
ELEM_KEYSYMS=23
TOKEN_MODIFIER_MAP=9
EOF=-1
TOKEN_TYPE=8
MAPTYPE=14
TOKEN_VIRTUAL_MODIFIERS=11
NAME=30
T__51=51
MAPMATERIAL=17
MAPOPTS=28
COMMENT=32
DQSTRING=29
T__50=50
T__42=42
T__43=43
T__40=40
STATE=21
T__41=41
T__46=46
T__47=47
T__44=44
T__45=45
LINE_COMMENT=33
KEYCODE=18
T__48=48
T__49=49
TOKEN_NAME=6
VALUE=20
LAYOUT=12
WS=31
T__34=34
T__35=35
T__36=36
T__37=37
OVERRIDE=26
T__38=38
T__39=39
ELEM_KEYSYMGROUP=22
TOKEN_SYMBOL=10
MAPNAME=15
TOKEN_KEY=7
SYMBOLS=13
KEYELEMENTS=25
TOKEN_KEY_TYPE=5
KEYCODEX=19


class XKBGrammarLexer(Lexer):

    grammarFileName = "XKBGrammar.g"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa1 = self.DFA1(
            self, 1,
            eot = self.DFA1_eot,
            eof = self.DFA1_eof,
            min = self.DFA1_min,
            max = self.DFA1_max,
            accept = self.DFA1_accept,
            special = self.DFA1_special,
            transition = self.DFA1_transition
            )

        self.dfa2 = self.DFA2(
            self, 2,
            eot = self.DFA2_eot,
            eof = self.DFA2_eof,
            min = self.DFA2_min,
            max = self.DFA2_max,
            accept = self.DFA2_accept,
            special = self.DFA2_special,
            transition = self.DFA2_transition
            )

        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )






    # $ANTLR start T__34
    def mT__34(self, ):

        try:
            _type = T__34
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:7:7: ( '{' )
            # XKBGrammar.g:7:9: '{'
            self.match(123)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__34



    # $ANTLR start T__35
    def mT__35(self, ):

        try:
            _type = T__35
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:8:7: ( '}' )
            # XKBGrammar.g:8:9: '}'
            self.match(125)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__35



    # $ANTLR start T__36
    def mT__36(self, ):

        try:
            _type = T__36
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:9:7: ( ';' )
            # XKBGrammar.g:9:9: ';'
            self.match(59)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__36



    # $ANTLR start T__37
    def mT__37(self, ):

        try:
            _type = T__37
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:10:7: ( 'include' )
            # XKBGrammar.g:10:9: 'include'
            self.match("include")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__37



    # $ANTLR start T__38
    def mT__38(self, ):

        try:
            _type = T__38
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:11:7: ( 'name' )
            # XKBGrammar.g:11:9: 'name'
            self.match("name")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__38



    # $ANTLR start T__39
    def mT__39(self, ):

        try:
            _type = T__39
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:12:7: ( '[' )
            # XKBGrammar.g:12:9: '['
            self.match(91)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__39



    # $ANTLR start T__40
    def mT__40(self, ):

        try:
            _type = T__40
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:13:7: ( ']' )
            # XKBGrammar.g:13:9: ']'
            self.match(93)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__40



    # $ANTLR start T__41
    def mT__41(self, ):

        try:
            _type = T__41
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:14:7: ( '=' )
            # XKBGrammar.g:14:9: '='
            self.match(61)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__41



    # $ANTLR start T__42
    def mT__42(self, ):

        try:
            _type = T__42
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:15:7: ( 'key.type' )
            # XKBGrammar.g:15:9: 'key.type'
            self.match("key.type")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__42



    # $ANTLR start T__43
    def mT__43(self, ):

        try:
            _type = T__43
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:16:7: ( 'key' )
            # XKBGrammar.g:16:9: 'key'
            self.match("key")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__43



    # $ANTLR start T__44
    def mT__44(self, ):

        try:
            _type = T__44
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:17:7: ( '<' )
            # XKBGrammar.g:17:9: '<'
            self.match(60)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__44



    # $ANTLR start T__45
    def mT__45(self, ):

        try:
            _type = T__45
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:18:7: ( '>' )
            # XKBGrammar.g:18:9: '>'
            self.match(62)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__45



    # $ANTLR start T__46
    def mT__46(self, ):

        try:
            _type = T__46
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:19:7: ( ',' )
            # XKBGrammar.g:19:9: ','
            self.match(44)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__46



    # $ANTLR start T__47
    def mT__47(self, ):

        try:
            _type = T__47
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:20:7: ( 'modifier_map' )
            # XKBGrammar.g:20:9: 'modifier_map'
            self.match("modifier_map")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__47



    # $ANTLR start T__48
    def mT__48(self, ):

        try:
            _type = T__48
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:21:7: ( 'virtual_modifiers' )
            # XKBGrammar.g:21:9: 'virtual_modifiers'
            self.match("virtual_modifiers")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__48



    # $ANTLR start T__49
    def mT__49(self, ):

        try:
            _type = T__49
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:22:7: ( 'type' )
            # XKBGrammar.g:22:9: 'type'
            self.match("type")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__49



    # $ANTLR start T__50
    def mT__50(self, ):

        try:
            _type = T__50
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:23:7: ( 'symbols' )
            # XKBGrammar.g:23:9: 'symbols'
            self.match("symbols")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__50



    # $ANTLR start T__51
    def mT__51(self, ):

        try:
            _type = T__51
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:24:7: ( 'virtualMods' )
            # XKBGrammar.g:24:9: 'virtualMods'
            self.match("virtualMods")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__51



    # $ANTLR start MAPOPTS
    def mMAPOPTS(self, ):

        try:
            _type = MAPOPTS
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:151:2: ( 'default' | 'hidden' | 'partial' | 'alphanumeric_keys' | 'keypad_keys' | 'function_keys' | 'modifier_keys' | 'alternate_group' | 'xkb_symbols' )
            alt1 = 9
            alt1 = self.dfa1.predict(self.input)
            if alt1 == 1:
                # XKBGrammar.g:151:4: 'default'
                self.match("default")



            elif alt1 == 2:
                # XKBGrammar.g:152:4: 'hidden'
                self.match("hidden")



            elif alt1 == 3:
                # XKBGrammar.g:153:4: 'partial'
                self.match("partial")



            elif alt1 == 4:
                # XKBGrammar.g:154:4: 'alphanumeric_keys'
                self.match("alphanumeric_keys")



            elif alt1 == 5:
                # XKBGrammar.g:155:4: 'keypad_keys'
                self.match("keypad_keys")



            elif alt1 == 6:
                # XKBGrammar.g:156:4: 'function_keys'
                self.match("function_keys")



            elif alt1 == 7:
                # XKBGrammar.g:157:4: 'modifier_keys'
                self.match("modifier_keys")



            elif alt1 == 8:
                # XKBGrammar.g:158:4: 'alternate_group'
                self.match("alternate_group")



            elif alt1 == 9:
                # XKBGrammar.g:159:4: 'xkb_symbols'
                self.match("xkb_symbols")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end MAPOPTS



    # $ANTLR start STATE
    def mSTATE(self, ):

        try:
            _type = STATE
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:163:2: ( 'Shift' | 'Control' | 'Lock' | 'Mod1' | 'Mod2' | 'Mod3' | 'Mod4' | 'Mod5' )
            alt2 = 8
            alt2 = self.dfa2.predict(self.input)
            if alt2 == 1:
                # XKBGrammar.g:163:4: 'Shift'
                self.match("Shift")



            elif alt2 == 2:
                # XKBGrammar.g:164:4: 'Control'
                self.match("Control")



            elif alt2 == 3:
                # XKBGrammar.g:165:4: 'Lock'
                self.match("Lock")



            elif alt2 == 4:
                # XKBGrammar.g:166:4: 'Mod1'
                self.match("Mod1")



            elif alt2 == 5:
                # XKBGrammar.g:167:4: 'Mod2'
                self.match("Mod2")



            elif alt2 == 6:
                # XKBGrammar.g:168:4: 'Mod3'
                self.match("Mod3")



            elif alt2 == 7:
                # XKBGrammar.g:169:4: 'Mod4'
                self.match("Mod4")



            elif alt2 == 8:
                # XKBGrammar.g:170:4: 'Mod5'
                self.match("Mod5")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end STATE



    # $ANTLR start OVERRIDE
    def mOVERRIDE(self, ):

        try:
            _type = OVERRIDE
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:174:2: ( 'override' )
            # XKBGrammar.g:174:4: 'override'
            self.match("override")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end OVERRIDE



    # $ANTLR start NAME
    def mNAME(self, ):

        try:
            _type = NAME
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:178:2: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' | '+' | '-' )* )
            # XKBGrammar.g:178:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' | '+' | '-' )*
            # XKBGrammar.g:178:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' | '+' | '-' )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 43 or LA3_0 == 45 or (48 <= LA3_0 <= 57) or (65 <= LA3_0 <= 90) or LA3_0 == 95 or (97 <= LA3_0 <= 122)) :
                    alt3 = 1


                if alt3 == 1:
                    # XKBGrammar.g:
                    if self.input.LA(1) == 43 or self.input.LA(1) == 45 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume();
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop3






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end NAME



    # $ANTLR start WS
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:182:2: ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )
            # XKBGrammar.g:183:2: ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
            if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                self.input.consume();
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            #action start
            _channel=HIDDEN; 
            #action end




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end WS



    # $ANTLR start COMMENT
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:188:6: ( '/*' ( . )* '*/' )
            # XKBGrammar.g:189:2: '/*' ( . )* '*/'
            self.match("/*")
            # XKBGrammar.g:189:7: ( . )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 42) :
                    LA4_1 = self.input.LA(2)

                    if (LA4_1 == 47) :
                        alt4 = 2
                    elif ((0 <= LA4_1 <= 46) or (48 <= LA4_1 <= 65534)) :
                        alt4 = 1


                elif ((0 <= LA4_0 <= 41) or (43 <= LA4_0 <= 65534)) :
                    alt4 = 1


                if alt4 == 1:
                    # XKBGrammar.g:189:7: .
                    self.matchAny()



                else:
                    break #loop4


            self.match("*/")
            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end COMMENT



    # $ANTLR start LINE_COMMENT
    def mLINE_COMMENT(self, ):

        try:
            _type = LINE_COMMENT
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:193:6: ( ( '//' | '#' ) (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # XKBGrammar.g:194:2: ( '//' | '#' ) (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            # XKBGrammar.g:194:2: ( '//' | '#' )
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 47) :
                alt5 = 1
            elif (LA5_0 == 35) :
                alt5 = 2
            else:
                nvae = NoViableAltException("", 5, 0, self.input)

                raise nvae

            if alt5 == 1:
                # XKBGrammar.g:194:3: '//'
                self.match("//")



            elif alt5 == 2:
                # XKBGrammar.g:194:10: '#'
                self.match(35)




            # XKBGrammar.g:194:16: (~ ( '\\n' | '\\r' ) )*
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((0 <= LA6_0 <= 9) or (11 <= LA6_0 <= 12) or (14 <= LA6_0 <= 65534)) :
                    alt6 = 1


                if alt6 == 1:
                    # XKBGrammar.g:194:16: ~ ( '\\n' | '\\r' )
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65534):
                        self.input.consume();
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop6


            # XKBGrammar.g:194:32: ( '\\r' )?
            alt7 = 2
            LA7_0 = self.input.LA(1)

            if (LA7_0 == 13) :
                alt7 = 1
            if alt7 == 1:
                # XKBGrammar.g:194:32: '\\r'
                self.match(13)




            self.match(10)
            #action start
            _channel=HIDDEN; 
            #action end




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end LINE_COMMENT



    # $ANTLR start DQSTRING
    def mDQSTRING(self, ):

        try:
            _type = DQSTRING
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:202:6: ( '\"' ( options {greedy=false; } : ~ ( '\"' ) )* '\"' )
            # XKBGrammar.g:202:10: '\"' ( options {greedy=false; } : ~ ( '\"' ) )* '\"'
            self.match(34)
            # XKBGrammar.g:202:14: ( options {greedy=false; } : ~ ( '\"' ) )*
            while True: #loop8
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if ((0 <= LA8_0 <= 33) or (35 <= LA8_0 <= 65534)) :
                    alt8 = 1
                elif (LA8_0 == 34) :
                    alt8 = 2


                if alt8 == 1:
                    # XKBGrammar.g:202:39: ~ ( '\"' )
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 65534):
                        self.input.consume();
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop8


            self.match(34)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end DQSTRING



    def mTokens(self):
        # XKBGrammar.g:1:8: ( T__34 | T__35 | T__36 | T__37 | T__38 | T__39 | T__40 | T__41 | T__42 | T__43 | T__44 | T__45 | T__46 | T__47 | T__48 | T__49 | T__50 | T__51 | MAPOPTS | STATE | OVERRIDE | NAME | WS | COMMENT | LINE_COMMENT | DQSTRING )
        alt9 = 26
        alt9 = self.dfa9.predict(self.input)
        if alt9 == 1:
            # XKBGrammar.g:1:10: T__34
            self.mT__34()



        elif alt9 == 2:
            # XKBGrammar.g:1:16: T__35
            self.mT__35()



        elif alt9 == 3:
            # XKBGrammar.g:1:22: T__36
            self.mT__36()



        elif alt9 == 4:
            # XKBGrammar.g:1:28: T__37
            self.mT__37()



        elif alt9 == 5:
            # XKBGrammar.g:1:34: T__38
            self.mT__38()



        elif alt9 == 6:
            # XKBGrammar.g:1:40: T__39
            self.mT__39()



        elif alt9 == 7:
            # XKBGrammar.g:1:46: T__40
            self.mT__40()



        elif alt9 == 8:
            # XKBGrammar.g:1:52: T__41
            self.mT__41()



        elif alt9 == 9:
            # XKBGrammar.g:1:58: T__42
            self.mT__42()



        elif alt9 == 10:
            # XKBGrammar.g:1:64: T__43
            self.mT__43()



        elif alt9 == 11:
            # XKBGrammar.g:1:70: T__44
            self.mT__44()



        elif alt9 == 12:
            # XKBGrammar.g:1:76: T__45
            self.mT__45()



        elif alt9 == 13:
            # XKBGrammar.g:1:82: T__46
            self.mT__46()



        elif alt9 == 14:
            # XKBGrammar.g:1:88: T__47
            self.mT__47()



        elif alt9 == 15:
            # XKBGrammar.g:1:94: T__48
            self.mT__48()



        elif alt9 == 16:
            # XKBGrammar.g:1:100: T__49
            self.mT__49()



        elif alt9 == 17:
            # XKBGrammar.g:1:106: T__50
            self.mT__50()



        elif alt9 == 18:
            # XKBGrammar.g:1:112: T__51
            self.mT__51()



        elif alt9 == 19:
            # XKBGrammar.g:1:118: MAPOPTS
            self.mMAPOPTS()



        elif alt9 == 20:
            # XKBGrammar.g:1:126: STATE
            self.mSTATE()



        elif alt9 == 21:
            # XKBGrammar.g:1:132: OVERRIDE
            self.mOVERRIDE()



        elif alt9 == 22:
            # XKBGrammar.g:1:141: NAME
            self.mNAME()



        elif alt9 == 23:
            # XKBGrammar.g:1:146: WS
            self.mWS()



        elif alt9 == 24:
            # XKBGrammar.g:1:149: COMMENT
            self.mCOMMENT()



        elif alt9 == 25:
            # XKBGrammar.g:1:157: LINE_COMMENT
            self.mLINE_COMMENT()



        elif alt9 == 26:
            # XKBGrammar.g:1:170: DQSTRING
            self.mDQSTRING()








    # lookup tables for DFA #1

    DFA1_eot = DFA.unpack(
        u"\14\uffff"
        )

    DFA1_eof = DFA.unpack(
        u"\14\uffff"
        )

    DFA1_min = DFA.unpack(
        u"\1\141\3\uffff\1\154\4\uffff\1\160\2\uffff"
        )

    DFA1_max = DFA.unpack(
        u"\1\170\3\uffff\1\154\4\uffff\1\164\2\uffff"
        )

    DFA1_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\uffff\1\5\1\6\1\7\1\11\1\uffff\1\4\1\10"
        )

    DFA1_special = DFA.unpack(
        u"\14\uffff"
        )

            
    DFA1_transition = [
        DFA.unpack(u"\1\4\2\uffff\1\1\1\uffff\1\6\1\uffff\1\2\2\uffff\1\5"
        u"\1\uffff\1\7\2\uffff\1\3\7\uffff\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12\3\uffff\1\13"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #1

    DFA1 = DFA
    # lookup tables for DFA #2

    DFA2_eot = DFA.unpack(
        u"\14\uffff"
        )

    DFA2_eof = DFA.unpack(
        u"\14\uffff"
        )

    DFA2_min = DFA.unpack(
        u"\1\103\3\uffff\1\157\1\144\1\61\5\uffff"
        )

    DFA2_max = DFA.unpack(
        u"\1\123\3\uffff\1\157\1\144\1\65\5\uffff"
        )

    DFA2_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\3\uffff\1\4\1\5\1\6\1\7\1\10"
        )

    DFA2_special = DFA.unpack(
        u"\14\uffff"
        )

            
    DFA2_transition = [
        DFA.unpack(u"\1\2\10\uffff\1\3\1\4\5\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u"\1\7\1\10\1\11\1\12\1\13"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #2

    DFA2 = DFA
    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        u"\1\34\3\uffff\2\34\3\uffff\1\34\3\uffff\17\34\5\uffff\22\34\1\uffff"
        u"\2\34\1\113\21\34\1\141\1\uffff\1\34\1\uffff\2\34\1\145\12\34\6"
        u"\160\2\34\1\uffff\3\34\1\uffff\10\34\1\160\1\34\1\uffff\7\34\1"
        u"\u0086\7\34\1\u008e\3\34\1\u0093\1\u0086\1\uffff\1\u0086\4\34\1"
        u"\160\1\34\1\uffff\4\34\1\uffff\4\34\1\u00a1\10\34\1\uffff\11\34"
        u"\1\u0086\3\34\1\u00b7\3\34\1\u0086\1\u00bb\2\34\1\uffff\3\34\1"
        u"\uffff\1\u0086\3\34\1\u0086\5\34\1\u0086\2\34\1\u00cb\1\u0086\1"
        u"\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\u00cc\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\1\11\3\uffff\1\156\1\141\3\uffff\1\145\3\uffff\1\157\1\151\2\171"
        u"\1\145\1\151\1\141\1\154\1\165\1\153\1\150\3\157\1\166\2\uffff"
        u"\1\52\2\uffff\1\143\1\155\1\171\1\144\1\162\1\160\1\155\1\146\1"
        u"\144\1\162\1\160\1\156\1\142\1\151\1\156\1\143\1\144\1\145\1\uffff"
        u"\1\154\1\145\1\53\1\151\1\164\1\145\1\142\1\141\1\144\1\164\1\150"
        u"\1\145\1\143\1\137\1\146\1\164\1\153\1\61\1\162\1\165\1\53\1\uffff"
        u"\1\141\1\uffff\1\146\1\165\1\53\1\157\1\165\1\145\1\151\1\141\1"
        u"\162\1\164\1\163\1\164\1\162\6\53\1\162\1\144\1\uffff\1\144\1\151"
        u"\1\141\1\uffff\2\154\1\156\1\141\2\156\1\151\1\171\1\53\1\157\1"
        u"\uffff\1\151\1\145\1\137\1\145\1\154\1\163\1\164\1\53\1\154\1\165"
        u"\1\141\1\157\1\155\1\154\1\144\1\53\1\153\1\162\1\115\2\53\1\uffff"
        u"\1\53\1\155\1\164\1\156\1\142\1\53\1\145\1\uffff\1\145\1\137\1"
        u"\155\1\157\1\uffff\2\145\1\137\1\157\1\53\1\171\1\153\1\157\1\144"
        u"\1\162\1\137\1\153\1\154\1\uffff\1\163\1\141\1\145\1\144\1\163"
        u"\1\151\1\147\1\145\1\163\1\53\1\160\1\171\1\151\1\53\1\143\1\162"
        u"\1\171\2\53\1\163\1\146\1\uffff\1\137\1\157\1\163\1\uffff\1\53"
        u"\1\151\1\153\1\165\1\53\2\145\1\160\1\162\1\171\1\53\2\163\2\53"
        u"\1\uffff"
        )

    DFA9_max = DFA.unpack(
        u"\1\175\3\uffff\1\156\1\141\3\uffff\1\145\3\uffff\1\157\1\151\2"
        u"\171\1\145\1\151\1\141\1\154\1\165\1\153\1\150\3\157\1\166\2\uffff"
        u"\1\57\2\uffff\1\143\1\155\1\171\1\144\1\162\1\160\1\155\1\146\1"
        u"\144\1\162\1\164\1\156\1\142\1\151\1\156\1\143\1\144\1\145\1\uffff"
        u"\1\154\1\145\1\172\1\151\1\164\1\145\1\142\1\141\1\144\1\164\1"
        u"\150\1\145\1\143\1\137\1\146\1\164\1\153\1\65\1\162\1\165\1\172"
        u"\1\uffff\1\141\1\uffff\1\146\1\165\1\172\1\157\1\165\1\145\1\151"
        u"\1\141\1\162\1\164\1\163\1\164\1\162\6\172\1\162\1\144\1\uffff"
        u"\1\144\1\151\1\141\1\uffff\2\154\1\156\1\141\2\156\1\151\1\171"
        u"\1\172\1\157\1\uffff\1\151\1\145\1\137\1\145\1\154\1\163\1\164"
        u"\1\172\1\154\1\165\1\141\1\157\1\155\1\154\1\144\1\172\1\153\1"
        u"\162\1\137\2\172\1\uffff\1\172\1\155\1\164\1\156\1\142\1\172\1"
        u"\145\1\uffff\1\145\1\137\1\155\1\157\1\uffff\2\145\1\137\1\157"
        u"\1\172\1\171\1\155\1\157\1\144\1\162\1\137\1\153\1\154\1\uffff"
        u"\1\163\1\141\1\145\1\144\1\163\1\151\1\147\1\145\1\163\1\172\1"
        u"\160\1\171\1\151\1\172\1\143\1\162\1\171\2\172\1\163\1\146\1\uffff"
        u"\1\137\1\157\1\163\1\uffff\1\172\1\151\1\153\1\165\1\172\2\145"
        u"\1\160\1\162\1\171\1\172\2\163\2\172\1\uffff"
        )

    DFA9_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\2\uffff\1\6\1\7\1\10\1\uffff\1\13\1\14\1\15"
        u"\17\uffff\1\26\1\27\1\uffff\1\31\1\32\22\uffff\1\30\25\uffff\1"
        u"\11\1\uffff\1\12\25\uffff\1\5\3\uffff\1\20\12\uffff\1\24\25\uffff"
        u"\1\23\7\uffff\1\4\4\uffff\1\21\15\uffff\1\25\25\uffff\1\22\3\uffff"
        u"\1\16\17\uffff\1\17"
        )

    DFA9_special = DFA.unpack(
        u"\u00cc\uffff"
        )

            
    DFA9_transition = [
        DFA.unpack(u"\2\35\1\uffff\2\35\22\uffff\1\35\1\uffff\1\40\1\37\10"
        u"\uffff\1\14\2\uffff\1\36\13\uffff\1\3\1\12\1\10\1\13\4\uffff\1"
        u"\30\10\uffff\1\31\1\32\5\uffff\1\27\7\uffff\1\6\1\uffff\1\7\3\uffff"
        u"\1\24\2\uffff\1\21\1\uffff\1\25\1\uffff\1\22\1\4\1\uffff\1\11\1"
        u"\uffff\1\15\1\5\1\33\1\23\2\uffff\1\20\1\17\1\uffff\1\16\1\uffff"
        u"\1\26\2\uffff\1\1\1\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\41"),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\44"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u"\1\53"),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u"\1\57"),
        DFA.unpack(u"\1\60"),
        DFA.unpack(u"\1\61"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\63\4\uffff\1\37"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u"\1\75"),
        DFA.unpack(u"\1\76\3\uffff\1\77"),
        DFA.unpack(u"\1\100"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\102"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\1\34\1\uffff\1\34\1\111\1\uffff\12\34\7\uffff\32\34"
        u"\4\uffff\1\34\1\uffff\17\34\1\112\12\34"),
        DFA.unpack(u"\1\114"),
        DFA.unpack(u"\1\115"),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u"\1\117"),
        DFA.unpack(u"\1\120"),
        DFA.unpack(u"\1\121"),
        DFA.unpack(u"\1\122"),
        DFA.unpack(u"\1\123"),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u"\1\125"),
        DFA.unpack(u"\1\126"),
        DFA.unpack(u"\1\127"),
        DFA.unpack(u"\1\130"),
        DFA.unpack(u"\1\131"),
        DFA.unpack(u"\1\132\1\133\1\134\1\135\1\136"),
        DFA.unpack(u"\1\137"),
        DFA.unpack(u"\1\140"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\142"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\143"),
        DFA.unpack(u"\1\144"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\146"),
        DFA.unpack(u"\1\147"),
        DFA.unpack(u"\1\150"),
        DFA.unpack(u"\1\151"),
        DFA.unpack(u"\1\152"),
        DFA.unpack(u"\1\153"),
        DFA.unpack(u"\1\154"),
        DFA.unpack(u"\1\155"),
        DFA.unpack(u"\1\156"),
        DFA.unpack(u"\1\157"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\161"),
        DFA.unpack(u"\1\162"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\163"),
        DFA.unpack(u"\1\164"),
        DFA.unpack(u"\1\165"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\166"),
        DFA.unpack(u"\1\167"),
        DFA.unpack(u"\1\170"),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u"\1\172"),
        DFA.unpack(u"\1\173"),
        DFA.unpack(u"\1\174"),
        DFA.unpack(u"\1\175"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\177"),
        DFA.unpack(u"\1\u0080"),
        DFA.unpack(u"\1\u0081"),
        DFA.unpack(u"\1\u0082"),
        DFA.unpack(u"\1\u0083"),
        DFA.unpack(u"\1\u0084"),
        DFA.unpack(u"\1\u0085"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u0087"),
        DFA.unpack(u"\1\u0088"),
        DFA.unpack(u"\1\u0089"),
        DFA.unpack(u"\1\u008a"),
        DFA.unpack(u"\1\u008b"),
        DFA.unpack(u"\1\u008c"),
        DFA.unpack(u"\1\u008d"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u008f"),
        DFA.unpack(u"\1\u0090"),
        DFA.unpack(u"\1\u0092\21\uffff\1\u0091"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u0094"),
        DFA.unpack(u"\1\u0095"),
        DFA.unpack(u"\1\u0096"),
        DFA.unpack(u"\1\u0097"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u0098"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0099"),
        DFA.unpack(u"\1\u009a"),
        DFA.unpack(u"\1\u009b"),
        DFA.unpack(u"\1\u009c"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u009d"),
        DFA.unpack(u"\1\u009e"),
        DFA.unpack(u"\1\u009f"),
        DFA.unpack(u"\1\u00a0"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00a2"),
        DFA.unpack(u"\1\u00a4\1\uffff\1\u00a3"),
        DFA.unpack(u"\1\u00a5"),
        DFA.unpack(u"\1\u00a6"),
        DFA.unpack(u"\1\u00a7"),
        DFA.unpack(u"\1\u00a8"),
        DFA.unpack(u"\1\u00a9"),
        DFA.unpack(u"\1\u00aa"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00ab"),
        DFA.unpack(u"\1\u00ac"),
        DFA.unpack(u"\1\u00ad"),
        DFA.unpack(u"\1\u00ae"),
        DFA.unpack(u"\1\u00af"),
        DFA.unpack(u"\1\u00b0"),
        DFA.unpack(u"\1\u00b1"),
        DFA.unpack(u"\1\u00b2"),
        DFA.unpack(u"\1\u00b3"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00b4"),
        DFA.unpack(u"\1\u00b5"),
        DFA.unpack(u"\1\u00b6"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00b8"),
        DFA.unpack(u"\1\u00b9"),
        DFA.unpack(u"\1\u00ba"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00bc"),
        DFA.unpack(u"\1\u00bd"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00be"),
        DFA.unpack(u"\1\u00bf"),
        DFA.unpack(u"\1\u00c0"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00c1"),
        DFA.unpack(u"\1\u00c2"),
        DFA.unpack(u"\1\u00c3"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00c4"),
        DFA.unpack(u"\1\u00c5"),
        DFA.unpack(u"\1\u00c6"),
        DFA.unpack(u"\1\u00c7"),
        DFA.unpack(u"\1\u00c8"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00c9"),
        DFA.unpack(u"\1\u00ca"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff\32\34\4\uffff"
        u"\1\34\1\uffff\32\34"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #9

    DFA9 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(XKBGrammarLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)

if __name__ == '__main__':
    main(sys.argv)
