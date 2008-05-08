# $ANTLR 3.0.1 XKBGrammar.g 2008-05-08 01:14:03

from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
TOKEN_ALTERNATE_GROUP=9
ATTRIBUTES=29
SECTION=35
TOKEN_INCLUDE=11
KEY=33
KEYTYPE=34
ATTRIBUTE=30
TOKEN_NAME=13
DQUOTE=21
LCURLY=18
SEMICOLON=24
TOKEN_MODIFIER_MAP=15
NAME_INCLUDE=39
MINUS=22
TOKEN_XKB_SYMBOLS=10
EOF=-1
SECTIONNAME=36
NAME_KEYSYM=38
NAME_GROUP=40
LBRACKET=16
NAME=32
TOKEN_PARTIAL=6
WS=42
NEWLINE=41
TOKEN_ALPHANUMERIC_KEYS=7
TOKEN_HIDDEN=5
COMMA=20
LOWERTHAN=26
INCLUDE=31
EQUAL=25
RCURLY=19
TOKEN_MODIFIER_KEYS=8
PLUS=23
TOKEN_KEY=14
RBRACKET=17
COMMENT=37
DOT=28
TOKEN_DEFAULT=4
TOKEN_KEY_TYPE=12
GREATERTHAN=27

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "TOKEN_DEFAULT", "TOKEN_HIDDEN", "TOKEN_PARTIAL", "TOKEN_ALPHANUMERIC_KEYS", 
    "TOKEN_MODIFIER_KEYS", "TOKEN_ALTERNATE_GROUP", "TOKEN_XKB_SYMBOLS", 
    "TOKEN_INCLUDE", "TOKEN_KEY_TYPE", "TOKEN_NAME", "TOKEN_KEY", "TOKEN_MODIFIER_MAP", 
    "LBRACKET", "RBRACKET", "LCURLY", "RCURLY", "COMMA", "DQUOTE", "MINUS", 
    "PLUS", "SEMICOLON", "EQUAL", "LOWERTHAN", "GREATERTHAN", "DOT", "ATTRIBUTES", 
    "ATTRIBUTE", "INCLUDE", "NAME", "KEY", "KEYTYPE", "SECTION", "SECTIONNAME", 
    "COMMENT", "NAME_KEYSYM", "NAME_INCLUDE", "NAME_GROUP", "NEWLINE", "WS"
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
    # XKBGrammar.g:55:1: layout : ( section )* EOF ;
    def layout(self, ):

        retval = self.layout_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF2 = None
        section1 = None


        EOF2_tree = None

        try:
            try:
                # XKBGrammar.g:55:9: ( ( section )* EOF )
                # XKBGrammar.g:55:11: ( section )* EOF
                root_0 = self.adaptor.nil()

                # XKBGrammar.g:55:11: ( section )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((TOKEN_DEFAULT <= LA1_0 <= TOKEN_ALPHANUMERIC_KEYS) or (TOKEN_ALTERNATE_GROUP <= LA1_0 <= TOKEN_XKB_SYMBOLS)) :
                        alt1 = 1


                    if alt1 == 1:
                        # XKBGrammar.g:55:11: section
                        self.following.append(self.FOLLOW_section_in_layout349)
                        section1 = self.section()
                        self.following.pop()

                        self.adaptor.addChild(root_0, section1.tree)


                    else:
                        break #loop1


                EOF2 = self.input.LT(1)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_layout352)




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
    # XKBGrammar.g:58:1: section : preamble sectionmaterial -> ^( SECTION ) ;
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
                # XKBGrammar.g:59:2: ( preamble sectionmaterial -> ^( SECTION ) )
                # XKBGrammar.g:60:2: preamble sectionmaterial
                self.following.append(self.FOLLOW_preamble_in_section368)
                preamble3 = self.preamble()
                self.following.pop()

                stream_preamble.add(preamble3.tree)
                self.following.append(self.FOLLOW_sectionmaterial_in_section370)
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
                # 62:2: -> ^( SECTION )
                # XKBGrammar.g:62:5: ^( SECTION )
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
    # XKBGrammar.g:65:1: preamble : ( attribute_xkb )+ sectionname= quotedstring ;
    def preamble(self, ):

        retval = self.preamble_return()
        retval.start = self.input.LT(1)

        root_0 = None

        sectionname = None

        attribute_xkb5 = None



        try:
            try:
                # XKBGrammar.g:65:10: ( ( attribute_xkb )+ sectionname= quotedstring )
                # XKBGrammar.g:65:12: ( attribute_xkb )+ sectionname= quotedstring
                root_0 = self.adaptor.nil()

                # XKBGrammar.g:65:12: ( attribute_xkb )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((TOKEN_DEFAULT <= LA2_0 <= TOKEN_ALPHANUMERIC_KEYS) or (TOKEN_ALTERNATE_GROUP <= LA2_0 <= TOKEN_XKB_SYMBOLS)) :
                        alt2 = 1


                    if alt2 == 1:
                        # XKBGrammar.g:65:12: attribute_xkb
                        self.following.append(self.FOLLOW_attribute_xkb_in_preamble391)
                        attribute_xkb5 = self.attribute_xkb()
                        self.following.pop()

                        self.adaptor.addChild(root_0, attribute_xkb5.tree)


                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1


                self.following.append(self.FOLLOW_quotedstring_in_preamble396)
                sectionname = self.quotedstring()
                self.following.pop()

                self.adaptor.addChild(root_0, sectionname.tree)
                #action start
                print '%(sname)s {' % { "sname": self.input.toString(sectionname.start,sectionname.stop) } 
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
    # XKBGrammar.g:69:1: quotedstring returns [value] : DQUOTE (sectionname+=~ ( DQUOTE ) )+ DQUOTE ;
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
                # XKBGrammar.g:70:2: ( DQUOTE (sectionname+=~ ( DQUOTE ) )+ DQUOTE )
                # XKBGrammar.g:70:4: DQUOTE (sectionname+=~ ( DQUOTE ) )+ DQUOTE
                root_0 = self.adaptor.nil()

                DQUOTE6 = self.input.LT(1)
                self.match(self.input, DQUOTE, self.FOLLOW_DQUOTE_in_quotedstring414)


                DQUOTE6_tree = self.adaptor.createWithPayload(DQUOTE6)
                self.adaptor.addChild(root_0, DQUOTE6_tree)

                # XKBGrammar.g:70:22: (sectionname+=~ ( DQUOTE ) )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((TOKEN_DEFAULT <= LA3_0 <= COMMA) or (MINUS <= LA3_0 <= WS)) :
                        alt3 = 1


                    if alt3 == 1:
                        # XKBGrammar.g:70:22: sectionname+=~ ( DQUOTE )
                        sectionname = self.input.LT(1)
                        if (TOKEN_DEFAULT <= self.input.LA(1) <= COMMA) or (MINUS <= self.input.LA(1) <= WS):
                            self.input.consume();
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(sectionname))
                            self.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_quotedstring418
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
                self.match(self.input, DQUOTE, self.FOLLOW_DQUOTE_in_quotedstring424)


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
    # XKBGrammar.g:80:1: sectionmaterial : LCURLY ( line_include | line_name | line_keytype | line_key | line_comment )+ RCURLY SEMICOLON ;
    def sectionmaterial(self, ):

        retval = self.sectionmaterial_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LCURLY8 = None
        RCURLY14 = None
        SEMICOLON15 = None
        line_include9 = None

        line_name10 = None

        line_keytype11 = None

        line_key12 = None

        line_comment13 = None


        LCURLY8_tree = None
        RCURLY14_tree = None
        SEMICOLON15_tree = None

        try:
            try:
                # XKBGrammar.g:81:2: ( LCURLY ( line_include | line_name | line_keytype | line_key | line_comment )+ RCURLY SEMICOLON )
                # XKBGrammar.g:81:4: LCURLY ( line_include | line_name | line_keytype | line_key | line_comment )+ RCURLY SEMICOLON
                root_0 = self.adaptor.nil()

                LCURLY8 = self.input.LT(1)
                self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_sectionmaterial438)


                LCURLY8_tree = self.adaptor.createWithPayload(LCURLY8)
                self.adaptor.addChild(root_0, LCURLY8_tree)

                # XKBGrammar.g:81:11: ( line_include | line_name | line_keytype | line_key | line_comment )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 6
                    LA4 = self.input.LA(1)
                    if LA4 == TOKEN_INCLUDE:
                        alt4 = 1
                    elif LA4 == TOKEN_NAME:
                        alt4 = 2
                    elif LA4 == TOKEN_KEY_TYPE:
                        alt4 = 3
                    elif LA4 == TOKEN_KEY:
                        alt4 = 4
                    elif LA4 == COMMENT:
                        alt4 = 5

                    if alt4 == 1:
                        # XKBGrammar.g:81:12: line_include
                        self.following.append(self.FOLLOW_line_include_in_sectionmaterial441)
                        line_include9 = self.line_include()
                        self.following.pop()

                        self.adaptor.addChild(root_0, line_include9.tree)


                    elif alt4 == 2:
                        # XKBGrammar.g:82:4: line_name
                        self.following.append(self.FOLLOW_line_name_in_sectionmaterial447)
                        line_name10 = self.line_name()
                        self.following.pop()

                        self.adaptor.addChild(root_0, line_name10.tree)


                    elif alt4 == 3:
                        # XKBGrammar.g:83:4: line_keytype
                        self.following.append(self.FOLLOW_line_keytype_in_sectionmaterial453)
                        line_keytype11 = self.line_keytype()
                        self.following.pop()

                        self.adaptor.addChild(root_0, line_keytype11.tree)


                    elif alt4 == 4:
                        # XKBGrammar.g:84:4: line_key
                        self.following.append(self.FOLLOW_line_key_in_sectionmaterial459)
                        line_key12 = self.line_key()
                        self.following.pop()

                        self.adaptor.addChild(root_0, line_key12.tree)


                    elif alt4 == 5:
                        # XKBGrammar.g:86:4: line_comment
                        self.following.append(self.FOLLOW_line_comment_in_sectionmaterial466)
                        line_comment13 = self.line_comment()
                        self.following.pop()

                        self.adaptor.addChild(root_0, line_comment13.tree)


                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1


                RCURLY14 = self.input.LT(1)
                self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_sectionmaterial470)


                RCURLY14_tree = self.adaptor.createWithPayload(RCURLY14)
                self.adaptor.addChild(root_0, RCURLY14_tree)

                SEMICOLON15 = self.input.LT(1)
                self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_sectionmaterial472)


                SEMICOLON15_tree = self.adaptor.createWithPayload(SEMICOLON15)
                self.adaptor.addChild(root_0, SEMICOLON15_tree)




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

    class line_comment_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start line_comment
    # XKBGrammar.g:89:1: line_comment : COMMENT ;
    def line_comment(self, ):

        retval = self.line_comment_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMENT16 = None

        COMMENT16_tree = None

        try:
            try:
                # XKBGrammar.g:90:2: ( COMMENT )
                # XKBGrammar.g:90:4: COMMENT
                root_0 = self.adaptor.nil()

                COMMENT16 = self.input.LT(1)
                self.match(self.input, COMMENT, self.FOLLOW_COMMENT_in_line_comment483)


                COMMENT16_tree = self.adaptor.createWithPayload(COMMENT16)
                self.adaptor.addChild(root_0, COMMENT16_tree)

                #action start
                skip(); 
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

    # $ANTLR end line_comment

    class line_include_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start line_include
    # XKBGrammar.g:92:1: line_include : TOKEN_INCLUDE include= quotedstring ;
    def line_include(self, ):

        retval = self.line_include_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TOKEN_INCLUDE17 = None
        include = None


        TOKEN_INCLUDE17_tree = None

        try:
            try:
                # XKBGrammar.g:94:2: ( TOKEN_INCLUDE include= quotedstring )
                # XKBGrammar.g:94:4: TOKEN_INCLUDE include= quotedstring
                root_0 = self.adaptor.nil()

                TOKEN_INCLUDE17 = self.input.LT(1)
                self.match(self.input, TOKEN_INCLUDE, self.FOLLOW_TOKEN_INCLUDE_in_line_include497)


                TOKEN_INCLUDE17_tree = self.adaptor.createWithPayload(TOKEN_INCLUDE17)
                self.adaptor.addChild(root_0, TOKEN_INCLUDE17_tree)

                self.following.append(self.FOLLOW_quotedstring_in_line_include501)
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
    # XKBGrammar.g:98:1: line_name : TOKEN_NAME LBRACKET name= NAME RBRACKET EQUAL nameval= quotedstring SEMICOLON ;
    def line_name(self, ):

        retval = self.line_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        name = None
        TOKEN_NAME18 = None
        LBRACKET19 = None
        RBRACKET20 = None
        EQUAL21 = None
        SEMICOLON22 = None
        nameval = None


        name_tree = None
        TOKEN_NAME18_tree = None
        LBRACKET19_tree = None
        RBRACKET20_tree = None
        EQUAL21_tree = None
        SEMICOLON22_tree = None

        try:
            try:
                # XKBGrammar.g:99:2: ( TOKEN_NAME LBRACKET name= NAME RBRACKET EQUAL nameval= quotedstring SEMICOLON )
                # XKBGrammar.g:99:4: TOKEN_NAME LBRACKET name= NAME RBRACKET EQUAL nameval= quotedstring SEMICOLON
                root_0 = self.adaptor.nil()

                TOKEN_NAME18 = self.input.LT(1)
                self.match(self.input, TOKEN_NAME, self.FOLLOW_TOKEN_NAME_in_line_name516)


                TOKEN_NAME18_tree = self.adaptor.createWithPayload(TOKEN_NAME18)
                self.adaptor.addChild(root_0, TOKEN_NAME18_tree)

                LBRACKET19 = self.input.LT(1)
                self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_line_name518)


                LBRACKET19_tree = self.adaptor.createWithPayload(LBRACKET19)
                self.adaptor.addChild(root_0, LBRACKET19_tree)

                name = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_name522)


                name_tree = self.adaptor.createWithPayload(name)
                self.adaptor.addChild(root_0, name_tree)

                RBRACKET20 = self.input.LT(1)
                self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_line_name524)


                RBRACKET20_tree = self.adaptor.createWithPayload(RBRACKET20)
                self.adaptor.addChild(root_0, RBRACKET20_tree)

                EQUAL21 = self.input.LT(1)
                self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_line_name526)


                EQUAL21_tree = self.adaptor.createWithPayload(EQUAL21)
                self.adaptor.addChild(root_0, EQUAL21_tree)

                self.following.append(self.FOLLOW_quotedstring_in_line_name530)
                nameval = self.quotedstring()
                self.following.pop()

                self.adaptor.addChild(root_0, nameval.tree)
                SEMICOLON22 = self.input.LT(1)
                self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_line_name532)


                SEMICOLON22_tree = self.adaptor.createWithPayload(SEMICOLON22)
                self.adaptor.addChild(root_0, SEMICOLON22_tree)

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
    # XKBGrammar.g:103:1: line_keytype : TOKEN_KEY_TYPE LBRACKET keytype= NAME RBRACKET EQUAL DQUOTE keytypevalue= NAME DQUOTE SEMICOLON ;
    def line_keytype(self, ):

        retval = self.line_keytype_return()
        retval.start = self.input.LT(1)

        root_0 = None

        keytype = None
        keytypevalue = None
        TOKEN_KEY_TYPE23 = None
        LBRACKET24 = None
        RBRACKET25 = None
        EQUAL26 = None
        DQUOTE27 = None
        DQUOTE28 = None
        SEMICOLON29 = None

        keytype_tree = None
        keytypevalue_tree = None
        TOKEN_KEY_TYPE23_tree = None
        LBRACKET24_tree = None
        RBRACKET25_tree = None
        EQUAL26_tree = None
        DQUOTE27_tree = None
        DQUOTE28_tree = None
        SEMICOLON29_tree = None

        try:
            try:
                # XKBGrammar.g:104:2: ( TOKEN_KEY_TYPE LBRACKET keytype= NAME RBRACKET EQUAL DQUOTE keytypevalue= NAME DQUOTE SEMICOLON )
                # XKBGrammar.g:104:4: TOKEN_KEY_TYPE LBRACKET keytype= NAME RBRACKET EQUAL DQUOTE keytypevalue= NAME DQUOTE SEMICOLON
                root_0 = self.adaptor.nil()

                TOKEN_KEY_TYPE23 = self.input.LT(1)
                self.match(self.input, TOKEN_KEY_TYPE, self.FOLLOW_TOKEN_KEY_TYPE_in_line_keytype546)


                TOKEN_KEY_TYPE23_tree = self.adaptor.createWithPayload(TOKEN_KEY_TYPE23)
                self.adaptor.addChild(root_0, TOKEN_KEY_TYPE23_tree)

                LBRACKET24 = self.input.LT(1)
                self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_line_keytype548)


                LBRACKET24_tree = self.adaptor.createWithPayload(LBRACKET24)
                self.adaptor.addChild(root_0, LBRACKET24_tree)

                keytype = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype552)


                keytype_tree = self.adaptor.createWithPayload(keytype)
                self.adaptor.addChild(root_0, keytype_tree)

                RBRACKET25 = self.input.LT(1)
                self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_line_keytype554)


                RBRACKET25_tree = self.adaptor.createWithPayload(RBRACKET25)
                self.adaptor.addChild(root_0, RBRACKET25_tree)

                EQUAL26 = self.input.LT(1)
                self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_line_keytype556)


                EQUAL26_tree = self.adaptor.createWithPayload(EQUAL26)
                self.adaptor.addChild(root_0, EQUAL26_tree)

                DQUOTE27 = self.input.LT(1)
                self.match(self.input, DQUOTE, self.FOLLOW_DQUOTE_in_line_keytype558)


                DQUOTE27_tree = self.adaptor.createWithPayload(DQUOTE27)
                self.adaptor.addChild(root_0, DQUOTE27_tree)

                keytypevalue = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype562)


                keytypevalue_tree = self.adaptor.createWithPayload(keytypevalue)
                self.adaptor.addChild(root_0, keytypevalue_tree)

                DQUOTE28 = self.input.LT(1)
                self.match(self.input, DQUOTE, self.FOLLOW_DQUOTE_in_line_keytype564)


                DQUOTE28_tree = self.adaptor.createWithPayload(DQUOTE28)
                self.adaptor.addChild(root_0, DQUOTE28_tree)

                SEMICOLON29 = self.input.LT(1)
                self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_line_keytype566)


                SEMICOLON29_tree = self.adaptor.createWithPayload(SEMICOLON29)
                self.adaptor.addChild(root_0, SEMICOLON29_tree)

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
    # XKBGrammar.g:113:1: line_key : TOKEN_KEY keycode keysyms SEMICOLON ;
    def line_key(self, ):

        retval = self.line_key_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TOKEN_KEY30 = None
        SEMICOLON33 = None
        keycode31 = None

        keysyms32 = None


        TOKEN_KEY30_tree = None
        SEMICOLON33_tree = None

        try:
            try:
                # XKBGrammar.g:114:2: ( TOKEN_KEY keycode keysyms SEMICOLON )
                # XKBGrammar.g:114:4: TOKEN_KEY keycode keysyms SEMICOLON
                root_0 = self.adaptor.nil()

                TOKEN_KEY30 = self.input.LT(1)
                self.match(self.input, TOKEN_KEY, self.FOLLOW_TOKEN_KEY_in_line_key586)


                TOKEN_KEY30_tree = self.adaptor.createWithPayload(TOKEN_KEY30)
                self.adaptor.addChild(root_0, TOKEN_KEY30_tree)

                self.following.append(self.FOLLOW_keycode_in_line_key588)
                keycode31 = self.keycode()
                self.following.pop()

                self.adaptor.addChild(root_0, keycode31.tree)
                self.following.append(self.FOLLOW_keysyms_in_line_key590)
                keysyms32 = self.keysyms()
                self.following.pop()

                self.adaptor.addChild(root_0, keysyms32.tree)
                SEMICOLON33 = self.input.LT(1)
                self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_line_key592)


                SEMICOLON33_tree = self.adaptor.createWithPayload(SEMICOLON33)
                self.adaptor.addChild(root_0, SEMICOLON33_tree)

                #action start
                print "\tkey %(keycode)s %(keysyms)s ;" % {  "keycode": self.input.toString(keycode31.start,keycode31.stop), "keysyms": self.input.toString(keysyms32.start,keysyms32.stop) } 
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
    # XKBGrammar.g:118:1: keycode : LOWERTHAN NAME GREATERTHAN -> ^( INCLUDE NAME ) ;
    def keycode(self, ):

        retval = self.keycode_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LOWERTHAN34 = None
        NAME35 = None
        GREATERTHAN36 = None

        LOWERTHAN34_tree = None
        NAME35_tree = None
        GREATERTHAN36_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_LOWERTHAN = RewriteRuleTokenStream(self.adaptor, "token LOWERTHAN")
        stream_GREATERTHAN = RewriteRuleTokenStream(self.adaptor, "token GREATERTHAN")

        try:
            try:
                # XKBGrammar.g:119:2: ( LOWERTHAN NAME GREATERTHAN -> ^( INCLUDE NAME ) )
                # XKBGrammar.g:119:4: LOWERTHAN NAME GREATERTHAN
                LOWERTHAN34 = self.input.LT(1)
                self.match(self.input, LOWERTHAN, self.FOLLOW_LOWERTHAN_in_keycode608)

                stream_LOWERTHAN.add(LOWERTHAN34)
                NAME35 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode610)

                stream_NAME.add(NAME35)
                GREATERTHAN36 = self.input.LT(1)
                self.match(self.input, GREATERTHAN, self.FOLLOW_GREATERTHAN_in_keycode612)

                stream_GREATERTHAN.add(GREATERTHAN36)
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
                # 120:2: -> ^( INCLUDE NAME )
                # XKBGrammar.g:120:5: ^( INCLUDE NAME )
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
    # XKBGrammar.g:123:1: keysyms : LCURLY LBRACKET ( NAME | NAME_KEYSYM ) ( COMMA ( NAME | NAME_KEYSYM ) )* RBRACKET RCURLY ;
    def keysyms(self, ):

        retval = self.keysyms_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LCURLY37 = None
        LBRACKET38 = None
        set39 = None
        COMMA40 = None
        set41 = None
        RBRACKET42 = None
        RCURLY43 = None

        LCURLY37_tree = None
        LBRACKET38_tree = None
        set39_tree = None
        COMMA40_tree = None
        set41_tree = None
        RBRACKET42_tree = None
        RCURLY43_tree = None

        try:
            try:
                # XKBGrammar.g:124:2: ( LCURLY LBRACKET ( NAME | NAME_KEYSYM ) ( COMMA ( NAME | NAME_KEYSYM ) )* RBRACKET RCURLY )
                # XKBGrammar.g:124:4: LCURLY LBRACKET ( NAME | NAME_KEYSYM ) ( COMMA ( NAME | NAME_KEYSYM ) )* RBRACKET RCURLY
                root_0 = self.adaptor.nil()

                LCURLY37 = self.input.LT(1)
                self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_keysyms634)


                LCURLY37_tree = self.adaptor.createWithPayload(LCURLY37)
                self.adaptor.addChild(root_0, LCURLY37_tree)

                LBRACKET38 = self.input.LT(1)
                self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_keysyms636)


                LBRACKET38_tree = self.adaptor.createWithPayload(LBRACKET38)
                self.adaptor.addChild(root_0, LBRACKET38_tree)

                set39 = self.input.LT(1)
                if self.input.LA(1) == NAME or self.input.LA(1) == NAME_KEYSYM:
                    self.input.consume();
                    self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set39))
                    self.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_keysyms638
                        )
                    raise mse


                # XKBGrammar.g:124:39: ( COMMA ( NAME | NAME_KEYSYM ) )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == COMMA) :
                        alt5 = 1


                    if alt5 == 1:
                        # XKBGrammar.g:124:40: COMMA ( NAME | NAME_KEYSYM )
                        COMMA40 = self.input.LT(1)
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_keysyms645)


                        COMMA40_tree = self.adaptor.createWithPayload(COMMA40)
                        self.adaptor.addChild(root_0, COMMA40_tree)

                        set41 = self.input.LT(1)
                        if self.input.LA(1) == NAME or self.input.LA(1) == NAME_KEYSYM:
                            self.input.consume();
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set41))
                            self.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_keysyms647
                                )
                            raise mse




                    else:
                        break #loop5


                RBRACKET42 = self.input.LT(1)
                self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_keysyms655)


                RBRACKET42_tree = self.adaptor.createWithPayload(RBRACKET42)
                self.adaptor.addChild(root_0, RBRACKET42_tree)

                RCURLY43 = self.input.LT(1)
                self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_keysyms657)


                RCURLY43_tree = self.adaptor.createWithPayload(RCURLY43)
                self.adaptor.addChild(root_0, RCURLY43_tree)




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
    # XKBGrammar.g:131:1: attribute_xkb : ( TOKEN_DEFAULT | TOKEN_HIDDEN | TOKEN_PARTIAL | TOKEN_ALPHANUMERIC_KEYS | TOKEN_ALTERNATE_GROUP | TOKEN_XKB_SYMBOLS -> ^( ATTRIBUTES ATTRIBUTE ) );
    def attribute_xkb(self, ):

        retval = self.attribute_xkb_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TOKEN_DEFAULT44 = None
        TOKEN_HIDDEN45 = None
        TOKEN_PARTIAL46 = None
        TOKEN_ALPHANUMERIC_KEYS47 = None
        TOKEN_ALTERNATE_GROUP48 = None
        TOKEN_XKB_SYMBOLS49 = None

        TOKEN_DEFAULT44_tree = None
        TOKEN_HIDDEN45_tree = None
        TOKEN_PARTIAL46_tree = None
        TOKEN_ALPHANUMERIC_KEYS47_tree = None
        TOKEN_ALTERNATE_GROUP48_tree = None
        TOKEN_XKB_SYMBOLS49_tree = None
        stream_TOKEN_XKB_SYMBOLS = RewriteRuleTokenStream(self.adaptor, "token TOKEN_XKB_SYMBOLS")

        try:
            try:
                # XKBGrammar.g:132:2: ( TOKEN_DEFAULT | TOKEN_HIDDEN | TOKEN_PARTIAL | TOKEN_ALPHANUMERIC_KEYS | TOKEN_ALTERNATE_GROUP | TOKEN_XKB_SYMBOLS -> ^( ATTRIBUTES ATTRIBUTE ) )
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
                    nvae = NoViableAltException("131:1: attribute_xkb : ( TOKEN_DEFAULT | TOKEN_HIDDEN | TOKEN_PARTIAL | TOKEN_ALPHANUMERIC_KEYS | TOKEN_ALTERNATE_GROUP | TOKEN_XKB_SYMBOLS -> ^( ATTRIBUTES ATTRIBUTE ) );", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # XKBGrammar.g:132:4: TOKEN_DEFAULT
                    root_0 = self.adaptor.nil()

                    TOKEN_DEFAULT44 = self.input.LT(1)
                    self.match(self.input, TOKEN_DEFAULT, self.FOLLOW_TOKEN_DEFAULT_in_attribute_xkb674)


                    TOKEN_DEFAULT44_tree = self.adaptor.createWithPayload(TOKEN_DEFAULT44)
                    self.adaptor.addChild(root_0, TOKEN_DEFAULT44_tree)

                    #action start
                    print "default", 
                    #action end


                elif alt6 == 2:
                    # XKBGrammar.g:133:4: TOKEN_HIDDEN
                    root_0 = self.adaptor.nil()

                    TOKEN_HIDDEN45 = self.input.LT(1)
                    self.match(self.input, TOKEN_HIDDEN, self.FOLLOW_TOKEN_HIDDEN_in_attribute_xkb682)


                    TOKEN_HIDDEN45_tree = self.adaptor.createWithPayload(TOKEN_HIDDEN45)
                    self.adaptor.addChild(root_0, TOKEN_HIDDEN45_tree)

                    #action start
                    print "hidden", 
                    #action end


                elif alt6 == 3:
                    # XKBGrammar.g:134:4: TOKEN_PARTIAL
                    root_0 = self.adaptor.nil()

                    TOKEN_PARTIAL46 = self.input.LT(1)
                    self.match(self.input, TOKEN_PARTIAL, self.FOLLOW_TOKEN_PARTIAL_in_attribute_xkb691)


                    TOKEN_PARTIAL46_tree = self.adaptor.createWithPayload(TOKEN_PARTIAL46)
                    self.adaptor.addChild(root_0, TOKEN_PARTIAL46_tree)

                    #action start
                    print "partial", 
                    #action end


                elif alt6 == 4:
                    # XKBGrammar.g:135:4: TOKEN_ALPHANUMERIC_KEYS
                    root_0 = self.adaptor.nil()

                    TOKEN_ALPHANUMERIC_KEYS47 = self.input.LT(1)
                    self.match(self.input, TOKEN_ALPHANUMERIC_KEYS, self.FOLLOW_TOKEN_ALPHANUMERIC_KEYS_in_attribute_xkb700)


                    TOKEN_ALPHANUMERIC_KEYS47_tree = self.adaptor.createWithPayload(TOKEN_ALPHANUMERIC_KEYS47)
                    self.adaptor.addChild(root_0, TOKEN_ALPHANUMERIC_KEYS47_tree)

                    #action start
                    print "alphanumeric_keys", 
                    #action end


                elif alt6 == 5:
                    # XKBGrammar.g:137:4: TOKEN_ALTERNATE_GROUP
                    root_0 = self.adaptor.nil()

                    TOKEN_ALTERNATE_GROUP48 = self.input.LT(1)
                    self.match(self.input, TOKEN_ALTERNATE_GROUP, self.FOLLOW_TOKEN_ALTERNATE_GROUP_in_attribute_xkb710)


                    TOKEN_ALTERNATE_GROUP48_tree = self.adaptor.createWithPayload(TOKEN_ALTERNATE_GROUP48)
                    self.adaptor.addChild(root_0, TOKEN_ALTERNATE_GROUP48_tree)

                    #action start
                    print "alternate_group", 
                    #action end


                elif alt6 == 6:
                    # XKBGrammar.g:138:4: TOKEN_XKB_SYMBOLS
                    TOKEN_XKB_SYMBOLS49 = self.input.LT(1)
                    self.match(self.input, TOKEN_XKB_SYMBOLS, self.FOLLOW_TOKEN_XKB_SYMBOLS_in_attribute_xkb717)

                    stream_TOKEN_XKB_SYMBOLS.add(TOKEN_XKB_SYMBOLS49)
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
                    # 139:2: -> ^( ATTRIBUTES ATTRIBUTE )
                    # XKBGrammar.g:139:5: ^( ATTRIBUTES ATTRIBUTE )
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


 

    FOLLOW_section_in_layout349 = frozenset([4, 5, 6, 7, 9, 10])
    FOLLOW_EOF_in_layout352 = frozenset([1])
    FOLLOW_preamble_in_section368 = frozenset([18])
    FOLLOW_sectionmaterial_in_section370 = frozenset([1])
    FOLLOW_attribute_xkb_in_preamble391 = frozenset([4, 5, 6, 7, 9, 10, 21])
    FOLLOW_quotedstring_in_preamble396 = frozenset([1])
    FOLLOW_DQUOTE_in_quotedstring414 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42])
    FOLLOW_set_in_quotedstring418 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42])
    FOLLOW_DQUOTE_in_quotedstring424 = frozenset([1])
    FOLLOW_LCURLY_in_sectionmaterial438 = frozenset([11, 12, 13, 14, 37])
    FOLLOW_line_include_in_sectionmaterial441 = frozenset([11, 12, 13, 14, 19, 37])
    FOLLOW_line_name_in_sectionmaterial447 = frozenset([11, 12, 13, 14, 19, 37])
    FOLLOW_line_keytype_in_sectionmaterial453 = frozenset([11, 12, 13, 14, 19, 37])
    FOLLOW_line_key_in_sectionmaterial459 = frozenset([11, 12, 13, 14, 19, 37])
    FOLLOW_line_comment_in_sectionmaterial466 = frozenset([11, 12, 13, 14, 19, 37])
    FOLLOW_RCURLY_in_sectionmaterial470 = frozenset([24])
    FOLLOW_SEMICOLON_in_sectionmaterial472 = frozenset([1])
    FOLLOW_COMMENT_in_line_comment483 = frozenset([1])
    FOLLOW_TOKEN_INCLUDE_in_line_include497 = frozenset([21])
    FOLLOW_quotedstring_in_line_include501 = frozenset([1])
    FOLLOW_TOKEN_NAME_in_line_name516 = frozenset([16])
    FOLLOW_LBRACKET_in_line_name518 = frozenset([32])
    FOLLOW_NAME_in_line_name522 = frozenset([17])
    FOLLOW_RBRACKET_in_line_name524 = frozenset([25])
    FOLLOW_EQUAL_in_line_name526 = frozenset([21])
    FOLLOW_quotedstring_in_line_name530 = frozenset([24])
    FOLLOW_SEMICOLON_in_line_name532 = frozenset([1])
    FOLLOW_TOKEN_KEY_TYPE_in_line_keytype546 = frozenset([16])
    FOLLOW_LBRACKET_in_line_keytype548 = frozenset([32])
    FOLLOW_NAME_in_line_keytype552 = frozenset([17])
    FOLLOW_RBRACKET_in_line_keytype554 = frozenset([25])
    FOLLOW_EQUAL_in_line_keytype556 = frozenset([21])
    FOLLOW_DQUOTE_in_line_keytype558 = frozenset([32])
    FOLLOW_NAME_in_line_keytype562 = frozenset([21])
    FOLLOW_DQUOTE_in_line_keytype564 = frozenset([24])
    FOLLOW_SEMICOLON_in_line_keytype566 = frozenset([1])
    FOLLOW_TOKEN_KEY_in_line_key586 = frozenset([26])
    FOLLOW_keycode_in_line_key588 = frozenset([18])
    FOLLOW_keysyms_in_line_key590 = frozenset([24])
    FOLLOW_SEMICOLON_in_line_key592 = frozenset([1])
    FOLLOW_LOWERTHAN_in_keycode608 = frozenset([32])
    FOLLOW_NAME_in_keycode610 = frozenset([27])
    FOLLOW_GREATERTHAN_in_keycode612 = frozenset([1])
    FOLLOW_LCURLY_in_keysyms634 = frozenset([16])
    FOLLOW_LBRACKET_in_keysyms636 = frozenset([32, 38])
    FOLLOW_set_in_keysyms638 = frozenset([17, 20])
    FOLLOW_COMMA_in_keysyms645 = frozenset([32, 38])
    FOLLOW_set_in_keysyms647 = frozenset([17, 20])
    FOLLOW_RBRACKET_in_keysyms655 = frozenset([19])
    FOLLOW_RCURLY_in_keysyms657 = frozenset([1])
    FOLLOW_TOKEN_DEFAULT_in_attribute_xkb674 = frozenset([1])
    FOLLOW_TOKEN_HIDDEN_in_attribute_xkb682 = frozenset([1])
    FOLLOW_TOKEN_PARTIAL_in_attribute_xkb691 = frozenset([1])
    FOLLOW_TOKEN_ALPHANUMERIC_KEYS_in_attribute_xkb700 = frozenset([1])
    FOLLOW_TOKEN_ALTERNATE_GROUP_in_attribute_xkb710 = frozenset([1])
    FOLLOW_TOKEN_XKB_SYMBOLS_in_attribute_xkb717 = frozenset([1])

