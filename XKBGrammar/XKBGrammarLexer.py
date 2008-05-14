# $ANTLR 3.0.1 XKBGrammar.g 2008-05-14 21:55:39

from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
ATTRIBUTES=17
TOKEN_INCLUDE=11
ATTRIBUTE=18
TOKEN_XKB_SYMBOLS=10
EOF=-1
SECTIONNAME=24
MAPTYPE=15
TOKEN_PARTIAL=6
NAME=27
MAPMATERIAL=16
INCLUDE=19
T38=38
KEYSYMS=26
T37=37
T39=39
COMMENT=29
T34=34
TOKEN_DEFAULT=4
T33=33
T36=36
T35=35
T32=32
T31=31
QUOTEDSTRING=25
TOKEN_ALTERNATE_GROUP=9
SECTION=23
LINE_COMMENT=30
KEYCODE=22
KEY=20
KEYTYPE=21
TOKEN_NAME=13
T49=49
T48=48
T43=43
Tokens=51
T42=42
T41=41
T40=40
T47=47
T46=46
T45=45
T44=44
WS=28
TOKEN_ALPHANUMERIC_KEYS=7
TOKEN_HIDDEN=5
T50=50
TOKEN_MODIFIER_KEYS=8
TOKEN_KEY=14
TOKEN_KEY_TYPE=12

class XKBGrammarLexer(Lexer):

    grammarFileName = "XKBGrammar.g"

    def __init__(self, input=None):
        Lexer.__init__(self, input)





    # $ANTLR start T31
    def mT31(self, ):

        try:
            self.type = T31

            # XKBGrammar.g:7:5: ( '\"' )
            # XKBGrammar.g:7:7: '\"'
            self.match(u'"')





        finally:

            pass

    # $ANTLR end T31



    # $ANTLR start T32
    def mT32(self, ):

        try:
            self.type = T32

            # XKBGrammar.g:8:5: ( '{' )
            # XKBGrammar.g:8:7: '{'
            self.match(u'{')





        finally:

            pass

    # $ANTLR end T32



    # $ANTLR start T33
    def mT33(self, ):

        try:
            self.type = T33

            # XKBGrammar.g:9:5: ( ';' )
            # XKBGrammar.g:9:7: ';'
            self.match(u';')





        finally:

            pass

    # $ANTLR end T33



    # $ANTLR start T34
    def mT34(self, ):

        try:
            self.type = T34

            # XKBGrammar.g:10:5: ( '}' )
            # XKBGrammar.g:10:7: '}'
            self.match(u'}')





        finally:

            pass

    # $ANTLR end T34



    # $ANTLR start T35
    def mT35(self, ):

        try:
            self.type = T35

            # XKBGrammar.g:11:5: ( 'include' )
            # XKBGrammar.g:11:7: 'include'
            self.match("include")






        finally:

            pass

    # $ANTLR end T35



    # $ANTLR start T36
    def mT36(self, ):

        try:
            self.type = T36

            # XKBGrammar.g:12:5: ( 'name' )
            # XKBGrammar.g:12:7: 'name'
            self.match("name")






        finally:

            pass

    # $ANTLR end T36



    # $ANTLR start T37
    def mT37(self, ):

        try:
            self.type = T37

            # XKBGrammar.g:13:5: ( '[' )
            # XKBGrammar.g:13:7: '['
            self.match(u'[')





        finally:

            pass

    # $ANTLR end T37



    # $ANTLR start T38
    def mT38(self, ):

        try:
            self.type = T38

            # XKBGrammar.g:14:5: ( ']' )
            # XKBGrammar.g:14:7: ']'
            self.match(u']')





        finally:

            pass

    # $ANTLR end T38



    # $ANTLR start T39
    def mT39(self, ):

        try:
            self.type = T39

            # XKBGrammar.g:15:5: ( '=' )
            # XKBGrammar.g:15:7: '='
            self.match(u'=')





        finally:

            pass

    # $ANTLR end T39



    # $ANTLR start T40
    def mT40(self, ):

        try:
            self.type = T40

            # XKBGrammar.g:16:5: ( 'key.type' )
            # XKBGrammar.g:16:7: 'key.type'
            self.match("key.type")






        finally:

            pass

    # $ANTLR end T40



    # $ANTLR start T41
    def mT41(self, ):

        try:
            self.type = T41

            # XKBGrammar.g:17:5: ( 'key' )
            # XKBGrammar.g:17:7: 'key'
            self.match("key")






        finally:

            pass

    # $ANTLR end T41



    # $ANTLR start T42
    def mT42(self, ):

        try:
            self.type = T42

            # XKBGrammar.g:18:5: ( '<' )
            # XKBGrammar.g:18:7: '<'
            self.match(u'<')





        finally:

            pass

    # $ANTLR end T42



    # $ANTLR start T43
    def mT43(self, ):

        try:
            self.type = T43

            # XKBGrammar.g:19:5: ( '>' )
            # XKBGrammar.g:19:7: '>'
            self.match(u'>')





        finally:

            pass

    # $ANTLR end T43



    # $ANTLR start T44
    def mT44(self, ):

        try:
            self.type = T44

            # XKBGrammar.g:20:5: ( ',' )
            # XKBGrammar.g:20:7: ','
            self.match(u',')





        finally:

            pass

    # $ANTLR end T44



    # $ANTLR start T45
    def mT45(self, ):

        try:
            self.type = T45

            # XKBGrammar.g:21:5: ( 'default' )
            # XKBGrammar.g:21:7: 'default'
            self.match("default")






        finally:

            pass

    # $ANTLR end T45



    # $ANTLR start T46
    def mT46(self, ):

        try:
            self.type = T46

            # XKBGrammar.g:22:5: ( 'hidden' )
            # XKBGrammar.g:22:7: 'hidden'
            self.match("hidden")






        finally:

            pass

    # $ANTLR end T46



    # $ANTLR start T47
    def mT47(self, ):

        try:
            self.type = T47

            # XKBGrammar.g:23:5: ( 'partial' )
            # XKBGrammar.g:23:7: 'partial'
            self.match("partial")






        finally:

            pass

    # $ANTLR end T47



    # $ANTLR start T48
    def mT48(self, ):

        try:
            self.type = T48

            # XKBGrammar.g:24:5: ( 'alphanumeric_keys' )
            # XKBGrammar.g:24:7: 'alphanumeric_keys'
            self.match("alphanumeric_keys")






        finally:

            pass

    # $ANTLR end T48



    # $ANTLR start T49
    def mT49(self, ):

        try:
            self.type = T49

            # XKBGrammar.g:25:5: ( 'alternate_group' )
            # XKBGrammar.g:25:7: 'alternate_group'
            self.match("alternate_group")






        finally:

            pass

    # $ANTLR end T49



    # $ANTLR start T50
    def mT50(self, ):

        try:
            self.type = T50

            # XKBGrammar.g:26:5: ( 'xkb_symbols' )
            # XKBGrammar.g:26:7: 'xkb_symbols'
            self.match("xkb_symbols")






        finally:

            pass

    # $ANTLR end T50



    # $ANTLR start NAME
    def mNAME(self, ):

        try:
            self.type = NAME

            # XKBGrammar.g:124:2: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '-' | '(' | ')' | '0' .. '9' )* )
            # XKBGrammar.g:124:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '-' | '(' | ')' | '0' .. '9' )*
            # XKBGrammar.g:124:4: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '-' | '(' | ')' | '0' .. '9' )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((u'(' <= LA1_0 <= u')') or LA1_0 == u'-' or (u'0' <= LA1_0 <= u'9') or (u'A' <= LA1_0 <= u'Z') or LA1_0 == u'_' or (u'a' <= LA1_0 <= u'z')) :
                    alt1 = 1


                if alt1 == 1:
                    # XKBGrammar.g:
                    if (u'(' <= self.input.LA(1) <= u')') or self.input.LA(1) == u'-' or (u'0' <= self.input.LA(1) <= u'9') or (u'A' <= self.input.LA(1) <= u'Z') or self.input.LA(1) == u'_' or (u'a' <= self.input.LA(1) <= u'z'):
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

            # XKBGrammar.g:129:2: ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )
            # XKBGrammar.g:130:2: ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
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

            # XKBGrammar.g:135:6: ( '/*' ( . )* '*/' )
            # XKBGrammar.g:136:2: '/*' ( . )* '*/'
            self.match("/*")


            # XKBGrammar.g:136:7: ( . )*
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
                    # XKBGrammar.g:136:7: .
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

            # XKBGrammar.g:140:6: ( '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # XKBGrammar.g:141:2: '//' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            self.match("//")


            # XKBGrammar.g:141:7: (~ ( '\\n' | '\\r' ) )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((u'\u0000' <= LA3_0 <= u'\t') or (u'\u000B' <= LA3_0 <= u'\f') or (u'\u000E' <= LA3_0 <= u'\uFFFE')) :
                    alt3 = 1


                if alt3 == 1:
                    # XKBGrammar.g:141:7: ~ ( '\\n' | '\\r' )
                    if (u'\u0000' <= self.input.LA(1) <= u'\t') or (u'\u000B' <= self.input.LA(1) <= u'\f') or (u'\u000E' <= self.input.LA(1) <= u'\uFFFE'):
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop3


            # XKBGrammar.g:141:23: ( '\\r' )?
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == u'\r') :
                alt4 = 1
            if alt4 == 1:
                # XKBGrammar.g:141:23: '\\r'
                self.match(u'\r')




            self.match(u'\n')

            #action start
            self.channel=HIDDEN; 
            #action end




        finally:

            pass

    # $ANTLR end LINE_COMMENT



    def mTokens(self):
        # XKBGrammar.g:1:8: ( T31 | T32 | T33 | T34 | T35 | T36 | T37 | T38 | T39 | T40 | T41 | T42 | T43 | T44 | T45 | T46 | T47 | T48 | T49 | T50 | NAME | WS | COMMENT | LINE_COMMENT )
        alt5 = 24
        LA5 = self.input.LA(1)
        if LA5 == u'"':
            alt5 = 1
        elif LA5 == u'{':
            alt5 = 2
        elif LA5 == u';':
            alt5 = 3
        elif LA5 == u'}':
            alt5 = 4
        elif LA5 == u'i':
            LA5_5 = self.input.LA(2)

            if (LA5_5 == u'n') :
                LA5_22 = self.input.LA(3)

                if (LA5_22 == u'c') :
                    LA5_32 = self.input.LA(4)

                    if (LA5_32 == u'l') :
                        LA5_41 = self.input.LA(5)

                        if (LA5_41 == u'u') :
                            LA5_51 = self.input.LA(6)

                            if (LA5_51 == u'd') :
                                LA5_59 = self.input.LA(7)

                                if (LA5_59 == u'e') :
                                    LA5_66 = self.input.LA(8)

                                    if ((u'(' <= LA5_66 <= u')') or LA5_66 == u'-' or (u'0' <= LA5_66 <= u'9') or (u'A' <= LA5_66 <= u'Z') or LA5_66 == u'_' or (u'a' <= LA5_66 <= u'z')) :
                                        alt5 = 21
                                    else:
                                        alt5 = 5
                                else:
                                    alt5 = 21
                            else:
                                alt5 = 21
                        else:
                            alt5 = 21
                    else:
                        alt5 = 21
                else:
                    alt5 = 21
            else:
                alt5 = 21
        elif LA5 == u'n':
            LA5_6 = self.input.LA(2)

            if (LA5_6 == u'a') :
                LA5_23 = self.input.LA(3)

                if (LA5_23 == u'm') :
                    LA5_33 = self.input.LA(4)

                    if (LA5_33 == u'e') :
                        LA5_42 = self.input.LA(5)

                        if ((u'(' <= LA5_42 <= u')') or LA5_42 == u'-' or (u'0' <= LA5_42 <= u'9') or (u'A' <= LA5_42 <= u'Z') or LA5_42 == u'_' or (u'a' <= LA5_42 <= u'z')) :
                            alt5 = 21
                        else:
                            alt5 = 6
                    else:
                        alt5 = 21
                else:
                    alt5 = 21
            else:
                alt5 = 21
        elif LA5 == u'[':
            alt5 = 7
        elif LA5 == u']':
            alt5 = 8
        elif LA5 == u'=':
            alt5 = 9
        elif LA5 == u'k':
            LA5_10 = self.input.LA(2)

            if (LA5_10 == u'e') :
                LA5_24 = self.input.LA(3)

                if (LA5_24 == u'y') :
                    LA5 = self.input.LA(4)
                    if LA5 == u'.':
                        alt5 = 10
                    elif LA5 == u'(' or LA5 == u')' or LA5 == u'-' or LA5 == u'0' or LA5 == u'1' or LA5 == u'2' or LA5 == u'3' or LA5 == u'4' or LA5 == u'5' or LA5 == u'6' or LA5 == u'7' or LA5 == u'8' or LA5 == u'9' or LA5 == u'A' or LA5 == u'B' or LA5 == u'C' or LA5 == u'D' or LA5 == u'E' or LA5 == u'F' or LA5 == u'G' or LA5 == u'H' or LA5 == u'I' or LA5 == u'J' or LA5 == u'K' or LA5 == u'L' or LA5 == u'M' or LA5 == u'N' or LA5 == u'O' or LA5 == u'P' or LA5 == u'Q' or LA5 == u'R' or LA5 == u'S' or LA5 == u'T' or LA5 == u'U' or LA5 == u'V' or LA5 == u'W' or LA5 == u'X' or LA5 == u'Y' or LA5 == u'Z' or LA5 == u'_' or LA5 == u'a' or LA5 == u'b' or LA5 == u'c' or LA5 == u'd' or LA5 == u'e' or LA5 == u'f' or LA5 == u'g' or LA5 == u'h' or LA5 == u'i' or LA5 == u'j' or LA5 == u'k' or LA5 == u'l' or LA5 == u'm' or LA5 == u'n' or LA5 == u'o' or LA5 == u'p' or LA5 == u'q' or LA5 == u'r' or LA5 == u's' or LA5 == u't' or LA5 == u'u' or LA5 == u'v' or LA5 == u'w' or LA5 == u'x' or LA5 == u'y' or LA5 == u'z':
                        alt5 = 21
                    else:
                        alt5 = 11
                else:
                    alt5 = 21
            else:
                alt5 = 21
        elif LA5 == u'<':
            alt5 = 12
        elif LA5 == u'>':
            alt5 = 13
        elif LA5 == u',':
            alt5 = 14
        elif LA5 == u'd':
            LA5_14 = self.input.LA(2)

            if (LA5_14 == u'e') :
                LA5_25 = self.input.LA(3)

                if (LA5_25 == u'f') :
                    LA5_35 = self.input.LA(4)

                    if (LA5_35 == u'a') :
                        LA5_45 = self.input.LA(5)

                        if (LA5_45 == u'u') :
                            LA5_53 = self.input.LA(6)

                            if (LA5_53 == u'l') :
                                LA5_60 = self.input.LA(7)

                                if (LA5_60 == u't') :
                                    LA5_67 = self.input.LA(8)

                                    if ((u'(' <= LA5_67 <= u')') or LA5_67 == u'-' or (u'0' <= LA5_67 <= u'9') or (u'A' <= LA5_67 <= u'Z') or LA5_67 == u'_' or (u'a' <= LA5_67 <= u'z')) :
                                        alt5 = 21
                                    else:
                                        alt5 = 15
                                else:
                                    alt5 = 21
                            else:
                                alt5 = 21
                        else:
                            alt5 = 21
                    else:
                        alt5 = 21
                else:
                    alt5 = 21
            else:
                alt5 = 21
        elif LA5 == u'h':
            LA5_15 = self.input.LA(2)

            if (LA5_15 == u'i') :
                LA5_26 = self.input.LA(3)

                if (LA5_26 == u'd') :
                    LA5_36 = self.input.LA(4)

                    if (LA5_36 == u'd') :
                        LA5_46 = self.input.LA(5)

                        if (LA5_46 == u'e') :
                            LA5_54 = self.input.LA(6)

                            if (LA5_54 == u'n') :
                                LA5_61 = self.input.LA(7)

                                if ((u'(' <= LA5_61 <= u')') or LA5_61 == u'-' or (u'0' <= LA5_61 <= u'9') or (u'A' <= LA5_61 <= u'Z') or LA5_61 == u'_' or (u'a' <= LA5_61 <= u'z')) :
                                    alt5 = 21
                                else:
                                    alt5 = 16
                            else:
                                alt5 = 21
                        else:
                            alt5 = 21
                    else:
                        alt5 = 21
                else:
                    alt5 = 21
            else:
                alt5 = 21
        elif LA5 == u'p':
            LA5_16 = self.input.LA(2)

            if (LA5_16 == u'a') :
                LA5_27 = self.input.LA(3)

                if (LA5_27 == u'r') :
                    LA5_37 = self.input.LA(4)

                    if (LA5_37 == u't') :
                        LA5_47 = self.input.LA(5)

                        if (LA5_47 == u'i') :
                            LA5_55 = self.input.LA(6)

                            if (LA5_55 == u'a') :
                                LA5_62 = self.input.LA(7)

                                if (LA5_62 == u'l') :
                                    LA5_69 = self.input.LA(8)

                                    if ((u'(' <= LA5_69 <= u')') or LA5_69 == u'-' or (u'0' <= LA5_69 <= u'9') or (u'A' <= LA5_69 <= u'Z') or LA5_69 == u'_' or (u'a' <= LA5_69 <= u'z')) :
                                        alt5 = 21
                                    else:
                                        alt5 = 17
                                else:
                                    alt5 = 21
                            else:
                                alt5 = 21
                        else:
                            alt5 = 21
                    else:
                        alt5 = 21
                else:
                    alt5 = 21
            else:
                alt5 = 21
        elif LA5 == u'a':
            LA5_17 = self.input.LA(2)

            if (LA5_17 == u'l') :
                LA5 = self.input.LA(3)
                if LA5 == u'p':
                    LA5_38 = self.input.LA(4)

                    if (LA5_38 == u'h') :
                        LA5_48 = self.input.LA(5)

                        if (LA5_48 == u'a') :
                            LA5_56 = self.input.LA(6)

                            if (LA5_56 == u'n') :
                                LA5_63 = self.input.LA(7)

                                if (LA5_63 == u'u') :
                                    LA5_70 = self.input.LA(8)

                                    if (LA5_70 == u'm') :
                                        LA5_76 = self.input.LA(9)

                                        if (LA5_76 == u'e') :
                                            LA5_79 = self.input.LA(10)

                                            if (LA5_79 == u'r') :
                                                LA5_82 = self.input.LA(11)

                                                if (LA5_82 == u'i') :
                                                    LA5_85 = self.input.LA(12)

                                                    if (LA5_85 == u'c') :
                                                        LA5_88 = self.input.LA(13)

                                                        if (LA5_88 == u'_') :
                                                            LA5_91 = self.input.LA(14)

                                                            if (LA5_91 == u'k') :
                                                                LA5_93 = self.input.LA(15)

                                                                if (LA5_93 == u'e') :
                                                                    LA5_95 = self.input.LA(16)

                                                                    if (LA5_95 == u'y') :
                                                                        LA5_97 = self.input.LA(17)

                                                                        if (LA5_97 == u's') :
                                                                            LA5_99 = self.input.LA(18)

                                                                            if ((u'(' <= LA5_99 <= u')') or LA5_99 == u'-' or (u'0' <= LA5_99 <= u'9') or (u'A' <= LA5_99 <= u'Z') or LA5_99 == u'_' or (u'a' <= LA5_99 <= u'z')) :
                                                                                alt5 = 21
                                                                            else:
                                                                                alt5 = 18
                                                                        else:
                                                                            alt5 = 21
                                                                    else:
                                                                        alt5 = 21
                                                                else:
                                                                    alt5 = 21
                                                            else:
                                                                alt5 = 21
                                                        else:
                                                            alt5 = 21
                                                    else:
                                                        alt5 = 21
                                                else:
                                                    alt5 = 21
                                            else:
                                                alt5 = 21
                                        else:
                                            alt5 = 21
                                    else:
                                        alt5 = 21
                                else:
                                    alt5 = 21
                            else:
                                alt5 = 21
                        else:
                            alt5 = 21
                    else:
                        alt5 = 21
                elif LA5 == u't':
                    LA5_39 = self.input.LA(4)

                    if (LA5_39 == u'e') :
                        LA5_49 = self.input.LA(5)

                        if (LA5_49 == u'r') :
                            LA5_57 = self.input.LA(6)

                            if (LA5_57 == u'n') :
                                LA5_64 = self.input.LA(7)

                                if (LA5_64 == u'a') :
                                    LA5_71 = self.input.LA(8)

                                    if (LA5_71 == u't') :
                                        LA5_77 = self.input.LA(9)

                                        if (LA5_77 == u'e') :
                                            LA5_80 = self.input.LA(10)

                                            if (LA5_80 == u'_') :
                                                LA5_83 = self.input.LA(11)

                                                if (LA5_83 == u'g') :
                                                    LA5_86 = self.input.LA(12)

                                                    if (LA5_86 == u'r') :
                                                        LA5_89 = self.input.LA(13)

                                                        if (LA5_89 == u'o') :
                                                            LA5_92 = self.input.LA(14)

                                                            if (LA5_92 == u'u') :
                                                                LA5_94 = self.input.LA(15)

                                                                if (LA5_94 == u'p') :
                                                                    LA5_96 = self.input.LA(16)

                                                                    if ((u'(' <= LA5_96 <= u')') or LA5_96 == u'-' or (u'0' <= LA5_96 <= u'9') or (u'A' <= LA5_96 <= u'Z') or LA5_96 == u'_' or (u'a' <= LA5_96 <= u'z')) :
                                                                        alt5 = 21
                                                                    else:
                                                                        alt5 = 19
                                                                else:
                                                                    alt5 = 21
                                                            else:
                                                                alt5 = 21
                                                        else:
                                                            alt5 = 21
                                                    else:
                                                        alt5 = 21
                                                else:
                                                    alt5 = 21
                                            else:
                                                alt5 = 21
                                        else:
                                            alt5 = 21
                                    else:
                                        alt5 = 21
                                else:
                                    alt5 = 21
                            else:
                                alt5 = 21
                        else:
                            alt5 = 21
                    else:
                        alt5 = 21
                else:
                    alt5 = 21
            else:
                alt5 = 21
        elif LA5 == u'x':
            LA5_18 = self.input.LA(2)

            if (LA5_18 == u'k') :
                LA5_29 = self.input.LA(3)

                if (LA5_29 == u'b') :
                    LA5_40 = self.input.LA(4)

                    if (LA5_40 == u'_') :
                        LA5_50 = self.input.LA(5)

                        if (LA5_50 == u's') :
                            LA5_58 = self.input.LA(6)

                            if (LA5_58 == u'y') :
                                LA5_65 = self.input.LA(7)

                                if (LA5_65 == u'm') :
                                    LA5_72 = self.input.LA(8)

                                    if (LA5_72 == u'b') :
                                        LA5_78 = self.input.LA(9)

                                        if (LA5_78 == u'o') :
                                            LA5_81 = self.input.LA(10)

                                            if (LA5_81 == u'l') :
                                                LA5_84 = self.input.LA(11)

                                                if (LA5_84 == u's') :
                                                    LA5_87 = self.input.LA(12)

                                                    if ((u'(' <= LA5_87 <= u')') or LA5_87 == u'-' or (u'0' <= LA5_87 <= u'9') or (u'A' <= LA5_87 <= u'Z') or LA5_87 == u'_' or (u'a' <= LA5_87 <= u'z')) :
                                                        alt5 = 21
                                                    else:
                                                        alt5 = 20
                                                else:
                                                    alt5 = 21
                                            else:
                                                alt5 = 21
                                        else:
                                            alt5 = 21
                                    else:
                                        alt5 = 21
                                else:
                                    alt5 = 21
                            else:
                                alt5 = 21
                        else:
                            alt5 = 21
                    else:
                        alt5 = 21
                else:
                    alt5 = 21
            else:
                alt5 = 21
        elif LA5 == u'\t' or LA5 == u'\n' or LA5 == u'\f' or LA5 == u'\r' or LA5 == u' ':
            alt5 = 22
        elif LA5 == u'/':
            LA5_21 = self.input.LA(2)

            if (LA5_21 == u'/') :
                alt5 = 24
            elif (LA5_21 == u'*') :
                alt5 = 23
            else:
                nvae = NoViableAltException("1:1: Tokens : ( T31 | T32 | T33 | T34 | T35 | T36 | T37 | T38 | T39 | T40 | T41 | T42 | T43 | T44 | T45 | T46 | T47 | T48 | T49 | T50 | NAME | WS | COMMENT | LINE_COMMENT );", 5, 21, self.input)

                raise nvae

        else:
            alt5 = 21
        if alt5 == 1:
            # XKBGrammar.g:1:10: T31
            self.mT31()



        elif alt5 == 2:
            # XKBGrammar.g:1:14: T32
            self.mT32()



        elif alt5 == 3:
            # XKBGrammar.g:1:18: T33
            self.mT33()



        elif alt5 == 4:
            # XKBGrammar.g:1:22: T34
            self.mT34()



        elif alt5 == 5:
            # XKBGrammar.g:1:26: T35
            self.mT35()



        elif alt5 == 6:
            # XKBGrammar.g:1:30: T36
            self.mT36()



        elif alt5 == 7:
            # XKBGrammar.g:1:34: T37
            self.mT37()



        elif alt5 == 8:
            # XKBGrammar.g:1:38: T38
            self.mT38()



        elif alt5 == 9:
            # XKBGrammar.g:1:42: T39
            self.mT39()



        elif alt5 == 10:
            # XKBGrammar.g:1:46: T40
            self.mT40()



        elif alt5 == 11:
            # XKBGrammar.g:1:50: T41
            self.mT41()



        elif alt5 == 12:
            # XKBGrammar.g:1:54: T42
            self.mT42()



        elif alt5 == 13:
            # XKBGrammar.g:1:58: T43
            self.mT43()



        elif alt5 == 14:
            # XKBGrammar.g:1:62: T44
            self.mT44()



        elif alt5 == 15:
            # XKBGrammar.g:1:66: T45
            self.mT45()



        elif alt5 == 16:
            # XKBGrammar.g:1:70: T46
            self.mT46()



        elif alt5 == 17:
            # XKBGrammar.g:1:74: T47
            self.mT47()



        elif alt5 == 18:
            # XKBGrammar.g:1:78: T48
            self.mT48()



        elif alt5 == 19:
            # XKBGrammar.g:1:82: T49
            self.mT49()



        elif alt5 == 20:
            # XKBGrammar.g:1:86: T50
            self.mT50()



        elif alt5 == 21:
            # XKBGrammar.g:1:90: NAME
            self.mNAME()



        elif alt5 == 22:
            # XKBGrammar.g:1:95: WS
            self.mWS()



        elif alt5 == 23:
            # XKBGrammar.g:1:98: COMMENT
            self.mCOMMENT()



        elif alt5 == 24:
            # XKBGrammar.g:1:106: LINE_COMMENT
            self.mLINE_COMMENT()








 

