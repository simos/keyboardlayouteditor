# $ANTLR 3.0.1 XKBGrammar.g 2008-05-09 13:01:19

from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
TOKEN_ALTERNATE_GROUP=9
ATTRIBUTES=28
SECTION=33
TOKEN_INCLUDE=11
KEY=31
KEYTYPE=32
ATTRIBUTE=29
TOKEN_NAME=13
DQUOTE=20
LCURLY=17
SEMICOLON=23
MINUS=21
TOKEN_XKB_SYMBOLS=10
Tokens=40
EOF=-1
GENERIC_NAME=36
SECTIONNAME=34
LBRACKET=15
TOKEN_PARTIAL=6
NAME=35
WS=39
TOKEN_HIDDEN=5
TOKEN_ALPHANUMERIC_KEYS=7
NEWLINE=38
COMMA=19
LOWERTHAN=25
EQUAL=24
INCLUDE=30
RCURLY=18
TOKEN_MODIFIER_KEYS=8
PLUS=22
TOKEN_KEY=14
RBRACKET=16
DOT=27
COMMENT=37
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
            # XKBGrammar.g:165:2: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' ) )
            # XKBGrammar.g:165:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )
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

            # XKBGrammar.g:169:2: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' )* )
            # XKBGrammar.g:169:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' )*
            # XKBGrammar.g:169:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' )*
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



    # $ANTLR start COMMENT
    def mCOMMENT(self, ):

        try:
            self.type = COMMENT

            # XKBGrammar.g:174:2: ( '//' (~ ( '\\n' | '\\r' ) )* )
            # XKBGrammar.g:174:4: '//' (~ ( '\\n' | '\\r' ) )*
            self.match("//")


            # XKBGrammar.g:174:9: (~ ( '\\n' | '\\r' ) )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((u'\u0000' <= LA2_0 <= u'\t') or (u'\u000B' <= LA2_0 <= u'\f') or (u'\u000E' <= LA2_0 <= u'\uFFFE')) :
                    alt2 = 1


                if alt2 == 1:
                    # XKBGrammar.g:174:10: ~ ( '\\n' | '\\r' )
                    if (u'\u0000' <= self.input.LA(1) <= u'\t') or (u'\u000B' <= self.input.LA(1) <= u'\f') or (u'\u000E' <= self.input.LA(1) <= u'\uFFFE'):
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop2


            #action start
            self.channel = HIDDEN; 
            #action end




        finally:

            pass

    # $ANTLR end COMMENT



    # $ANTLR start WS
    def mWS(self, ):

        try:
            self.type = WS

            # XKBGrammar.g:178:9: ( ( '\\t' | ' ' | NEWLINE )+ )
            # XKBGrammar.g:178:17: ( '\\t' | ' ' | NEWLINE )+
            # XKBGrammar.g:178:17: ( '\\t' | ' ' | NEWLINE )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((u'\t' <= LA3_0 <= u'\n') or LA3_0 == u'\r' or LA3_0 == u' ') :
                    alt3 = 1


                if alt3 == 1:
                    # XKBGrammar.g:
                    if (u'\t' <= self.input.LA(1) <= u'\n') or self.input.LA(1) == u'\r' or self.input.LA(1) == u' ':
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1


            #action start
            self.channel=HIDDEN; 
            #action end




        finally:

            pass

    # $ANTLR end WS



    # $ANTLR start NEWLINE
    def mNEWLINE(self, ):

        try:
            # XKBGrammar.g:183:9: ( '\\r' | '\\n' )
            # XKBGrammar.g:
            if self.input.LA(1) == u'\n' or self.input.LA(1) == u'\r':
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:

            pass

    # $ANTLR end NEWLINE



    def mTokens(self):
        # XKBGrammar.g:1:8: ( TOKEN_DEFAULT | TOKEN_HIDDEN | TOKEN_PARTIAL | TOKEN_ALPHANUMERIC_KEYS | TOKEN_MODIFIER_KEYS | TOKEN_ALTERNATE_GROUP | TOKEN_XKB_SYMBOLS | TOKEN_INCLUDE | TOKEN_KEY_TYPE | TOKEN_NAME | TOKEN_KEY | LBRACKET | RBRACKET | LCURLY | RCURLY | COMMA | DQUOTE | MINUS | PLUS | SEMICOLON | EQUAL | LOWERTHAN | GREATERTHAN | DOT | NAME | COMMENT | WS )
        alt4 = 27
        LA4 = self.input.LA(1)
        if LA4 == u'd':
            LA4_1 = self.input.LA(2)

            if (LA4_1 == u'e') :
                LA4_26 = self.input.LA(3)

                if (LA4_26 == u'f') :
                    LA4_35 = self.input.LA(4)

                    if (LA4_35 == u'a') :
                        LA4_45 = self.input.LA(5)

                        if (LA4_45 == u'u') :
                            LA4_56 = self.input.LA(6)

                            if (LA4_56 == u'l') :
                                LA4_65 = self.input.LA(7)

                                if (LA4_65 == u't') :
                                    LA4_73 = self.input.LA(8)

                                    if ((u'(' <= LA4_73 <= u')') or (u'0' <= LA4_73 <= u'9') or (u'A' <= LA4_73 <= u'Z') or LA4_73 == u'_' or (u'a' <= LA4_73 <= u'z')) :
                                        alt4 = 25
                                    else:
                                        alt4 = 1
                                else:
                                    alt4 = 25
                            else:
                                alt4 = 25
                        else:
                            alt4 = 25
                    else:
                        alt4 = 25
                else:
                    alt4 = 25
            else:
                alt4 = 25
        elif LA4 == u'h':
            LA4_2 = self.input.LA(2)

            if (LA4_2 == u'i') :
                LA4_27 = self.input.LA(3)

                if (LA4_27 == u'd') :
                    LA4_36 = self.input.LA(4)

                    if (LA4_36 == u'd') :
                        LA4_46 = self.input.LA(5)

                        if (LA4_46 == u'e') :
                            LA4_57 = self.input.LA(6)

                            if (LA4_57 == u'n') :
                                LA4_66 = self.input.LA(7)

                                if ((u'(' <= LA4_66 <= u')') or (u'0' <= LA4_66 <= u'9') or (u'A' <= LA4_66 <= u'Z') or LA4_66 == u'_' or (u'a' <= LA4_66 <= u'z')) :
                                    alt4 = 25
                                else:
                                    alt4 = 2
                            else:
                                alt4 = 25
                        else:
                            alt4 = 25
                    else:
                        alt4 = 25
                else:
                    alt4 = 25
            else:
                alt4 = 25
        elif LA4 == u'p':
            LA4_3 = self.input.LA(2)

            if (LA4_3 == u'a') :
                LA4_28 = self.input.LA(3)

                if (LA4_28 == u'r') :
                    LA4_37 = self.input.LA(4)

                    if (LA4_37 == u't') :
                        LA4_47 = self.input.LA(5)

                        if (LA4_47 == u'i') :
                            LA4_58 = self.input.LA(6)

                            if (LA4_58 == u'a') :
                                LA4_67 = self.input.LA(7)

                                if (LA4_67 == u'l') :
                                    LA4_75 = self.input.LA(8)

                                    if ((u'(' <= LA4_75 <= u')') or (u'0' <= LA4_75 <= u'9') or (u'A' <= LA4_75 <= u'Z') or LA4_75 == u'_' or (u'a' <= LA4_75 <= u'z')) :
                                        alt4 = 25
                                    else:
                                        alt4 = 3
                                else:
                                    alt4 = 25
                            else:
                                alt4 = 25
                        else:
                            alt4 = 25
                    else:
                        alt4 = 25
                else:
                    alt4 = 25
            else:
                alt4 = 25
        elif LA4 == u'a':
            LA4_4 = self.input.LA(2)

            if (LA4_4 == u'l') :
                LA4 = self.input.LA(3)
                if LA4 == u'p':
                    LA4_38 = self.input.LA(4)

                    if (LA4_38 == u'h') :
                        LA4_48 = self.input.LA(5)

                        if (LA4_48 == u'a') :
                            LA4_59 = self.input.LA(6)

                            if (LA4_59 == u'n') :
                                LA4_68 = self.input.LA(7)

                                if (LA4_68 == u'u') :
                                    LA4_76 = self.input.LA(8)

                                    if (LA4_76 == u'm') :
                                        LA4_83 = self.input.LA(9)

                                        if (LA4_83 == u'e') :
                                            LA4_88 = self.input.LA(10)

                                            if (LA4_88 == u'r') :
                                                LA4_92 = self.input.LA(11)

                                                if (LA4_92 == u'i') :
                                                    LA4_96 = self.input.LA(12)

                                                    if (LA4_96 == u'c') :
                                                        LA4_100 = self.input.LA(13)

                                                        if (LA4_100 == u'_') :
                                                            LA4_104 = self.input.LA(14)

                                                            if (LA4_104 == u'k') :
                                                                LA4_107 = self.input.LA(15)

                                                                if (LA4_107 == u'e') :
                                                                    LA4_110 = self.input.LA(16)

                                                                    if (LA4_110 == u'y') :
                                                                        LA4_112 = self.input.LA(17)

                                                                        if (LA4_112 == u's') :
                                                                            LA4_114 = self.input.LA(18)

                                                                            if ((u'(' <= LA4_114 <= u')') or (u'0' <= LA4_114 <= u'9') or (u'A' <= LA4_114 <= u'Z') or LA4_114 == u'_' or (u'a' <= LA4_114 <= u'z')) :
                                                                                alt4 = 25
                                                                            else:
                                                                                alt4 = 4
                                                                        else:
                                                                            alt4 = 25
                                                                    else:
                                                                        alt4 = 25
                                                                else:
                                                                    alt4 = 25
                                                            else:
                                                                alt4 = 25
                                                        else:
                                                            alt4 = 25
                                                    else:
                                                        alt4 = 25
                                                else:
                                                    alt4 = 25
                                            else:
                                                alt4 = 25
                                        else:
                                            alt4 = 25
                                    else:
                                        alt4 = 25
                                else:
                                    alt4 = 25
                            else:
                                alt4 = 25
                        else:
                            alt4 = 25
                    else:
                        alt4 = 25
                elif LA4 == u't':
                    LA4_39 = self.input.LA(4)

                    if (LA4_39 == u'e') :
                        LA4_49 = self.input.LA(5)

                        if (LA4_49 == u'r') :
                            LA4_60 = self.input.LA(6)

                            if (LA4_60 == u'n') :
                                LA4_69 = self.input.LA(7)

                                if (LA4_69 == u'a') :
                                    LA4_77 = self.input.LA(8)

                                    if (LA4_77 == u't') :
                                        LA4_84 = self.input.LA(9)

                                        if (LA4_84 == u'e') :
                                            LA4_89 = self.input.LA(10)

                                            if (LA4_89 == u'_') :
                                                LA4_93 = self.input.LA(11)

                                                if (LA4_93 == u'g') :
                                                    LA4_97 = self.input.LA(12)

                                                    if (LA4_97 == u'r') :
                                                        LA4_101 = self.input.LA(13)

                                                        if (LA4_101 == u'o') :
                                                            LA4_105 = self.input.LA(14)

                                                            if (LA4_105 == u'u') :
                                                                LA4_108 = self.input.LA(15)

                                                                if (LA4_108 == u'p') :
                                                                    LA4_111 = self.input.LA(16)

                                                                    if ((u'(' <= LA4_111 <= u')') or (u'0' <= LA4_111 <= u'9') or (u'A' <= LA4_111 <= u'Z') or LA4_111 == u'_' or (u'a' <= LA4_111 <= u'z')) :
                                                                        alt4 = 25
                                                                    else:
                                                                        alt4 = 6
                                                                else:
                                                                    alt4 = 25
                                                            else:
                                                                alt4 = 25
                                                        else:
                                                            alt4 = 25
                                                    else:
                                                        alt4 = 25
                                                else:
                                                    alt4 = 25
                                            else:
                                                alt4 = 25
                                        else:
                                            alt4 = 25
                                    else:
                                        alt4 = 25
                                else:
                                    alt4 = 25
                            else:
                                alt4 = 25
                        else:
                            alt4 = 25
                    else:
                        alt4 = 25
                else:
                    alt4 = 25
            else:
                alt4 = 25
        elif LA4 == u'm':
            LA4_5 = self.input.LA(2)

            if (LA4_5 == u'o') :
                LA4_30 = self.input.LA(3)

                if (LA4_30 == u'd') :
                    LA4_40 = self.input.LA(4)

                    if (LA4_40 == u'i') :
                        LA4_50 = self.input.LA(5)

                        if (LA4_50 == u'f') :
                            LA4_61 = self.input.LA(6)

                            if (LA4_61 == u'i') :
                                LA4_70 = self.input.LA(7)

                                if (LA4_70 == u'e') :
                                    LA4_78 = self.input.LA(8)

                                    if (LA4_78 == u'r') :
                                        LA4_85 = self.input.LA(9)

                                        if (LA4_85 == u'_') :
                                            LA4_90 = self.input.LA(10)

                                            if (LA4_90 == u'k') :
                                                LA4_94 = self.input.LA(11)

                                                if (LA4_94 == u'e') :
                                                    LA4_98 = self.input.LA(12)

                                                    if (LA4_98 == u'y') :
                                                        LA4_102 = self.input.LA(13)

                                                        if (LA4_102 == u's') :
                                                            LA4_106 = self.input.LA(14)

                                                            if ((u'(' <= LA4_106 <= u')') or (u'0' <= LA4_106 <= u'9') or (u'A' <= LA4_106 <= u'Z') or LA4_106 == u'_' or (u'a' <= LA4_106 <= u'z')) :
                                                                alt4 = 25
                                                            else:
                                                                alt4 = 5
                                                        else:
                                                            alt4 = 25
                                                    else:
                                                        alt4 = 25
                                                else:
                                                    alt4 = 25
                                            else:
                                                alt4 = 25
                                        else:
                                            alt4 = 25
                                    else:
                                        alt4 = 25
                                else:
                                    alt4 = 25
                            else:
                                alt4 = 25
                        else:
                            alt4 = 25
                    else:
                        alt4 = 25
                else:
                    alt4 = 25
            else:
                alt4 = 25
        elif LA4 == u'x':
            LA4_6 = self.input.LA(2)

            if (LA4_6 == u'k') :
                LA4_31 = self.input.LA(3)

                if (LA4_31 == u'b') :
                    LA4_41 = self.input.LA(4)

                    if (LA4_41 == u'_') :
                        LA4_51 = self.input.LA(5)

                        if (LA4_51 == u's') :
                            LA4_62 = self.input.LA(6)

                            if (LA4_62 == u'y') :
                                LA4_71 = self.input.LA(7)

                                if (LA4_71 == u'm') :
                                    LA4_79 = self.input.LA(8)

                                    if (LA4_79 == u'b') :
                                        LA4_86 = self.input.LA(9)

                                        if (LA4_86 == u'o') :
                                            LA4_91 = self.input.LA(10)

                                            if (LA4_91 == u'l') :
                                                LA4_95 = self.input.LA(11)

                                                if (LA4_95 == u's') :
                                                    LA4_99 = self.input.LA(12)

                                                    if ((u'(' <= LA4_99 <= u')') or (u'0' <= LA4_99 <= u'9') or (u'A' <= LA4_99 <= u'Z') or LA4_99 == u'_' or (u'a' <= LA4_99 <= u'z')) :
                                                        alt4 = 25
                                                    else:
                                                        alt4 = 7
                                                else:
                                                    alt4 = 25
                                            else:
                                                alt4 = 25
                                        else:
                                            alt4 = 25
                                    else:
                                        alt4 = 25
                                else:
                                    alt4 = 25
                            else:
                                alt4 = 25
                        else:
                            alt4 = 25
                    else:
                        alt4 = 25
                else:
                    alt4 = 25
            else:
                alt4 = 25
        elif LA4 == u'i':
            LA4_7 = self.input.LA(2)

            if (LA4_7 == u'n') :
                LA4_32 = self.input.LA(3)

                if (LA4_32 == u'c') :
                    LA4_42 = self.input.LA(4)

                    if (LA4_42 == u'l') :
                        LA4_52 = self.input.LA(5)

                        if (LA4_52 == u'u') :
                            LA4_63 = self.input.LA(6)

                            if (LA4_63 == u'd') :
                                LA4_72 = self.input.LA(7)

                                if (LA4_72 == u'e') :
                                    LA4_80 = self.input.LA(8)

                                    if ((u'(' <= LA4_80 <= u')') or (u'0' <= LA4_80 <= u'9') or (u'A' <= LA4_80 <= u'Z') or LA4_80 == u'_' or (u'a' <= LA4_80 <= u'z')) :
                                        alt4 = 25
                                    else:
                                        alt4 = 8
                                else:
                                    alt4 = 25
                            else:
                                alt4 = 25
                        else:
                            alt4 = 25
                    else:
                        alt4 = 25
                else:
                    alt4 = 25
            else:
                alt4 = 25
        elif LA4 == u'k':
            LA4_8 = self.input.LA(2)

            if (LA4_8 == u'e') :
                LA4_33 = self.input.LA(3)

                if (LA4_33 == u'y') :
                    LA4 = self.input.LA(4)
                    if LA4 == u'.':
                        alt4 = 9
                    elif LA4 == u'(' or LA4 == u')' or LA4 == u'0' or LA4 == u'1' or LA4 == u'2' or LA4 == u'3' or LA4 == u'4' or LA4 == u'5' or LA4 == u'6' or LA4 == u'7' or LA4 == u'8' or LA4 == u'9' or LA4 == u'A' or LA4 == u'B' or LA4 == u'C' or LA4 == u'D' or LA4 == u'E' or LA4 == u'F' or LA4 == u'G' or LA4 == u'H' or LA4 == u'I' or LA4 == u'J' or LA4 == u'K' or LA4 == u'L' or LA4 == u'M' or LA4 == u'N' or LA4 == u'O' or LA4 == u'P' or LA4 == u'Q' or LA4 == u'R' or LA4 == u'S' or LA4 == u'T' or LA4 == u'U' or LA4 == u'V' or LA4 == u'W' or LA4 == u'X' or LA4 == u'Y' or LA4 == u'Z' or LA4 == u'_' or LA4 == u'a' or LA4 == u'b' or LA4 == u'c' or LA4 == u'd' or LA4 == u'e' or LA4 == u'f' or LA4 == u'g' or LA4 == u'h' or LA4 == u'i' or LA4 == u'j' or LA4 == u'k' or LA4 == u'l' or LA4 == u'm' or LA4 == u'n' or LA4 == u'o' or LA4 == u'p' or LA4 == u'q' or LA4 == u'r' or LA4 == u's' or LA4 == u't' or LA4 == u'u' or LA4 == u'v' or LA4 == u'w' or LA4 == u'x' or LA4 == u'y' or LA4 == u'z':
                        alt4 = 25
                    else:
                        alt4 = 11
                else:
                    alt4 = 25
            else:
                alt4 = 25
        elif LA4 == u'n':
            LA4_9 = self.input.LA(2)

            if (LA4_9 == u'a') :
                LA4_34 = self.input.LA(3)

                if (LA4_34 == u'm') :
                    LA4_44 = self.input.LA(4)

                    if (LA4_44 == u'e') :
                        LA4_55 = self.input.LA(5)

                        if ((u'(' <= LA4_55 <= u')') or (u'0' <= LA4_55 <= u'9') or (u'A' <= LA4_55 <= u'Z') or LA4_55 == u'_' or (u'a' <= LA4_55 <= u'z')) :
                            alt4 = 25
                        else:
                            alt4 = 10
                    else:
                        alt4 = 25
                else:
                    alt4 = 25
            else:
                alt4 = 25
        elif LA4 == u'[':
            alt4 = 12
        elif LA4 == u']':
            alt4 = 13
        elif LA4 == u'{':
            alt4 = 14
        elif LA4 == u'}':
            alt4 = 15
        elif LA4 == u',':
            alt4 = 16
        elif LA4 == u'"':
            alt4 = 17
        elif LA4 == u'-':
            alt4 = 18
        elif LA4 == u'+':
            alt4 = 19
        elif LA4 == u';':
            alt4 = 20
        elif LA4 == u'=':
            alt4 = 21
        elif LA4 == u'<':
            alt4 = 22
        elif LA4 == u'>':
            alt4 = 23
        elif LA4 == u'.':
            alt4 = 24
        elif LA4 == u'/':
            alt4 = 26
        elif LA4 == u'\t' or LA4 == u'\n' or LA4 == u'\r' or LA4 == u' ':
            alt4 = 27
        else:
            alt4 = 25
        if alt4 == 1:
            # XKBGrammar.g:1:10: TOKEN_DEFAULT
            self.mTOKEN_DEFAULT()



        elif alt4 == 2:
            # XKBGrammar.g:1:24: TOKEN_HIDDEN
            self.mTOKEN_HIDDEN()



        elif alt4 == 3:
            # XKBGrammar.g:1:37: TOKEN_PARTIAL
            self.mTOKEN_PARTIAL()



        elif alt4 == 4:
            # XKBGrammar.g:1:51: TOKEN_ALPHANUMERIC_KEYS
            self.mTOKEN_ALPHANUMERIC_KEYS()



        elif alt4 == 5:
            # XKBGrammar.g:1:75: TOKEN_MODIFIER_KEYS
            self.mTOKEN_MODIFIER_KEYS()



        elif alt4 == 6:
            # XKBGrammar.g:1:95: TOKEN_ALTERNATE_GROUP
            self.mTOKEN_ALTERNATE_GROUP()



        elif alt4 == 7:
            # XKBGrammar.g:1:117: TOKEN_XKB_SYMBOLS
            self.mTOKEN_XKB_SYMBOLS()



        elif alt4 == 8:
            # XKBGrammar.g:1:135: TOKEN_INCLUDE
            self.mTOKEN_INCLUDE()



        elif alt4 == 9:
            # XKBGrammar.g:1:149: TOKEN_KEY_TYPE
            self.mTOKEN_KEY_TYPE()



        elif alt4 == 10:
            # XKBGrammar.g:1:164: TOKEN_NAME
            self.mTOKEN_NAME()



        elif alt4 == 11:
            # XKBGrammar.g:1:175: TOKEN_KEY
            self.mTOKEN_KEY()



        elif alt4 == 12:
            # XKBGrammar.g:1:185: LBRACKET
            self.mLBRACKET()



        elif alt4 == 13:
            # XKBGrammar.g:1:194: RBRACKET
            self.mRBRACKET()



        elif alt4 == 14:
            # XKBGrammar.g:1:203: LCURLY
            self.mLCURLY()



        elif alt4 == 15:
            # XKBGrammar.g:1:210: RCURLY
            self.mRCURLY()



        elif alt4 == 16:
            # XKBGrammar.g:1:217: COMMA
            self.mCOMMA()



        elif alt4 == 17:
            # XKBGrammar.g:1:223: DQUOTE
            self.mDQUOTE()



        elif alt4 == 18:
            # XKBGrammar.g:1:230: MINUS
            self.mMINUS()



        elif alt4 == 19:
            # XKBGrammar.g:1:236: PLUS
            self.mPLUS()



        elif alt4 == 20:
            # XKBGrammar.g:1:241: SEMICOLON
            self.mSEMICOLON()



        elif alt4 == 21:
            # XKBGrammar.g:1:251: EQUAL
            self.mEQUAL()



        elif alt4 == 22:
            # XKBGrammar.g:1:257: LOWERTHAN
            self.mLOWERTHAN()



        elif alt4 == 23:
            # XKBGrammar.g:1:267: GREATERTHAN
            self.mGREATERTHAN()



        elif alt4 == 24:
            # XKBGrammar.g:1:279: DOT
            self.mDOT()



        elif alt4 == 25:
            # XKBGrammar.g:1:283: NAME
            self.mNAME()



        elif alt4 == 26:
            # XKBGrammar.g:1:288: COMMENT
            self.mCOMMENT()



        elif alt4 == 27:
            # XKBGrammar.g:1:296: WS
            self.mWS()








 

