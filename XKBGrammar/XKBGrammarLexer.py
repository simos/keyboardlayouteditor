# $ANTLR 3.1b1 XKBGrammar.g 2008-05-15 22:34:00

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__29=29
T__28=28
MAPOPTIONS=17
TOKEN_INCLUDE=11
TOKEN_XKB_SYMBOLS=10
EOF=-1
MAPTYPE=15
NAME=24
TOKEN_PARTIAL=6
MAPMATERIAL=18
KEYSYMS=21
COMMENT=26
DQSTRING=23
TOKEN_DEFAULT=4
T__42=42
TOKEN_ALTERNATE_GROUP=9
T__43=43
T__40=40
T__41=41
T__46=46
T__44=44
T__45=45
SECTION=19
LINE_COMMENT=27
KEYCODE=20
TOKEN_NAME=13
VALUE=22
T__30=30
T__31=31
T__32=32
WS=25
T__33=33
T__34=34
T__35=35
TOKEN_HIDDEN=5
TOKEN_ALPHANUMERIC_KEYS=7
T__36=36
T__37=37
T__38=38
T__39=39
TOKEN_MODIFIER_KEYS=8
MAPNAME=16
TOKEN_KEY=14
TOKEN_KEY_TYPE=12


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

            # XKBGrammar.g:16:7: ( 'key' )
            # XKBGrammar.g:16:9: 'key'
            self.match("key")




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

            # XKBGrammar.g:17:7: ( '<' )
            # XKBGrammar.g:17:9: '<'
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

            # XKBGrammar.g:18:7: ( '>' )
            # XKBGrammar.g:18:9: '>'
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

            # XKBGrammar.g:20:7: ( 'default' )
            # XKBGrammar.g:20:9: 'default'
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

            # XKBGrammar.g:21:7: ( 'hidden' )
            # XKBGrammar.g:21:9: 'hidden'
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

            # XKBGrammar.g:22:7: ( 'partial' )
            # XKBGrammar.g:22:9: 'partial'
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

            # XKBGrammar.g:23:7: ( 'alphanumeric_keys' )
            # XKBGrammar.g:23:9: 'alphanumeric_keys'
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

            # XKBGrammar.g:24:7: ( 'alternate_group' )
            # XKBGrammar.g:24:9: 'alternate_group'
            self.match("alternate_group")




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

            # XKBGrammar.g:25:7: ( 'xkb_symbols' )
            # XKBGrammar.g:25:9: 'xkb_symbols'
            self.match("xkb_symbols")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__46



    # $ANTLR start NAME
    def mNAME(self, ):

        try:
            _type = NAME
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:118:2: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '-' | '(' | ')' | '0' .. '9' )* )
            # XKBGrammar.g:118:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '-' | '(' | ')' | '0' .. '9' )*
            # XKBGrammar.g:118:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '-' | '(' | ')' | '0' .. '9' )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((40 <= LA1_0 <= 41) or LA1_0 == 45 or (48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 90) or LA1_0 == 95 or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # XKBGrammar.g:
                    if (40 <= self.input.LA(1) <= 41) or self.input.LA(1) == 45 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
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

            # XKBGrammar.g:122:2: ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )
            # XKBGrammar.g:123:2: ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
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

            # XKBGrammar.g:128:6: ( '/*' ( . )* '*/' )
            # XKBGrammar.g:129:2: '/*' ( . )* '*/'
            self.match("/*")
            # XKBGrammar.g:129:7: ( . )*
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
                    # XKBGrammar.g:129:7: .
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

            # XKBGrammar.g:133:6: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # XKBGrammar.g:134:2: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            self.match("//")
            # XKBGrammar.g:134:7: (~ ( '\\n' | '\\r' ) )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((0 <= LA3_0 <= 9) or (11 <= LA3_0 <= 12) or (14 <= LA3_0 <= 65534)) :
                    alt3 = 1


                if alt3 == 1:
                    # XKBGrammar.g:134:7: ~ ( '\\n' | '\\r' )
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65534):
                        self.input.consume();
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop3


            # XKBGrammar.g:134:23: ( '\\r' )?
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 13) :
                alt4 = 1
            if alt4 == 1:
                # XKBGrammar.g:134:23: '\\r'
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

            # XKBGrammar.g:142:6: ( '\"' ( options {greedy=false; } : ~ ( '\"' ) )* '\"' )
            # XKBGrammar.g:142:10: '\"' ( options {greedy=false; } : ~ ( '\"' ) )* '\"'
            self.match(34)
            # XKBGrammar.g:142:14: ( options {greedy=false; } : ~ ( '\"' ) )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((0 <= LA5_0 <= 33) or (35 <= LA5_0 <= 65534)) :
                    alt5 = 1
                elif (LA5_0 == 34) :
                    alt5 = 2


                if alt5 == 1:
                    # XKBGrammar.g:142:39: ~ ( '\"' )
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
        # XKBGrammar.g:1:8: ( T__28 | T__29 | T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | T__36 | T__37 | T__38 | T__39 | T__40 | T__41 | T__42 | T__43 | T__44 | T__45 | T__46 | NAME | WS | COMMENT | LINE_COMMENT | DQSTRING )
        alt6 = 24
        alt6 = self.dfa6.predict(self.input)
        if alt6 == 1:
            # XKBGrammar.g:1:10: T__28
            self.mT__28()



        elif alt6 == 2:
            # XKBGrammar.g:1:16: T__29
            self.mT__29()



        elif alt6 == 3:
            # XKBGrammar.g:1:22: T__30
            self.mT__30()



        elif alt6 == 4:
            # XKBGrammar.g:1:28: T__31
            self.mT__31()



        elif alt6 == 5:
            # XKBGrammar.g:1:34: T__32
            self.mT__32()



        elif alt6 == 6:
            # XKBGrammar.g:1:40: T__33
            self.mT__33()



        elif alt6 == 7:
            # XKBGrammar.g:1:46: T__34
            self.mT__34()



        elif alt6 == 8:
            # XKBGrammar.g:1:52: T__35
            self.mT__35()



        elif alt6 == 9:
            # XKBGrammar.g:1:58: T__36
            self.mT__36()



        elif alt6 == 10:
            # XKBGrammar.g:1:64: T__37
            self.mT__37()



        elif alt6 == 11:
            # XKBGrammar.g:1:70: T__38
            self.mT__38()



        elif alt6 == 12:
            # XKBGrammar.g:1:76: T__39
            self.mT__39()



        elif alt6 == 13:
            # XKBGrammar.g:1:82: T__40
            self.mT__40()



        elif alt6 == 14:
            # XKBGrammar.g:1:88: T__41
            self.mT__41()



        elif alt6 == 15:
            # XKBGrammar.g:1:94: T__42
            self.mT__42()



        elif alt6 == 16:
            # XKBGrammar.g:1:100: T__43
            self.mT__43()



        elif alt6 == 17:
            # XKBGrammar.g:1:106: T__44
            self.mT__44()



        elif alt6 == 18:
            # XKBGrammar.g:1:112: T__45
            self.mT__45()



        elif alt6 == 19:
            # XKBGrammar.g:1:118: T__46
            self.mT__46()



        elif alt6 == 20:
            # XKBGrammar.g:1:124: NAME
            self.mNAME()



        elif alt6 == 21:
            # XKBGrammar.g:1:129: WS
            self.mWS()



        elif alt6 == 22:
            # XKBGrammar.g:1:132: COMMENT
            self.mCOMMENT()



        elif alt6 == 23:
            # XKBGrammar.g:1:140: LINE_COMMENT
            self.mLINE_COMMENT()



        elif alt6 == 24:
            # XKBGrammar.g:1:153: DQSTRING
            self.mDQSTRING()








    # lookup tables for DFA #6

    DFA6_eot = DFA.unpack(
        u"\1\22\3\uffff\2\22\3\uffff\1\22\3\uffff\5\22\4\uffff\10\22\2\uffff"
        u"\2\22\1\54\7\22\1\64\2\uffff\7\22\1\uffff\10\22\1\104\4\22\1\111"
        u"\1\112\1\uffff\1\113\3\22\3\uffff\13\22\1\132\2\22\1\uffff\5\22"
        u"\1\142\1\22\1\uffff\1\144\1\uffff"
        )

    DFA6_eof = DFA.unpack(
        u"\145\uffff"
        )

    DFA6_min = DFA.unpack(
        u"\1\11\3\uffff\1\156\1\141\3\uffff\1\145\3\uffff\1\145\1\151\1\141"
        u"\1\154\1\153\2\uffff\1\52\1\uffff\1\143\1\155\1\171\1\146\1\144"
        u"\1\162\1\160\1\142\2\uffff\1\154\1\145\1\50\1\141\1\144\1\164\1"
        u"\150\1\145\1\137\1\165\1\50\2\uffff\1\165\1\145\1\151\1\141\1\162"
        u"\1\163\1\144\1\uffff\1\154\1\156\1\141\2\156\1\171\1\145\1\164"
        u"\1\50\1\154\1\165\1\141\1\155\2\50\1\uffff\1\50\1\155\1\164\1\142"
        u"\3\uffff\2\145\1\157\1\162\1\137\1\154\1\151\1\147\1\163\1\143"
        u"\1\162\1\50\1\137\1\157\1\uffff\1\153\1\165\1\145\1\160\1\171\1"
        u"\50\1\163\1\uffff\1\50\1\uffff"
        )

    DFA6_max = DFA.unpack(
        u"\1\175\3\uffff\1\156\1\141\3\uffff\1\145\3\uffff\1\145\1\151\1"
        u"\141\1\154\1\153\2\uffff\1\57\1\uffff\1\143\1\155\1\171\1\146\1"
        u"\144\1\162\1\164\1\142\2\uffff\1\154\1\145\1\172\1\141\1\144\1"
        u"\164\1\150\1\145\1\137\1\165\1\172\2\uffff\1\165\1\145\1\151\1"
        u"\141\1\162\1\163\1\144\1\uffff\1\154\1\156\1\141\2\156\1\171\1"
        u"\145\1\164\1\172\1\154\1\165\1\141\1\155\2\172\1\uffff\1\172\1"
        u"\155\1\164\1\142\3\uffff\2\145\1\157\1\162\1\137\1\154\1\151\1"
        u"\147\1\163\1\143\1\162\1\172\1\137\1\157\1\uffff\1\153\1\165\1"
        u"\145\1\160\1\171\1\172\1\163\1\uffff\1\172\1\uffff"
        )

    DFA6_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\2\uffff\1\6\1\7\1\10\1\uffff\1\13\1\14\1\15"
        u"\5\uffff\1\24\1\25\1\uffff\1\30\10\uffff\1\26\1\27\13\uffff\1\11"
        u"\1\12\7\uffff\1\5\17\uffff\1\17\4\uffff\1\4\1\16\1\20\16\uffff"
        u"\1\23\7\uffff\1\22\1\uffff\1\21"
        )

    DFA6_special = DFA.unpack(
        u"\145\uffff"
        )

            
    DFA6_transition = [
        DFA.unpack(u"\2\23\1\uffff\2\23\22\uffff\1\23\1\uffff\1\25\11\uffff"
        u"\1\14\2\uffff\1\24\13\uffff\1\3\1\12\1\10\1\13\34\uffff\1\6\1\uffff"
        u"\1\7\3\uffff\1\20\2\uffff\1\15\3\uffff\1\16\1\4\1\uffff\1\11\2"
        u"\uffff\1\5\1\uffff\1\17\7\uffff\1\21\2\uffff\1\1\1\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\26"),
        DFA.unpack(u"\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\30"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u"\1\32"),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u"\1\34"),
        DFA.unpack(u"\1\35"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\36\4\uffff\1\37"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\40"),
        DFA.unpack(u"\1\41"),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u"\1\44"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\46\3\uffff\1\47"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u"\2\22\3\uffff\1\22\1\53\1\uffff\12\22\7\uffff\32\22"
        u"\4\uffff\1\22\1\uffff\32\22"),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u"\1\57"),
        DFA.unpack(u"\1\60"),
        DFA.unpack(u"\1\61"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u"\2\22\3\uffff\1\22\2\uffff\12\22\7\uffff\32\22\4\uffff"
        u"\1\22\1\uffff\32\22"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u"\1\75"),
        DFA.unpack(u"\1\76"),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u"\1\100"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\102"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u"\2\22\3\uffff\1\22\2\uffff\12\22\7\uffff\32\22\4\uffff"
        u"\1\22\1\uffff\32\22"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\2\22\3\uffff\1\22\2\uffff\12\22\7\uffff\32\22\4\uffff"
        u"\1\22\1\uffff\32\22"),
        DFA.unpack(u"\2\22\3\uffff\1\22\2\uffff\12\22\7\uffff\32\22\4\uffff"
        u"\1\22\1\uffff\32\22"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\22\3\uffff\1\22\2\uffff\12\22\7\uffff\32\22\4\uffff"
        u"\1\22\1\uffff\32\22"),
        DFA.unpack(u"\1\114"),
        DFA.unpack(u"\1\115"),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
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
        DFA.unpack(u"\2\22\3\uffff\1\22\2\uffff\12\22\7\uffff\32\22\4\uffff"
        u"\1\22\1\uffff\32\22"),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\1\134"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\135"),
        DFA.unpack(u"\1\136"),
        DFA.unpack(u"\1\137"),
        DFA.unpack(u"\1\140"),
        DFA.unpack(u"\1\141"),
        DFA.unpack(u"\2\22\3\uffff\1\22\2\uffff\12\22\7\uffff\32\22\4\uffff"
        u"\1\22\1\uffff\32\22"),
        DFA.unpack(u"\1\143"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\22\3\uffff\1\22\2\uffff\12\22\7\uffff\32\22\4\uffff"
        u"\1\22\1\uffff\32\22"),
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
