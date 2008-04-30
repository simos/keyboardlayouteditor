# $ANTLR 3.0.1 XKBGrammar.g 2008-04-30 19:41:41

from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
TOKEN_ALTERNATE_GROUP=9
ATTRIBUTES=28
KEYCODE=30
TOKEN_INCLUDE=11
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
EOF=-1
NAME_KEYSYM=35
NAME_GROUP=37
LBRACKET=15
NAME=32
TOKEN_PARTIAL=6
WS=40
NEWLINE=39
TOKEN_ALPHANUMERIC_KEYS=7
TOKEN_HIDDEN=5
COMMA=19
LOWERTHAN=25
INCLUDE=31
EQUAL=24
RCURLY=18
TOKEN_MODIFIER_KEYS=8
PLUS=22
TOKEN_KEY=14
RBRACKET=16
COMMENT=38
DOT=27
TOKEN_DEFAULT=4
TOKEN_KEY_TYPE=12
GREATERTHAN=26

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "TOKEN_DEFAULT", "TOKEN_HIDDEN", "TOKEN_PARTIAL", "TOKEN_ALPHANUMERIC_KEYS", 
    "TOKEN_MODIFIER_KEYS", "TOKEN_ALTERNATE_GROUP", "TOKEN_XKB_SYMBOLS", 
    "TOKEN_INCLUDE", "TOKEN_KEY_TYPE", "TOKEN_NAME", "TOKEN_KEY", "LBRACKET", 
    "RBRACKET", "LCURLY", "RCURLY", "COMMA", "DQUOTE", "MINUS", "PLUS", 
    "SEMICOLON", "EQUAL", "LOWERTHAN", "GREATERTHAN", "DOT", "ATTRIBUTES", 
    "ATTRIBUTE", "KEYCODE", "INCLUDE", "NAME", "KEY", "KEYTYPE", "NAME_KEYSYM", 
    "NAME_INCLUDE", "NAME_GROUP", "COMMENT", "NEWLINE", "WS"
]



class XKBGrammarParser(Parser):
    grammarFileName = "XKBGrammar.g"
    tokenNames = tokenNames

    def __init__(self, input):
        Parser.__init__(self, input)



                
        self.adaptor = CommonTreeAdaptor()




    class layout_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start layout
    # XKBGrammar.g:53:1: layout : ( statement )* EOF ;
    def layout(self, ):

        retval = self.layout_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF2 = None
        statement1 = None


        EOF2_tree = None

        try:
            try:
                # XKBGrammar.g:53:9: ( ( statement )* EOF )
                # XKBGrammar.g:53:11: ( statement )* EOF
                root_0 = self.adaptor.nil()

                # XKBGrammar.g:53:11: ( statement )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((TOKEN_DEFAULT <= LA1_0 <= TOKEN_XKB_SYMBOLS)) :
                        alt1 = 1


                    if alt1 == 1:
                        # XKBGrammar.g:53:11: statement
                        self.following.append(self.FOLLOW_statement_in_layout336)
                        statement1 = self.statement()
                        self.following.pop()

                        self.adaptor.addChild(root_0, statement1.tree)


                    else:
                        break #loop1


                EOF2 = self.input.LT(1)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_layout339)




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end layout

    class statement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start statement
    # XKBGrammar.g:56:1: statement : preamble quotedstring LCURLY ( sectionmaterial )+ RCURLY SEMICOLON ;
    def statement(self, ):

        retval = self.statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LCURLY5 = None
        RCURLY7 = None
        SEMICOLON8 = None
        preamble3 = None

        quotedstring4 = None

        sectionmaterial6 = None


        LCURLY5_tree = None
        RCURLY7_tree = None
        SEMICOLON8_tree = None

        try:
            try:
                # XKBGrammar.g:57:2: ( preamble quotedstring LCURLY ( sectionmaterial )+ RCURLY SEMICOLON )
                # XKBGrammar.g:57:4: preamble quotedstring LCURLY ( sectionmaterial )+ RCURLY SEMICOLON
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_preamble_in_statement352)
                preamble3 = self.preamble()
                self.following.pop()

                self.adaptor.addChild(root_0, preamble3.tree)
                self.following.append(self.FOLLOW_quotedstring_in_statement354)
                quotedstring4 = self.quotedstring()
                self.following.pop()

                self.adaptor.addChild(root_0, quotedstring4.tree)
                LCURLY5 = self.input.LT(1)
                self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_statement356)


                LCURLY5_tree = self.adaptor.createWithPayload(LCURLY5)
                self.adaptor.addChild(root_0, LCURLY5_tree)

                # XKBGrammar.g:57:33: ( sectionmaterial )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((TOKEN_INCLUDE <= LA2_0 <= TOKEN_KEY)) :
                        alt2 = 1


                    if alt2 == 1:
                        # XKBGrammar.g:57:33: sectionmaterial
                        self.following.append(self.FOLLOW_sectionmaterial_in_statement358)
                        sectionmaterial6 = self.sectionmaterial()
                        self.following.pop()

                        self.adaptor.addChild(root_0, sectionmaterial6.tree)


                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1


                RCURLY7 = self.input.LT(1)
                self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_statement361)


                RCURLY7_tree = self.adaptor.createWithPayload(RCURLY7)
                self.adaptor.addChild(root_0, RCURLY7_tree)

                SEMICOLON8 = self.input.LT(1)
                self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_statement363)


                SEMICOLON8_tree = self.adaptor.createWithPayload(SEMICOLON8)
                self.adaptor.addChild(root_0, SEMICOLON8_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end statement

    class preamble_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start preamble
    # XKBGrammar.g:60:1: preamble : ( attribute_xkb )+ ;
    def preamble(self, ):

        retval = self.preamble_return()
        retval.start = self.input.LT(1)

        root_0 = None

        attribute_xkb9 = None



        try:
            try:
                # XKBGrammar.g:60:9: ( ( attribute_xkb )+ )
                # XKBGrammar.g:60:11: ( attribute_xkb )+
                root_0 = self.adaptor.nil()

                # XKBGrammar.g:60:11: ( attribute_xkb )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((TOKEN_DEFAULT <= LA3_0 <= TOKEN_XKB_SYMBOLS)) :
                        alt3 = 1


                    if alt3 == 1:
                        # XKBGrammar.g:60:11: attribute_xkb
                        self.following.append(self.FOLLOW_attribute_xkb_in_preamble373)
                        attribute_xkb9 = self.attribute_xkb()
                        self.following.pop()

                        self.adaptor.addChild(root_0, attribute_xkb9.tree)


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1





                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end preamble

    class quotedstring_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start quotedstring
    # XKBGrammar.g:62:1: quotedstring : DQUOTE (~ ( DQUOTE ) )+ DQUOTE ;
    def quotedstring(self, ):

        retval = self.quotedstring_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DQUOTE10 = None
        set11 = None
        DQUOTE12 = None

        DQUOTE10_tree = None
        set11_tree = None
        DQUOTE12_tree = None

        try:
            try:
                # XKBGrammar.g:63:2: ( DQUOTE (~ ( DQUOTE ) )+ DQUOTE )
                # XKBGrammar.g:63:4: DQUOTE (~ ( DQUOTE ) )+ DQUOTE
                root_0 = self.adaptor.nil()

                DQUOTE10 = self.input.LT(1)
                self.match(self.input, DQUOTE, self.FOLLOW_DQUOTE_in_quotedstring383)


                DQUOTE10_tree = self.adaptor.createWithPayload(DQUOTE10)
                self.adaptor.addChild(root_0, DQUOTE10_tree)

                # XKBGrammar.g:63:11: (~ ( DQUOTE ) )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if ((TOKEN_DEFAULT <= LA4_0 <= COMMA) or (MINUS <= LA4_0 <= WS)) :
                        alt4 = 1


                    if alt4 == 1:
                        # XKBGrammar.g:63:11: ~ ( DQUOTE )
                        set11 = self.input.LT(1)
                        if (TOKEN_DEFAULT <= self.input.LA(1) <= COMMA) or (MINUS <= self.input.LA(1) <= WS):
                            self.input.consume();
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set11))
                            self.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_quotedstring385
                                )
                            raise mse




                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1


                DQUOTE12 = self.input.LT(1)
                self.match(self.input, DQUOTE, self.FOLLOW_DQUOTE_in_quotedstring391)


                DQUOTE12_tree = self.adaptor.createWithPayload(DQUOTE12)
                self.adaptor.addChild(root_0, DQUOTE12_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end quotedstring

    class sectionmaterial_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start sectionmaterial
    # XKBGrammar.g:66:1: sectionmaterial : ( line_include | line_name | line_keytype | line_key );
    def sectionmaterial(self, ):

        retval = self.sectionmaterial_return()
        retval.start = self.input.LT(1)

        root_0 = None

        line_include13 = None

        line_name14 = None

        line_keytype15 = None

        line_key16 = None



        try:
            try:
                # XKBGrammar.g:67:2: ( line_include | line_name | line_keytype | line_key )
                alt5 = 4
                LA5 = self.input.LA(1)
                if LA5 == TOKEN_INCLUDE:
                    alt5 = 1
                elif LA5 == TOKEN_NAME:
                    alt5 = 2
                elif LA5 == TOKEN_KEY_TYPE:
                    alt5 = 3
                elif LA5 == TOKEN_KEY:
                    alt5 = 4
                else:
                    nvae = NoViableAltException("66:1: sectionmaterial : ( line_include | line_name | line_keytype | line_key );", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # XKBGrammar.g:67:4: line_include
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_line_include_in_sectionmaterial402)
                    line_include13 = self.line_include()
                    self.following.pop()

                    self.adaptor.addChild(root_0, line_include13.tree)


                elif alt5 == 2:
                    # XKBGrammar.g:68:4: line_name
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_line_name_in_sectionmaterial408)
                    line_name14 = self.line_name()
                    self.following.pop()

                    self.adaptor.addChild(root_0, line_name14.tree)


                elif alt5 == 3:
                    # XKBGrammar.g:69:4: line_keytype
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_line_keytype_in_sectionmaterial414)
                    line_keytype15 = self.line_keytype()
                    self.following.pop()

                    self.adaptor.addChild(root_0, line_keytype15.tree)


                elif alt5 == 4:
                    # XKBGrammar.g:70:4: line_key
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_line_key_in_sectionmaterial420)
                    line_key16 = self.line_key()
                    self.following.pop()

                    self.adaptor.addChild(root_0, line_key16.tree)


                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end sectionmaterial

    class line_include_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start line_include
    # XKBGrammar.g:76:1: line_include : TOKEN_INCLUDE quotedstring ;
    def line_include(self, ):

        retval = self.line_include_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TOKEN_INCLUDE17 = None
        quotedstring18 = None


        TOKEN_INCLUDE17_tree = None

        try:
            try:
                # XKBGrammar.g:78:2: ( TOKEN_INCLUDE quotedstring )
                # XKBGrammar.g:78:4: TOKEN_INCLUDE quotedstring
                root_0 = self.adaptor.nil()

                TOKEN_INCLUDE17 = self.input.LT(1)
                self.match(self.input, TOKEN_INCLUDE, self.FOLLOW_TOKEN_INCLUDE_in_line_include437)


                TOKEN_INCLUDE17_tree = self.adaptor.createWithPayload(TOKEN_INCLUDE17)
                self.adaptor.addChild(root_0, TOKEN_INCLUDE17_tree)

                self.following.append(self.FOLLOW_quotedstring_in_line_include439)
                quotedstring18 = self.quotedstring()
                self.following.pop()

                self.adaptor.addChild(root_0, quotedstring18.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end line_include

    class line_name_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start line_name
    # XKBGrammar.g:81:1: line_name : TOKEN_NAME LBRACKET name= NAME RBRACKET EQUAL quotedstring SEMICOLON ;
    def line_name(self, ):

        retval = self.line_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        name = None
        TOKEN_NAME19 = None
        LBRACKET20 = None
        RBRACKET21 = None
        EQUAL22 = None
        SEMICOLON24 = None
        quotedstring23 = None


        name_tree = None
        TOKEN_NAME19_tree = None
        LBRACKET20_tree = None
        RBRACKET21_tree = None
        EQUAL22_tree = None
        SEMICOLON24_tree = None

        try:
            try:
                # XKBGrammar.g:82:2: ( TOKEN_NAME LBRACKET name= NAME RBRACKET EQUAL quotedstring SEMICOLON )
                # XKBGrammar.g:82:4: TOKEN_NAME LBRACKET name= NAME RBRACKET EQUAL quotedstring SEMICOLON
                root_0 = self.adaptor.nil()

                TOKEN_NAME19 = self.input.LT(1)
                self.match(self.input, TOKEN_NAME, self.FOLLOW_TOKEN_NAME_in_line_name450)


                TOKEN_NAME19_tree = self.adaptor.createWithPayload(TOKEN_NAME19)
                self.adaptor.addChild(root_0, TOKEN_NAME19_tree)

                LBRACKET20 = self.input.LT(1)
                self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_line_name452)


                LBRACKET20_tree = self.adaptor.createWithPayload(LBRACKET20)
                self.adaptor.addChild(root_0, LBRACKET20_tree)

                name = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_name456)


                name_tree = self.adaptor.createWithPayload(name)
                self.adaptor.addChild(root_0, name_tree)

                RBRACKET21 = self.input.LT(1)
                self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_line_name458)


                RBRACKET21_tree = self.adaptor.createWithPayload(RBRACKET21)
                self.adaptor.addChild(root_0, RBRACKET21_tree)

                EQUAL22 = self.input.LT(1)
                self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_line_name460)


                EQUAL22_tree = self.adaptor.createWithPayload(EQUAL22)
                self.adaptor.addChild(root_0, EQUAL22_tree)

                self.following.append(self.FOLLOW_quotedstring_in_line_name462)
                quotedstring23 = self.quotedstring()
                self.following.pop()

                self.adaptor.addChild(root_0, quotedstring23.tree)
                SEMICOLON24 = self.input.LT(1)
                self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_line_name464)


                SEMICOLON24_tree = self.adaptor.createWithPayload(SEMICOLON24)
                self.adaptor.addChild(root_0, SEMICOLON24_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end line_name

    class line_keytype_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start line_keytype
    # XKBGrammar.g:85:1: line_keytype : TOKEN_KEY_TYPE LBRACKET keytype= NAME RBRACKET EQUAL DQUOTE keytypevalue= NAME DQUOTE SEMICOLON ;
    def line_keytype(self, ):

        retval = self.line_keytype_return()
        retval.start = self.input.LT(1)

        root_0 = None

        keytype = None
        keytypevalue = None
        TOKEN_KEY_TYPE25 = None
        LBRACKET26 = None
        RBRACKET27 = None
        EQUAL28 = None
        DQUOTE29 = None
        DQUOTE30 = None
        SEMICOLON31 = None

        keytype_tree = None
        keytypevalue_tree = None
        TOKEN_KEY_TYPE25_tree = None
        LBRACKET26_tree = None
        RBRACKET27_tree = None
        EQUAL28_tree = None
        DQUOTE29_tree = None
        DQUOTE30_tree = None
        SEMICOLON31_tree = None

        try:
            try:
                # XKBGrammar.g:86:2: ( TOKEN_KEY_TYPE LBRACKET keytype= NAME RBRACKET EQUAL DQUOTE keytypevalue= NAME DQUOTE SEMICOLON )
                # XKBGrammar.g:86:4: TOKEN_KEY_TYPE LBRACKET keytype= NAME RBRACKET EQUAL DQUOTE keytypevalue= NAME DQUOTE SEMICOLON
                root_0 = self.adaptor.nil()

                TOKEN_KEY_TYPE25 = self.input.LT(1)
                self.match(self.input, TOKEN_KEY_TYPE, self.FOLLOW_TOKEN_KEY_TYPE_in_line_keytype475)


                TOKEN_KEY_TYPE25_tree = self.adaptor.createWithPayload(TOKEN_KEY_TYPE25)
                self.adaptor.addChild(root_0, TOKEN_KEY_TYPE25_tree)

                LBRACKET26 = self.input.LT(1)
                self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_line_keytype477)


                LBRACKET26_tree = self.adaptor.createWithPayload(LBRACKET26)
                self.adaptor.addChild(root_0, LBRACKET26_tree)

                keytype = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype481)


                keytype_tree = self.adaptor.createWithPayload(keytype)
                self.adaptor.addChild(root_0, keytype_tree)

                RBRACKET27 = self.input.LT(1)
                self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_line_keytype483)


                RBRACKET27_tree = self.adaptor.createWithPayload(RBRACKET27)
                self.adaptor.addChild(root_0, RBRACKET27_tree)

                EQUAL28 = self.input.LT(1)
                self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_line_keytype485)


                EQUAL28_tree = self.adaptor.createWithPayload(EQUAL28)
                self.adaptor.addChild(root_0, EQUAL28_tree)

                DQUOTE29 = self.input.LT(1)
                self.match(self.input, DQUOTE, self.FOLLOW_DQUOTE_in_line_keytype487)


                DQUOTE29_tree = self.adaptor.createWithPayload(DQUOTE29)
                self.adaptor.addChild(root_0, DQUOTE29_tree)

                keytypevalue = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype491)


                keytypevalue_tree = self.adaptor.createWithPayload(keytypevalue)
                self.adaptor.addChild(root_0, keytypevalue_tree)

                DQUOTE30 = self.input.LT(1)
                self.match(self.input, DQUOTE, self.FOLLOW_DQUOTE_in_line_keytype493)


                DQUOTE30_tree = self.adaptor.createWithPayload(DQUOTE30)
                self.adaptor.addChild(root_0, DQUOTE30_tree)

                SEMICOLON31 = self.input.LT(1)
                self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_line_keytype495)


                SEMICOLON31_tree = self.adaptor.createWithPayload(SEMICOLON31)
                self.adaptor.addChild(root_0, SEMICOLON31_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end line_keytype

    class line_key_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start line_key
    # XKBGrammar.g:89:1: line_key : TOKEN_KEY keycode keysyms SEMICOLON ;
    def line_key(self, ):

        retval = self.line_key_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TOKEN_KEY32 = None
        SEMICOLON35 = None
        keycode33 = None

        keysyms34 = None


        TOKEN_KEY32_tree = None
        SEMICOLON35_tree = None

        try:
            try:
                # XKBGrammar.g:90:2: ( TOKEN_KEY keycode keysyms SEMICOLON )
                # XKBGrammar.g:90:4: TOKEN_KEY keycode keysyms SEMICOLON
                root_0 = self.adaptor.nil()

                TOKEN_KEY32 = self.input.LT(1)
                self.match(self.input, TOKEN_KEY, self.FOLLOW_TOKEN_KEY_in_line_key507)


                TOKEN_KEY32_tree = self.adaptor.createWithPayload(TOKEN_KEY32)
                self.adaptor.addChild(root_0, TOKEN_KEY32_tree)

                self.following.append(self.FOLLOW_keycode_in_line_key509)
                keycode33 = self.keycode()
                self.following.pop()

                self.adaptor.addChild(root_0, keycode33.tree)
                self.following.append(self.FOLLOW_keysyms_in_line_key511)
                keysyms34 = self.keysyms()
                self.following.pop()

                self.adaptor.addChild(root_0, keysyms34.tree)
                SEMICOLON35 = self.input.LT(1)
                self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_line_key513)


                SEMICOLON35_tree = self.adaptor.createWithPayload(SEMICOLON35)
                self.adaptor.addChild(root_0, SEMICOLON35_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end line_key

    class keycode_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start keycode
    # XKBGrammar.g:93:1: keycode : LOWERTHAN NAME GREATERTHAN -> ^( INCLUDE NAME ) ;
    def keycode(self, ):

        retval = self.keycode_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LOWERTHAN36 = None
        NAME37 = None
        GREATERTHAN38 = None

        LOWERTHAN36_tree = None
        NAME37_tree = None
        GREATERTHAN38_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_LOWERTHAN = RewriteRuleTokenStream(self.adaptor, "token LOWERTHAN")
        stream_GREATERTHAN = RewriteRuleTokenStream(self.adaptor, "token GREATERTHAN")

        try:
            try:
                # XKBGrammar.g:94:2: ( LOWERTHAN NAME GREATERTHAN -> ^( INCLUDE NAME ) )
                # XKBGrammar.g:94:4: LOWERTHAN NAME GREATERTHAN
                LOWERTHAN36 = self.input.LT(1)
                self.match(self.input, LOWERTHAN, self.FOLLOW_LOWERTHAN_in_keycode526)

                stream_LOWERTHAN.add(LOWERTHAN36)
                NAME37 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode528)

                stream_NAME.add(NAME37)
                GREATERTHAN38 = self.input.LT(1)
                self.match(self.input, GREATERTHAN, self.FOLLOW_GREATERTHAN_in_keycode530)

                stream_GREATERTHAN.add(GREATERTHAN38)
                # AST Rewrite
                # elements: NAME
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                root_0 = self.adaptor.nil()
                # 94:31: -> ^( INCLUDE NAME )
                # XKBGrammar.g:94:34: ^( INCLUDE NAME )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(INCLUDE, "INCLUDE"), root_1)

                self.adaptor.addChild(root_1, stream_NAME.next())

                self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end keycode

    class keysyms_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start keysyms
    # XKBGrammar.g:97:1: keysyms : LCURLY LBRACKET ( NAME | NAME_KEYSYM ) ( COMMA ( NAME | NAME_KEYSYM ) )* RBRACKET RCURLY ;
    def keysyms(self, ):

        retval = self.keysyms_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LCURLY39 = None
        LBRACKET40 = None
        set41 = None
        COMMA42 = None
        set43 = None
        RBRACKET44 = None
        RCURLY45 = None

        LCURLY39_tree = None
        LBRACKET40_tree = None
        set41_tree = None
        COMMA42_tree = None
        set43_tree = None
        RBRACKET44_tree = None
        RCURLY45_tree = None

        try:
            try:
                # XKBGrammar.g:98:2: ( LCURLY LBRACKET ( NAME | NAME_KEYSYM ) ( COMMA ( NAME | NAME_KEYSYM ) )* RBRACKET RCURLY )
                # XKBGrammar.g:98:4: LCURLY LBRACKET ( NAME | NAME_KEYSYM ) ( COMMA ( NAME | NAME_KEYSYM ) )* RBRACKET RCURLY
                root_0 = self.adaptor.nil()

                LCURLY39 = self.input.LT(1)
                self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_keysyms550)


                LCURLY39_tree = self.adaptor.createWithPayload(LCURLY39)
                self.adaptor.addChild(root_0, LCURLY39_tree)

                LBRACKET40 = self.input.LT(1)
                self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_keysyms552)


                LBRACKET40_tree = self.adaptor.createWithPayload(LBRACKET40)
                self.adaptor.addChild(root_0, LBRACKET40_tree)

                set41 = self.input.LT(1)
                if self.input.LA(1) == NAME or self.input.LA(1) == NAME_KEYSYM:
                    self.input.consume();
                    self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set41))
                    self.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_keysyms554
                        )
                    raise mse


                # XKBGrammar.g:98:39: ( COMMA ( NAME | NAME_KEYSYM ) )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == COMMA) :
                        alt6 = 1


                    if alt6 == 1:
                        # XKBGrammar.g:98:40: COMMA ( NAME | NAME_KEYSYM )
                        COMMA42 = self.input.LT(1)
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_keysyms561)


                        COMMA42_tree = self.adaptor.createWithPayload(COMMA42)
                        self.adaptor.addChild(root_0, COMMA42_tree)

                        set43 = self.input.LT(1)
                        if self.input.LA(1) == NAME or self.input.LA(1) == NAME_KEYSYM:
                            self.input.consume();
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set43))
                            self.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_keysyms563
                                )
                            raise mse




                    else:
                        break #loop6


                RBRACKET44 = self.input.LT(1)
                self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_keysyms571)


                RBRACKET44_tree = self.adaptor.createWithPayload(RBRACKET44)
                self.adaptor.addChild(root_0, RBRACKET44_tree)

                RCURLY45 = self.input.LT(1)
                self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_keysyms573)


                RCURLY45_tree = self.adaptor.createWithPayload(RCURLY45)
                self.adaptor.addChild(root_0, RCURLY45_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end keysyms

    class attribute_xkb_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start attribute_xkb
    # XKBGrammar.g:101:1: attribute_xkb : ( TOKEN_DEFAULT | TOKEN_HIDDEN | TOKEN_PARTIAL | TOKEN_ALPHANUMERIC_KEYS | TOKEN_MODIFIER_KEYS | TOKEN_ALTERNATE_GROUP | TOKEN_XKB_SYMBOLS -> ^( ATTRIBUTES ATTRIBUTE ) );
    def attribute_xkb(self, ):

        retval = self.attribute_xkb_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TOKEN_DEFAULT46 = None
        TOKEN_HIDDEN47 = None
        TOKEN_PARTIAL48 = None
        TOKEN_ALPHANUMERIC_KEYS49 = None
        TOKEN_MODIFIER_KEYS50 = None
        TOKEN_ALTERNATE_GROUP51 = None
        TOKEN_XKB_SYMBOLS52 = None

        TOKEN_DEFAULT46_tree = None
        TOKEN_HIDDEN47_tree = None
        TOKEN_PARTIAL48_tree = None
        TOKEN_ALPHANUMERIC_KEYS49_tree = None
        TOKEN_MODIFIER_KEYS50_tree = None
        TOKEN_ALTERNATE_GROUP51_tree = None
        TOKEN_XKB_SYMBOLS52_tree = None
        stream_TOKEN_XKB_SYMBOLS = RewriteRuleTokenStream(self.adaptor, "token TOKEN_XKB_SYMBOLS")

        try:
            try:
                # XKBGrammar.g:102:2: ( TOKEN_DEFAULT | TOKEN_HIDDEN | TOKEN_PARTIAL | TOKEN_ALPHANUMERIC_KEYS | TOKEN_MODIFIER_KEYS | TOKEN_ALTERNATE_GROUP | TOKEN_XKB_SYMBOLS -> ^( ATTRIBUTES ATTRIBUTE ) )
                alt7 = 7
                LA7 = self.input.LA(1)
                if LA7 == TOKEN_DEFAULT:
                    alt7 = 1
                elif LA7 == TOKEN_HIDDEN:
                    alt7 = 2
                elif LA7 == TOKEN_PARTIAL:
                    alt7 = 3
                elif LA7 == TOKEN_ALPHANUMERIC_KEYS:
                    alt7 = 4
                elif LA7 == TOKEN_MODIFIER_KEYS:
                    alt7 = 5
                elif LA7 == TOKEN_ALTERNATE_GROUP:
                    alt7 = 6
                elif LA7 == TOKEN_XKB_SYMBOLS:
                    alt7 = 7
                else:
                    nvae = NoViableAltException("101:1: attribute_xkb : ( TOKEN_DEFAULT | TOKEN_HIDDEN | TOKEN_PARTIAL | TOKEN_ALPHANUMERIC_KEYS | TOKEN_MODIFIER_KEYS | TOKEN_ALTERNATE_GROUP | TOKEN_XKB_SYMBOLS -> ^( ATTRIBUTES ATTRIBUTE ) );", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # XKBGrammar.g:102:4: TOKEN_DEFAULT
                    root_0 = self.adaptor.nil()

                    TOKEN_DEFAULT46 = self.input.LT(1)
                    self.match(self.input, TOKEN_DEFAULT, self.FOLLOW_TOKEN_DEFAULT_in_attribute_xkb586)


                    TOKEN_DEFAULT46_tree = self.adaptor.createWithPayload(TOKEN_DEFAULT46)
                    self.adaptor.addChild(root_0, TOKEN_DEFAULT46_tree)



                elif alt7 == 2:
                    # XKBGrammar.g:103:4: TOKEN_HIDDEN
                    root_0 = self.adaptor.nil()

                    TOKEN_HIDDEN47 = self.input.LT(1)
                    self.match(self.input, TOKEN_HIDDEN, self.FOLLOW_TOKEN_HIDDEN_in_attribute_xkb591)


                    TOKEN_HIDDEN47_tree = self.adaptor.createWithPayload(TOKEN_HIDDEN47)
                    self.adaptor.addChild(root_0, TOKEN_HIDDEN47_tree)



                elif alt7 == 3:
                    # XKBGrammar.g:104:4: TOKEN_PARTIAL
                    root_0 = self.adaptor.nil()

                    TOKEN_PARTIAL48 = self.input.LT(1)
                    self.match(self.input, TOKEN_PARTIAL, self.FOLLOW_TOKEN_PARTIAL_in_attribute_xkb600)


                    TOKEN_PARTIAL48_tree = self.adaptor.createWithPayload(TOKEN_PARTIAL48)
                    self.adaptor.addChild(root_0, TOKEN_PARTIAL48_tree)



                elif alt7 == 4:
                    # XKBGrammar.g:105:4: TOKEN_ALPHANUMERIC_KEYS
                    root_0 = self.adaptor.nil()

                    TOKEN_ALPHANUMERIC_KEYS49 = self.input.LT(1)
                    self.match(self.input, TOKEN_ALPHANUMERIC_KEYS, self.FOLLOW_TOKEN_ALPHANUMERIC_KEYS_in_attribute_xkb609)


                    TOKEN_ALPHANUMERIC_KEYS49_tree = self.adaptor.createWithPayload(TOKEN_ALPHANUMERIC_KEYS49)
                    self.adaptor.addChild(root_0, TOKEN_ALPHANUMERIC_KEYS49_tree)



                elif alt7 == 5:
                    # XKBGrammar.g:106:4: TOKEN_MODIFIER_KEYS
                    root_0 = self.adaptor.nil()

                    TOKEN_MODIFIER_KEYS50 = self.input.LT(1)
                    self.match(self.input, TOKEN_MODIFIER_KEYS, self.FOLLOW_TOKEN_MODIFIER_KEYS_in_attribute_xkb616)


                    TOKEN_MODIFIER_KEYS50_tree = self.adaptor.createWithPayload(TOKEN_MODIFIER_KEYS50)
                    self.adaptor.addChild(root_0, TOKEN_MODIFIER_KEYS50_tree)



                elif alt7 == 6:
                    # XKBGrammar.g:107:4: TOKEN_ALTERNATE_GROUP
                    root_0 = self.adaptor.nil()

                    TOKEN_ALTERNATE_GROUP51 = self.input.LT(1)
                    self.match(self.input, TOKEN_ALTERNATE_GROUP, self.FOLLOW_TOKEN_ALTERNATE_GROUP_in_attribute_xkb624)


                    TOKEN_ALTERNATE_GROUP51_tree = self.adaptor.createWithPayload(TOKEN_ALTERNATE_GROUP51)
                    self.adaptor.addChild(root_0, TOKEN_ALTERNATE_GROUP51_tree)



                elif alt7 == 7:
                    # XKBGrammar.g:108:4: TOKEN_XKB_SYMBOLS
                    TOKEN_XKB_SYMBOLS52 = self.input.LT(1)
                    self.match(self.input, TOKEN_XKB_SYMBOLS, self.FOLLOW_TOKEN_XKB_SYMBOLS_in_attribute_xkb631)

                    stream_TOKEN_XKB_SYMBOLS.add(TOKEN_XKB_SYMBOLS52)
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 108:22: -> ^( ATTRIBUTES ATTRIBUTE )
                    # XKBGrammar.g:108:25: ^( ATTRIBUTES ATTRIBUTE )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ATTRIBUTES, "ATTRIBUTES"), root_1)

                    self.adaptor.addChild(root_1, self.adaptor.createFromType(ATTRIBUTE, "ATTRIBUTE"))

                    self.adaptor.addChild(root_0, root_1)





                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end attribute_xkb


 

    FOLLOW_statement_in_layout336 = frozenset([4, 5, 6, 7, 8, 9, 10])
    FOLLOW_EOF_in_layout339 = frozenset([1])
    FOLLOW_preamble_in_statement352 = frozenset([20])
    FOLLOW_quotedstring_in_statement354 = frozenset([17])
    FOLLOW_LCURLY_in_statement356 = frozenset([11, 12, 13, 14])
    FOLLOW_sectionmaterial_in_statement358 = frozenset([11, 12, 13, 14, 18])
    FOLLOW_RCURLY_in_statement361 = frozenset([23])
    FOLLOW_SEMICOLON_in_statement363 = frozenset([1])
    FOLLOW_attribute_xkb_in_preamble373 = frozenset([1, 4, 5, 6, 7, 8, 9, 10])
    FOLLOW_DQUOTE_in_quotedstring383 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])
    FOLLOW_set_in_quotedstring385 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])
    FOLLOW_DQUOTE_in_quotedstring391 = frozenset([1])
    FOLLOW_line_include_in_sectionmaterial402 = frozenset([1])
    FOLLOW_line_name_in_sectionmaterial408 = frozenset([1])
    FOLLOW_line_keytype_in_sectionmaterial414 = frozenset([1])
    FOLLOW_line_key_in_sectionmaterial420 = frozenset([1])
    FOLLOW_TOKEN_INCLUDE_in_line_include437 = frozenset([20])
    FOLLOW_quotedstring_in_line_include439 = frozenset([1])
    FOLLOW_TOKEN_NAME_in_line_name450 = frozenset([15])
    FOLLOW_LBRACKET_in_line_name452 = frozenset([32])
    FOLLOW_NAME_in_line_name456 = frozenset([16])
    FOLLOW_RBRACKET_in_line_name458 = frozenset([24])
    FOLLOW_EQUAL_in_line_name460 = frozenset([20])
    FOLLOW_quotedstring_in_line_name462 = frozenset([23])
    FOLLOW_SEMICOLON_in_line_name464 = frozenset([1])
    FOLLOW_TOKEN_KEY_TYPE_in_line_keytype475 = frozenset([15])
    FOLLOW_LBRACKET_in_line_keytype477 = frozenset([32])
    FOLLOW_NAME_in_line_keytype481 = frozenset([16])
    FOLLOW_RBRACKET_in_line_keytype483 = frozenset([24])
    FOLLOW_EQUAL_in_line_keytype485 = frozenset([20])
    FOLLOW_DQUOTE_in_line_keytype487 = frozenset([32])
    FOLLOW_NAME_in_line_keytype491 = frozenset([20])
    FOLLOW_DQUOTE_in_line_keytype493 = frozenset([23])
    FOLLOW_SEMICOLON_in_line_keytype495 = frozenset([1])
    FOLLOW_TOKEN_KEY_in_line_key507 = frozenset([25])
    FOLLOW_keycode_in_line_key509 = frozenset([17])
    FOLLOW_keysyms_in_line_key511 = frozenset([23])
    FOLLOW_SEMICOLON_in_line_key513 = frozenset([1])
    FOLLOW_LOWERTHAN_in_keycode526 = frozenset([32])
    FOLLOW_NAME_in_keycode528 = frozenset([26])
    FOLLOW_GREATERTHAN_in_keycode530 = frozenset([1])
    FOLLOW_LCURLY_in_keysyms550 = frozenset([15])
    FOLLOW_LBRACKET_in_keysyms552 = frozenset([32, 35])
    FOLLOW_set_in_keysyms554 = frozenset([16, 19])
    FOLLOW_COMMA_in_keysyms561 = frozenset([32, 35])
    FOLLOW_set_in_keysyms563 = frozenset([16, 19])
    FOLLOW_RBRACKET_in_keysyms571 = frozenset([18])
    FOLLOW_RCURLY_in_keysyms573 = frozenset([1])
    FOLLOW_TOKEN_DEFAULT_in_attribute_xkb586 = frozenset([1])
    FOLLOW_TOKEN_HIDDEN_in_attribute_xkb591 = frozenset([1])
    FOLLOW_TOKEN_PARTIAL_in_attribute_xkb600 = frozenset([1])
    FOLLOW_TOKEN_ALPHANUMERIC_KEYS_in_attribute_xkb609 = frozenset([1])
    FOLLOW_TOKEN_MODIFIER_KEYS_in_attribute_xkb616 = frozenset([1])
    FOLLOW_TOKEN_ALTERNATE_GROUP_in_attribute_xkb624 = frozenset([1])
    FOLLOW_TOKEN_XKB_SYMBOLS_in_attribute_xkb631 = frozenset([1])

