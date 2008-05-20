# $ANTLR 3.1b1 XKBGrammar.g 2008-05-20 21:54:25

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__29=29
T__28=28
T__27=27
T__26=26
MAPOPTIONS=13
TOKEN_INCLUDE=4
TOKEN_MODIFIER_MAP=9
EOF=-1
TOKEN_TYPE=8
MAPTYPE=11
T__55=55
NAME=22
T__51=51
T__52=52
T__53=53
MAPMATERIAL=14
T__54=54
KEYSYMS=18
COMMENT=24
DQSTRING=21
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
LINE_COMMENT=25
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
WS=23
T__34=34
T__35=35
T__36=36
T__37=37
T__38=38
T__39=39
MAPNAME=12
TOKEN_KEY=7
TOKEN_KEY_TYPE=5
KEYCODEX=17


class XKBGrammarLexer(Lexer):

    grammarFileName = "XKBGrammar.g"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa6 = self.DFA6(
            self, 6,
            eot = self.DFA6_eot,
            eof = self.DFA6_eof,
            min = self.DFA6_min,
            max = self.DFA6_max,
            accept = self.DFA6_accept,
            special = self.DFA6_special,
            transition = self.DFA6_transition
            )






    # $ANTLR start T__26
    def mT__26(self, ):

        try:
            _type = T__26
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:7:7: ( '{' )
            # XKBGrammar.g:7:9: '{'
            self.match(123)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__26



    # $ANTLR start T__27
    def mT__27(self, ):

        try:
            _type = T__27
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:8:7: ( '}' )
            # XKBGrammar.g:8:9: '}'
            self.match(125)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__27



    # $ANTLR start T__28
    def mT__28(self, ):

        try:
            _type = T__28
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:9:7: ( ';' )
            # XKBGrammar.g:9:9: ';'
            self.match(59)




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

            # XKBGrammar.g:10:7: ( 'include' )
            # XKBGrammar.g:10:9: 'include'
            self.match("include")




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

            # XKBGrammar.g:11:7: ( 'name' )
            # XKBGrammar.g:11:9: 'name'
            self.match("name")




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

            # XKBGrammar.g:12:7: ( '[' )
            # XKBGrammar.g:12:9: '['
            self.match(91)




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

            # XKBGrammar.g:13:7: ( ']' )
            # XKBGrammar.g:13:9: ']'
            self.match(93)




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

            # XKBGrammar.g:14:7: ( '=' )
            # XKBGrammar.g:14:9: '='
            self.match(61)




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

            # XKBGrammar.g:15:7: ( 'key.type' )
            # XKBGrammar.g:15:9: 'key.type'
            self.match("key.type")




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

            # XKBGrammar.g:16:7: ( 'key' )
            # XKBGrammar.g:16:9: 'key'
            self.match("key")




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

            # XKBGrammar.g:17:7: ( 'modifier_map' )
            # XKBGrammar.g:17:9: 'modifier_map'
            self.match("modifier_map")




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

            # XKBGrammar.g:18:7: ( ',' )
            # XKBGrammar.g:18:9: ','
            self.match(44)




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

            # XKBGrammar.g:19:7: ( '<' )
            # XKBGrammar.g:19:9: '<'
            self.match(60)




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

            # XKBGrammar.g:20:7: ( '>' )
            # XKBGrammar.g:20:9: '>'
            self.match(62)




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

            # XKBGrammar.g:21:7: ( 'type' )
            # XKBGrammar.g:21:9: 'type'
            self.match("type")




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

            # XKBGrammar.g:22:7: ( 'default' )
            # XKBGrammar.g:22:9: 'default'
            self.match("default")




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

            # XKBGrammar.g:23:7: ( 'hidden' )
            # XKBGrammar.g:23:9: 'hidden'
            self.match("hidden")




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

            # XKBGrammar.g:24:7: ( 'partial' )
            # XKBGrammar.g:24:9: 'partial'
            self.match("partial")




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

            # XKBGrammar.g:25:7: ( 'alphanumeric_keys' )
            # XKBGrammar.g:25:9: 'alphanumeric_keys'
            self.match("alphanumeric_keys")




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

            # XKBGrammar.g:26:7: ( 'modifier_keys' )
            # XKBGrammar.g:26:9: 'modifier_keys'
            self.match("modifier_keys")




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

            # XKBGrammar.g:27:7: ( 'alternate_group' )
            # XKBGrammar.g:27:9: 'alternate_group'
            self.match("alternate_group")




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

            # XKBGrammar.g:28:7: ( 'xkb_symbols' )
            # XKBGrammar.g:28:9: 'xkb_symbols'
            self.match("xkb_symbols")




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

            # XKBGrammar.g:29:7: ( 'Shift' )
            # XKBGrammar.g:29:9: 'Shift'
            self.match("Shift")




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

            # XKBGrammar.g:30:7: ( 'Control' )
            # XKBGrammar.g:30:9: 'Control'
            self.match("Control")




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

            # XKBGrammar.g:31:7: ( 'Lock' )
            # XKBGrammar.g:31:9: 'Lock'
            self.match("Lock")




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

            # XKBGrammar.g:32:7: ( 'Mod1' )
            # XKBGrammar.g:32:9: 'Mod1'
            self.match("Mod1")




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

            # XKBGrammar.g:33:7: ( 'Mod2' )
            # XKBGrammar.g:33:9: 'Mod2'
            self.match("Mod2")




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

            # XKBGrammar.g:34:7: ( 'Mod3' )
            # XKBGrammar.g:34:9: 'Mod3'
            self.match("Mod3")




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

            # XKBGrammar.g:35:7: ( 'Mod4' )
            # XKBGrammar.g:35:9: 'Mod4'
            self.match("Mod4")




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

            # XKBGrammar.g:36:7: ( 'Mod5' )
            # XKBGrammar.g:36:9: 'Mod5'
            self.match("Mod5")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__55



    # $ANTLR start NAME
    def mNAME(self, ):

        try:
            _type = NAME
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:133:2: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' | '+' | '-' )* )
            # XKBGrammar.g:133:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' | '+' | '-' )*
            # XKBGrammar.g:133:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' | '+' | '-' )*
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

            # XKBGrammar.g:137:2: ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )
            # XKBGrammar.g:138:2: ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
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

            # XKBGrammar.g:143:6: ( '/*' ( . )* '*/' )
            # XKBGrammar.g:144:2: '/*' ( . )* '*/'
            self.match("/*")
            # XKBGrammar.g:144:7: ( . )*
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
                    # XKBGrammar.g:144:7: .
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

            # XKBGrammar.g:148:6: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # XKBGrammar.g:149:2: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            self.match("//")
            # XKBGrammar.g:149:7: (~ ( '\\n' | '\\r' ) )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((0 <= LA3_0 <= 9) or (11 <= LA3_0 <= 12) or (14 <= LA3_0 <= 65534)) :
                    alt3 = 1


                if alt3 == 1:
                    # XKBGrammar.g:149:7: ~ ( '\\n' | '\\r' )
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65534):
                        self.input.consume();
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop3


            # XKBGrammar.g:149:23: ( '\\r' )?
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 13) :
                alt4 = 1
            if alt4 == 1:
                # XKBGrammar.g:149:23: '\\r'
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

            # XKBGrammar.g:157:6: ( '\"' ( options {greedy=false; } : ~ ( '\"' ) )* '\"' )
            # XKBGrammar.g:157:10: '\"' ( options {greedy=false; } : ~ ( '\"' ) )* '\"'
            self.match(34)
            # XKBGrammar.g:157:14: ( options {greedy=false; } : ~ ( '\"' ) )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((0 <= LA5_0 <= 33) or (35 <= LA5_0 <= 65534)) :
                    alt5 = 1
                elif (LA5_0 == 34) :
                    alt5 = 2


                if alt5 == 1:
                    # XKBGrammar.g:157:39: ~ ( '\"' )
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 65534):
                        self.input.consume();
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop5


            self.match(34)




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end DQSTRING



    def mTokens(self):
        # XKBGrammar.g:1:8: ( T__26 | T__27 | T__28 | T__29 | T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | T__36 | T__37 | T__38 | T__39 | T__40 | T__41 | T__42 | T__43 | T__44 | T__45 | T__46 | T__47 | T__48 | T__49 | T__50 | T__51 | T__52 | T__53 | T__54 | T__55 | NAME | WS | COMMENT | LINE_COMMENT | DQSTRING )
        alt6 = 35
        alt6 = self.dfa6.predict(self.input)
        if alt6 == 1:
            # XKBGrammar.g:1:10: T__26
            self.mT__26()



        elif alt6 == 2:
            # XKBGrammar.g:1:16: T__27
            self.mT__27()



        elif alt6 == 3:
            # XKBGrammar.g:1:22: T__28
            self.mT__28()



        elif alt6 == 4:
            # XKBGrammar.g:1:28: T__29
            self.mT__29()



        elif alt6 == 5:
            # XKBGrammar.g:1:34: T__30
            self.mT__30()



        elif alt6 == 6:
            # XKBGrammar.g:1:40: T__31
            self.mT__31()



        elif alt6 == 7:
            # XKBGrammar.g:1:46: T__32
            self.mT__32()



        elif alt6 == 8:
            # XKBGrammar.g:1:52: T__33
            self.mT__33()



        elif alt6 == 9:
            # XKBGrammar.g:1:58: T__34
            self.mT__34()



        elif alt6 == 10:
            # XKBGrammar.g:1:64: T__35
            self.mT__35()



        elif alt6 == 11:
            # XKBGrammar.g:1:70: T__36
            self.mT__36()



        elif alt6 == 12:
            # XKBGrammar.g:1:76: T__37
            self.mT__37()



        elif alt6 == 13:
            # XKBGrammar.g:1:82: T__38
            self.mT__38()



        elif alt6 == 14:
            # XKBGrammar.g:1:88: T__39
            self.mT__39()



        elif alt6 == 15:
            # XKBGrammar.g:1:94: T__40
            self.mT__40()



        elif alt6 == 16:
            # XKBGrammar.g:1:100: T__41
            self.mT__41()



        elif alt6 == 17:
            # XKBGrammar.g:1:106: T__42
            self.mT__42()



        elif alt6 == 18:
            # XKBGrammar.g:1:112: T__43
            self.mT__43()



        elif alt6 == 19:
            # XKBGrammar.g:1:118: T__44
            self.mT__44()



        elif alt6 == 20:
            # XKBGrammar.g:1:124: T__45
            self.mT__45()



        elif alt6 == 21:
            # XKBGrammar.g:1:130: T__46
            self.mT__46()



        elif alt6 == 22:
            # XKBGrammar.g:1:136: T__47
            self.mT__47()



        elif alt6 == 23:
            # XKBGrammar.g:1:142: T__48
            self.mT__48()



        elif alt6 == 24:
            # XKBGrammar.g:1:148: T__49
            self.mT__49()



        elif alt6 == 25:
            # XKBGrammar.g:1:154: T__50
            self.mT__50()



        elif alt6 == 26:
            # XKBGrammar.g:1:160: T__51
            self.mT__51()



        elif alt6 == 27:
            # XKBGrammar.g:1:166: T__52
            self.mT__52()



        elif alt6 == 28:
            # XKBGrammar.g:1:172: T__53
            self.mT__53()



        elif alt6 == 29:
            # XKBGrammar.g:1:178: T__54
            self.mT__54()



        elif alt6 == 30:
            # XKBGrammar.g:1:184: T__55
            self.mT__55()



        elif alt6 == 31:
            # XKBGrammar.g:1:190: NAME
            self.mNAME()



        elif alt6 == 32:
            # XKBGrammar.g:1:195: WS
            self.mWS()



        elif alt6 == 33:
            # XKBGrammar.g:1:198: COMMENT
            self.mCOMMENT()



        elif alt6 == 34:
            # XKBGrammar.g:1:206: LINE_COMMENT
            self.mLINE_COMMENT()



        elif alt6 == 35:
            # XKBGrammar.g:1:219: DQSTRING
            self.mDQSTRING()








    # lookup tables for DFA #6

    DFA6_eot = DFA.unpack(
        u"\1\30\3\uffff\2\30\3\uffff\2\30\3\uffff\12\30\4\uffff\16\30\2\uffff"
        u"\2\30\1\76\15\30\1\120\2\uffff\1\30\1\122\10\30\1\133\1\134\1\135"
        u"\1\136\1\137\1\140\1\30\1\uffff\1\30\1\uffff\6\30\1\151\1\30\6"
        u"\uffff\3\30\1\156\4\30\1\uffff\1\30\1\164\1\30\1\166\1\uffff\1"
        u"\167\3\30\1\173\1\uffff\1\30\2\uffff\3\30\1\uffff\15\30\1\u008e"
        u"\1\u008f\3\30\2\uffff\1\u0093\2\30\1\uffff\3\30\1\u0099\1\30\1"
        u"\uffff\1\u009b\1\uffff"
        )

    DFA6_eof = DFA.unpack(
        u"\u009c\uffff"
        )

    DFA6_min = DFA.unpack(
        u"\1\11\3\uffff\1\156\1\141\3\uffff\1\145\1\157\3\uffff\1\171\1\145"
        u"\1\151\1\141\1\154\1\153\1\150\3\157\2\uffff\1\52\1\uffff\1\143"
        u"\1\155\1\171\1\144\1\160\1\146\1\144\1\162\1\160\1\142\1\151\1"
        u"\156\1\143\1\144\2\uffff\1\154\1\145\1\50\1\151\1\145\1\141\1\144"
        u"\1\164\1\150\1\145\1\137\1\146\1\164\1\153\1\61\1\165\1\50\2\uffff"
        u"\1\146\1\50\1\165\1\145\1\151\1\141\1\162\1\163\1\164\1\162\6\50"
        u"\1\144\1\uffff\1\151\1\uffff\1\154\1\156\1\141\2\156\1\171\1\50"
        u"\1\157\6\uffff\2\145\1\164\1\50\1\154\1\165\1\141\1\155\1\uffff"
        u"\1\154\1\50\1\162\1\50\1\uffff\1\50\1\155\1\164\1\142\1\50\1\uffff"
        u"\1\137\2\uffff\2\145\1\157\1\uffff\1\153\1\162\1\137\1\154\1\141"
        u"\1\145\1\151\1\147\1\163\1\160\1\171\1\143\1\162\2\50\1\163\1\137"
        u"\1\157\2\uffff\1\50\1\153\1\165\1\uffff\1\145\1\160\1\171\1\50"
        u"\1\163\1\uffff\1\50\1\uffff"
        )

    DFA6_max = DFA.unpack(
        u"\1\175\3\uffff\1\156\1\141\3\uffff\1\145\1\157\3\uffff\1\171\1"
        u"\145\1\151\1\141\1\154\1\153\1\150\3\157\2\uffff\1\57\1\uffff\1"
        u"\143\1\155\1\171\1\144\1\160\1\146\1\144\1\162\1\164\1\142\1\151"
        u"\1\156\1\143\1\144\2\uffff\1\154\1\145\1\172\1\151\1\145\1\141"
        u"\1\144\1\164\1\150\1\145\1\137\1\146\1\164\1\153\1\65\1\165\1\172"
        u"\2\uffff\1\146\1\172\1\165\1\145\1\151\1\141\1\162\1\163\1\164"
        u"\1\162\6\172\1\144\1\uffff\1\151\1\uffff\1\154\1\156\1\141\2\156"
        u"\1\171\1\172\1\157\6\uffff\2\145\1\164\1\172\1\154\1\165\1\141"
        u"\1\155\1\uffff\1\154\1\172\1\162\1\172\1\uffff\1\172\1\155\1\164"
        u"\1\142\1\172\1\uffff\1\137\2\uffff\2\145\1\157\1\uffff\1\155\1"
        u"\162\1\137\1\154\1\141\1\145\1\151\1\147\1\163\1\160\1\171\1\143"
        u"\1\162\2\172\1\163\1\137\1\157\2\uffff\1\172\1\153\1\165\1\uffff"
        u"\1\145\1\160\1\171\1\172\1\163\1\uffff\1\172\1\uffff"
        )

    DFA6_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\2\uffff\1\6\1\7\1\10\2\uffff\1\14\1\15\1\16"
        u"\12\uffff\1\37\1\40\1\uffff\1\43\16\uffff\1\41\1\42\21\uffff\1"
        u"\11\1\12\21\uffff\1\5\1\uffff\1\17\10\uffff\1\31\1\32\1\33\1\34"
        u"\1\35\1\36\10\uffff\1\27\4\uffff\1\21\5\uffff\1\4\1\uffff\1\20"
        u"\1\22\3\uffff\1\30\22\uffff\1\26\1\13\3\uffff\1\24\5\uffff\1\25"
        u"\1\uffff\1\23"
        )

    DFA6_special = DFA.unpack(
        u"\u009c\uffff"
        )

            
    DFA6_transition = [
        DFA.unpack(u"\2\31\1\uffff\2\31\22\uffff\1\31\1\uffff\1\33\11\uffff"
        u"\1\13\2\uffff\1\32\13\uffff\1\3\1\14\1\10\1\15\4\uffff\1\25\10"
        u"\uffff\1\26\1\27\5\uffff\1\24\7\uffff\1\6\1\uffff\1\7\3\uffff\1"
        u"\22\2\uffff\1\17\3\uffff\1\20\1\4\1\uffff\1\11\1\uffff\1\12\1\5"
        u"\1\uffff\1\21\3\uffff\1\16\3\uffff\1\23\2\uffff\1\1\1\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\34"),
        DFA.unpack(u"\1\35"),
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
        DFA.unpack(u"\1\43"),
        DFA.unpack(u"\1\44"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\52\4\uffff\1\53"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u"\1\57"),
        DFA.unpack(u"\1\60"),
        DFA.unpack(u"\1\61"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u"\1\64\3\uffff\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\1\75\1\uffff\12\30\7"
        u"\uffff\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u"\1\100"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\102"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u"\1\112\1\113\1\114\1\115\1\116"),
        DFA.unpack(u"\1\117"),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\121"),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u"\1\123"),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u"\1\125"),
        DFA.unpack(u"\1\126"),
        DFA.unpack(u"\1\127"),
        DFA.unpack(u"\1\130"),
        DFA.unpack(u"\1\131"),
        DFA.unpack(u"\1\132"),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u"\1\141"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\142"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\143"),
        DFA.unpack(u"\1\144"),
        DFA.unpack(u"\1\145"),
        DFA.unpack(u"\1\146"),
        DFA.unpack(u"\1\147"),
        DFA.unpack(u"\1\150"),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u"\1\152"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\153"),
        DFA.unpack(u"\1\154"),
        DFA.unpack(u"\1\155"),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u"\1\157"),
        DFA.unpack(u"\1\160"),
        DFA.unpack(u"\1\161"),
        DFA.unpack(u"\1\162"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\163"),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u"\1\165"),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u"\1\170"),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u"\1\172"),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\174"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\175"),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u"\1\177"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0081\1\uffff\1\u0080"),
        DFA.unpack(u"\1\u0082"),
        DFA.unpack(u"\1\u0083"),
        DFA.unpack(u"\1\u0084"),
        DFA.unpack(u"\1\u0085"),
        DFA.unpack(u"\1\u0086"),
        DFA.unpack(u"\1\u0087"),
        DFA.unpack(u"\1\u0088"),
        DFA.unpack(u"\1\u0089"),
        DFA.unpack(u"\1\u008a"),
        DFA.unpack(u"\1\u008b"),
        DFA.unpack(u"\1\u008c"),
        DFA.unpack(u"\1\u008d"),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u"\1\u0090"),
        DFA.unpack(u"\1\u0091"),
        DFA.unpack(u"\1\u0092"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u"\1\u0094"),
        DFA.unpack(u"\1\u0095"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0096"),
        DFA.unpack(u"\1\u0097"),
        DFA.unpack(u"\1\u0098"),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u"\1\u009a"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\30\1\uffff\1\30\1\uffff\1\30\2\uffff\12\30\7\uffff"
        u"\32\30\4\uffff\1\30\1\uffff\32\30"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #6

    DFA6 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(XKBGrammarLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)

if __name__ == '__main__':
    main(sys.argv)
