# $ANTLR 3.0.1 XKBGrammar.g 2008-05-09 21:53:06

from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
TOKEN_ALTERNATE_GROUP=9
ATTRIBUTES=29
SECTION=35
LINE_COMMENT=41
KEYCODE=34
TOKEN_INCLUDE=11
KEY=32
KEYTYPE=33
ATTRIBUTE=30
TOKEN_NAME=13
DQUOTE=20
LCURLY=17
SEMICOLON=23
MINUS=21
TOKEN_XKB_SYMBOLS=10
Tokens=42
EOF=-1
SECTIONNAME=36
GENERIC_NAME=38
MAPTYPE=28
LBRACKET=15
TOKEN_PARTIAL=6
NAME=37
WS=39
TOKEN_HIDDEN=5
TOKEN_ALPHANUMERIC_KEYS=7
COMMA=19
LOWERTHAN=25
EQUAL=24
INCLUDE=31
RCURLY=18
TOKEN_MODIFIER_KEYS=8
PLUS=22
TOKEN_KEY=14
RBRACKET=16
DOT=27
COMMENT=40
TOKEN_DEFAULT=4
TOKEN_KEY_TYPE=12
GREATERTHAN=26

class XKBGrammarLexer(Lexer):

    grammarFileName = "XKBGrammar.g"

    def __init__(self, input=None):
        Lexer.__init__(self, input)





    # $ANTLR start TOKEN_DEFAULT
    def mTOKEN_DEFAULT(self, ):

        try:
            self.type = TOKEN_DEFAULT

            # XKBGrammar.g:7:15: ( 'default' )
            # XKBGrammar.g:7:17: 'default'
            self.match("default")






        finally:

            pass

    # $ANTLR end TOKEN_DEFAULT



    # $ANTLR start TOKEN_HIDDEN
    def mTOKEN_HIDDEN(self, ):

        try:
            self.type = TOKEN_HIDDEN

            # XKBGrammar.g:8:14: ( 'hidden' )
            # XKBGrammar.g:8:16: 'hidden'
            self.match("hidden")






        finally:

            pass

    # $ANTLR end TOKEN_HIDDEN



    # $ANTLR start TOKEN_PARTIAL
    def mTOKEN_PARTIAL(self, ):

        try:
            self.type = TOKEN_PARTIAL

            # XKBGrammar.g:9:15: ( 'partial' )
            # XKBGrammar.g:9:17: 'partial'
            self.match("partial")






        finally:

            pass

    # $ANTLR end TOKEN_PARTIAL



    # $ANTLR start TOKEN_ALPHANUMERIC_KEYS
    def mTOKEN_ALPHANUMERIC_KEYS(self, ):

        try:
            self.type = TOKEN_ALPHANUMERIC_KEYS

            # XKBGrammar.g:10:25: ( 'alphanumeric_keys' )
            # XKBGrammar.g:10:27: 'alphanumeric_keys'
            self.match("alphanumeric_keys")






        finally:

            pass

    # $ANTLR end TOKEN_ALPHANUMERIC_KEYS



    # $ANTLR start TOKEN_MODIFIER_KEYS
    def mTOKEN_MODIFIER_KEYS(self, ):

        try:
            self.type = TOKEN_MODIFIER_KEYS

            # XKBGrammar.g:11:21: ( 'modifier_keys' )
            # XKBGrammar.g:11:23: 'modifier_keys'
            self.match("modifier_keys")






        finally:

            pass

    # $ANTLR end TOKEN_MODIFIER_KEYS



    # $ANTLR start TOKEN_ALTERNATE_GROUP
    def mTOKEN_ALTERNATE_GROUP(self, ):

        try:
            self.type = TOKEN_ALTERNATE_GROUP

            # XKBGrammar.g:12:23: ( 'alternate_group' )
            # XKBGrammar.g:12:25: 'alternate_group'
            self.match("alternate_group")






        finally:

            pass

    # $ANTLR end TOKEN_ALTERNATE_GROUP



    # $ANTLR start TOKEN_XKB_SYMBOLS
    def mTOKEN_XKB_SYMBOLS(self, ):

        try:
            self.type = TOKEN_XKB_SYMBOLS

            # XKBGrammar.g:13:19: ( 'xkb_symbols' )
            # XKBGrammar.g:13:21: 'xkb_symbols'
            self.match("xkb_symbols")






        finally:

            pass

    # $ANTLR end TOKEN_XKB_SYMBOLS



    # $ANTLR start TOKEN_INCLUDE
    def mTOKEN_INCLUDE(self, ):

        try:
            self.type = TOKEN_INCLUDE

            # XKBGrammar.g:14:15: ( 'include' )
            # XKBGrammar.g:14:17: 'include'
            self.match("include")






        finally:

            pass

    # $ANTLR end TOKEN_INCLUDE



    # $ANTLR start TOKEN_KEY_TYPE
    def mTOKEN_KEY_TYPE(self, ):

        try:
            self.type = TOKEN_KEY_TYPE

            # XKBGrammar.g:15:16: ( 'key.type' )
            # XKBGrammar.g:15:18: 'key.type'
            self.match("key.type")






        finally:

            pass

    # $ANTLR end TOKEN_KEY_TYPE



    # $ANTLR start TOKEN_NAME
    def mTOKEN_NAME(self, ):

        try:
            self.type = TOKEN_NAME

            # XKBGrammar.g:16:12: ( 'name' )
            # XKBGrammar.g:16:14: 'name'
            self.match("name")






        finally:

            pass

    # $ANTLR end TOKEN_NAME



    # $ANTLR start TOKEN_KEY
    def mTOKEN_KEY(self, ):

        try:
            self.type = TOKEN_KEY

            # XKBGrammar.g:17:11: ( 'key' )
            # XKBGrammar.g:17:13: 'key'
            self.match("key")






        finally:

            pass

    # $ANTLR end TOKEN_KEY



    # $ANTLR start LBRACKET
    def mLBRACKET(self, ):

        try:
            self.type = LBRACKET

            # XKBGrammar.g:18:10: ( '[' )
            # XKBGrammar.g:18:12: '['
            self.match(u'[')





        finally:

            pass

    # $ANTLR end LBRACKET



    # $ANTLR start RBRACKET
    def mRBRACKET(self, ):

        try:
            self.type = RBRACKET

            # XKBGrammar.g:19:10: ( ']' )
            # XKBGrammar.g:19:12: ']'
            self.match(u']')





        finally:

            pass

    # $ANTLR end RBRACKET



    # $ANTLR start LCURLY
    def mLCURLY(self, ):

        try:
            self.type = LCURLY

            # XKBGrammar.g:20:8: ( '{' )
            # XKBGrammar.g:20:10: '{'
            self.match(u'{')





        finally:

            pass

    # $ANTLR end LCURLY



    # $ANTLR start RCURLY
    def mRCURLY(self, ):

        try:
            self.type = RCURLY

            # XKBGrammar.g:21:8: ( '}' )
            # XKBGrammar.g:21:10: '}'
            self.match(u'}')





        finally:

            pass

    # $ANTLR end RCURLY



    # $ANTLR start COMMA
    def mCOMMA(self, ):

        try:
            self.type = COMMA

            # XKBGrammar.g:22:7: ( ',' )
            # XKBGrammar.g:22:9: ','
            self.match(u',')





        finally:

            pass

    # $ANTLR end COMMA



    # $ANTLR start DQUOTE
    def mDQUOTE(self, ):

        try:
            self.type = DQUOTE

            # XKBGrammar.g:23:8: ( '\"' )
            # XKBGrammar.g:23:10: '\"'
            self.match(u'"')





        finally:

            pass

    # $ANTLR end DQUOTE



    # $ANTLR start MINUS
    def mMINUS(self, ):

        try:
            self.type = MINUS

            # XKBGrammar.g:24:7: ( '-' )
            # XKBGrammar.g:24:9: '-'
            self.match(u'-')





        finally:

            pass

    # $ANTLR end MINUS



    # $ANTLR start PLUS
    def mPLUS(self, ):

        try:
            self.type = PLUS

            # XKBGrammar.g:25:6: ( '+' )
            # XKBGrammar.g:25:8: '+'
            self.match(u'+')





        finally:

            pass

    # $ANTLR end PLUS



    # $ANTLR start SEMICOLON
    def mSEMICOLON(self, ):

        try:
            self.type = SEMICOLON

            # XKBGrammar.g:26:11: ( ';' )
            # XKBGrammar.g:26:13: ';'
            self.match(u';')





        finally:

            pass

    # $ANTLR end SEMICOLON



    # $ANTLR start EQUAL
    def mEQUAL(self, ):

        try:
            self.type = EQUAL

            # XKBGrammar.g:27:7: ( '=' )
            # XKBGrammar.g:27:9: '='
            self.match(u'=')





        finally:

            pass

    # $ANTLR end EQUAL



    # $ANTLR start LOWERTHAN
    def mLOWERTHAN(self, ):

        try:
            self.type = LOWERTHAN

            # XKBGrammar.g:28:11: ( '<' )
            # XKBGrammar.g:28:13: '<'
            self.match(u'<')





        finally:

            pass

    # $ANTLR end LOWERTHAN



    # $ANTLR start GREATERTHAN
    def mGREATERTHAN(self, ):

        try:
            self.type = GREATERTHAN

            # XKBGrammar.g:29:13: ( '>' )
            # XKBGrammar.g:29:15: '>'
            self.match(u'>')





        finally:

            pass

    # $ANTLR end GREATERTHAN



    # $ANTLR start DOT
    def mDOT(self, ):

        try:
            self.type = DOT

            # XKBGrammar.g:30:5: ( '.' )
            # XKBGrammar.g:30:7: '.'
            self.match(u'.')





        finally:

            pass

    # $ANTLR end DOT



    # $ANTLR start GENERIC_NAME
    def mGENERIC_NAME(self, ):

        try:
            # XKBGrammar.g:171:2: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' ) )
            # XKBGrammar.g:171:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )
            if (u'A' <= self.input.LA(1) <= u'Z') or self.input.LA(1) == u'_' or (u'a' <= self.input.LA(1) <= u'z'):
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse


            if (u'0' <= self.input.LA(1) <= u'9') or (u'A' <= self.input.LA(1) <= u'Z') or self.input.LA(1) == u'_' or (u'a' <= self.input.LA(1) <= u'z'):
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:

            pass

    # $ANTLR end GENERIC_NAME



    # $ANTLR start NAME
    def mNAME(self, ):

        try:
            self.type = NAME

            # XKBGrammar.g:175:2: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' )* )
            # XKBGrammar.g:175:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' )*
            # XKBGrammar.g:175:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((u'(' <= LA1_0 <= u')') or (u'0' <= LA1_0 <= u'9') or (u'A' <= LA1_0 <= u'Z') or LA1_0 == u'_' or (u'a' <= LA1_0 <= u'z')) :
                    alt1 = 1


                if alt1 == 1:
                    # XKBGrammar.g:
                    if (u'(' <= self.input.LA(1) <= u')') or (u'0' <= self.input.LA(1) <= u'9') or (u'A' <= self.input.LA(1) <= u'Z') or self.input.LA(1) == u'_' or (u'a' <= self.input.LA(1) <= u'z'):
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop1






        finally:

            pass

    # $ANTLR end NAME



    # $ANTLR start WS
    def mWS(self, ):

        try:
            self.type = WS

            # XKBGrammar.g:180:2: ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )
            # XKBGrammar.g:181:2: ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
            if (u'\t' <= self.input.LA(1) <= u'\n') or (u'\f' <= self.input.LA(1) <= u'\r') or self.input.LA(1) == u' ':
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse


            #action start
            self.channel=HIDDEN;
            #action end




        finally:

            pass

    # $ANTLR end WS



    # $ANTLR start COMMENT
    def mCOMMENT(self, ):

        try:
            self.type = COMMENT

            # XKBGrammar.g:186:6: ( '/*' ( . )* '*/' )
            # XKBGrammar.g:187:2: '/*' ( . )* '*/'
            self.match("/*")


            # XKBGrammar.g:187:7: ( . )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == u'*') :
                    LA2_1 = self.input.LA(2)

                    if (LA2_1 == u'/') :
                        alt2 = 2
                    elif ((u'\u0000' <= LA2_1 <= u'.') or (u'0' <= LA2_1 <= u'\uFFFE')) :
                        alt2 = 1


                elif ((u'\u0000' <= LA2_0 <= u')') or (u'+' <= LA2_0 <= u'\uFFFE')) :
                    alt2 = 1


                if alt2 == 1:
                    # XKBGrammar.g:187:7: .
                    self.matchAny()



                else:
                    break #loop2


            self.match("*/")


            #action start
            self.channel=HIDDEN;
            #action end




        finally:

            pass

    # $ANTLR end COMMENT



    # $ANTLR start LINE_COMMENT
    def mLINE_COMMENT(self, ):

        try:
            self.type = LINE_COMMENT

            # XKBGrammar.g:191:6: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # XKBGrammar.g:192:2: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            self.match("//")


            # XKBGrammar.g:192:7: (~ ( '\\n' | '\\r' ) )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((u'\u0000' <= LA3_0 <= u'\t') or (u'\u000B' <= LA3_0 <= u'\f') or (u'\u000E' <= LA3_0 <= u'\uFFFE')) :
                    alt3 = 1


                if alt3 == 1:
                    # XKBGrammar.g:192:7: ~ ( '\\n' | '\\r' )
                    if (u'\u0000' <= self.input.LA(1) <= u'\t') or (u'\u000B' <= self.input.LA(1) <= u'\f') or (u'\u000E' <= self.input.LA(1) <= u'\uFFFE'):
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop3


            # XKBGrammar.g:192:21: ( '\\r' )?
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == u'\r') :
                alt4 = 1
            if alt4 == 1:
                # XKBGrammar.g:192:21: '\\r'
                self.match(u'\r')




            self.match(u'\n')

            #action start
            self.channel=HIDDEN;
            #action end




        finally:

            pass

    # $ANTLR end LINE_COMMENT



    def mTokens(self):
        # XKBGrammar.g:1:8: ( TOKEN_DEFAULT | TOKEN_HIDDEN | TOKEN_PARTIAL | TOKEN_ALPHANUMERIC_KEYS | TOKEN_MODIFIER_KEYS | TOKEN_ALTERNATE_GROUP | TOKEN_XKB_SYMBOLS | TOKEN_INCLUDE | TOKEN_KEY_TYPE | TOKEN_NAME | TOKEN_KEY | LBRACKET | RBRACKET | LCURLY | RCURLY | COMMA | DQUOTE | MINUS | PLUS | SEMICOLON | EQUAL | LOWERTHAN | GREATERTHAN | DOT | NAME | WS | COMMENT | LINE_COMMENT )
        alt5 = 28
        LA5 = self.input.LA(1)
        if LA5 == u'd':
            LA5_1 = self.input.LA(2)

            if (LA5_1 == u'e') :
                LA5_26 = self.input.LA(3)

                if (LA5_26 == u'f') :
                    LA5_37 = self.input.LA(4)

                    if (LA5_37 == u'a') :
                        LA5_47 = self.input.LA(5)

                        if (LA5_47 == u'u') :
                            LA5_58 = self.input.LA(6)

                            if (LA5_58 == u'l') :
                                LA5_67 = self.input.LA(7)

                                if (LA5_67 == u't') :
                                    LA5_75 = self.input.LA(8)

                                    if ((u'(' <= LA5_75 <= u')') or (u'0' <= LA5_75 <= u'9') or (u'A' <= LA5_75 <= u'Z') or LA5_75 == u'_' or (u'a' <= LA5_75 <= u'z')) :
                                        alt5 = 25
                                    else:
                                        alt5 = 1
                                else:
                                    alt5 = 25
                            else:
                                alt5 = 25
                        else:
                            alt5 = 25
                    else:
                        alt5 = 25
                else:
                    alt5 = 25
            else:
                alt5 = 25
        elif LA5 == u'h':
            LA5_2 = self.input.LA(2)

            if (LA5_2 == u'i') :
                LA5_27 = self.input.LA(3)

                if (LA5_27 == u'd') :
                    LA5_38 = self.input.LA(4)

                    if (LA5_38 == u'd') :
                        LA5_48 = self.input.LA(5)

                        if (LA5_48 == u'e') :
                            LA5_59 = self.input.LA(6)

                            if (LA5_59 == u'n') :
                                LA5_68 = self.input.LA(7)

                                if ((u'(' <= LA5_68 <= u')') or (u'0' <= LA5_68 <= u'9') or (u'A' <= LA5_68 <= u'Z') or LA5_68 == u'_' or (u'a' <= LA5_68 <= u'z')) :
                                    alt5 = 25
                                else:
                                    alt5 = 2
                            else:
                                alt5 = 25
                        else:
                            alt5 = 25
                    else:
                        alt5 = 25
                else:
                    alt5 = 25
            else:
                alt5 = 25
        elif LA5 == u'p':
            LA5_3 = self.input.LA(2)

            if (LA5_3 == u'a') :
                LA5_28 = self.input.LA(3)

                if (LA5_28 == u'r') :
                    LA5_39 = self.input.LA(4)

                    if (LA5_39 == u't') :
                        LA5_49 = self.input.LA(5)

                        if (LA5_49 == u'i') :
                            LA5_60 = self.input.LA(6)

                            if (LA5_60 == u'a') :
                                LA5_69 = self.input.LA(7)

                                if (LA5_69 == u'l') :
                                    LA5_77 = self.input.LA(8)

                                    if ((u'(' <= LA5_77 <= u')') or (u'0' <= LA5_77 <= u'9') or (u'A' <= LA5_77 <= u'Z') or LA5_77 == u'_' or (u'a' <= LA5_77 <= u'z')) :
                                        alt5 = 25
                                    else:
                                        alt5 = 3
                                else:
                                    alt5 = 25
                            else:
                                alt5 = 25
                        else:
                            alt5 = 25
                    else:
                        alt5 = 25
                else:
                    alt5 = 25
            else:
                alt5 = 25
        elif LA5 == u'a':
            LA5_4 = self.input.LA(2)

            if (LA5_4 == u'l') :
                LA5 = self.input.LA(3)
                if LA5 == u't':
                    LA5_40 = self.input.LA(4)

                    if (LA5_40 == u'e') :
                        LA5_50 = self.input.LA(5)

                        if (LA5_50 == u'r') :
                            LA5_61 = self.input.LA(6)

                            if (LA5_61 == u'n') :
                                LA5_70 = self.input.LA(7)

                                if (LA5_70 == u'a') :
                                    LA5_78 = self.input.LA(8)

                                    if (LA5_78 == u't') :
                                        LA5_85 = self.input.LA(9)

                                        if (LA5_85 == u'e') :
                                            LA5_90 = self.input.LA(10)

                                            if (LA5_90 == u'_') :
                                                LA5_94 = self.input.LA(11)

                                                if (LA5_94 == u'g') :
                                                    LA5_98 = self.input.LA(12)

                                                    if (LA5_98 == u'r') :
                                                        LA5_102 = self.input.LA(13)

                                                        if (LA5_102 == u'o') :
                                                            LA5_106 = self.input.LA(14)

                                                            if (LA5_106 == u'u') :
                                                                LA5_109 = self.input.LA(15)

                                                                if (LA5_109 == u'p') :
                                                                    LA5_112 = self.input.LA(16)

                                                                    if ((u'(' <= LA5_112 <= u')') or (u'0' <= LA5_112 <= u'9') or (u'A' <= LA5_112 <= u'Z') or LA5_112 == u'_' or (u'a' <= LA5_112 <= u'z')) :
                                                                        alt5 = 25
                                                                    else:
                                                                        alt5 = 6
                                                                else:
                                                                    alt5 = 25
                                                            else:
                                                                alt5 = 25
                                                        else:
                                                            alt5 = 25
                                                    else:
                                                        alt5 = 25
                                                else:
                                                    alt5 = 25
                                            else:
                                                alt5 = 25
                                        else:
                                            alt5 = 25
                                    else:
                                        alt5 = 25
                                else:
                                    alt5 = 25
                            else:
                                alt5 = 25
                        else:
                            alt5 = 25
                    else:
                        alt5 = 25
                elif LA5 == u'p':
                    LA5_41 = self.input.LA(4)

                    if (LA5_41 == u'h') :
                        LA5_51 = self.input.LA(5)

                        if (LA5_51 == u'a') :
                            LA5_62 = self.input.LA(6)

                            if (LA5_62 == u'n') :
                                LA5_71 = self.input.LA(7)

                                if (LA5_71 == u'u') :
                                    LA5_79 = self.input.LA(8)

                                    if (LA5_79 == u'm') :
                                        LA5_86 = self.input.LA(9)

                                        if (LA5_86 == u'e') :
                                            LA5_91 = self.input.LA(10)

                                            if (LA5_91 == u'r') :
                                                LA5_95 = self.input.LA(11)

                                                if (LA5_95 == u'i') :
                                                    LA5_99 = self.input.LA(12)

                                                    if (LA5_99 == u'c') :
                                                        LA5_103 = self.input.LA(13)

                                                        if (LA5_103 == u'_') :
                                                            LA5_107 = self.input.LA(14)

                                                            if (LA5_107 == u'k') :
                                                                LA5_110 = self.input.LA(15)

                                                                if (LA5_110 == u'e') :
                                                                    LA5_113 = self.input.LA(16)

                                                                    if (LA5_113 == u'y') :
                                                                        LA5_115 = self.input.LA(17)

                                                                        if (LA5_115 == u's') :
                                                                            LA5_116 = self.input.LA(18)

                                                                            if ((u'(' <= LA5_116 <= u')') or (u'0' <= LA5_116 <= u'9') or (u'A' <= LA5_116 <= u'Z') or LA5_116 == u'_' or (u'a' <= LA5_116 <= u'z')) :
                                                                                alt5 = 25
                                                                            else:
                                                                                alt5 = 4
                                                                        else:
                                                                            alt5 = 25
                                                                    else:
                                                                        alt5 = 25
                                                                else:
                                                                    alt5 = 25
                                                            else:
                                                                alt5 = 25
                                                        else:
                                                            alt5 = 25
                                                    else:
                                                        alt5 = 25
                                                else:
                                                    alt5 = 25
                                            else:
                                                alt5 = 25
                                        else:
                                            alt5 = 25
                                    else:
                                        alt5 = 25
                                else:
                                    alt5 = 25
                            else:
                                alt5 = 25
                        else:
                            alt5 = 25
                    else:
                        alt5 = 25
                else:
                    alt5 = 25
            else:
                alt5 = 25
        elif LA5 == u'm':
            LA5_5 = self.input.LA(2)

            if (LA5_5 == u'o') :
                LA5_30 = self.input.LA(3)

                if (LA5_30 == u'd') :
                    LA5_42 = self.input.LA(4)

                    if (LA5_42 == u'i') :
                        LA5_52 = self.input.LA(5)

                        if (LA5_52 == u'f') :
                            LA5_63 = self.input.LA(6)

                            if (LA5_63 == u'i') :
                                LA5_72 = self.input.LA(7)

                                if (LA5_72 == u'e') :
                                    LA5_80 = self.input.LA(8)

                                    if (LA5_80 == u'r') :
                                        LA5_87 = self.input.LA(9)

                                        if (LA5_87 == u'_') :
                                            LA5_92 = self.input.LA(10)

                                            if (LA5_92 == u'k') :
                                                LA5_96 = self.input.LA(11)

                                                if (LA5_96 == u'e') :
                                                    LA5_100 = self.input.LA(12)

                                                    if (LA5_100 == u'y') :
                                                        LA5_104 = self.input.LA(13)

                                                        if (LA5_104 == u's') :
                                                            LA5_108 = self.input.LA(14)

                                                            if ((u'(' <= LA5_108 <= u')') or (u'0' <= LA5_108 <= u'9') or (u'A' <= LA5_108 <= u'Z') or LA5_108 == u'_' or (u'a' <= LA5_108 <= u'z')) :
                                                                alt5 = 25
                                                            else:
                                                                alt5 = 5
                                                        else:
                                                            alt5 = 25
                                                    else:
                                                        alt5 = 25
                                                else:
                                                    alt5 = 25
                                            else:
                                                alt5 = 25
                                        else:
                                            alt5 = 25
                                    else:
                                        alt5 = 25
                                else:
                                    alt5 = 25
                            else:
                                alt5 = 25
                        else:
                            alt5 = 25
                    else:
                        alt5 = 25
                else:
                    alt5 = 25
            else:
                alt5 = 25
        elif LA5 == u'x':
            LA5_6 = self.input.LA(2)

            if (LA5_6 == u'k') :
                LA5_31 = self.input.LA(3)

                if (LA5_31 == u'b') :
                    LA5_43 = self.input.LA(4)

                    if (LA5_43 == u'_') :
                        LA5_53 = self.input.LA(5)

                        if (LA5_53 == u's') :
                            LA5_64 = self.input.LA(6)

                            if (LA5_64 == u'y') :
                                LA5_73 = self.input.LA(7)

                                if (LA5_73 == u'm') :
                                    LA5_81 = self.input.LA(8)

                                    if (LA5_81 == u'b') :
                                        LA5_88 = self.input.LA(9)

                                        if (LA5_88 == u'o') :
                                            LA5_93 = self.input.LA(10)

                                            if (LA5_93 == u'l') :
                                                LA5_97 = self.input.LA(11)

                                                if (LA5_97 == u's') :
                                                    LA5_101 = self.input.LA(12)

                                                    if ((u'(' <= LA5_101 <= u')') or (u'0' <= LA5_101 <= u'9') or (u'A' <= LA5_101 <= u'Z') or LA5_101 == u'_' or (u'a' <= LA5_101 <= u'z')) :
                                                        alt5 = 25
                                                    else:
                                                        alt5 = 7
                                                else:
                                                    alt5 = 25
                                            else:
                                                alt5 = 25
                                        else:
                                            alt5 = 25
                                    else:
                                        alt5 = 25
                                else:
                                    alt5 = 25
                            else:
                                alt5 = 25
                        else:
                            alt5 = 25
                    else:
                        alt5 = 25
                else:
                    alt5 = 25
            else:
                alt5 = 25
        elif LA5 == u'i':
            LA5_7 = self.input.LA(2)

            if (LA5_7 == u'n') :
                LA5_32 = self.input.LA(3)

                if (LA5_32 == u'c') :
                    LA5_44 = self.input.LA(4)

                    if (LA5_44 == u'l') :
                        LA5_54 = self.input.LA(5)

                        if (LA5_54 == u'u') :
                            LA5_65 = self.input.LA(6)

                            if (LA5_65 == u'd') :
                                LA5_74 = self.input.LA(7)

                                if (LA5_74 == u'e') :
                                    LA5_82 = self.input.LA(8)

                                    if ((u'(' <= LA5_82 <= u')') or (u'0' <= LA5_82 <= u'9') or (u'A' <= LA5_82 <= u'Z') or LA5_82 == u'_' or (u'a' <= LA5_82 <= u'z')) :
                                        alt5 = 25
                                    else:
                                        alt5 = 8
                                else:
                                    alt5 = 25
                            else:
                                alt5 = 25
                        else:
                            alt5 = 25
                    else:
                        alt5 = 25
                else:
                    alt5 = 25
            else:
                alt5 = 25
        elif LA5 == u'k':
            LA5_8 = self.input.LA(2)

            if (LA5_8 == u'e') :
                LA5_33 = self.input.LA(3)

                if (LA5_33 == u'y') :
                    LA5 = self.input.LA(4)
                    if LA5 == u'.':
                        alt5 = 9
                    elif LA5 == u'(' or LA5 == u')' or LA5 == u'0' or LA5 == u'1' or LA5 == u'2' or LA5 == u'3' or LA5 == u'4' or LA5 == u'5' or LA5 == u'6' or LA5 == u'7' or LA5 == u'8' or LA5 == u'9' or LA5 == u'A' or LA5 == u'B' or LA5 == u'C' or LA5 == u'D' or LA5 == u'E' or LA5 == u'F' or LA5 == u'G' or LA5 == u'H' or LA5 == u'I' or LA5 == u'J' or LA5 == u'K' or LA5 == u'L' or LA5 == u'M' or LA5 == u'N' or LA5 == u'O' or LA5 == u'P' or LA5 == u'Q' or LA5 == u'R' or LA5 == u'S' or LA5 == u'T' or LA5 == u'U' or LA5 == u'V' or LA5 == u'W' or LA5 == u'X' or LA5 == u'Y' or LA5 == u'Z' or LA5 == u'_' or LA5 == u'a' or LA5 == u'b' or LA5 == u'c' or LA5 == u'd' or LA5 == u'e' or LA5 == u'f' or LA5 == u'g' or LA5 == u'h' or LA5 == u'i' or LA5 == u'j' or LA5 == u'k' or LA5 == u'l' or LA5 == u'm' or LA5 == u'n' or LA5 == u'o' or LA5 == u'p' or LA5 == u'q' or LA5 == u'r' or LA5 == u's' or LA5 == u't' or LA5 == u'u' or LA5 == u'v' or LA5 == u'w' or LA5 == u'x' or LA5 == u'y' or LA5 == u'z':
                        alt5 = 25
                    else:
                        alt5 = 11
                else:
                    alt5 = 25
            else:
                alt5 = 25
        elif LA5 == u'n':
            LA5_9 = self.input.LA(2)

            if (LA5_9 == u'a') :
                LA5_34 = self.input.LA(3)

                if (LA5_34 == u'm') :
                    LA5_46 = self.input.LA(4)

                    if (LA5_46 == u'e') :
                        LA5_57 = self.input.LA(5)

                        if ((u'(' <= LA5_57 <= u')') or (u'0' <= LA5_57 <= u'9') or (u'A' <= LA5_57 <= u'Z') or LA5_57 == u'_' or (u'a' <= LA5_57 <= u'z')) :
                            alt5 = 25
                        else:
                            alt5 = 10
                    else:
                        alt5 = 25
                else:
                    alt5 = 25
            else:
                alt5 = 25
        elif LA5 == u'[':
            alt5 = 12
        elif LA5 == u']':
            alt5 = 13
        elif LA5 == u'{':
            alt5 = 14
        elif LA5 == u'}':
            alt5 = 15
        elif LA5 == u',':
            alt5 = 16
        elif LA5 == u'"':
            alt5 = 17
        elif LA5 == u'-':
            alt5 = 18
        elif LA5 == u'+':
            alt5 = 19
        elif LA5 == u';':
            alt5 = 20
        elif LA5 == u'=':
            alt5 = 21
        elif LA5 == u'<':
            alt5 = 22
        elif LA5 == u'>':
            alt5 = 23
        elif LA5 == u'.':
            alt5 = 24
        elif LA5 == u'\t' or LA5 == u'\n' or LA5 == u'\f' or LA5 == u'\r' or LA5 == u' ':
            alt5 = 26
        elif LA5 == u'/':
            LA5_25 = self.input.LA(2)

            if (LA5_25 == u'*') :
                alt5 = 27
            elif (LA5_25 == u'/') :
                alt5 = 28
            else:
                nvae = NoViableAltException("1:1: Tokens : ( TOKEN_DEFAULT | TOKEN_HIDDEN | TOKEN_PARTIAL | TOKEN_ALPHANUMERIC_KEYS | TOKEN_MODIFIER_KEYS | TOKEN_ALTERNATE_GROUP | TOKEN_XKB_SYMBOLS | TOKEN_INCLUDE | TOKEN_KEY_TYPE | TOKEN_NAME | TOKEN_KEY | LBRACKET | RBRACKET | LCURLY | RCURLY | COMMA | DQUOTE | MINUS | PLUS | SEMICOLON | EQUAL | LOWERTHAN | GREATERTHAN | DOT | NAME | WS | COMMENT | LINE_COMMENT );", 5, 25, self.input)

                raise nvae

        else:
            alt5 = 25
        if alt5 == 1:
            # XKBGrammar.g:1:10: TOKEN_DEFAULT
            self.mTOKEN_DEFAULT()



        elif alt5 == 2:
            # XKBGrammar.g:1:24: TOKEN_HIDDEN
            self.mTOKEN_HIDDEN()



        elif alt5 == 3:
            # XKBGrammar.g:1:37: TOKEN_PARTIAL
            self.mTOKEN_PARTIAL()



        elif alt5 == 4:
            # XKBGrammar.g:1:51: TOKEN_ALPHANUMERIC_KEYS
            self.mTOKEN_ALPHANUMERIC_KEYS()



        elif alt5 == 5:
            # XKBGrammar.g:1:75: TOKEN_MODIFIER_KEYS
            self.mTOKEN_MODIFIER_KEYS()



        elif alt5 == 6:
            # XKBGrammar.g:1:95: TOKEN_ALTERNATE_GROUP
            self.mTOKEN_ALTERNATE_GROUP()



        elif alt5 == 7:
            # XKBGrammar.g:1:117: TOKEN_XKB_SYMBOLS
            self.mTOKEN_XKB_SYMBOLS()



        elif alt5 == 8:
            # XKBGrammar.g:1:135: TOKEN_INCLUDE
            self.mTOKEN_INCLUDE()



        elif alt5 == 9:
            # XKBGrammar.g:1:149: TOKEN_KEY_TYPE
            self.mTOKEN_KEY_TYPE()



        elif alt5 == 10:
            # XKBGrammar.g:1:164: TOKEN_NAME
            self.mTOKEN_NAME()



        elif alt5 == 11:
            # XKBGrammar.g:1:175: TOKEN_KEY
            self.mTOKEN_KEY()



        elif alt5 == 12:
            # XKBGrammar.g:1:185: LBRACKET
            self.mLBRACKET()



        elif alt5 == 13:
            # XKBGrammar.g:1:194: RBRACKET
            self.mRBRACKET()



        elif alt5 == 14:
            # XKBGrammar.g:1:203: LCURLY
            self.mLCURLY()



        elif alt5 == 15:
            # XKBGrammar.g:1:210: RCURLY
            self.mRCURLY()



        elif alt5 == 16:
            # XKBGrammar.g:1:217: COMMA
            self.mCOMMA()



        elif alt5 == 17:
            # XKBGrammar.g:1:223: DQUOTE
            self.mDQUOTE()



        elif alt5 == 18:
            # XKBGrammar.g:1:230: MINUS
            self.mMINUS()



        elif alt5 == 19:
            # XKBGrammar.g:1:236: PLUS
            self.mPLUS()



        elif alt5 == 20:
            # XKBGrammar.g:1:241: SEMICOLON
            self.mSEMICOLON()



        elif alt5 == 21:
            # XKBGrammar.g:1:251: EQUAL
            self.mEQUAL()



        elif alt5 == 22:
            # XKBGrammar.g:1:257: LOWERTHAN
            self.mLOWERTHAN()



        elif alt5 == 23:
            # XKBGrammar.g:1:267: GREATERTHAN
            self.mGREATERTHAN()



        elif alt5 == 24:
            # XKBGrammar.g:1:279: DOT
            self.mDOT()



        elif alt5 == 25:
            # XKBGrammar.g:1:283: NAME
            self.mNAME()



        elif alt5 == 26:
            # XKBGrammar.g:1:288: WS
            self.mWS()



        elif alt5 == 27:
            # XKBGrammar.g:1:291: COMMENT
            self.mCOMMENT()



        elif alt5 == 28:
            # XKBGrammar.g:1:299: LINE_COMMENT
            self.mLINE_COMMENT()








 

