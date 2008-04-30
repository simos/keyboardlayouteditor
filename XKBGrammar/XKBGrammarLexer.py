# $ANTLR 3.0.1 XKBGrammar.g 2008-04-30 19:41:41

from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
TOKEN_ALTERNATE_GROUP=9
ATTRIBUTES=28
TOKEN_INCLUDE=11
KEYCODE=30
KEY=33
KEYTYPE=34
ATTRIBUTE=29
TOKEN_NAME=13
DQUOTE=20
LCURLY=17
SEMICOLON=23
NAME_INCLUDE=36
MINUS=21
TOKEN_XKB_SYMBOLS=10
Tokens=41
EOF=-1
NAME_KEYSYM=35
NAME_GROUP=37
LBRACKET=15
TOKEN_PARTIAL=6
NAME=32
WS=40
TOKEN_HIDDEN=5
TOKEN_ALPHANUMERIC_KEYS=7
NEWLINE=39
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
COMMENT=38
TOKEN_DEFAULT=4
TOKEN_KEY_TYPE=12
GREATERTHAN=26

class XKBGrammarLexer(Lexer):

    grammarFileName = "XKBGrammar.g"

    def __init__(self, input=None):
        Lexer.__init__(self, input)
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



    # $ANTLR start NAME
    def mNAME(self, ):

        try:
            self.type = NAME

            # XKBGrammar.g:124:2: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )* )
            # XKBGrammar.g:124:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )*
            if (u'A' <= self.input.LA(1) <= u'Z') or self.input.LA(1) == u'_' or (u'a' <= self.input.LA(1) <= u'z'):
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse


            # XKBGrammar.g:124:27: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((u'0' <= LA1_0 <= u'9') or (u'A' <= LA1_0 <= u'Z') or LA1_0 == u'_' or (u'a' <= LA1_0 <= u'z')) :
                    alt1 = 1


                if alt1 == 1:
                    # XKBGrammar.g:
                    if (u'0' <= self.input.LA(1) <= u'9') or (u'A' <= self.input.LA(1) <= u'Z') or self.input.LA(1) == u'_' or (u'a' <= self.input.LA(1) <= u'z'):
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



    # $ANTLR start NAME_INCLUDE
    def mNAME_INCLUDE(self, ):

        try:
            self.type = NAME_INCLUDE

            # XKBGrammar.g:128:2: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' )* )
            # XKBGrammar.g:128:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' )*
            if (u'A' <= self.input.LA(1) <= u'Z') or self.input.LA(1) == u'_' or (u'a' <= self.input.LA(1) <= u'z'):
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse


            # XKBGrammar.g:128:27: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '(' | ')' | '0' .. '9' )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((u'(' <= LA2_0 <= u')') or (u'0' <= LA2_0 <= u'9') or (u'A' <= LA2_0 <= u'Z') or LA2_0 == u'_' or (u'a' <= LA2_0 <= u'z')) :
                    alt2 = 1


                if alt2 == 1:
                    # XKBGrammar.g:
                    if (u'(' <= self.input.LA(1) <= u')') or (u'0' <= self.input.LA(1) <= u'9') or (u'A' <= self.input.LA(1) <= u'Z') or self.input.LA(1) == u'_' or (u'a' <= self.input.LA(1) <= u'z'):
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop2






        finally:

            pass

    # $ANTLR end NAME_INCLUDE



    # $ANTLR start NAME_KEYSYM
    def mNAME_KEYSYM(self, ):

        try:
            self.type = NAME_KEYSYM

            # XKBGrammar.g:132:2: ( ( '0' .. '9' | 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )* )
            # XKBGrammar.g:132:4: ( '0' .. '9' | 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )*
            if (u'0' <= self.input.LA(1) <= u'9') or (u'A' <= self.input.LA(1) <= u'Z') or (u'a' <= self.input.LA(1) <= u'z'):
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse


            # XKBGrammar.g:132:32: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((u'0' <= LA3_0 <= u'9') or (u'A' <= LA3_0 <= u'Z') or LA3_0 == u'_' or (u'a' <= LA3_0 <= u'z')) :
                    alt3 = 1


                if alt3 == 1:
                    # XKBGrammar.g:
                    if (u'0' <= self.input.LA(1) <= u'9') or (u'A' <= self.input.LA(1) <= u'Z') or self.input.LA(1) == u'_' or (u'a' <= self.input.LA(1) <= u'z'):
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop3






        finally:

            pass

    # $ANTLR end NAME_KEYSYM



    # $ANTLR start NAME_GROUP
    def mNAME_GROUP(self, ):

        try:
            self.type = NAME_GROUP

            # XKBGrammar.g:136:2: ( ( '0' .. '9' | 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '-' | '.' | '0' .. '9' )* )
            # XKBGrammar.g:136:4: ( '0' .. '9' | 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '-' | '.' | '0' .. '9' )*
            if (u'0' <= self.input.LA(1) <= u'9') or (u'A' <= self.input.LA(1) <= u'Z') or (u'a' <= self.input.LA(1) <= u'z'):
                self.input.consume();

            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse


            # XKBGrammar.g:136:32: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '-' | '.' | '0' .. '9' )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((u'-' <= LA4_0 <= u'.') or (u'0' <= LA4_0 <= u'9') or (u'A' <= LA4_0 <= u'Z') or LA4_0 == u'_' or (u'a' <= LA4_0 <= u'z')) :
                    alt4 = 1


                if alt4 == 1:
                    # XKBGrammar.g:
                    if (u'-' <= self.input.LA(1) <= u'.') or (u'0' <= self.input.LA(1) <= u'9') or (u'A' <= self.input.LA(1) <= u'Z') or self.input.LA(1) == u'_' or (u'a' <= self.input.LA(1) <= u'z'):
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop4






        finally:

            pass

    # $ANTLR end NAME_GROUP



    # $ANTLR start COMMENT
    def mCOMMENT(self, ):

        try:
            self.type = COMMENT

            # XKBGrammar.g:139:9: ( '//' (~ ( '\\n' | '\\r' ) )* )
            # XKBGrammar.g:139:11: '//' (~ ( '\\n' | '\\r' ) )*
            self.match("//")


            # XKBGrammar.g:139:16: (~ ( '\\n' | '\\r' ) )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((u'\u0000' <= LA5_0 <= u'\t') or (u'\u000B' <= LA5_0 <= u'\f') or (u'\u000E' <= LA5_0 <= u'\uFFFE')) :
                    alt5 = 1


                if alt5 == 1:
                    # XKBGrammar.g:139:17: ~ ( '\\n' | '\\r' )
                    if (u'\u0000' <= self.input.LA(1) <= u'\t') or (u'\u000B' <= self.input.LA(1) <= u'\f') or (u'\u000E' <= self.input.LA(1) <= u'\uFFFE'):
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop5


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

            # XKBGrammar.g:143:9: ( ( '\\t' | ' ' | NEWLINE )+ )
            # XKBGrammar.g:143:17: ( '\\t' | ' ' | NEWLINE )+
            # XKBGrammar.g:143:17: ( '\\t' | ' ' | NEWLINE )+
            cnt6 = 0
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((u'\t' <= LA6_0 <= u'\n') or LA6_0 == u'\r' or LA6_0 == u' ') :
                    alt6 = 1


                if alt6 == 1:
                    # XKBGrammar.g:
                    if (u'\t' <= self.input.LA(1) <= u'\n') or self.input.LA(1) == u'\r' or self.input.LA(1) == u' ':
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt6 >= 1:
                        break #loop6

                    eee = EarlyExitException(6, self.input)
                    raise eee

                cnt6 += 1


            #action start
            self.channel=HIDDEN; 
            #action end




        finally:

            pass

    # $ANTLR end WS



    # $ANTLR start NEWLINE
    def mNEWLINE(self, ):

        try:
            # XKBGrammar.g:148:9: ( '\\r' | '\\n' )
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
        # XKBGrammar.g:1:8: ( TOKEN_DEFAULT | TOKEN_HIDDEN | TOKEN_PARTIAL | TOKEN_ALPHANUMERIC_KEYS | TOKEN_MODIFIER_KEYS | TOKEN_ALTERNATE_GROUP | TOKEN_XKB_SYMBOLS | TOKEN_INCLUDE | TOKEN_KEY_TYPE | TOKEN_NAME | TOKEN_KEY | LBRACKET | RBRACKET | LCURLY | RCURLY | COMMA | DQUOTE | MINUS | PLUS | SEMICOLON | EQUAL | LOWERTHAN | GREATERTHAN | DOT | NAME | NAME_INCLUDE | NAME_KEYSYM | NAME_GROUP | COMMENT | WS )
        alt7 = 30
        alt7 = self.dfa7.predict(self.input)
        if alt7 == 1:
            # XKBGrammar.g:1:10: TOKEN_DEFAULT
            self.mTOKEN_DEFAULT()



        elif alt7 == 2:
            # XKBGrammar.g:1:24: TOKEN_HIDDEN
            self.mTOKEN_HIDDEN()



        elif alt7 == 3:
            # XKBGrammar.g:1:37: TOKEN_PARTIAL
            self.mTOKEN_PARTIAL()



        elif alt7 == 4:
            # XKBGrammar.g:1:51: TOKEN_ALPHANUMERIC_KEYS
            self.mTOKEN_ALPHANUMERIC_KEYS()



        elif alt7 == 5:
            # XKBGrammar.g:1:75: TOKEN_MODIFIER_KEYS
            self.mTOKEN_MODIFIER_KEYS()



        elif alt7 == 6:
            # XKBGrammar.g:1:95: TOKEN_ALTERNATE_GROUP
            self.mTOKEN_ALTERNATE_GROUP()



        elif alt7 == 7:
            # XKBGrammar.g:1:117: TOKEN_XKB_SYMBOLS
            self.mTOKEN_XKB_SYMBOLS()



        elif alt7 == 8:
            # XKBGrammar.g:1:135: TOKEN_INCLUDE
            self.mTOKEN_INCLUDE()



        elif alt7 == 9:
            # XKBGrammar.g:1:149: TOKEN_KEY_TYPE
            self.mTOKEN_KEY_TYPE()



        elif alt7 == 10:
            # XKBGrammar.g:1:164: TOKEN_NAME
            self.mTOKEN_NAME()



        elif alt7 == 11:
            # XKBGrammar.g:1:175: TOKEN_KEY
            self.mTOKEN_KEY()



        elif alt7 == 12:
            # XKBGrammar.g:1:185: LBRACKET
            self.mLBRACKET()



        elif alt7 == 13:
            # XKBGrammar.g:1:194: RBRACKET
            self.mRBRACKET()



        elif alt7 == 14:
            # XKBGrammar.g:1:203: LCURLY
            self.mLCURLY()



        elif alt7 == 15:
            # XKBGrammar.g:1:210: RCURLY
            self.mRCURLY()



        elif alt7 == 16:
            # XKBGrammar.g:1:217: COMMA
            self.mCOMMA()



        elif alt7 == 17:
            # XKBGrammar.g:1:223: DQUOTE
            self.mDQUOTE()



        elif alt7 == 18:
            # XKBGrammar.g:1:230: MINUS
            self.mMINUS()



        elif alt7 == 19:
            # XKBGrammar.g:1:236: PLUS
            self.mPLUS()



        elif alt7 == 20:
            # XKBGrammar.g:1:241: SEMICOLON
            self.mSEMICOLON()



        elif alt7 == 21:
            # XKBGrammar.g:1:251: EQUAL
            self.mEQUAL()



        elif alt7 == 22:
            # XKBGrammar.g:1:257: LOWERTHAN
            self.mLOWERTHAN()



        elif alt7 == 23:
            # XKBGrammar.g:1:267: GREATERTHAN
            self.mGREATERTHAN()



        elif alt7 == 24:
            # XKBGrammar.g:1:279: DOT
            self.mDOT()



        elif alt7 == 25:
            # XKBGrammar.g:1:283: NAME
            self.mNAME()



        elif alt7 == 26:
            # XKBGrammar.g:1:288: NAME_INCLUDE
            self.mNAME_INCLUDE()



        elif alt7 == 27:
            # XKBGrammar.g:1:301: NAME_KEYSYM
            self.mNAME_KEYSYM()



        elif alt7 == 28:
            # XKBGrammar.g:1:313: NAME_GROUP
            self.mNAME_GROUP()



        elif alt7 == 29:
            # XKBGrammar.g:1:324: COMMENT
            self.mCOMMENT()



        elif alt7 == 30:
            # XKBGrammar.g:1:332: WS
            self.mWS()








    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\1\uffff\11\36\15\uffff\2\36\1\53\2\uffff\2\36\3\uffff\11\36\1"
        u"\53\1\uffff\10\36\1\77\11\36\1\37\1\uffff\1\112\10\36\1\37\1\uffff"
        u"\1\36\1\125\6\36\1\37\1\135\1\uffff\1\136\4\36\1\143\1\37\2\uffff"
        u"\4\36\1\uffff\1\151\4\36\1\uffff\7\36\1\165\3\36\1\uffff\2\36\1"
        u"\173\2\36\1\uffff\1\36\1\177\1\36\1\uffff\1\u0081\1\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\u0082\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\1\11\11\50\15\uffff\2\50\1\55\2\uffff\2\50\3\uffff\11\50\1\55"
        u"\1\uffff\22\50\1\164\1\uffff\11\50\1\171\1\uffff\10\50\1\160\1"
        u"\50\1\uffff\6\50\1\145\2\uffff\4\50\1\uffff\1\55\4\50\1\uffff\13"
        u"\50\1\uffff\5\50\1\uffff\3\50\1\uffff\1\50\1\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\1\175\11\172\15\uffff\3\172\2\uffff\2\172\3\uffff\12\172\1\uffff"
        u"\22\172\1\164\1\uffff\11\172\1\171\1\uffff\10\172\1\160\1\172\1"
        u"\uffff\6\172\1\145\2\uffff\4\172\1\uffff\5\172\1\uffff\13\172\1"
        u"\uffff\5\172\1\uffff\3\172\1\uffff\1\172\1\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\12\uffff\1\14\1\15\1\16\1\17\1\20\1\21\1\22\1\23\1\24\1\25\1\26"
        u"\1\27\1\30\3\uffff\1\35\1\36\2\uffff\1\31\1\34\1\32\12\uffff\1"
        u"\33\23\uffff\1\13\12\uffff\1\12\12\uffff\1\2\7\uffff\1\1\1\3\4"
        u"\uffff\1\10\5\uffff\1\11\13\uffff\1\7\5\uffff\1\5\3\uffff\1\6\1"
        u"\uffff\1\4"
        )

    DFA7_special = DFA.unpack(
        u"\u0082\uffff"
        )

            
    DFA7_transition = [
        DFA.unpack(u"\2\33\2\uffff\1\33\22\uffff\1\33\1\uffff\1\17\10\uffff"
        u"\1\21\1\16\1\20\1\26\1\32\12\31\1\uffff\1\22\1\24\1\23\1\25\2\uffff"
        u"\32\27\1\12\1\uffff\1\13\1\uffff\1\30\1\uffff\1\4\2\27\1\1\3\27"
        u"\1\2\1\7\1\27\1\10\1\27\1\5\1\11\1\27\1\3\7\27\1\6\2\27\1\14\1"
        u"\uffff\1\15"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\4\35\1\34\25\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\10\35\1\41\21\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\1\42\31\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\13\35\1\43\16\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\16\35\1\44\13\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\12\35\1\45\17\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\15\35\1\46\14\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\4\35\1\47\25\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\1\50\31\35"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\32\35"),
        DFA.unpack(u"\2\40\6\uffff\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff"
        u"\32\51"),
        DFA.unpack(u"\2\37\1\uffff\12\52\7\uffff\32\52\4\uffff\1\52\1\uffff"
        u"\32\52"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\5\35\1\54\24\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\32\35"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\3\35\1\55\26\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\21\35\1\56\10\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\17\35\1\57\3\35\1\60\6\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\3\35\1\61\26\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\1\35\1\62\30\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\2\35\1\63\27\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\30\35\1\64\1\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\14\35\1\65\15\35"),
        DFA.unpack(u"\2\40\6\uffff\12\51\7\uffff\32\51\4\uffff\1\51\1\uffff"
        u"\32\51"),
        DFA.unpack(u"\2\37\1\uffff\12\52\7\uffff\32\52\4\uffff\1\52\1\uffff"
        u"\32\52"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\1\66\31\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\3\35\1\67\26\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\23\35\1\70\6\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\7\35\1\71\22\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\4\35\1\72\25\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\10\35\1\73\21\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\74\1\uffff\32\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\13\35\1\75\16\35"),
        DFA.unpack(u"\2\40\3\uffff\1\37\1\76\1\uffff\12\35\7\uffff\32\35"
        u"\4\uffff\1\35\1\uffff\32\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\4\35\1\100\25\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\24\35\1\101\5\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\4\35\1\102\25\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\10\35\1\103\21\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\1\104\31\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\21\35\1\105\10\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\5\35\1\106\24\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\22\35\1\107\7\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\24\35\1\110\5\35"),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\32\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\13\35\1\113\16\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\15\35\1\114\14\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\1\115\31\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\15\35\1\116\14\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\15\35\1\117\14\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\10\35\1\120\21\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\30\35\1\121\1\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\3\35\1\122\26\35"),
        DFA.unpack(u"\1\123"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\23\35\1\124\6\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\32\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\13\35\1\126\16\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\24\35\1\127\5\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\1\130\31\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\4\35\1\131\25\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\14\35\1\132\15\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\4\35\1\133\25\35"),
        DFA.unpack(u"\1\134"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\32\35"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\32\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\14\35\1\137\15\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\23\35\1\140\6\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\21\35\1\141\10\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\1\35\1\142\30\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\32\35"),
        DFA.unpack(u"\1\144"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\4\35\1\145\25\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\4\35\1\146\25\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\147\1\uffff\32\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\16\35\1\150\13\35"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\37\1\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\21\35\1\152\10\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\153\1\uffff\32\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\12\35\1\154\17\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\13\35\1\155\16\35"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\10\35\1\156\21\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\6\35\1\157\23\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\4\35\1\160\25\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\22\35\1\161\7\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\2\35\1\162\27\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\21\35\1\163\10\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\30\35\1\164\1\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\32\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\166\1\uffff\32\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\16\35\1\167\13\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\22\35\1\170\7\35"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\12\35\1\171\17\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\24\35\1\172\5\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\32\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\4\35\1\174\25\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\17\35\1\175\12\35"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\30\35\1\176\1\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\32\35"),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\22\35\1\u0080\7\35"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\40\3\uffff\2\37\1\uffff\12\35\7\uffff\32\35\4\uffff"
        u"\1\35\1\uffff\32\35"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #7

    DFA7 = DFA
 

