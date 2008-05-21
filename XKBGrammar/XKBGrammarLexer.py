# $ANTLR 3.1b1 XKBGrammar.g 2008-05-21 02:16:01

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__29=29
T__28=28
MAPOPTIONS=13
TOKEN_INCLUDE=4
TOKEN_MODIFIER_MAP=9
EOF=-1
TOKEN_TYPE=8
MAPTYPE=11
T__55=55
T__56=56
T__57=57
T__58=58
NAME=24
T__51=51
T__52=52
T__53=53
MAPMATERIAL=14
T__54=54
T__59=59
KEYSYMS=18
COMMENT=26
DQSTRING=23
T__50=50
T__42=42
T__43=43
STATE=20
T__40=40
T__41=41
T__46=46
T__47=47
T__44=44
SECTION=15
T__45=45
LINE_COMMENT=27
KEYCODE=16
T__48=48
T__49=49
TOKEN_NAME=6
VALUE=19
LAYOUT=10
T__30=30
T__31=31
T__32=32
T__33=33
WS=25
T__34=34
T__35=35
T__36=36
T__37=37
T__38=38
OVERRIDE=22
T__39=39
KEYSYMGROUP=21
TOKEN_KEY=7
MAPNAME=12
TOKEN_KEY_TYPE=5
KEYCODEX=17


class XKBGrammarLexer(Lexer):

    grammarFileName = "XKBGrammar.g"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa7 = self.DFA7(
            self, 7,
            eot = self.DFA7_eot,
            eof = self.DFA7_eof,
            min = self.DFA7_min,
            max = self.DFA7_max,
            accept = self.DFA7_accept,
            special = self.DFA7_special,
            transition = self.DFA7_transition
            )






    # $ANTLR start T__28
    def mT__28(self, ):

        try:
            _type = T__28
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:7:7: ( '{' )
            # XKBGrammar.g:7:9: '{'
            self.match(123)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__28



    # $ANTLR start T__29
    def mT__29(self, ):

        try:
            _type = T__29
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:8:7: ( '}' )
            # XKBGrammar.g:8:9: '}'
            self.match(125)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__29



    # $ANTLR start T__30
    def mT__30(self, ):

        try:
            _type = T__30
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:9:7: ( ';' )
            # XKBGrammar.g:9:9: ';'
            self.match(59)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__30



    # $ANTLR start T__31
    def mT__31(self, ):

        try:
            _type = T__31
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:10:7: ( 'include' )
            # XKBGrammar.g:10:9: 'include'
            self.match("include")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__31



    # $ANTLR start T__32
    def mT__32(self, ):

        try:
            _type = T__32
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:11:7: ( 'name' )
            # XKBGrammar.g:11:9: 'name'
            self.match("name")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__32



    # $ANTLR start T__33
    def mT__33(self, ):

        try:
            _type = T__33
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:12:7: ( '[' )
            # XKBGrammar.g:12:9: '['
            self.match(91)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__33



    # $ANTLR start T__34
    def mT__34(self, ):

        try:
            _type = T__34
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:13:7: ( ']' )
            # XKBGrammar.g:13:9: ']'
            self.match(93)




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

            # XKBGrammar.g:14:7: ( '=' )
            # XKBGrammar.g:14:9: '='
            self.match(61)




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

            # XKBGrammar.g:15:7: ( 'key.type' )
            # XKBGrammar.g:15:9: 'key.type'
            self.match("key.type")




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

            # XKBGrammar.g:16:7: ( 'override' )
            # XKBGrammar.g:16:9: 'override'
            self.match("override")




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

            # XKBGrammar.g:17:7: ( 'key' )
            # XKBGrammar.g:17:9: 'key'
            self.match("key")




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

            # XKBGrammar.g:18:7: ( 'modifier_map' )
            # XKBGrammar.g:18:9: 'modifier_map'
            self.match("modifier_map")




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

            # XKBGrammar.g:19:7: ( ',' )
            # XKBGrammar.g:19:9: ','
            self.match(44)




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

            # XKBGrammar.g:20:7: ( '<' )
            # XKBGrammar.g:20:9: '<'
            self.match(60)




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

            # XKBGrammar.g:21:7: ( '>' )
            # XKBGrammar.g:21:9: '>'
            self.match(62)




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

            # XKBGrammar.g:22:7: ( 'type' )
            # XKBGrammar.g:22:9: 'type'
            self.match("type")




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

            # XKBGrammar.g:23:7: ( 'default' )
            # XKBGrammar.g:23:9: 'default'
            self.match("default")




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

            # XKBGrammar.g:24:7: ( 'hidden' )
            # XKBGrammar.g:24:9: 'hidden'
            self.match("hidden")




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

            # XKBGrammar.g:25:7: ( 'partial' )
            # XKBGrammar.g:25:9: 'partial'
            self.match("partial")




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

            # XKBGrammar.g:26:7: ( 'alphanumeric_keys' )
            # XKBGrammar.g:26:9: 'alphanumeric_keys'
            self.match("alphanumeric_keys")




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

            # XKBGrammar.g:27:7: ( 'keypad_keys' )
            # XKBGrammar.g:27:9: 'keypad_keys'
            self.match("keypad_keys")




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

            # XKBGrammar.g:28:7: ( 'modifier_keys' )
            # XKBGrammar.g:28:9: 'modifier_keys'
            self.match("modifier_keys")




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

            # XKBGrammar.g:29:7: ( 'alternate_group' )
            # XKBGrammar.g:29:9: 'alternate_group'
            self.match("alternate_group")




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

            # XKBGrammar.g:30:7: ( 'xkb_symbols' )
            # XKBGrammar.g:30:9: 'xkb_symbols'
            self.match("xkb_symbols")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__51



    # $ANTLR start T__52
    def mT__52(self, ):

        try:
            _type = T__52
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:31:7: ( 'Shift' )
            # XKBGrammar.g:31:9: 'Shift'
            self.match("Shift")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__52



    # $ANTLR start T__53
    def mT__53(self, ):

        try:
            _type = T__53
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:32:7: ( 'Control' )
            # XKBGrammar.g:32:9: 'Control'
            self.match("Control")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__53



    # $ANTLR start T__54
    def mT__54(self, ):

        try:
            _type = T__54
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:33:7: ( 'Lock' )
            # XKBGrammar.g:33:9: 'Lock'
            self.match("Lock")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__54



    # $ANTLR start T__55
    def mT__55(self, ):

        try:
            _type = T__55
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:34:7: ( 'Mod1' )
            # XKBGrammar.g:34:9: 'Mod1'
            self.match("Mod1")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__55



    # $ANTLR start T__56
    def mT__56(self, ):

        try:
            _type = T__56
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:35:7: ( 'Mod2' )
            # XKBGrammar.g:35:9: 'Mod2'
            self.match("Mod2")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__56



    # $ANTLR start T__57
    def mT__57(self, ):

        try:
            _type = T__57
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:36:7: ( 'Mod3' )
            # XKBGrammar.g:36:9: 'Mod3'
            self.match("Mod3")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__57



    # $ANTLR start T__58
    def mT__58(self, ):

        try:
            _type = T__58
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:37:7: ( 'Mod4' )
            # XKBGrammar.g:37:9: 'Mod4'
            self.match("Mod4")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__58



    # $ANTLR start T__59
    def mT__59(self, ):

        try:
            _type = T__59
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:38:7: ( 'Mod5' )
            # XKBGrammar.g:38:9: 'Mod5'
            self.match("Mod5")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__59



    # $ANTLR start NAME
    def mNAME(self, ):

        try:
            _type = NAME
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:141:2: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' | '+' | '-' )* )
            # XKBGrammar.g:141:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' | '+' | '-' )*
            # XKBGrammar.g:141:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' | '+' | '-' )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((40 <= LA1_0 <= 41) or LA1_0 == 43 or LA1_0 == 45 or (48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 90) or LA1_0 == 95 or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # XKBGrammar.g:
                    if (40 <= self.input.LA(1) <= 41) or self.input.LA(1) == 43 or self.input.LA(1) == 45 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume();
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop1






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

            # XKBGrammar.g:145:2: ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )
            # XKBGrammar.g:146:2: ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
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

            # XKBGrammar.g:151:6: ( '/*' ( . )* '*/' )
            # XKBGrammar.g:152:2: '/*' ( . )* '*/'
            self.match("/*")
            # XKBGrammar.g:152:7: ( . )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 42) :
                    LA2_1 = self.input.LA(2)

                    if (LA2_1 == 47) :
                        alt2 = 2
                    elif ((0 <= LA2_1 <= 46) or (48 <= LA2_1 <= 65534)) :
                        alt2 = 1


                elif ((0 <= LA2_0 <= 41) or (43 <= LA2_0 <= 65534)) :
                    alt2 = 1


                if alt2 == 1:
                    # XKBGrammar.g:152:7: .
                    self.matchAny()



                else:
                    break #loop2


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

            # XKBGrammar.g:156:6: ( ( '//' | '#' ) (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # XKBGrammar.g:157:2: ( '//' | '#' ) (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            # XKBGrammar.g:157:2: ( '//' | '#' )
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 47) :
                alt3 = 1
            elif (LA3_0 == 35) :
                alt3 = 2
            else:
                nvae = NoViableAltException("", 3, 0, self.input)

                raise nvae

            if alt3 == 1:
                # XKBGrammar.g:157:3: '//'
                self.match("//")



            elif alt3 == 2:
                # XKBGrammar.g:157:10: '#'
                self.match(35)




            # XKBGrammar.g:157:16: (~ ( '\\n' | '\\r' ) )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((0 <= LA4_0 <= 9) or (11 <= LA4_0 <= 12) or (14 <= LA4_0 <= 65534)) :
                    alt4 = 1


                if alt4 == 1:
                    # XKBGrammar.g:157:16: ~ ( '\\n' | '\\r' )
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65534):
                        self.input.consume();
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop4


            # XKBGrammar.g:157:32: ( '\\r' )?
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 13) :
                alt5 = 1
            if alt5 == 1:
                # XKBGrammar.g:157:32: '\\r'
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

            # XKBGrammar.g:165:6: ( '\"' ( options {greedy=false; } : ~ ( '\"' ) )* '\"' )
            # XKBGrammar.g:165:10: '\"' ( options {greedy=false; } : ~ ( '\"' ) )* '\"'
            self.match(34)
            # XKBGrammar.g:165:14: ( options {greedy=false; } : ~ ( '\"' ) )*
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((0 <= LA6_0 <= 33) or (35 <= LA6_0 <= 65534)) :
                    alt6 = 1
                elif (LA6_0 == 34) :
                    alt6 = 2


                if alt6 == 1:
                    # XKBGrammar.g:165:39: ~ ( '\"' )
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 65534):
                        self.input.consume();
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop6


            self.match(34)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end DQSTRING



    def mTokens(self):
        # XKBGrammar.g:1:8: ( T__28 | T__29 | T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | T__36 | T__37 | T__38 | T__39 | T__40 | T__41 | T__42 | T__43 | T__44 | T__45 | T__46 | T__47 | T__48 | T__49 | T__50 | T__51 | T__52 | T__53 | T__54 | T__55 | T__56 | T__57 | T__58 | T__59 | NAME | WS | COMMENT | LINE_COMMENT | DQSTRING )
        alt7 = 37
        alt7 = self.dfa7.predict(self.input)
        if alt7 == 1:
            # XKBGrammar.g:1:10: T__28
            self.mT__28()



        elif alt7 == 2:
            # XKBGrammar.g:1:16: T__29
            self.mT__29()



        elif alt7 == 3:
            # XKBGrammar.g:1:22: T__30
            self.mT__30()



        elif alt7 == 4:
            # XKBGrammar.g:1:28: T__31
            self.mT__31()



        elif alt7 == 5:
            # XKBGrammar.g:1:34: T__32
            self.mT__32()



        elif alt7 == 6:
            # XKBGrammar.g:1:40: T__33
            self.mT__33()



        elif alt7 == 7:
            # XKBGrammar.g:1:46: T__34
            self.mT__34()



        elif alt7 == 8:
            # XKBGrammar.g:1:52: T__35
            self.mT__35()



        elif alt7 == 9:
            # XKBGrammar.g:1:58: T__36
            self.mT__36()



        elif alt7 == 10:
            # XKBGrammar.g:1:64: T__37
            self.mT__37()



        elif alt7 == 11:
            # XKBGrammar.g:1:70: T__38
            self.mT__38()



        elif alt7 == 12:
            # XKBGrammar.g:1:76: T__39
            self.mT__39()



        elif alt7 == 13:
            # XKBGrammar.g:1:82: T__40
            self.mT__40()



        elif alt7 == 14:
            # XKBGrammar.g:1:88: T__41
            self.mT__41()



        elif alt7 == 15:
            # XKBGrammar.g:1:94: T__42
            self.mT__42()



        elif alt7 == 16:
            # XKBGrammar.g:1:100: T__43
            self.mT__43()



        elif alt7 == 17:
            # XKBGrammar.g:1:106: T__44
            self.mT__44()



        elif alt7 == 18:
            # XKBGrammar.g:1:112: T__45
            self.mT__45()



        elif alt7 == 19:
            # XKBGrammar.g:1:118: T__46
            self.mT__46()



        elif alt7 == 20:
            # XKBGrammar.g:1:124: T__47
            self.mT__47()



        elif alt7 == 21:
            # XKBGrammar.g:1:130: T__48
            self.mT__48()



        elif alt7 == 22:
            # XKBGrammar.g:1:136: T__49
            self.mT__49()



        elif alt7 == 23:
            # XKBGrammar.g:1:142: T__50
            self.mT__50()



        elif alt7 == 24:
            # XKBGrammar.g:1:148: T__51
            self.mT__51()



        elif alt7 == 25:
            # XKBGrammar.g:1:154: T__52
            self.mT__52()



        elif alt7 == 26:
            # XKBGrammar.g:1:160: T__53
            self.mT__53()



        elif alt7 == 27:
            # XKBGrammar.g:1:166: T__54
            self.mT__54()



        elif alt7 == 28:
            # XKBGrammar.g:1:172: T__55
            self.mT__55()



        elif alt7 == 29:
            # XKBGrammar.g:1:178: T__56
            self.mT__56()



        elif alt7 == 30:
            # XKBGrammar.g:1:184: T__57
            self.mT__57()



        elif alt7 == 31:
            # XKBGrammar.g:1:190: T__58
            self.mT__58()



        elif alt7 == 32:
            # XKBGrammar.g:1:196: T__59
            self.mT__59()



        elif alt7 == 33:
            # XKBGrammar.g:1:202: NAME
            self.mNAME()



        elif alt7 == 34:
            # XKBGrammar.g:1:207: WS
            self.mWS()



        elif alt7 == 35:
            # XKBGrammar.g:1:210: COMMENT
            self.mCOMMENT()



        elif alt7 == 36:
            # XKBGrammar.g:1:218: LINE_COMMENT
            self.mLINE_COMMENT()



        elif alt7 == 37:
            # XKBGrammar.g:1:231: DQSTRING
            self.mDQSTRING()








    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\1\31\3\uffff\2\31\3\uffff\3\31\3\uffff\12\31\5\uffff\17\31\1\uffff"
        u"\2\31\1\102\16\31\1\125\1\uffff\1\31\1\uffff\2\31\1\131\10\31\1"
        u"\142\1\143\1\144\1\145\1\146\1\147\1\31\1\uffff\3\31\1\uffff\6"
        u"\31\1\162\1\31\6\uffff\5\31\1\171\4\31\1\uffff\1\31\1\177\3\31"
        u"\1\u0083\1\uffff\1\u0084\3\31\1\u0088\1\uffff\1\31\1\u008a\1\31"
        u"\2\uffff\3\31\1\uffff\1\31\1\uffff\12\31\1\u009b\4\31\1\u00a0\1"
        u"\uffff\1\u00a1\3\31\2\uffff\1\u00a5\2\31\1\uffff\3\31\1\u00ab\1"
        u"\31\1\uffff\1\u00ad\1\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\u00ae\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\1\11\3\uffff\1\156\1\141\3\uffff\1\145\1\166\1\157\3\uffff\1\171"
        u"\1\145\1\151\1\141\1\154\1\153\1\150\3\157\2\uffff\1\52\2\uffff"
        u"\1\143\1\155\1\171\1\145\1\144\1\160\1\146\1\144\1\162\1\160\1"
        u"\142\1\151\1\156\1\143\1\144\1\uffff\1\154\1\145\1\50\1\162\1\151"
        u"\1\145\1\141\1\144\1\164\1\150\1\145\1\137\1\146\1\164\1\153\1"
        u"\61\1\165\1\50\1\uffff\1\141\1\uffff\1\162\1\146\1\50\1\165\1\145"
        u"\1\151\1\141\1\162\1\163\1\164\1\162\6\50\1\144\1\uffff\1\144\2"
        u"\151\1\uffff\1\154\1\156\1\141\2\156\1\171\1\50\1\157\6\uffff\1"
        u"\145\1\137\1\144\1\145\1\164\1\50\1\154\1\165\1\141\1\155\1\uffff"
        u"\1\154\1\50\1\153\1\145\1\162\1\50\1\uffff\1\50\1\155\1\164\1\142"
        u"\1\50\1\uffff\1\145\1\50\1\137\2\uffff\2\145\1\157\1\uffff\1\171"
        u"\1\uffff\1\153\1\162\1\137\1\154\1\163\1\141\1\145\1\151\1\147"
        u"\1\163\1\50\1\160\1\171\1\143\1\162\1\50\1\uffff\1\50\1\163\1\137"
        u"\1\157\2\uffff\1\50\1\153\1\165\1\uffff\1\145\1\160\1\171\1\50"
        u"\1\163\1\uffff\1\50\1\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\1\175\3\uffff\1\156\1\141\3\uffff\1\145\1\166\1\157\3\uffff\1"
        u"\171\1\145\1\151\1\141\1\154\1\153\1\150\3\157\2\uffff\1\57\2\uffff"
        u"\1\143\1\155\1\171\1\145\1\144\1\160\1\146\1\144\1\162\1\164\1"
        u"\142\1\151\1\156\1\143\1\144\1\uffff\1\154\1\145\1\172\1\162\1"
        u"\151\1\145\1\141\1\144\1\164\1\150\1\145\1\137\1\146\1\164\1\153"
        u"\1\65\1\165\1\172\1\uffff\1\141\1\uffff\1\162\1\146\1\172\1\165"
        u"\1\145\1\151\1\141\1\162\1\163\1\164\1\162\6\172\1\144\1\uffff"
        u"\1\144\2\151\1\uffff\1\154\1\156\1\141\2\156\1\171\1\172\1\157"
        u"\6\uffff\1\145\1\137\1\144\1\145\1\164\1\172\1\154\1\165\1\141"
        u"\1\155\1\uffff\1\154\1\172\1\153\1\145\1\162\1\172\1\uffff\1\172"
        u"\1\155\1\164\1\142\1\172\1\uffff\1\145\1\172\1\137\2\uffff\2\145"
        u"\1\157\1\uffff\1\171\1\uffff\1\155\1\162\1\137\1\154\1\163\1\141"
        u"\1\145\1\151\1\147\1\163\1\172\1\160\1\171\1\143\1\162\1\172\1"
        u"\uffff\1\172\1\163\1\137\1\157\2\uffff\1\172\1\153\1\165\1\uffff"
        u"\1\145\1\160\1\171\1\172\1\163\1\uffff\1\172\1\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\2\uffff\1\6\1\7\1\10\3\uffff\1\15\1\16\1\17"
        u"\12\uffff\1\41\1\42\1\uffff\1\44\1\45\17\uffff\1\43\22\uffff\1"
        u"\11\1\uffff\1\13\22\uffff\1\5\3\uffff\1\20\10\uffff\1\33\1\34\1"
        u"\35\1\36\1\37\1\40\12\uffff\1\31\6\uffff\1\22\5\uffff\1\4\3\uffff"
        u"\1\21\1\23\3\uffff\1\32\1\uffff\1\12\20\uffff\1\25\4\uffff\1\30"
        u"\1\14\3\uffff\1\26\5\uffff\1\27\1\uffff\1\24"
        )

    DFA7_special = DFA.unpack(
        u"\u00ae\uffff"
        )

            
    DFA7_transition = [
        DFA.unpack(u"\2\32\1\uffff\2\32\22\uffff\1\32\1\uffff\1\35\1\34\10"
        u"\uffff\1\14\2\uffff\1\33\13\uffff\1\3\1\15\1\10\1\16\4\uffff\1"
        u"\26\10\uffff\1\27\1\30\5\uffff\1\25\7\uffff\1\6\1\uffff\1\7\3\uffff"
        u"\1\23\2\uffff\1\20\3\uffff\1\21\1\4\1\uffff\1\11\1\uffff\1\13\1"
        u"\5\1\12\1\22\3\uffff\1\17\3\uffff\1\24\2\uffff\1\1\1\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\36"),
        DFA.unpack(u"\1\37"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\40"),
        DFA.unpack(u"\1\41"),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u"\1\44"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u"\1\53"),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\55\4\uffff\1\34"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u"\1\57"),
        DFA.unpack(u"\1\60"),
        DFA.unpack(u"\1\61"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\67\3\uffff\1\70"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u"\1\75"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\76"),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\1\100\1\uffff\12\31"
        u"\7\uffff\32\31\4\uffff\1\31\1\uffff\17\31\1\101\12\31"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u"\1\113"),
        DFA.unpack(u"\1\114"),
        DFA.unpack(u"\1\115"),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u"\1\117\1\120\1\121\1\122\1\123"),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\126"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\127"),
        DFA.unpack(u"\1\130"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\132"),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\1\134"),
        DFA.unpack(u"\1\135"),
        DFA.unpack(u"\1\136"),
        DFA.unpack(u"\1\137"),
        DFA.unpack(u"\1\140"),
        DFA.unpack(u"\1\141"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\150"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\151"),
        DFA.unpack(u"\1\152"),
        DFA.unpack(u"\1\153"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\154"),
        DFA.unpack(u"\1\155"),
        DFA.unpack(u"\1\156"),
        DFA.unpack(u"\1\157"),
        DFA.unpack(u"\1\160"),
        DFA.unpack(u"\1\161"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\163"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\164"),
        DFA.unpack(u"\1\165"),
        DFA.unpack(u"\1\166"),
        DFA.unpack(u"\1\167"),
        DFA.unpack(u"\1\170"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\172"),
        DFA.unpack(u"\1\173"),
        DFA.unpack(u"\1\174"),
        DFA.unpack(u"\1\175"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\u0080"),
        DFA.unpack(u"\1\u0081"),
        DFA.unpack(u"\1\u0082"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\u0085"),
        DFA.unpack(u"\1\u0086"),
        DFA.unpack(u"\1\u0087"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0089"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\u008b"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008c"),
        DFA.unpack(u"\1\u008d"),
        DFA.unpack(u"\1\u008e"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008f"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0091\1\uffff\1\u0090"),
        DFA.unpack(u"\1\u0092"),
        DFA.unpack(u"\1\u0093"),
        DFA.unpack(u"\1\u0094"),
        DFA.unpack(u"\1\u0095"),
        DFA.unpack(u"\1\u0096"),
        DFA.unpack(u"\1\u0097"),
        DFA.unpack(u"\1\u0098"),
        DFA.unpack(u"\1\u0099"),
        DFA.unpack(u"\1\u009a"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\u009c"),
        DFA.unpack(u"\1\u009d"),
        DFA.unpack(u"\1\u009e"),
        DFA.unpack(u"\1\u009f"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\u00a2"),
        DFA.unpack(u"\1\u00a3"),
        DFA.unpack(u"\1\u00a4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\u00a6"),
        DFA.unpack(u"\1\u00a7"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a8"),
        DFA.unpack(u"\1\u00a9"),
        DFA.unpack(u"\1\u00aa"),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"\1\u00ac"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\31\1\uffff\1\31\1\uffff\1\31\2\uffff\12\31\7\uffff"
        u"\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #7

    DFA7 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(XKBGrammarLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)

if __name__ == '__main__':
    main(sys.argv)
