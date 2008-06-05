# $ANTLR 3.1b1 XKBGrammar.g 2008-06-04 20:51:55

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__66=66
T__67=67
T__64=64
T__65=65
T__62=62
T__63=63
MAPOPTIONS=16
TOKEN_INCLUDE=4
TOKEN_MODIFIER_MAP=9
T__61=61
T__60=60
EOF=-1
TOKEN_TYPE=8
MAPTYPE=14
TOKEN_VIRTUAL_MODIFIERS=11
T__55=55
T__56=56
T__57=57
NAME=28
T__58=58
T__51=51
T__52=52
MAPMATERIAL=17
T__53=53
T__54=54
T__59=59
KEYSYMS=20
COMMENT=30
DQSTRING=27
T__50=50
T__42=42
T__43=43
STATE=22
T__40=40
T__41=41
T__46=46
T__47=47
T__44=44
T__45=45
LINE_COMMENT=31
KEYCODE=18
T__48=48
T__49=49
TOKEN_NAME=6
VALUE=21
LAYOUT=12
T__32=32
T__33=33
WS=29
T__34=34
T__35=35
T__36=36
T__37=37
T__38=38
OVERRIDE=24
T__39=39
KEYSYMGROUP=23
TOKEN_SYMBOL=10
TOKEN_KEY=7
MAPNAME=15
SYMBOLS=13
VIRTUALMODS=25
KEYELEMENTS=26
TOKEN_KEY_TYPE=5
KEYCODEX=19


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






    # $ANTLR start T__32
    def mT__32(self, ):

        try:
            _type = T__32
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:7:7: ( '{' )
            # XKBGrammar.g:7:9: '{'
            self.match(123)




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

            # XKBGrammar.g:8:7: ( '}' )
            # XKBGrammar.g:8:9: '}'
            self.match(125)




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

            # XKBGrammar.g:9:7: ( ';' )
            # XKBGrammar.g:9:9: ';'
            self.match(59)




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

            # XKBGrammar.g:10:7: ( 'include' )
            # XKBGrammar.g:10:9: 'include'
            self.match("include")




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

            # XKBGrammar.g:11:7: ( 'name' )
            # XKBGrammar.g:11:9: 'name'
            self.match("name")




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

            # XKBGrammar.g:12:7: ( '[' )
            # XKBGrammar.g:12:9: '['
            self.match(91)




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

            # XKBGrammar.g:13:7: ( ']' )
            # XKBGrammar.g:13:9: ']'
            self.match(93)




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

            # XKBGrammar.g:14:7: ( '=' )
            # XKBGrammar.g:14:9: '='
            self.match(61)




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

            # XKBGrammar.g:15:7: ( 'key.type' )
            # XKBGrammar.g:15:9: 'key.type'
            self.match("key.type")




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

            # XKBGrammar.g:16:7: ( 'override' )
            # XKBGrammar.g:16:9: 'override'
            self.match("override")




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

            # XKBGrammar.g:17:7: ( 'key' )
            # XKBGrammar.g:17:9: 'key'
            self.match("key")




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

            # XKBGrammar.g:18:7: ( ',' )
            # XKBGrammar.g:18:9: ','
            self.match(44)




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

            # XKBGrammar.g:19:7: ( 'modifier_map' )
            # XKBGrammar.g:19:9: 'modifier_map'
            self.match("modifier_map")




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

            # XKBGrammar.g:20:7: ( 'virtual_modifiers' )
            # XKBGrammar.g:20:9: 'virtual_modifiers'
            self.match("virtual_modifiers")




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

            # XKBGrammar.g:21:7: ( '<' )
            # XKBGrammar.g:21:9: '<'
            self.match(60)




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

            # XKBGrammar.g:22:7: ( '>' )
            # XKBGrammar.g:22:9: '>'
            self.match(62)




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

            # XKBGrammar.g:23:7: ( 'type' )
            # XKBGrammar.g:23:9: 'type'
            self.match("type")




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

            # XKBGrammar.g:24:7: ( 'symbols' )
            # XKBGrammar.g:24:9: 'symbols'
            self.match("symbols")




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

            # XKBGrammar.g:25:7: ( 'virtualMods' )
            # XKBGrammar.g:25:9: 'virtualMods'
            self.match("virtualMods")




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

            # XKBGrammar.g:26:7: ( 'default' )
            # XKBGrammar.g:26:9: 'default'
            self.match("default")




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

            # XKBGrammar.g:27:7: ( 'hidden' )
            # XKBGrammar.g:27:9: 'hidden'
            self.match("hidden")




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

            # XKBGrammar.g:28:7: ( 'partial' )
            # XKBGrammar.g:28:9: 'partial'
            self.match("partial")




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

            # XKBGrammar.g:29:7: ( 'alphanumeric_keys' )
            # XKBGrammar.g:29:9: 'alphanumeric_keys'
            self.match("alphanumeric_keys")




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

            # XKBGrammar.g:30:7: ( 'keypad_keys' )
            # XKBGrammar.g:30:9: 'keypad_keys'
            self.match("keypad_keys")




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

            # XKBGrammar.g:31:7: ( 'function_keys' )
            # XKBGrammar.g:31:9: 'function_keys'
            self.match("function_keys")




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

            # XKBGrammar.g:32:7: ( 'modifier_keys' )
            # XKBGrammar.g:32:9: 'modifier_keys'
            self.match("modifier_keys")




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

            # XKBGrammar.g:33:7: ( 'alternate_group' )
            # XKBGrammar.g:33:9: 'alternate_group'
            self.match("alternate_group")




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

            # XKBGrammar.g:34:7: ( 'xkb_symbols' )
            # XKBGrammar.g:34:9: 'xkb_symbols'
            self.match("xkb_symbols")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__59



    # $ANTLR start T__60
    def mT__60(self, ):

        try:
            _type = T__60
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:35:7: ( 'Shift' )
            # XKBGrammar.g:35:9: 'Shift'
            self.match("Shift")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__60



    # $ANTLR start T__61
    def mT__61(self, ):

        try:
            _type = T__61
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:36:7: ( 'Control' )
            # XKBGrammar.g:36:9: 'Control'
            self.match("Control")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__61



    # $ANTLR start T__62
    def mT__62(self, ):

        try:
            _type = T__62
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:37:7: ( 'Lock' )
            # XKBGrammar.g:37:9: 'Lock'
            self.match("Lock")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__62



    # $ANTLR start T__63
    def mT__63(self, ):

        try:
            _type = T__63
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:38:7: ( 'Mod1' )
            # XKBGrammar.g:38:9: 'Mod1'
            self.match("Mod1")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__63



    # $ANTLR start T__64
    def mT__64(self, ):

        try:
            _type = T__64
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:39:7: ( 'Mod2' )
            # XKBGrammar.g:39:9: 'Mod2'
            self.match("Mod2")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__64



    # $ANTLR start T__65
    def mT__65(self, ):

        try:
            _type = T__65
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:40:7: ( 'Mod3' )
            # XKBGrammar.g:40:9: 'Mod3'
            self.match("Mod3")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__65



    # $ANTLR start T__66
    def mT__66(self, ):

        try:
            _type = T__66
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:41:7: ( 'Mod4' )
            # XKBGrammar.g:41:9: 'Mod4'
            self.match("Mod4")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__66



    # $ANTLR start T__67
    def mT__67(self, ):

        try:
            _type = T__67
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:42:7: ( 'Mod5' )
            # XKBGrammar.g:42:9: 'Mod5'
            self.match("Mod5")




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end T__67



    # $ANTLR start NAME
    def mNAME(self, ):

        try:
            _type = NAME
            _channel = DEFAULT_CHANNEL

            # XKBGrammar.g:163:2: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' | '+' | '-' )* )
            # XKBGrammar.g:163:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' | '+' | '-' )*
            # XKBGrammar.g:163:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' | '+' | '-' )*
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

            # XKBGrammar.g:167:2: ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )
            # XKBGrammar.g:168:2: ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
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

            # XKBGrammar.g:173:6: ( '/*' ( . )* '*/' )
            # XKBGrammar.g:174:2: '/*' ( . )* '*/'
            self.match("/*")
            # XKBGrammar.g:174:7: ( . )*
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
                    # XKBGrammar.g:174:7: .
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

            # XKBGrammar.g:178:6: ( ( '//' | '#' ) (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # XKBGrammar.g:179:2: ( '//' | '#' ) (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            # XKBGrammar.g:179:2: ( '//' | '#' )
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
                # XKBGrammar.g:179:3: '//'
                self.match("//")



            elif alt3 == 2:
                # XKBGrammar.g:179:10: '#'
                self.match(35)




            # XKBGrammar.g:179:16: (~ ( '\\n' | '\\r' ) )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((0 <= LA4_0 <= 9) or (11 <= LA4_0 <= 12) or (14 <= LA4_0 <= 65534)) :
                    alt4 = 1


                if alt4 == 1:
                    # XKBGrammar.g:179:16: ~ ( '\\n' | '\\r' )
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65534):
                        self.input.consume();
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop4


            # XKBGrammar.g:179:32: ( '\\r' )?
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 13) :
                alt5 = 1
            if alt5 == 1:
                # XKBGrammar.g:179:32: '\\r'
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

            # XKBGrammar.g:187:6: ( '\"' ( options {greedy=false; } : ~ ( '\"' ) )* '\"' )
            # XKBGrammar.g:187:10: '\"' ( options {greedy=false; } : ~ ( '\"' ) )* '\"'
            self.match(34)
            # XKBGrammar.g:187:14: ( options {greedy=false; } : ~ ( '\"' ) )*
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((0 <= LA6_0 <= 33) or (35 <= LA6_0 <= 65534)) :
                    alt6 = 1
                elif (LA6_0 == 34) :
                    alt6 = 2


                if alt6 == 1:
                    # XKBGrammar.g:187:39: ~ ( '\"' )
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
        # XKBGrammar.g:1:8: ( T__32 | T__33 | T__34 | T__35 | T__36 | T__37 | T__38 | T__39 | T__40 | T__41 | T__42 | T__43 | T__44 | T__45 | T__46 | T__47 | T__48 | T__49 | T__50 | T__51 | T__52 | T__53 | T__54 | T__55 | T__56 | T__57 | T__58 | T__59 | T__60 | T__61 | T__62 | T__63 | T__64 | T__65 | T__66 | T__67 | NAME | WS | COMMENT | LINE_COMMENT | DQSTRING )
        alt7 = 41
        alt7 = self.dfa7.predict(self.input)
        if alt7 == 1:
            # XKBGrammar.g:1:10: T__32
            self.mT__32()



        elif alt7 == 2:
            # XKBGrammar.g:1:16: T__33
            self.mT__33()



        elif alt7 == 3:
            # XKBGrammar.g:1:22: T__34
            self.mT__34()



        elif alt7 == 4:
            # XKBGrammar.g:1:28: T__35
            self.mT__35()



        elif alt7 == 5:
            # XKBGrammar.g:1:34: T__36
            self.mT__36()



        elif alt7 == 6:
            # XKBGrammar.g:1:40: T__37
            self.mT__37()



        elif alt7 == 7:
            # XKBGrammar.g:1:46: T__38
            self.mT__38()



        elif alt7 == 8:
            # XKBGrammar.g:1:52: T__39
            self.mT__39()



        elif alt7 == 9:
            # XKBGrammar.g:1:58: T__40
            self.mT__40()



        elif alt7 == 10:
            # XKBGrammar.g:1:64: T__41
            self.mT__41()



        elif alt7 == 11:
            # XKBGrammar.g:1:70: T__42
            self.mT__42()



        elif alt7 == 12:
            # XKBGrammar.g:1:76: T__43
            self.mT__43()



        elif alt7 == 13:
            # XKBGrammar.g:1:82: T__44
            self.mT__44()



        elif alt7 == 14:
            # XKBGrammar.g:1:88: T__45
            self.mT__45()



        elif alt7 == 15:
            # XKBGrammar.g:1:94: T__46
            self.mT__46()



        elif alt7 == 16:
            # XKBGrammar.g:1:100: T__47
            self.mT__47()



        elif alt7 == 17:
            # XKBGrammar.g:1:106: T__48
            self.mT__48()



        elif alt7 == 18:
            # XKBGrammar.g:1:112: T__49
            self.mT__49()



        elif alt7 == 19:
            # XKBGrammar.g:1:118: T__50
            self.mT__50()



        elif alt7 == 20:
            # XKBGrammar.g:1:124: T__51
            self.mT__51()



        elif alt7 == 21:
            # XKBGrammar.g:1:130: T__52
            self.mT__52()



        elif alt7 == 22:
            # XKBGrammar.g:1:136: T__53
            self.mT__53()



        elif alt7 == 23:
            # XKBGrammar.g:1:142: T__54
            self.mT__54()



        elif alt7 == 24:
            # XKBGrammar.g:1:148: T__55
            self.mT__55()



        elif alt7 == 25:
            # XKBGrammar.g:1:154: T__56
            self.mT__56()



        elif alt7 == 26:
            # XKBGrammar.g:1:160: T__57
            self.mT__57()



        elif alt7 == 27:
            # XKBGrammar.g:1:166: T__58
            self.mT__58()



        elif alt7 == 28:
            # XKBGrammar.g:1:172: T__59
            self.mT__59()



        elif alt7 == 29:
            # XKBGrammar.g:1:178: T__60
            self.mT__60()



        elif alt7 == 30:
            # XKBGrammar.g:1:184: T__61
            self.mT__61()



        elif alt7 == 31:
            # XKBGrammar.g:1:190: T__62
            self.mT__62()



        elif alt7 == 32:
            # XKBGrammar.g:1:196: T__63
            self.mT__63()



        elif alt7 == 33:
            # XKBGrammar.g:1:202: T__64
            self.mT__64()



        elif alt7 == 34:
            # XKBGrammar.g:1:208: T__65
            self.mT__65()



        elif alt7 == 35:
            # XKBGrammar.g:1:214: T__66
            self.mT__66()



        elif alt7 == 36:
            # XKBGrammar.g:1:220: T__67
            self.mT__67()



        elif alt7 == 37:
            # XKBGrammar.g:1:226: NAME
            self.mNAME()



        elif alt7 == 38:
            # XKBGrammar.g:1:231: WS
            self.mWS()



        elif alt7 == 39:
            # XKBGrammar.g:1:234: COMMENT
            self.mCOMMENT()



        elif alt7 == 40:
            # XKBGrammar.g:1:242: LINE_COMMENT
            self.mLINE_COMMENT()



        elif alt7 == 41:
            # XKBGrammar.g:1:255: DQSTRING
            self.mDQSTRING()








    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\1\34\3\uffff\2\34\3\uffff\2\34\1\uffff\2\34\2\uffff\14\34\5\uffff"
        u"\22\34\1\uffff\2\34\1\113\21\34\1\141\1\uffff\1\34\1\uffff\3\34"
        u"\1\146\12\34\1\161\1\162\1\163\1\164\1\165\1\166\1\34\1\uffff\4"
        u"\34\1\uffff\10\34\1\u0084\1\34\6\uffff\7\34\1\u008d\5\34\1\uffff"
        u"\1\34\1\u0094\4\34\1\u009a\1\u009b\1\uffff\1\u009c\4\34\1\u00a1"
        u"\1\uffff\1\34\1\u00a3\3\34\3\uffff\4\34\1\uffff\1\34\1\uffff\20"
        u"\34\1\u00bd\3\34\1\u00c1\3\34\1\u00c5\1\uffff\1\u00c6\2\34\1\uffff"
        u"\3\34\2\uffff\1\u00cc\3\34\1\u00d0\1\uffff\3\34\1\uffff\2\34\1"
        u"\u00d6\2\34\1\uffff\1\u00d9\1\u00da\2\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\u00db\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\1\11\3\uffff\1\156\1\141\3\uffff\1\145\1\166\1\uffff\1\157\1\151"
        u"\2\uffff\2\171\1\145\1\151\1\141\1\154\1\165\1\153\1\150\3\157"
        u"\2\uffff\1\52\2\uffff\1\143\1\155\1\171\1\145\1\144\1\162\1\160"
        u"\1\155\1\146\1\144\1\162\1\160\1\156\1\142\1\151\1\156\1\143\1"
        u"\144\1\uffff\1\154\1\145\1\50\1\162\1\151\1\164\1\145\1\142\1\141"
        u"\1\144\1\164\1\150\1\145\1\143\1\137\1\146\1\164\1\153\1\61\1\165"
        u"\1\50\1\uffff\1\141\1\uffff\1\162\1\146\1\165\1\50\1\157\1\165"
        u"\1\145\1\151\1\141\1\162\1\164\1\163\1\164\1\162\6\50\1\144\1\uffff"
        u"\1\144\2\151\1\141\1\uffff\2\154\1\156\1\141\2\156\1\151\1\171"
        u"\1\50\1\157\6\uffff\1\145\1\137\1\144\1\145\1\154\1\163\1\164\1"
        u"\50\1\154\1\165\1\141\1\157\1\155\1\uffff\1\154\1\50\1\153\1\145"
        u"\1\162\1\115\2\50\1\uffff\1\50\1\155\1\164\1\156\1\142\1\50\1\uffff"
        u"\1\145\1\50\1\137\1\155\1\157\3\uffff\2\145\1\137\1\157\1\uffff"
        u"\1\171\1\uffff\1\153\1\157\1\144\1\162\1\137\1\153\1\154\1\163"
        u"\1\141\1\145\1\144\1\163\1\151\1\147\1\145\1\163\1\50\1\160\1\171"
        u"\1\151\1\50\1\143\1\162\1\171\1\50\1\uffff\1\50\1\163\1\146\1\uffff"
        u"\1\137\1\157\1\163\2\uffff\1\50\1\151\1\153\1\165\1\50\1\uffff"
        u"\2\145\1\160\1\uffff\1\162\1\171\1\50\2\163\1\uffff\2\50\2\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\1\175\3\uffff\1\156\1\141\3\uffff\1\145\1\166\1\uffff\1\157\1"
        u"\151\2\uffff\2\171\1\145\1\151\1\141\1\154\1\165\1\153\1\150\3"
        u"\157\2\uffff\1\57\2\uffff\1\143\1\155\1\171\1\145\1\144\1\162\1"
        u"\160\1\155\1\146\1\144\1\162\1\164\1\156\1\142\1\151\1\156\1\143"
        u"\1\144\1\uffff\1\154\1\145\1\172\1\162\1\151\1\164\1\145\1\142"
        u"\1\141\1\144\1\164\1\150\1\145\1\143\1\137\1\146\1\164\1\153\1"
        u"\65\1\165\1\172\1\uffff\1\141\1\uffff\1\162\1\146\1\165\1\172\1"
        u"\157\1\165\1\145\1\151\1\141\1\162\1\164\1\163\1\164\1\162\6\172"
        u"\1\144\1\uffff\1\144\2\151\1\141\1\uffff\2\154\1\156\1\141\2\156"
        u"\1\151\1\171\1\172\1\157\6\uffff\1\145\1\137\1\144\1\145\1\154"
        u"\1\163\1\164\1\172\1\154\1\165\1\141\1\157\1\155\1\uffff\1\154"
        u"\1\172\1\153\1\145\1\162\1\137\2\172\1\uffff\1\172\1\155\1\164"
        u"\1\156\1\142\1\172\1\uffff\1\145\1\172\1\137\1\155\1\157\3\uffff"
        u"\2\145\1\137\1\157\1\uffff\1\171\1\uffff\1\155\1\157\1\144\1\162"
        u"\1\137\1\153\1\154\1\163\1\141\1\145\1\144\1\163\1\151\1\147\1"
        u"\145\1\163\1\172\1\160\1\171\1\151\1\172\1\143\1\162\1\171\1\172"
        u"\1\uffff\1\172\1\163\1\146\1\uffff\1\137\1\157\1\163\2\uffff\1"
        u"\172\1\151\1\153\1\165\1\172\1\uffff\2\145\1\160\1\uffff\1\162"
        u"\1\171\1\172\2\163\1\uffff\2\172\2\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\2\uffff\1\6\1\7\1\10\2\uffff\1\14\2\uffff"
        u"\1\17\1\20\14\uffff\1\45\1\46\1\uffff\1\50\1\51\22\uffff\1\47\25"
        u"\uffff\1\11\1\uffff\1\13\25\uffff\1\5\4\uffff\1\21\12\uffff\1\37"
        u"\1\40\1\41\1\42\1\43\1\44\15\uffff\1\35\10\uffff\1\25\6\uffff\1"
        u"\4\5\uffff\1\22\1\24\1\26\4\uffff\1\36\1\uffff\1\12\31\uffff\1"
        u"\30\3\uffff\1\23\3\uffff\1\34\1\15\5\uffff\1\32\3\uffff\1\31\5"
        u"\uffff\1\33\2\uffff\1\16\1\27"
        )

    DFA7_special = DFA.unpack(
        u"\u00db\uffff"
        )

            
    DFA7_transition = [
        DFA.unpack(u"\2\35\1\uffff\2\35\22\uffff\1\35\1\uffff\1\40\1\37\10"
        u"\uffff\1\13\2\uffff\1\36\13\uffff\1\3\1\16\1\10\1\17\4\uffff\1"
        u"\31\10\uffff\1\32\1\33\5\uffff\1\30\7\uffff\1\6\1\uffff\1\7\3\uffff"
        u"\1\25\2\uffff\1\22\1\uffff\1\26\1\uffff\1\23\1\4\1\uffff\1\11\1"
        u"\uffff\1\14\1\5\1\12\1\24\2\uffff\1\21\1\20\1\uffff\1\15\1\uffff"
        u"\1\27\2\uffff\1\1\1\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\41"),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u"\1\44"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u""),
        DFA.unpack(u""),
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
        DFA.unpack(u"\1\76"),
        DFA.unpack(u"\1\77\3\uffff\1\100"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\102"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\1\111\1\uffff\12\34"
        u"\7\uffff\32\34\4\uffff\1\34\1\uffff\17\34\1\112\12\34"),
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
        DFA.unpack(u"\1\132"),
        DFA.unpack(u"\1\133\1\134\1\135\1\136\1\137"),
        DFA.unpack(u"\1\140"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\142"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\143"),
        DFA.unpack(u"\1\144"),
        DFA.unpack(u"\1\145"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\147"),
        DFA.unpack(u"\1\150"),
        DFA.unpack(u"\1\151"),
        DFA.unpack(u"\1\152"),
        DFA.unpack(u"\1\153"),
        DFA.unpack(u"\1\154"),
        DFA.unpack(u"\1\155"),
        DFA.unpack(u"\1\156"),
        DFA.unpack(u"\1\157"),
        DFA.unpack(u"\1\160"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\167"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\170"),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u"\1\172"),
        DFA.unpack(u"\1\173"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\174"),
        DFA.unpack(u"\1\175"),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u"\1\177"),
        DFA.unpack(u"\1\u0080"),
        DFA.unpack(u"\1\u0081"),
        DFA.unpack(u"\1\u0082"),
        DFA.unpack(u"\1\u0083"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u0085"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0086"),
        DFA.unpack(u"\1\u0087"),
        DFA.unpack(u"\1\u0088"),
        DFA.unpack(u"\1\u0089"),
        DFA.unpack(u"\1\u008a"),
        DFA.unpack(u"\1\u008b"),
        DFA.unpack(u"\1\u008c"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u008e"),
        DFA.unpack(u"\1\u008f"),
        DFA.unpack(u"\1\u0090"),
        DFA.unpack(u"\1\u0091"),
        DFA.unpack(u"\1\u0092"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0093"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u0095"),
        DFA.unpack(u"\1\u0096"),
        DFA.unpack(u"\1\u0097"),
        DFA.unpack(u"\1\u0099\21\uffff\1\u0098"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u009d"),
        DFA.unpack(u"\1\u009e"),
        DFA.unpack(u"\1\u009f"),
        DFA.unpack(u"\1\u00a0"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a2"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00a4"),
        DFA.unpack(u"\1\u00a5"),
        DFA.unpack(u"\1\u00a6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a7"),
        DFA.unpack(u"\1\u00a8"),
        DFA.unpack(u"\1\u00a9"),
        DFA.unpack(u"\1\u00aa"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00ab"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00ad\1\uffff\1\u00ac"),
        DFA.unpack(u"\1\u00ae"),
        DFA.unpack(u"\1\u00af"),
        DFA.unpack(u"\1\u00b0"),
        DFA.unpack(u"\1\u00b1"),
        DFA.unpack(u"\1\u00b2"),
        DFA.unpack(u"\1\u00b3"),
        DFA.unpack(u"\1\u00b4"),
        DFA.unpack(u"\1\u00b5"),
        DFA.unpack(u"\1\u00b6"),
        DFA.unpack(u"\1\u00b7"),
        DFA.unpack(u"\1\u00b8"),
        DFA.unpack(u"\1\u00b9"),
        DFA.unpack(u"\1\u00ba"),
        DFA.unpack(u"\1\u00bb"),
        DFA.unpack(u"\1\u00bc"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00be"),
        DFA.unpack(u"\1\u00bf"),
        DFA.unpack(u"\1\u00c0"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00c2"),
        DFA.unpack(u"\1\u00c3"),
        DFA.unpack(u"\1\u00c4"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00c7"),
        DFA.unpack(u"\1\u00c8"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00c9"),
        DFA.unpack(u"\1\u00ca"),
        DFA.unpack(u"\1\u00cb"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00cd"),
        DFA.unpack(u"\1\u00ce"),
        DFA.unpack(u"\1\u00cf"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d1"),
        DFA.unpack(u"\1\u00d2"),
        DFA.unpack(u"\1\u00d3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d4"),
        DFA.unpack(u"\1\u00d5"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\1\u00d7"),
        DFA.unpack(u"\1\u00d8"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u"\2\34\1\uffff\1\34\1\uffff\1\34\2\uffff\12\34\7\uffff"
        u"\32\34\4\uffff\1\34\1\uffff\32\34"),
        DFA.unpack(u""),
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
