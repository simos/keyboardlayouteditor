# $ANTLR 3.0.1 XKBGrammar.g 2008-05-09 21:53:06

from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



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
EOF=-1
GENERIC_NAME=38
SECTIONNAME=36
MAPTYPE=28
LBRACKET=15
NAME=37
TOKEN_PARTIAL=6
WS=39
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
COMMENT=40
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
    "SEMICOLON", "EQUAL", "LOWERTHAN", "GREATERTHAN", "DOT", "MAPTYPE", 
    "ATTRIBUTES", "ATTRIBUTE", "INCLUDE", "KEY", "KEYTYPE", "KEYCODE", "SECTION", 
    "SECTIONNAME", "NAME", "GENERIC_NAME", "WS", "COMMENT", "LINE_COMMENT"
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
    # XKBGrammar.g:76:1: layout : ( section )+ ;
    def layout(self, ):

        retval = self.layout_return()
        retval.start = self.input.LT(1)

        root_0 = None

        section1 = None



        try:
            try:
                # XKBGrammar.g:77:2: ( ( section )+ )
                # XKBGrammar.g:77:4: ( section )+
                root_0 = self.adaptor.nil()

                # XKBGrammar.g:77:4: ( section )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((TOKEN_DEFAULT <= LA1_0 <= TOKEN_ALPHANUMERIC_KEYS) or (TOKEN_ALTERNATE_GROUP <= LA1_0 <= TOKEN_XKB_SYMBOLS)) :
                        alt1 = 1


                    if alt1 == 1:
                        # XKBGrammar.g:77:4: section
                        self.following.append(self.FOLLOW_section_in_layout369)
                        section1 = self.section()
                        self.following.pop()

                        self.adaptor.addChild(root_0, section1.tree)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1





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
    # XKBGrammar.g:80:1: section : mapType sectionmaterial ;
    def section(self, ):

        retval = self.section_return()
        retval.start = self.input.LT(1)

        root_0 = None

        mapType2 = None

        sectionmaterial3 = None



        try:
            try:
                # XKBGrammar.g:81:2: ( mapType sectionmaterial )
                # XKBGrammar.g:81:4: mapType sectionmaterial
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_mapType_in_section383)
                mapType2 = self.mapType()
                self.following.pop()

                self.adaptor.addChild(root_0, mapType2.tree)
                self.following.append(self.FOLLOW_sectionmaterial_in_section385)
                sectionmaterial3 = self.sectionmaterial()
                self.following.pop()

                self.adaptor.addChild(root_0, sectionmaterial3.tree)
                #action start
                print '}' 
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

    # $ANTLR end section

    class mapType_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mapType
    # XKBGrammar.g:85:1: mapType : ( mapOptions )+ sectionname= quotedstring -> ^( MAPTYPE ( mapOptions )+ $sectionname) ;
    def mapType(self, ):

        retval = self.mapType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        sectionname = None

        mapOptions4 = None


        stream_quotedstring = RewriteRuleSubtreeStream(self.adaptor, "rule quotedstring")
        stream_mapOptions = RewriteRuleSubtreeStream(self.adaptor, "rule mapOptions")
        try:
            try:
                # XKBGrammar.g:86:2: ( ( mapOptions )+ sectionname= quotedstring -> ^( MAPTYPE ( mapOptions )+ $sectionname) )
                # XKBGrammar.g:86:4: ( mapOptions )+ sectionname= quotedstring
                # XKBGrammar.g:86:4: ( mapOptions )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((TOKEN_DEFAULT <= LA2_0 <= TOKEN_ALPHANUMERIC_KEYS) or (TOKEN_ALTERNATE_GROUP <= LA2_0 <= TOKEN_XKB_SYMBOLS)) :
                        alt2 = 1


                    if alt2 == 1:
                        # XKBGrammar.g:86:4: mapOptions
                        self.following.append(self.FOLLOW_mapOptions_in_mapType401)
                        mapOptions4 = self.mapOptions()
                        self.following.pop()

                        stream_mapOptions.add(mapOptions4.tree)


                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1


                self.following.append(self.FOLLOW_quotedstring_in_mapType406)
                sectionname = self.quotedstring()
                self.following.pop()

                stream_quotedstring.add(sectionname.tree)
                #action start
                print '%(sectionname)s {' % { "sectionname": self.input.toString(sectionname.start,sectionname.stop) } 
                #action end
                # AST Rewrite
                # elements: mapOptions, sectionname
                # token labels: 
                # rule labels: retval, sectionname
                # token list labels: 
                # rule list labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                if sectionname is not None:
                    stream_sectionname = RewriteRuleSubtreeStream(self.adaptor, "token sectionname", sectionname.tree)
                else:
                    stream_sectionname = RewriteRuleSubtreeStream(self.adaptor, "token sectionname", None)


                root_0 = self.adaptor.nil()
                # 88:2: -> ^( MAPTYPE ( mapOptions )+ $sectionname)
                # XKBGrammar.g:88:5: ^( MAPTYPE ( mapOptions )+ $sectionname)
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPTYPE, "MAPTYPE"), root_1)

                # XKBGrammar.g:88:15: ( mapOptions )+
                if not (stream_mapOptions.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_mapOptions.hasNext():
                    self.adaptor.addChild(root_1, stream_mapOptions.next())


                stream_mapOptions.reset()
                self.adaptor.addChild(root_1, stream_sectionname.next())

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

    # $ANTLR end mapType

    class quotedstring_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.value = None
            self.tree = None


    # $ANTLR start quotedstring
    # XKBGrammar.g:91:1: quotedstring returns [value] : DQUOTE (sectionname+=~ ( DQUOTE ) )+ DQUOTE ;
    def quotedstring(self, ):

        retval = self.quotedstring_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DQUOTE5 = None
        DQUOTE6 = None
        sectionname = None
        list_sectionname = None

        DQUOTE5_tree = None
        DQUOTE6_tree = None
        sectionname_tree = None

        try:
            try:
                # XKBGrammar.g:92:9: ( DQUOTE (sectionname+=~ ( DQUOTE ) )+ DQUOTE )
                # XKBGrammar.g:92:11: DQUOTE (sectionname+=~ ( DQUOTE ) )+ DQUOTE
                root_0 = self.adaptor.nil()

                DQUOTE5 = self.input.LT(1)
                self.match(self.input, DQUOTE, self.FOLLOW_DQUOTE_in_quotedstring444)


                DQUOTE5_tree = self.adaptor.createWithPayload(DQUOTE5)
                self.adaptor.addChild(root_0, DQUOTE5_tree)

                # XKBGrammar.g:92:29: (sectionname+=~ ( DQUOTE ) )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((TOKEN_DEFAULT <= LA3_0 <= COMMA) or (MINUS <= LA3_0 <= LINE_COMMENT)) :
                        alt3 = 1


                    if alt3 == 1:
                        # XKBGrammar.g:92:29: sectionname+=~ ( DQUOTE )
                        sectionname = self.input.LT(1)
                        if (TOKEN_DEFAULT <= self.input.LA(1) <= COMMA) or (MINUS <= self.input.LA(1) <= LINE_COMMENT):
                            self.input.consume();
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(sectionname))
                            self.errorRecovery = False

                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_quotedstring448
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


                DQUOTE6 = self.input.LT(1)
                self.match(self.input, DQUOTE, self.FOLLOW_DQUOTE_in_quotedstring454)


                DQUOTE6_tree = self.adaptor.createWithPayload(DQUOTE6)
                self.adaptor.addChild(root_0, DQUOTE6_tree)

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
    # XKBGrammar.g:102:1: sectionmaterial : lc= LCURLY ( line_include | line_name | line_keytype | line_key )+ RCURLY SEMICOLON -> ^( SECTION ) ;
    def sectionmaterial(self, ):

        retval = self.sectionmaterial_return()
        retval.start = self.input.LT(1)

        root_0 = None

        lc = None
        RCURLY11 = None
        SEMICOLON12 = None
        line_include7 = None

        line_name8 = None

        line_keytype9 = None

        line_key10 = None


        lc_tree = None
        RCURLY11_tree = None
        SEMICOLON12_tree = None
        stream_LCURLY = RewriteRuleTokenStream(self.adaptor, "token LCURLY")
        stream_SEMICOLON = RewriteRuleTokenStream(self.adaptor, "token SEMICOLON")
        stream_RCURLY = RewriteRuleTokenStream(self.adaptor, "token RCURLY")
        stream_line_name = RewriteRuleSubtreeStream(self.adaptor, "rule line_name")
        stream_line_include = RewriteRuleSubtreeStream(self.adaptor, "rule line_include")
        stream_line_keytype = RewriteRuleSubtreeStream(self.adaptor, "rule line_keytype")
        stream_line_key = RewriteRuleSubtreeStream(self.adaptor, "rule line_key")
        try:
            try:
                # XKBGrammar.g:103:2: (lc= LCURLY ( line_include | line_name | line_keytype | line_key )+ RCURLY SEMICOLON -> ^( SECTION ) )
                # XKBGrammar.g:103:4: lc= LCURLY ( line_include | line_name | line_keytype | line_key )+ RCURLY SEMICOLON
                lc = self.input.LT(1)
                self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_sectionmaterial486)

                stream_LCURLY.add(lc)
                # XKBGrammar.g:103:14: ( line_include | line_name | line_keytype | line_key )+
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
                        # XKBGrammar.g:103:15: line_include
                        self.following.append(self.FOLLOW_line_include_in_sectionmaterial489)
                        line_include7 = self.line_include()
                        self.following.pop()

                        stream_line_include.add(line_include7.tree)


                    elif alt4 == 2:
                        # XKBGrammar.g:104:4: line_name
                        self.following.append(self.FOLLOW_line_name_in_sectionmaterial495)
                        line_name8 = self.line_name()
                        self.following.pop()

                        stream_line_name.add(line_name8.tree)


                    elif alt4 == 3:
                        # XKBGrammar.g:105:4: line_keytype
                        self.following.append(self.FOLLOW_line_keytype_in_sectionmaterial501)
                        line_keytype9 = self.line_keytype()
                        self.following.pop()

                        stream_line_keytype.add(line_keytype9.tree)


                    elif alt4 == 4:
                        # XKBGrammar.g:106:4: line_key
                        self.following.append(self.FOLLOW_line_key_in_sectionmaterial507)
                        line_key10 = self.line_key()
                        self.following.pop()

                        stream_line_key.add(line_key10.tree)


                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1


                RCURLY11 = self.input.LT(1)
                self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_sectionmaterial514)

                stream_RCURLY.add(RCURLY11)
                SEMICOLON12 = self.input.LT(1)
                self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_sectionmaterial516)

                stream_SEMICOLON.add(SEMICOLON12)
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
                # 108:2: -> ^( SECTION )
                # XKBGrammar.g:108:5: ^( SECTION )
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

    # $ANTLR end sectionmaterial

    class line_include_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start line_include
    # XKBGrammar.g:111:1: line_include : TOKEN_INCLUDE include= quotedstring -> ^( TOKEN_INCLUDE $include) ;
    def line_include(self, ):

        retval = self.line_include_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TOKEN_INCLUDE13 = None
        include = None


        TOKEN_INCLUDE13_tree = None
        stream_TOKEN_INCLUDE = RewriteRuleTokenStream(self.adaptor, "token TOKEN_INCLUDE")
        stream_quotedstring = RewriteRuleSubtreeStream(self.adaptor, "rule quotedstring")
        try:
            try:
                # XKBGrammar.g:112:2: ( TOKEN_INCLUDE include= quotedstring -> ^( TOKEN_INCLUDE $include) )
                # XKBGrammar.g:112:4: TOKEN_INCLUDE include= quotedstring
                TOKEN_INCLUDE13 = self.input.LT(1)
                self.match(self.input, TOKEN_INCLUDE, self.FOLLOW_TOKEN_INCLUDE_in_line_include534)

                stream_TOKEN_INCLUDE.add(TOKEN_INCLUDE13)
                self.following.append(self.FOLLOW_quotedstring_in_line_include538)
                include = self.quotedstring()
                self.following.pop()

                stream_quotedstring.add(include.tree)
                #action start
                print '\tinclude %(inc)s' % { "inc": self.input.toString(include.start,include.stop) } 
                #action end
                # AST Rewrite
                # elements: TOKEN_INCLUDE, include
                # token labels: 
                # rule labels: retval, include
                # token list labels: 
                # rule list labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                if include is not None:
                    stream_include = RewriteRuleSubtreeStream(self.adaptor, "token include", include.tree)
                else:
                    stream_include = RewriteRuleSubtreeStream(self.adaptor, "token include", None)


                root_0 = self.adaptor.nil()
                # 114:2: -> ^( TOKEN_INCLUDE $include)
                # XKBGrammar.g:114:5: ^( TOKEN_INCLUDE $include)
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(stream_TOKEN_INCLUDE.next(), root_1)

                self.adaptor.addChild(root_1, stream_include.next())

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

    # $ANTLR end line_include

    class line_name_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start line_name
    # XKBGrammar.g:117:1: line_name : TOKEN_NAME LBRACKET name= NAME RBRACKET EQUAL nameval= quotedstring SEMICOLON -> ^( TOKEN_NAME $name $nameval) ;
    def line_name(self, ):

        retval = self.line_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        name = None
        TOKEN_NAME14 = None
        LBRACKET15 = None
        RBRACKET16 = None
        EQUAL17 = None
        SEMICOLON18 = None
        nameval = None


        name_tree = None
        TOKEN_NAME14_tree = None
        LBRACKET15_tree = None
        RBRACKET16_tree = None
        EQUAL17_tree = None
        SEMICOLON18_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self.adaptor, "token LBRACKET")
        stream_TOKEN_NAME = RewriteRuleTokenStream(self.adaptor, "token TOKEN_NAME")
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_SEMICOLON = RewriteRuleTokenStream(self.adaptor, "token SEMICOLON")
        stream_RBRACKET = RewriteRuleTokenStream(self.adaptor, "token RBRACKET")
        stream_EQUAL = RewriteRuleTokenStream(self.adaptor, "token EQUAL")
        stream_quotedstring = RewriteRuleSubtreeStream(self.adaptor, "rule quotedstring")
        try:
            try:
                # XKBGrammar.g:118:2: ( TOKEN_NAME LBRACKET name= NAME RBRACKET EQUAL nameval= quotedstring SEMICOLON -> ^( TOKEN_NAME $name $nameval) )
                # XKBGrammar.g:118:4: TOKEN_NAME LBRACKET name= NAME RBRACKET EQUAL nameval= quotedstring SEMICOLON
                TOKEN_NAME14 = self.input.LT(1)
                self.match(self.input, TOKEN_NAME, self.FOLLOW_TOKEN_NAME_in_line_name563)

                stream_TOKEN_NAME.add(TOKEN_NAME14)
                LBRACKET15 = self.input.LT(1)
                self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_line_name565)

                stream_LBRACKET.add(LBRACKET15)
                name = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_name569)

                stream_NAME.add(name)
                RBRACKET16 = self.input.LT(1)
                self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_line_name571)

                stream_RBRACKET.add(RBRACKET16)
                EQUAL17 = self.input.LT(1)
                self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_line_name573)

                stream_EQUAL.add(EQUAL17)
                self.following.append(self.FOLLOW_quotedstring_in_line_name577)
                nameval = self.quotedstring()
                self.following.pop()

                stream_quotedstring.add(nameval.tree)
                SEMICOLON18 = self.input.LT(1)
                self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_line_name579)

                stream_SEMICOLON.add(SEMICOLON18)
                #action start
                print '\tname[%(name)s] = %(nameval)s;' % {  "name": name.text, "nameval": self.input.toString(nameval.start,nameval.stop) } 
                #action end
                # AST Rewrite
                # elements: nameval, name, TOKEN_NAME
                # token labels: name
                # rule labels: nameval, retval
                # token list labels: 
                # rule list labels: 

                retval.tree = root_0
                stream_name = RewriteRuleTokenStream(self.adaptor, "token name", name)

                if nameval is not None:
                    stream_nameval = RewriteRuleSubtreeStream(self.adaptor, "token nameval", nameval.tree)
                else:
                    stream_nameval = RewriteRuleSubtreeStream(self.adaptor, "token nameval", None)


                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                root_0 = self.adaptor.nil()
                # 120:2: -> ^( TOKEN_NAME $name $nameval)
                # XKBGrammar.g:120:5: ^( TOKEN_NAME $name $nameval)
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(stream_TOKEN_NAME.next(), root_1)

                self.adaptor.addChild(root_1, stream_name.next())
                self.adaptor.addChild(root_1, stream_nameval.next())

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

    # $ANTLR end line_name

    class line_keytype_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start line_keytype
    # XKBGrammar.g:123:1: line_keytype : TOKEN_KEY_TYPE LBRACKET keytype= NAME RBRACKET EQUAL DQUOTE keytypevalue= NAME DQUOTE SEMICOLON -> ^( TOKEN_KEY_TYPE $keytype $keytypevalue) ;
    def line_keytype(self, ):

        retval = self.line_keytype_return()
        retval.start = self.input.LT(1)

        root_0 = None

        keytype = None
        keytypevalue = None
        TOKEN_KEY_TYPE19 = None
        LBRACKET20 = None
        RBRACKET21 = None
        EQUAL22 = None
        DQUOTE23 = None
        DQUOTE24 = None
        SEMICOLON25 = None

        keytype_tree = None
        keytypevalue_tree = None
        TOKEN_KEY_TYPE19_tree = None
        LBRACKET20_tree = None
        RBRACKET21_tree = None
        EQUAL22_tree = None
        DQUOTE23_tree = None
        DQUOTE24_tree = None
        SEMICOLON25_tree = None
        stream_LBRACKET = RewriteRuleTokenStream(self.adaptor, "token LBRACKET")
        stream_DQUOTE = RewriteRuleTokenStream(self.adaptor, "token DQUOTE")
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_SEMICOLON = RewriteRuleTokenStream(self.adaptor, "token SEMICOLON")
        stream_RBRACKET = RewriteRuleTokenStream(self.adaptor, "token RBRACKET")
        stream_EQUAL = RewriteRuleTokenStream(self.adaptor, "token EQUAL")
        stream_TOKEN_KEY_TYPE = RewriteRuleTokenStream(self.adaptor, "token TOKEN_KEY_TYPE")

        try:
            try:
                # XKBGrammar.g:124:2: ( TOKEN_KEY_TYPE LBRACKET keytype= NAME RBRACKET EQUAL DQUOTE keytypevalue= NAME DQUOTE SEMICOLON -> ^( TOKEN_KEY_TYPE $keytype $keytypevalue) )
                # XKBGrammar.g:124:4: TOKEN_KEY_TYPE LBRACKET keytype= NAME RBRACKET EQUAL DQUOTE keytypevalue= NAME DQUOTE SEMICOLON
                TOKEN_KEY_TYPE19 = self.input.LT(1)
                self.match(self.input, TOKEN_KEY_TYPE, self.FOLLOW_TOKEN_KEY_TYPE_in_line_keytype606)

                stream_TOKEN_KEY_TYPE.add(TOKEN_KEY_TYPE19)
                LBRACKET20 = self.input.LT(1)
                self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_line_keytype608)

                stream_LBRACKET.add(LBRACKET20)
                keytype = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype612)

                stream_NAME.add(keytype)
                RBRACKET21 = self.input.LT(1)
                self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_line_keytype614)

                stream_RBRACKET.add(RBRACKET21)
                EQUAL22 = self.input.LT(1)
                self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_line_keytype616)

                stream_EQUAL.add(EQUAL22)
                DQUOTE23 = self.input.LT(1)
                self.match(self.input, DQUOTE, self.FOLLOW_DQUOTE_in_line_keytype618)

                stream_DQUOTE.add(DQUOTE23)
                keytypevalue = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype622)

                stream_NAME.add(keytypevalue)
                DQUOTE24 = self.input.LT(1)
                self.match(self.input, DQUOTE, self.FOLLOW_DQUOTE_in_line_keytype624)

                stream_DQUOTE.add(DQUOTE24)
                SEMICOLON25 = self.input.LT(1)
                self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_line_keytype626)

                stream_SEMICOLON.add(SEMICOLON25)
                #action start
                print '\tkey.type[%(kt)s] = \"%(ktv)s\";' % {  "kt": keytype.text, "ktv": keytypevalue.text } 
                #action end
                # AST Rewrite
                # elements: keytypevalue, keytype, TOKEN_KEY_TYPE
                # token labels: keytype, keytypevalue
                # rule labels: retval
                # token list labels: 
                # rule list labels: 

                retval.tree = root_0
                stream_keytype = RewriteRuleTokenStream(self.adaptor, "token keytype", keytype)
                stream_keytypevalue = RewriteRuleTokenStream(self.adaptor, "token keytypevalue", keytypevalue)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                root_0 = self.adaptor.nil()
                # 126:2: -> ^( TOKEN_KEY_TYPE $keytype $keytypevalue)
                # XKBGrammar.g:126:5: ^( TOKEN_KEY_TYPE $keytype $keytypevalue)
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(stream_TOKEN_KEY_TYPE.next(), root_1)

                self.adaptor.addChild(root_1, stream_keytype.next())
                self.adaptor.addChild(root_1, stream_keytypevalue.next())

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

    # $ANTLR end line_keytype

    class line_key_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start line_key
    # XKBGrammar.g:129:1: line_key : TOKEN_KEY keycode keysyms SEMICOLON -> ^( TOKEN_KEY keycode keysyms ) ;
    def line_key(self, ):

        retval = self.line_key_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TOKEN_KEY26 = None
        SEMICOLON29 = None
        keycode27 = None

        keysyms28 = None


        TOKEN_KEY26_tree = None
        SEMICOLON29_tree = None
        stream_SEMICOLON = RewriteRuleTokenStream(self.adaptor, "token SEMICOLON")
        stream_TOKEN_KEY = RewriteRuleTokenStream(self.adaptor, "token TOKEN_KEY")
        stream_keysyms = RewriteRuleSubtreeStream(self.adaptor, "rule keysyms")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        try:
            try:
                # XKBGrammar.g:130:2: ( TOKEN_KEY keycode keysyms SEMICOLON -> ^( TOKEN_KEY keycode keysyms ) )
                # XKBGrammar.g:130:4: TOKEN_KEY keycode keysyms SEMICOLON
                TOKEN_KEY26 = self.input.LT(1)
                self.match(self.input, TOKEN_KEY, self.FOLLOW_TOKEN_KEY_in_line_key654)

                stream_TOKEN_KEY.add(TOKEN_KEY26)
                self.following.append(self.FOLLOW_keycode_in_line_key656)
                keycode27 = self.keycode()
                self.following.pop()

                stream_keycode.add(keycode27.tree)
                self.following.append(self.FOLLOW_keysyms_in_line_key658)
                keysyms28 = self.keysyms()
                self.following.pop()

                stream_keysyms.add(keysyms28.tree)
                SEMICOLON29 = self.input.LT(1)
                self.match(self.input, SEMICOLON, self.FOLLOW_SEMICOLON_in_line_key660)

                stream_SEMICOLON.add(SEMICOLON29)
                #action start
                print '\tkey %(keycode)s %(keysyms)s;' % {  "keycode": self.input.toString(keycode27.start,keycode27.stop), "keysyms": keysyms28.value } 
                #action end
                # AST Rewrite
                # elements: keysyms, TOKEN_KEY, keycode
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
                # 132:2: -> ^( TOKEN_KEY keycode keysyms )
                # XKBGrammar.g:132:5: ^( TOKEN_KEY keycode keysyms )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(stream_TOKEN_KEY.next(), root_1)

                self.adaptor.addChild(root_1, stream_keycode.next())
                self.adaptor.addChild(root_1, stream_keysyms.next())

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

    # $ANTLR end line_key

    class keycode_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start keycode
    # XKBGrammar.g:135:1: keycode : LOWERTHAN NAME GREATERTHAN -> ^( KEYCODE NAME ) ;
    def keycode(self, ):

        retval = self.keycode_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LOWERTHAN30 = None
        NAME31 = None
        GREATERTHAN32 = None

        LOWERTHAN30_tree = None
        NAME31_tree = None
        GREATERTHAN32_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_LOWERTHAN = RewriteRuleTokenStream(self.adaptor, "token LOWERTHAN")
        stream_GREATERTHAN = RewriteRuleTokenStream(self.adaptor, "token GREATERTHAN")

        try:
            try:
                # XKBGrammar.g:136:2: ( LOWERTHAN NAME GREATERTHAN -> ^( KEYCODE NAME ) )
                # XKBGrammar.g:136:4: LOWERTHAN NAME GREATERTHAN
                LOWERTHAN30 = self.input.LT(1)
                self.match(self.input, LOWERTHAN, self.FOLLOW_LOWERTHAN_in_keycode687)

                stream_LOWERTHAN.add(LOWERTHAN30)
                NAME31 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode689)

                stream_NAME.add(NAME31)
                GREATERTHAN32 = self.input.LT(1)
                self.match(self.input, GREATERTHAN, self.FOLLOW_GREATERTHAN_in_keycode691)

                stream_GREATERTHAN.add(GREATERTHAN32)
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
                # 137:2: -> ^( KEYCODE NAME )
                # XKBGrammar.g:137:5: ^( KEYCODE NAME )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYCODE, "KEYCODE"), root_1)

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
    # XKBGrammar.g:140:1: keysyms returns [value] : LCURLY LBRACKET keysym+= NAME ( COMMA keysym+= NAME )* RBRACKET RCURLY ;
    def keysyms(self, ):

        retval = self.keysyms_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LCURLY33 = None
        LBRACKET34 = None
        COMMA35 = None
        RBRACKET36 = None
        RCURLY37 = None
        keysym = None
        list_keysym = None

        LCURLY33_tree = None
        LBRACKET34_tree = None
        COMMA35_tree = None
        RBRACKET36_tree = None
        RCURLY37_tree = None
        keysym_tree = None

        try:
            try:
                # XKBGrammar.g:141:2: ( LCURLY LBRACKET keysym+= NAME ( COMMA keysym+= NAME )* RBRACKET RCURLY )
                # XKBGrammar.g:141:4: LCURLY LBRACKET keysym+= NAME ( COMMA keysym+= NAME )* RBRACKET RCURLY
                root_0 = self.adaptor.nil()

                LCURLY33 = self.input.LT(1)
                self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_keysyms716)


                LCURLY33_tree = self.adaptor.createWithPayload(LCURLY33)
                self.adaptor.addChild(root_0, LCURLY33_tree)

                LBRACKET34 = self.input.LT(1)
                self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_keysyms718)


                LBRACKET34_tree = self.adaptor.createWithPayload(LBRACKET34)
                self.adaptor.addChild(root_0, LBRACKET34_tree)

                keysym = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_keysyms722)


                keysym_tree = self.adaptor.createWithPayload(keysym)
                self.adaptor.addChild(root_0, keysym_tree)

                if list_keysym is None:
                    list_keysym = []
                list_keysym.append(keysym)

                # XKBGrammar.g:141:33: ( COMMA keysym+= NAME )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == COMMA) :
                        alt5 = 1


                    if alt5 == 1:
                        # XKBGrammar.g:141:34: COMMA keysym+= NAME
                        COMMA35 = self.input.LT(1)
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_keysyms725)


                        COMMA35_tree = self.adaptor.createWithPayload(COMMA35)
                        self.adaptor.addChild(root_0, COMMA35_tree)

                        keysym = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_keysyms729)


                        keysym_tree = self.adaptor.createWithPayload(keysym)
                        self.adaptor.addChild(root_0, keysym_tree)

                        if list_keysym is None:
                            list_keysym = []
                        list_keysym.append(keysym)



                    else:
                        break #loop5


                RBRACKET36 = self.input.LT(1)
                self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_keysyms733)


                RBRACKET36_tree = self.adaptor.createWithPayload(RBRACKET36)
                self.adaptor.addChild(root_0, RBRACKET36_tree)

                RCURLY37 = self.input.LT(1)
                self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_keysyms735)


                RCURLY37_tree = self.adaptor.createWithPayload(RCURLY37)
                self.adaptor.addChild(root_0, RCURLY37_tree)

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

    class mapOptions_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mapOptions
    # XKBGrammar.g:161:1: mapOptions : ( TOKEN_DEFAULT | TOKEN_HIDDEN | TOKEN_PARTIAL | TOKEN_ALPHANUMERIC_KEYS | TOKEN_ALTERNATE_GROUP | TOKEN_XKB_SYMBOLS );
    def mapOptions(self, ):

        retval = self.mapOptions_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TOKEN_DEFAULT38 = None
        TOKEN_HIDDEN39 = None
        TOKEN_PARTIAL40 = None
        TOKEN_ALPHANUMERIC_KEYS41 = None
        TOKEN_ALTERNATE_GROUP42 = None
        TOKEN_XKB_SYMBOLS43 = None

        TOKEN_DEFAULT38_tree = None
        TOKEN_HIDDEN39_tree = None
        TOKEN_PARTIAL40_tree = None
        TOKEN_ALPHANUMERIC_KEYS41_tree = None
        TOKEN_ALTERNATE_GROUP42_tree = None
        TOKEN_XKB_SYMBOLS43_tree = None

        try:
            try:
                # XKBGrammar.g:162:2: ( TOKEN_DEFAULT | TOKEN_HIDDEN | TOKEN_PARTIAL | TOKEN_ALPHANUMERIC_KEYS | TOKEN_ALTERNATE_GROUP | TOKEN_XKB_SYMBOLS )
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
                    nvae = NoViableAltException("161:1: mapOptions : ( TOKEN_DEFAULT | TOKEN_HIDDEN | TOKEN_PARTIAL | TOKEN_ALPHANUMERIC_KEYS | TOKEN_ALTERNATE_GROUP | TOKEN_XKB_SYMBOLS );", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # XKBGrammar.g:162:4: TOKEN_DEFAULT
                    root_0 = self.adaptor.nil()

                    TOKEN_DEFAULT38 = self.input.LT(1)
                    self.match(self.input, TOKEN_DEFAULT, self.FOLLOW_TOKEN_DEFAULT_in_mapOptions760)


                    TOKEN_DEFAULT38_tree = self.adaptor.createWithPayload(TOKEN_DEFAULT38)
                    self.adaptor.addChild(root_0, TOKEN_DEFAULT38_tree)

                    #action start
                    print "default", 
                    #action end


                elif alt6 == 2:
                    # XKBGrammar.g:163:4: TOKEN_HIDDEN
                    root_0 = self.adaptor.nil()

                    TOKEN_HIDDEN39 = self.input.LT(1)
                    self.match(self.input, TOKEN_HIDDEN, self.FOLLOW_TOKEN_HIDDEN_in_mapOptions768)


                    TOKEN_HIDDEN39_tree = self.adaptor.createWithPayload(TOKEN_HIDDEN39)
                    self.adaptor.addChild(root_0, TOKEN_HIDDEN39_tree)

                    #action start
                    print "hidden", 
                    #action end


                elif alt6 == 3:
                    # XKBGrammar.g:164:4: TOKEN_PARTIAL
                    root_0 = self.adaptor.nil()

                    TOKEN_PARTIAL40 = self.input.LT(1)
                    self.match(self.input, TOKEN_PARTIAL, self.FOLLOW_TOKEN_PARTIAL_in_mapOptions777)


                    TOKEN_PARTIAL40_tree = self.adaptor.createWithPayload(TOKEN_PARTIAL40)
                    self.adaptor.addChild(root_0, TOKEN_PARTIAL40_tree)

                    #action start
                    print "partial", 
                    #action end


                elif alt6 == 4:
                    # XKBGrammar.g:165:4: TOKEN_ALPHANUMERIC_KEYS
                    root_0 = self.adaptor.nil()

                    TOKEN_ALPHANUMERIC_KEYS41 = self.input.LT(1)
                    self.match(self.input, TOKEN_ALPHANUMERIC_KEYS, self.FOLLOW_TOKEN_ALPHANUMERIC_KEYS_in_mapOptions786)


                    TOKEN_ALPHANUMERIC_KEYS41_tree = self.adaptor.createWithPayload(TOKEN_ALPHANUMERIC_KEYS41)
                    self.adaptor.addChild(root_0, TOKEN_ALPHANUMERIC_KEYS41_tree)

                    #action start
                    print "alphanumeric_keys", 
                    #action end


                elif alt6 == 5:
                    # XKBGrammar.g:166:4: TOKEN_ALTERNATE_GROUP
                    root_0 = self.adaptor.nil()

                    TOKEN_ALTERNATE_GROUP42 = self.input.LT(1)
                    self.match(self.input, TOKEN_ALTERNATE_GROUP, self.FOLLOW_TOKEN_ALTERNATE_GROUP_in_mapOptions795)


                    TOKEN_ALTERNATE_GROUP42_tree = self.adaptor.createWithPayload(TOKEN_ALTERNATE_GROUP42)
                    self.adaptor.addChild(root_0, TOKEN_ALTERNATE_GROUP42_tree)

                    #action start
                    print "alternate_group", 
                    #action end


                elif alt6 == 6:
                    # XKBGrammar.g:167:4: TOKEN_XKB_SYMBOLS
                    root_0 = self.adaptor.nil()

                    TOKEN_XKB_SYMBOLS43 = self.input.LT(1)
                    self.match(self.input, TOKEN_XKB_SYMBOLS, self.FOLLOW_TOKEN_XKB_SYMBOLS_in_mapOptions802)


                    TOKEN_XKB_SYMBOLS43_tree = self.adaptor.createWithPayload(TOKEN_XKB_SYMBOLS43)
                    self.adaptor.addChild(root_0, TOKEN_XKB_SYMBOLS43_tree)

                    #action start
                    print "xkb_symbols", 
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

    # $ANTLR end mapOptions


 

    FOLLOW_section_in_layout369 = frozenset([1, 4, 5, 6, 7, 9, 10])
    FOLLOW_mapType_in_section383 = frozenset([17])
    FOLLOW_sectionmaterial_in_section385 = frozenset([1])
    FOLLOW_mapOptions_in_mapType401 = frozenset([4, 5, 6, 7, 9, 10, 20])
    FOLLOW_quotedstring_in_mapType406 = frozenset([1])
    FOLLOW_DQUOTE_in_quotedstring444 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41])
    FOLLOW_set_in_quotedstring448 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41])
    FOLLOW_DQUOTE_in_quotedstring454 = frozenset([1])
    FOLLOW_LCURLY_in_sectionmaterial486 = frozenset([11, 12, 13, 14])
    FOLLOW_line_include_in_sectionmaterial489 = frozenset([11, 12, 13, 14, 18])
    FOLLOW_line_name_in_sectionmaterial495 = frozenset([11, 12, 13, 14, 18])
    FOLLOW_line_keytype_in_sectionmaterial501 = frozenset([11, 12, 13, 14, 18])
    FOLLOW_line_key_in_sectionmaterial507 = frozenset([11, 12, 13, 14, 18])
    FOLLOW_RCURLY_in_sectionmaterial514 = frozenset([23])
    FOLLOW_SEMICOLON_in_sectionmaterial516 = frozenset([1])
    FOLLOW_TOKEN_INCLUDE_in_line_include534 = frozenset([20])
    FOLLOW_quotedstring_in_line_include538 = frozenset([1])
    FOLLOW_TOKEN_NAME_in_line_name563 = frozenset([15])
    FOLLOW_LBRACKET_in_line_name565 = frozenset([37])
    FOLLOW_NAME_in_line_name569 = frozenset([16])
    FOLLOW_RBRACKET_in_line_name571 = frozenset([24])
    FOLLOW_EQUAL_in_line_name573 = frozenset([20])
    FOLLOW_quotedstring_in_line_name577 = frozenset([23])
    FOLLOW_SEMICOLON_in_line_name579 = frozenset([1])
    FOLLOW_TOKEN_KEY_TYPE_in_line_keytype606 = frozenset([15])
    FOLLOW_LBRACKET_in_line_keytype608 = frozenset([37])
    FOLLOW_NAME_in_line_keytype612 = frozenset([16])
    FOLLOW_RBRACKET_in_line_keytype614 = frozenset([24])
    FOLLOW_EQUAL_in_line_keytype616 = frozenset([20])
    FOLLOW_DQUOTE_in_line_keytype618 = frozenset([37])
    FOLLOW_NAME_in_line_keytype622 = frozenset([20])
    FOLLOW_DQUOTE_in_line_keytype624 = frozenset([23])
    FOLLOW_SEMICOLON_in_line_keytype626 = frozenset([1])
    FOLLOW_TOKEN_KEY_in_line_key654 = frozenset([25])
    FOLLOW_keycode_in_line_key656 = frozenset([17])
    FOLLOW_keysyms_in_line_key658 = frozenset([23])
    FOLLOW_SEMICOLON_in_line_key660 = frozenset([1])
    FOLLOW_LOWERTHAN_in_keycode687 = frozenset([37])
    FOLLOW_NAME_in_keycode689 = frozenset([26])
    FOLLOW_GREATERTHAN_in_keycode691 = frozenset([1])
    FOLLOW_LCURLY_in_keysyms716 = frozenset([15])
    FOLLOW_LBRACKET_in_keysyms718 = frozenset([37])
    FOLLOW_NAME_in_keysyms722 = frozenset([16, 19])
    FOLLOW_COMMA_in_keysyms725 = frozenset([37])
    FOLLOW_NAME_in_keysyms729 = frozenset([16, 19])
    FOLLOW_RBRACKET_in_keysyms733 = frozenset([18])
    FOLLOW_RCURLY_in_keysyms735 = frozenset([1])
    FOLLOW_TOKEN_DEFAULT_in_mapOptions760 = frozenset([1])
    FOLLOW_TOKEN_HIDDEN_in_mapOptions768 = frozenset([1])
    FOLLOW_TOKEN_PARTIAL_in_mapOptions777 = frozenset([1])
    FOLLOW_TOKEN_ALPHANUMERIC_KEYS_in_mapOptions786 = frozenset([1])
    FOLLOW_TOKEN_ALTERNATE_GROUP_in_mapOptions795 = frozenset([1])
    FOLLOW_TOKEN_XKB_SYMBOLS_in_mapOptions802 = frozenset([1])

