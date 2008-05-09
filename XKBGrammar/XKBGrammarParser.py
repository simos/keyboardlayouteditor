# $ANTLR 3.0.1 XKBGrammar.g 2008-05-09 13:01:19

from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



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
EOF=-1
GENERIC_NAME=36
SECTIONNAME=34
LBRACKET=15
NAME=35
TOKEN_PARTIAL=6
WS=39
NEWLINE=38
TOKEN_ALPHANUMERIC_KEYS=7
TOKEN_HIDDEN=5
COMMA=19
LOWERTHAN=25
INCLUDE=30
EQUAL=24
RCURLY=18
TOKEN_MODIFIER_KEYS=8
PLUS=22
TOKEN_KEY=14
RBRACKET=16
COMMENT=37
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
    "ATTRIBUTE", "INCLUDE", "KEY", "KEYTYPE", "SECTION", "SECTIONNAME", 
    "NAME", "GENERIC_NAME", "COMMENT", "NEWLINE", "WS"
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
    # XKBGrammar.g:74:1: layout : ( section )* EOF ;
    def layout(self, ):

        retval = self.layout_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF2 = None
        section1 = None


        EOF2_tree = None

        try:
            try:
                # XKBGrammar.g:75:2: ( ( section )* EOF )
                # XKBGrammar.g:75:4: ( section )* EOF
                root_0 = self.adaptor.nil()

                # XKBGrammar.g:75:4: ( section )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((TOKEN_DEFAULT <= LA1_0 <= TOKEN_ALPHANUMERIC_KEYS) or (TOKEN_ALTERNATE_GROUP <= LA1_0 <= TOKEN_XKB_SYMBOLS)) :
                        alt1 = 1


                    if alt1 == 1:
                        # XKBGrammar.g:75:4: section
                        self.following.append(self.FOLLOW_section_in_layout361)
                        section1 = self.section()
                        self.following.pop()

                        self.adaptor.addChild(root_0, section1.tree)


                    else:
                        break #loop1


                EOF2 = self.input.LT(1)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_layout364)




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

    class section_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start section
    # XKBGrammar.g:78:1: section : preamble sectionmaterial -> ^( SECTION ) ;
    def section(self, ):

        retval = self.section_return()
        retval.start = self.input.LT(1)

        root_0 = None

        preamble3 = None

        sectionmaterial4 = None


        stream_preamble = RewriteRuleSubtreeStream(self.adaptor, "rule preamble")
        stream_sectionmaterial = RewriteRuleSubtreeStream(self.adaptor, "rule sectionmaterial")
        try:
            try:
                # XKBGrammar.g:79:2: ( preamble sectionmaterial -> ^( SECTION ) )
                # XKBGrammar.g:79:4: preamble sectionmaterial
                self.following.append(self.FOLLOW_preamble_in_section380)
                preamble3 = self.preamble()
                self.following.pop()

                stream_preamble.add(preamble3.tree)
                self.following.append(self.FOLLOW_sectionmaterial_in_section382)
                sectionmaterial4 = self.sectionmaterial()
                self.following.pop()

                stream_sectionmaterial.add(sectionmaterial4.tree)
                #action start
                print '}' 
                #action end
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
                # 81:2: -> ^( SECTION )
                # XKBGrammar.g:81:5: ^( SECTION )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(SECTION, "SECTION"), root_1)

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

    # $ANTLR end section

    class preamble_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start preamble
    # XKBGrammar.g:84:1: preamble : ( attribute_xkb )+ sectionname= quotedstring ;
    def preamble(self, ):

        retval = self.preamble_return()
        retval.start = self.input.LT(1)

        root_0 = None

        sectionname = None

        attribute_xkb5 = None



        try:
            try:
                # XKBGrammar.g:85:2: ( ( attribute_xkb )+ sectionname= quotedstring )
                # XKBGrammar.g:85:4: ( attribute_xkb )+ sectionname= quotedstring
                root_0 = self.adaptor.nil()

                # XKBGrammar.g:85:4: ( attribute_xkb )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((TOKEN_DEFAULT <= LA2_0 <= TOKEN_ALPHANUMERIC_KEYS) or (TOKEN_ALTERNATE_GROUP <= LA2_0 <= TOKEN_XKB_SYMBOLS)) :
                        alt2 = 1


                    if alt2 == 1:
                        # XKBGrammar.g:85:4: attribute_xkb
                        self.following.append(self.FOLLOW_attribute_xkb_in_preamble407)
                        attribute_xkb5 = self.attribute_xkb()
                        self.following.pop()

                        self.adaptor.addChild(root_0, attribute_xkb5.tree)


                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1


                self.following.append(self.FOLLOW_quotedstring_in_preamble412)
                sectionname = self.quotedstring()
                self.following.pop()

                self.adaptor.addChild(root_0, sectionname.tree)
                #action start
                print '%(sectionname)s {' % { "sectionname": self.input.toString(sectionname.start,sectionname.stop) } 
                #action end



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

            self.value = None
            self.tree = None


    # $ANTLR start quotedstring
    # XKBGrammar.g:89:1: quotedstring returns [value] : DQUOTE (sectionname+=~ ( DQUOTE ) )+ DQUOTE ;
    def quotedstring(self, ):

        retval = self.quotedstring_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DQUOTE6 = None
        DQUOTE7 = None
        sectionname = None
        list_sectionname = None

        DQUOTE6_tree = None
        DQUOTE7_tree = None
        sectionname_tree = None

        try:
            try:
                # XKBGrammar.g:90:9: ( DQUOTE (sectionname+=~ ( DQUOTE ) )+ DQUOTE )
                # XKBGrammar.g:90:11: DQUOTE (sectionname+=~ ( DQUOTE ) )+ DQUOTE
                root_0 = self.adaptor.nil()

                DQUOTE6 = self.input.LT(1)
                self.match(self.input, DQUOTE, self.FOLLOW_DQUOTE_in_quotedstring437)


                DQUOTE6_tree = self.adaptor.createWithPayload(DQUOTE6)
                self.adaptor.addChild(root_0, DQUOTE6_tree)

                # XKBGrammar.g:90:29: (sectionname+=~ ( DQUOTE ) )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((TOKEN_DEFAULT <= LA3_0 <= COMMA) or (MINUS <= LA3_0 <= WS)) :
                        alt3 = 1


                    if alt3 == 1:
                        # XKBGrammar.g:90:29: sectionname+=~ ( DQUOTE )
                        sectionname = self.input.LT(1)
                        if (TOKEN_DEFAULT <= self.input.LA(1) <= COMMA) or (MINUS <= self.input.LA(1) <= WS):
                            self.input.consume();
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(sectionname))
                            self.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_quotedstring441
                                )
                            raise mse


                        if list_sectionname is None:
                            list_sectionname = []
                        list_sectionname.append(sectionname)



                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


                DQUOTE7 = self.input.LT(1)
                self.match(self.input, DQUOTE, self.FOLLOW_DQUOTE_in_quotedstring447)


                DQUOTE7_tree = self.adaptor.createWithPayload(DQUOTE7)
                self.adaptor.addChild(root_0, DQUOTE7_tree)

                #action start
                                
                qstring = ['"']
                for elem in list_sectionname:
                        qstring.append(elem.getText())
                qstring.append('"')
                retval.value = "".join(qstring)
                        
                #action end



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
    # XKBGrammar.g:100:1: sectionmaterial : LCURLY ( line_include | line_name | line_keytype | line_key )+ RCURLY SEMICOLON ;
    def sectionmaterial(self, ):

        retval = self.sectionmaterial_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LCURLY8 = None
        RCURLY13 = None
        SEMICOLON14 = None
        line_include9 = None

        line_name10 = None

        line_keytype11 = None

        line_key12 = None


        LCURLY8_tree = None
        RCURLY13_tree = None
        SEMICOLON14_tree = None

        try:
            try:
                # XKBGrammar.g:101:2: ( LCURLY ( line_include | line_name | line_keytype | line_key )+ RCURLY SEMICOLON )
                # XKBGrammar.g:101:4: LCURLY ( line_include | line_name | line_keytype | line_key )+ RCURLY SEMICOLON
                root_0 = self.adaptor.nil()

                LCURLY8 = self.input.LT(1)
                self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_sectionmaterial477)


                LCURLY8_tree = self.adaptor.createWithPayload(LCURLY8)
                self.adaptor.addChild(root_0, LCURLY8_tree)

                # XKBGrammar.g:101:11: ( line_include | line_name | line_keytype | line_key )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 5
                    LA4 = self.input.LA(1)
                    if LA4 == TOKEN_INCLUDE:
                        alt4 = 1
                    elif LA4 == TOKEN_NAME:
                        alt4 = 2
                    elif LA4 == TOKEN_KEY_TYPE:
                        alt4 = 3
                    elif LA4 == TOKEN_KEY:
                        alt4 = 4

                    if alt4 == 1:
                        # XKBGrammar.g:101:12: line_include
                        self.following.append(self.FOLLOW_line_include_in_sectionmaterial480)
                        line_include9 = self.line_include()
                        self.following.pop()

                        self.adaptor.addChild(root_0, line_include9.tree)


                    elif alt4 == 2:
                        # XKBGrammar.g:102:4: line_name
                        self.following.append(self.FOLLOW_line_name_in_sectionmaterial486)
                        line_name10 = self.line_name()
                        self.following.pop()

                        self.adaptor.addChild(root_0, line_name10.tree)


                    elif alt4 == 3:
                        # XKBGrammar.g:103:4: line_keytype
                        self.following.append(self.FOLLOW_line_keytype_in_sectionmaterial492)
                        line_keytype11 = self.line_keytype()
                        self.following.pop()

                        self.adaptor.addChild(root_0, line_keytype11.tree)


                    elif alt4 == 4:
                        # XKBGrammar.g:104:4: line_key
                        self.following.append(self.FOLLOW_line_key_in_sectionmaterial498)
                        line_key12 = self.line_key()
                        self.following.pop()

                        self.adaptor.addChild(root_0, line_key12.tree)


                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1


                RCURLY13 = self.input.LT(1)
                self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_sectionmaterial505)


                RCURLY13_tree = self.adaptor.createWithPayload(RCURLY13)
                self.adaptor.addChild(root_0, RCURLY13_tree)

                SEMICOLON14 = self.input.LT(1)
                self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_sectionmaterial507)


                SEMICOLON14_tree = self.adaptor.createWithPayload(SEMICOLON14)
                self.adaptor.addChild(root_0, SEMICOLON14_tree)




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
    # XKBGrammar.g:108:1: line_include : TOKEN_INCLUDE include= quotedstring ;
    def line_include(self, ):

        retval = self.line_include_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TOKEN_INCLUDE15 = None
        include = None


        TOKEN_INCLUDE15_tree = None

        try:
            try:
                # XKBGrammar.g:109:2: ( TOKEN_INCLUDE include= quotedstring )
                # XKBGrammar.g:109:4: TOKEN_INCLUDE include= quotedstring
                root_0 = self.adaptor.nil()

                TOKEN_INCLUDE15 = self.input.LT(1)
                self.match(self.input, TOKEN_INCLUDE, self.FOLLOW_TOKEN_INCLUDE_in_line_include518)


                TOKEN_INCLUDE15_tree = self.adaptor.createWithPayload(TOKEN_INCLUDE15)
                self.adaptor.addChild(root_0, TOKEN_INCLUDE15_tree)

                self.following.append(self.FOLLOW_quotedstring_in_line_include522)
                include = self.quotedstring()
                self.following.pop()

                self.adaptor.addChild(root_0, include.tree)
                #action start
                print '\tinclude %(inc)s' % { "inc": self.input.toString(include.start,include.stop) } 
                #action end



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
    # XKBGrammar.g:113:1: line_name : TOKEN_NAME LBRACKET name= NAME RBRACKET EQUAL nameval= quotedstring SEMICOLON ;
    def line_name(self, ):

        retval = self.line_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        name = None
        TOKEN_NAME16 = None
        LBRACKET17 = None
        RBRACKET18 = None
        EQUAL19 = None
        SEMICOLON20 = None
        nameval = None


        name_tree = None
        TOKEN_NAME16_tree = None
        LBRACKET17_tree = None
        RBRACKET18_tree = None
        EQUAL19_tree = None
        SEMICOLON20_tree = None

        try:
            try:
                # XKBGrammar.g:114:2: ( TOKEN_NAME LBRACKET name= NAME RBRACKET EQUAL nameval= quotedstring SEMICOLON )
                # XKBGrammar.g:114:4: TOKEN_NAME LBRACKET name= NAME RBRACKET EQUAL nameval= quotedstring SEMICOLON
                root_0 = self.adaptor.nil()

                TOKEN_NAME16 = self.input.LT(1)
                self.match(self.input, TOKEN_NAME, self.FOLLOW_TOKEN_NAME_in_line_name537)


                TOKEN_NAME16_tree = self.adaptor.createWithPayload(TOKEN_NAME16)
                self.adaptor.addChild(root_0, TOKEN_NAME16_tree)

                LBRACKET17 = self.input.LT(1)
                self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_line_name539)


                LBRACKET17_tree = self.adaptor.createWithPayload(LBRACKET17)
                self.adaptor.addChild(root_0, LBRACKET17_tree)

                name = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_name543)


                name_tree = self.adaptor.createWithPayload(name)
                self.adaptor.addChild(root_0, name_tree)

                RBRACKET18 = self.input.LT(1)
                self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_line_name545)


                RBRACKET18_tree = self.adaptor.createWithPayload(RBRACKET18)
                self.adaptor.addChild(root_0, RBRACKET18_tree)

                EQUAL19 = self.input.LT(1)
                self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_line_name547)


                EQUAL19_tree = self.adaptor.createWithPayload(EQUAL19)
                self.adaptor.addChild(root_0, EQUAL19_tree)

                self.following.append(self.FOLLOW_quotedstring_in_line_name551)
                nameval = self.quotedstring()
                self.following.pop()

                self.adaptor.addChild(root_0, nameval.tree)
                SEMICOLON20 = self.input.LT(1)
                self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_line_name553)


                SEMICOLON20_tree = self.adaptor.createWithPayload(SEMICOLON20)
                self.adaptor.addChild(root_0, SEMICOLON20_tree)

                #action start
                print '\tname[%(name)s] = %(nameval)s;' % {  "name": name.text, "nameval": self.input.toString(nameval.start,nameval.stop) } 
                #action end



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
    # XKBGrammar.g:118:1: line_keytype : TOKEN_KEY_TYPE LBRACKET keytype= NAME RBRACKET EQUAL DQUOTE keytypevalue= NAME DQUOTE SEMICOLON ;
    def line_keytype(self, ):

        retval = self.line_keytype_return()
        retval.start = self.input.LT(1)

        root_0 = None

        keytype = None
        keytypevalue = None
        TOKEN_KEY_TYPE21 = None
        LBRACKET22 = None
        RBRACKET23 = None
        EQUAL24 = None
        DQUOTE25 = None
        DQUOTE26 = None
        SEMICOLON27 = None

        keytype_tree = None
        keytypevalue_tree = None
        TOKEN_KEY_TYPE21_tree = None
        LBRACKET22_tree = None
        RBRACKET23_tree = None
        EQUAL24_tree = None
        DQUOTE25_tree = None
        DQUOTE26_tree = None
        SEMICOLON27_tree = None

        try:
            try:
                # XKBGrammar.g:119:2: ( TOKEN_KEY_TYPE LBRACKET keytype= NAME RBRACKET EQUAL DQUOTE keytypevalue= NAME DQUOTE SEMICOLON )
                # XKBGrammar.g:119:4: TOKEN_KEY_TYPE LBRACKET keytype= NAME RBRACKET EQUAL DQUOTE keytypevalue= NAME DQUOTE SEMICOLON
                root_0 = self.adaptor.nil()

                TOKEN_KEY_TYPE21 = self.input.LT(1)
                self.match(self.input, TOKEN_KEY_TYPE, self.FOLLOW_TOKEN_KEY_TYPE_in_line_keytype567)


                TOKEN_KEY_TYPE21_tree = self.adaptor.createWithPayload(TOKEN_KEY_TYPE21)
                self.adaptor.addChild(root_0, TOKEN_KEY_TYPE21_tree)

                LBRACKET22 = self.input.LT(1)
                self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_line_keytype569)


                LBRACKET22_tree = self.adaptor.createWithPayload(LBRACKET22)
                self.adaptor.addChild(root_0, LBRACKET22_tree)

                keytype = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype573)


                keytype_tree = self.adaptor.createWithPayload(keytype)
                self.adaptor.addChild(root_0, keytype_tree)

                RBRACKET23 = self.input.LT(1)
                self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_line_keytype575)


                RBRACKET23_tree = self.adaptor.createWithPayload(RBRACKET23)
                self.adaptor.addChild(root_0, RBRACKET23_tree)

                EQUAL24 = self.input.LT(1)
                self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_line_keytype577)


                EQUAL24_tree = self.adaptor.createWithPayload(EQUAL24)
                self.adaptor.addChild(root_0, EQUAL24_tree)

                DQUOTE25 = self.input.LT(1)
                self.match(self.input, DQUOTE, self.FOLLOW_DQUOTE_in_line_keytype579)


                DQUOTE25_tree = self.adaptor.createWithPayload(DQUOTE25)
                self.adaptor.addChild(root_0, DQUOTE25_tree)

                keytypevalue = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype583)


                keytypevalue_tree = self.adaptor.createWithPayload(keytypevalue)
                self.adaptor.addChild(root_0, keytypevalue_tree)

                DQUOTE26 = self.input.LT(1)
                self.match(self.input, DQUOTE, self.FOLLOW_DQUOTE_in_line_keytype585)


                DQUOTE26_tree = self.adaptor.createWithPayload(DQUOTE26)
                self.adaptor.addChild(root_0, DQUOTE26_tree)

                SEMICOLON27 = self.input.LT(1)
                self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_line_keytype587)


                SEMICOLON27_tree = self.adaptor.createWithPayload(SEMICOLON27)
                self.adaptor.addChild(root_0, SEMICOLON27_tree)

                #action start
                print '\tkey.type[%(kt)s] = \"%(ktv)s\";' % {  "kt": keytype.text, "ktv": keytypevalue.text } 
                #action end



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
    # XKBGrammar.g:123:1: line_key : TOKEN_KEY keycode keysyms SEMICOLON ;
    def line_key(self, ):

        retval = self.line_key_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TOKEN_KEY28 = None
        SEMICOLON31 = None
        keycode29 = None

        keysyms30 = None


        TOKEN_KEY28_tree = None
        SEMICOLON31_tree = None

        try:
            try:
                # XKBGrammar.g:124:2: ( TOKEN_KEY keycode keysyms SEMICOLON )
                # XKBGrammar.g:124:4: TOKEN_KEY keycode keysyms SEMICOLON
                root_0 = self.adaptor.nil()

                TOKEN_KEY28 = self.input.LT(1)
                self.match(self.input, TOKEN_KEY, self.FOLLOW_TOKEN_KEY_in_line_key602)


                TOKEN_KEY28_tree = self.adaptor.createWithPayload(TOKEN_KEY28)
                self.adaptor.addChild(root_0, TOKEN_KEY28_tree)

                self.following.append(self.FOLLOW_keycode_in_line_key604)
                keycode29 = self.keycode()
                self.following.pop()

                self.adaptor.addChild(root_0, keycode29.tree)
                self.following.append(self.FOLLOW_keysyms_in_line_key606)
                keysyms30 = self.keysyms()
                self.following.pop()

                self.adaptor.addChild(root_0, keysyms30.tree)
                SEMICOLON31 = self.input.LT(1)
                self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_line_key608)


                SEMICOLON31_tree = self.adaptor.createWithPayload(SEMICOLON31)
                self.adaptor.addChild(root_0, SEMICOLON31_tree)

                #action start
                print '\tkey %(keycode)s %(keysyms)s;' % {  "keycode": self.input.toString(keycode29.start,keycode29.stop), "keysyms": keysyms30.value } 
                #action end



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
    # XKBGrammar.g:128:1: keycode : LOWERTHAN NAME GREATERTHAN -> ^( INCLUDE NAME ) ;
    def keycode(self, ):

        retval = self.keycode_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LOWERTHAN32 = None
        NAME33 = None
        GREATERTHAN34 = None

        LOWERTHAN32_tree = None
        NAME33_tree = None
        GREATERTHAN34_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_LOWERTHAN = RewriteRuleTokenStream(self.adaptor, "token LOWERTHAN")
        stream_GREATERTHAN = RewriteRuleTokenStream(self.adaptor, "token GREATERTHAN")

        try:
            try:
                # XKBGrammar.g:129:2: ( LOWERTHAN NAME GREATERTHAN -> ^( INCLUDE NAME ) )
                # XKBGrammar.g:129:4: LOWERTHAN NAME GREATERTHAN
                LOWERTHAN32 = self.input.LT(1)
                self.match(self.input, LOWERTHAN, self.FOLLOW_LOWERTHAN_in_keycode624)

                stream_LOWERTHAN.add(LOWERTHAN32)
                NAME33 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode626)

                stream_NAME.add(NAME33)
                GREATERTHAN34 = self.input.LT(1)
                self.match(self.input, GREATERTHAN, self.FOLLOW_GREATERTHAN_in_keycode628)

                stream_GREATERTHAN.add(GREATERTHAN34)
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
                # 130:2: -> ^( INCLUDE NAME )
                # XKBGrammar.g:130:5: ^( INCLUDE NAME )
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

            self.value = None
            self.tree = None


    # $ANTLR start keysyms
    # XKBGrammar.g:133:1: keysyms returns [value] : LCURLY LBRACKET keysym+= NAME ( COMMA keysym+= NAME )* RBRACKET RCURLY ;
    def keysyms(self, ):

        retval = self.keysyms_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LCURLY35 = None
        LBRACKET36 = None
        COMMA37 = None
        RBRACKET38 = None
        RCURLY39 = None
        keysym = None
        list_keysym = None

        LCURLY35_tree = None
        LBRACKET36_tree = None
        COMMA37_tree = None
        RBRACKET38_tree = None
        RCURLY39_tree = None
        keysym_tree = None

        try:
            try:
                # XKBGrammar.g:134:2: ( LCURLY LBRACKET keysym+= NAME ( COMMA keysym+= NAME )* RBRACKET RCURLY )
                # XKBGrammar.g:134:4: LCURLY LBRACKET keysym+= NAME ( COMMA keysym+= NAME )* RBRACKET RCURLY
                root_0 = self.adaptor.nil()

                LCURLY35 = self.input.LT(1)
                self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_keysyms653)


                LCURLY35_tree = self.adaptor.createWithPayload(LCURLY35)
                self.adaptor.addChild(root_0, LCURLY35_tree)

                LBRACKET36 = self.input.LT(1)
                self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_keysyms655)


                LBRACKET36_tree = self.adaptor.createWithPayload(LBRACKET36)
                self.adaptor.addChild(root_0, LBRACKET36_tree)

                keysym = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_keysyms659)


                keysym_tree = self.adaptor.createWithPayload(keysym)
                self.adaptor.addChild(root_0, keysym_tree)

                if list_keysym is None:
                    list_keysym = []
                list_keysym.append(keysym)

                # XKBGrammar.g:134:33: ( COMMA keysym+= NAME )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == COMMA) :
                        alt5 = 1


                    if alt5 == 1:
                        # XKBGrammar.g:134:34: COMMA keysym+= NAME
                        COMMA37 = self.input.LT(1)
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_keysyms662)


                        COMMA37_tree = self.adaptor.createWithPayload(COMMA37)
                        self.adaptor.addChild(root_0, COMMA37_tree)

                        keysym = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_keysyms666)


                        keysym_tree = self.adaptor.createWithPayload(keysym)
                        self.adaptor.addChild(root_0, keysym_tree)

                        if list_keysym is None:
                            list_keysym = []
                        list_keysym.append(keysym)



                    else:
                        break #loop5


                RBRACKET38 = self.input.LT(1)
                self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_keysyms670)


                RBRACKET38_tree = self.adaptor.createWithPayload(RBRACKET38)
                self.adaptor.addChild(root_0, RBRACKET38_tree)

                RCURLY39 = self.input.LT(1)
                self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_keysyms672)


                RCURLY39_tree = self.adaptor.createWithPayload(RCURLY39)
                self.adaptor.addChild(root_0, RCURLY39_tree)

                #action start
                                
                qstring = ["{ [ "]
                first_elem = list_keysym[0].getText()
                qstring.append(first_elem)
                for elem in list_keysym:
                        if first_elem != "":
                                first_elem = ""
                                continue
                        qstring.append(", ")
                        qstring.append(elem.getText())
                qstring.append(" ] }")
                retval.value = "".join(qstring)
                        
                #action end



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
    # XKBGrammar.g:154:1: attribute_xkb : ( TOKEN_DEFAULT | TOKEN_HIDDEN | TOKEN_PARTIAL | TOKEN_ALPHANUMERIC_KEYS | TOKEN_ALTERNATE_GROUP | TOKEN_XKB_SYMBOLS -> ^( ATTRIBUTES ATTRIBUTE ) );
    def attribute_xkb(self, ):

        retval = self.attribute_xkb_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TOKEN_DEFAULT40 = None
        TOKEN_HIDDEN41 = None
        TOKEN_PARTIAL42 = None
        TOKEN_ALPHANUMERIC_KEYS43 = None
        TOKEN_ALTERNATE_GROUP44 = None
        TOKEN_XKB_SYMBOLS45 = None

        TOKEN_DEFAULT40_tree = None
        TOKEN_HIDDEN41_tree = None
        TOKEN_PARTIAL42_tree = None
        TOKEN_ALPHANUMERIC_KEYS43_tree = None
        TOKEN_ALTERNATE_GROUP44_tree = None
        TOKEN_XKB_SYMBOLS45_tree = None
        stream_TOKEN_XKB_SYMBOLS = RewriteRuleTokenStream(self.adaptor, "token TOKEN_XKB_SYMBOLS")

        try:
            try:
                # XKBGrammar.g:155:2: ( TOKEN_DEFAULT | TOKEN_HIDDEN | TOKEN_PARTIAL | TOKEN_ALPHANUMERIC_KEYS | TOKEN_ALTERNATE_GROUP | TOKEN_XKB_SYMBOLS -> ^( ATTRIBUTES ATTRIBUTE ) )
                alt6 = 6
                LA6 = self.input.LA(1)
                if LA6 == TOKEN_DEFAULT:
                    alt6 = 1
                elif LA6 == TOKEN_HIDDEN:
                    alt6 = 2
                elif LA6 == TOKEN_PARTIAL:
                    alt6 = 3
                elif LA6 == TOKEN_ALPHANUMERIC_KEYS:
                    alt6 = 4
                elif LA6 == TOKEN_ALTERNATE_GROUP:
                    alt6 = 5
                elif LA6 == TOKEN_XKB_SYMBOLS:
                    alt6 = 6
                else:
                    nvae = NoViableAltException("154:1: attribute_xkb : ( TOKEN_DEFAULT | TOKEN_HIDDEN | TOKEN_PARTIAL | TOKEN_ALPHANUMERIC_KEYS | TOKEN_ALTERNATE_GROUP | TOKEN_XKB_SYMBOLS -> ^( ATTRIBUTES ATTRIBUTE ) );", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # XKBGrammar.g:155:4: TOKEN_DEFAULT
                    root_0 = self.adaptor.nil()

                    TOKEN_DEFAULT40 = self.input.LT(1)
                    self.match(self.input, TOKEN_DEFAULT, self.FOLLOW_TOKEN_DEFAULT_in_attribute_xkb697)


                    TOKEN_DEFAULT40_tree = self.adaptor.createWithPayload(TOKEN_DEFAULT40)
                    self.adaptor.addChild(root_0, TOKEN_DEFAULT40_tree)

                    #action start
                    print "default", 
                    #action end


                elif alt6 == 2:
                    # XKBGrammar.g:156:4: TOKEN_HIDDEN
                    root_0 = self.adaptor.nil()

                    TOKEN_HIDDEN41 = self.input.LT(1)
                    self.match(self.input, TOKEN_HIDDEN, self.FOLLOW_TOKEN_HIDDEN_in_attribute_xkb705)


                    TOKEN_HIDDEN41_tree = self.adaptor.createWithPayload(TOKEN_HIDDEN41)
                    self.adaptor.addChild(root_0, TOKEN_HIDDEN41_tree)

                    #action start
                    print "hidden", 
                    #action end


                elif alt6 == 3:
                    # XKBGrammar.g:157:4: TOKEN_PARTIAL
                    root_0 = self.adaptor.nil()

                    TOKEN_PARTIAL42 = self.input.LT(1)
                    self.match(self.input, TOKEN_PARTIAL, self.FOLLOW_TOKEN_PARTIAL_in_attribute_xkb714)


                    TOKEN_PARTIAL42_tree = self.adaptor.createWithPayload(TOKEN_PARTIAL42)
                    self.adaptor.addChild(root_0, TOKEN_PARTIAL42_tree)

                    #action start
                    print "partial", 
                    #action end


                elif alt6 == 4:
                    # XKBGrammar.g:158:4: TOKEN_ALPHANUMERIC_KEYS
                    root_0 = self.adaptor.nil()

                    TOKEN_ALPHANUMERIC_KEYS43 = self.input.LT(1)
                    self.match(self.input, TOKEN_ALPHANUMERIC_KEYS, self.FOLLOW_TOKEN_ALPHANUMERIC_KEYS_in_attribute_xkb723)


                    TOKEN_ALPHANUMERIC_KEYS43_tree = self.adaptor.createWithPayload(TOKEN_ALPHANUMERIC_KEYS43)
                    self.adaptor.addChild(root_0, TOKEN_ALPHANUMERIC_KEYS43_tree)

                    #action start
                    print "alphanumeric_keys", 
                    #action end


                elif alt6 == 5:
                    # XKBGrammar.g:159:4: TOKEN_ALTERNATE_GROUP
                    root_0 = self.adaptor.nil()

                    TOKEN_ALTERNATE_GROUP44 = self.input.LT(1)
                    self.match(self.input, TOKEN_ALTERNATE_GROUP, self.FOLLOW_TOKEN_ALTERNATE_GROUP_in_attribute_xkb732)


                    TOKEN_ALTERNATE_GROUP44_tree = self.adaptor.createWithPayload(TOKEN_ALTERNATE_GROUP44)
                    self.adaptor.addChild(root_0, TOKEN_ALTERNATE_GROUP44_tree)

                    #action start
                    print "alternate_group", 
                    #action end


                elif alt6 == 6:
                    # XKBGrammar.g:160:4: TOKEN_XKB_SYMBOLS
                    TOKEN_XKB_SYMBOLS45 = self.input.LT(1)
                    self.match(self.input, TOKEN_XKB_SYMBOLS, self.FOLLOW_TOKEN_XKB_SYMBOLS_in_attribute_xkb739)

                    stream_TOKEN_XKB_SYMBOLS.add(TOKEN_XKB_SYMBOLS45)
                    #action start
                    print "xkb_symbols", 
                    #action end
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
                    # 161:2: -> ^( ATTRIBUTES ATTRIBUTE )
                    # XKBGrammar.g:161:5: ^( ATTRIBUTES ATTRIBUTE )
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


 

    FOLLOW_section_in_layout361 = frozenset([4, 5, 6, 7, 9, 10])
    FOLLOW_EOF_in_layout364 = frozenset([1])
    FOLLOW_preamble_in_section380 = frozenset([17])
    FOLLOW_sectionmaterial_in_section382 = frozenset([1])
    FOLLOW_attribute_xkb_in_preamble407 = frozenset([4, 5, 6, 7, 9, 10, 20])
    FOLLOW_quotedstring_in_preamble412 = frozenset([1])
    FOLLOW_DQUOTE_in_quotedstring437 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39])
    FOLLOW_set_in_quotedstring441 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39])
    FOLLOW_DQUOTE_in_quotedstring447 = frozenset([1])
    FOLLOW_LCURLY_in_sectionmaterial477 = frozenset([11, 12, 13, 14])
    FOLLOW_line_include_in_sectionmaterial480 = frozenset([11, 12, 13, 14, 18])
    FOLLOW_line_name_in_sectionmaterial486 = frozenset([11, 12, 13, 14, 18])
    FOLLOW_line_keytype_in_sectionmaterial492 = frozenset([11, 12, 13, 14, 18])
    FOLLOW_line_key_in_sectionmaterial498 = frozenset([11, 12, 13, 14, 18])
    FOLLOW_RCURLY_in_sectionmaterial505 = frozenset([23])
    FOLLOW_SEMICOLON_in_sectionmaterial507 = frozenset([1])
    FOLLOW_TOKEN_INCLUDE_in_line_include518 = frozenset([20])
    FOLLOW_quotedstring_in_line_include522 = frozenset([1])
    FOLLOW_TOKEN_NAME_in_line_name537 = frozenset([15])
    FOLLOW_LBRACKET_in_line_name539 = frozenset([35])
    FOLLOW_NAME_in_line_name543 = frozenset([16])
    FOLLOW_RBRACKET_in_line_name545 = frozenset([24])
    FOLLOW_EQUAL_in_line_name547 = frozenset([20])
    FOLLOW_quotedstring_in_line_name551 = frozenset([23])
    FOLLOW_SEMICOLON_in_line_name553 = frozenset([1])
    FOLLOW_TOKEN_KEY_TYPE_in_line_keytype567 = frozenset([15])
    FOLLOW_LBRACKET_in_line_keytype569 = frozenset([35])
    FOLLOW_NAME_in_line_keytype573 = frozenset([16])
    FOLLOW_RBRACKET_in_line_keytype575 = frozenset([24])
    FOLLOW_EQUAL_in_line_keytype577 = frozenset([20])
    FOLLOW_DQUOTE_in_line_keytype579 = frozenset([35])
    FOLLOW_NAME_in_line_keytype583 = frozenset([20])
    FOLLOW_DQUOTE_in_line_keytype585 = frozenset([23])
    FOLLOW_SEMICOLON_in_line_keytype587 = frozenset([1])
    FOLLOW_TOKEN_KEY_in_line_key602 = frozenset([25])
    FOLLOW_keycode_in_line_key604 = frozenset([17])
    FOLLOW_keysyms_in_line_key606 = frozenset([23])
    FOLLOW_SEMICOLON_in_line_key608 = frozenset([1])
    FOLLOW_LOWERTHAN_in_keycode624 = frozenset([35])
    FOLLOW_NAME_in_keycode626 = frozenset([26])
    FOLLOW_GREATERTHAN_in_keycode628 = frozenset([1])
    FOLLOW_LCURLY_in_keysyms653 = frozenset([15])
    FOLLOW_LBRACKET_in_keysyms655 = frozenset([35])
    FOLLOW_NAME_in_keysyms659 = frozenset([16, 19])
    FOLLOW_COMMA_in_keysyms662 = frozenset([35])
    FOLLOW_NAME_in_keysyms666 = frozenset([16, 19])
    FOLLOW_RBRACKET_in_keysyms670 = frozenset([18])
    FOLLOW_RCURLY_in_keysyms672 = frozenset([1])
    FOLLOW_TOKEN_DEFAULT_in_attribute_xkb697 = frozenset([1])
    FOLLOW_TOKEN_HIDDEN_in_attribute_xkb705 = frozenset([1])
    FOLLOW_TOKEN_PARTIAL_in_attribute_xkb714 = frozenset([1])
    FOLLOW_TOKEN_ALPHANUMERIC_KEYS_in_attribute_xkb723 = frozenset([1])
    FOLLOW_TOKEN_ALTERNATE_GROUP_in_attribute_xkb732 = frozenset([1])
    FOLLOW_TOKEN_XKB_SYMBOLS_in_attribute_xkb739 = frozenset([1])

