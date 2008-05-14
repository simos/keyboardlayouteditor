# $ANTLR 3.0.1 XKBGrammar.g 2008-05-14 21:55:38

from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
QUOTEDSTRING=25
TOKEN_ALTERNATE_GROUP=9
ATTRIBUTES=17
SECTION=23
LINE_COMMENT=30
KEYCODE=22
TOKEN_INCLUDE=11
KEY=20
KEYTYPE=21
ATTRIBUTE=18
TOKEN_NAME=13
TOKEN_XKB_SYMBOLS=10
EOF=-1
SECTIONNAME=24
MAPTYPE=15
NAME=27
TOKEN_PARTIAL=6
WS=28
TOKEN_ALPHANUMERIC_KEYS=7
TOKEN_HIDDEN=5
MAPMATERIAL=16
INCLUDE=19
TOKEN_MODIFIER_KEYS=8
KEYSYMS=26
TOKEN_KEY=14
COMMENT=29
TOKEN_DEFAULT=4
TOKEN_KEY_TYPE=12

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "TOKEN_DEFAULT", "TOKEN_HIDDEN", "TOKEN_PARTIAL", "TOKEN_ALPHANUMERIC_KEYS", 
    "TOKEN_MODIFIER_KEYS", "TOKEN_ALTERNATE_GROUP", "TOKEN_XKB_SYMBOLS", 
    "TOKEN_INCLUDE", "TOKEN_KEY_TYPE", "TOKEN_NAME", "TOKEN_KEY", "MAPTYPE", 
    "MAPMATERIAL", "ATTRIBUTES", "ATTRIBUTE", "INCLUDE", "KEY", "KEYTYPE", 
    "KEYCODE", "SECTION", "SECTIONNAME", "QUOTEDSTRING", "KEYSYMS", "NAME", 
    "WS", "COMMENT", "LINE_COMMENT", "'\"'", "'{'", "';'", "'}'", "'include'", 
    "'name'", "'['", "']'", "'='", "'key.type'", "'key'", "'<'", "'>'", 
    "','", "'default'", "'hidden'", "'partial'", "'alphanumeric_keys'", 
    "'alternate_group'", "'xkb_symbols'"
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
    # XKBGrammar.g:61:1: layout : ( section )+ EOF ;
    def layout(self, ):

        retval = self.layout_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF2 = None
        section1 = None


        EOF2_tree = None

        try:
            try:
                # XKBGrammar.g:62:2: ( ( section )+ EOF )
                # XKBGrammar.g:62:4: ( section )+ EOF
                root_0 = self.adaptor.nil()

                # XKBGrammar.g:62:4: ( section )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((45 <= LA1_0 <= 50)) :
                        alt1 = 1


                    if alt1 == 1:
                        # XKBGrammar.g:62:4: section
                        self.following.append(self.FOLLOW_section_in_layout160)
                        section1 = self.section()
                        self.following.pop()

                        self.adaptor.addChild(root_0, section1.tree)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                EOF2 = self.input.LT(1)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_layout163)




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
    # XKBGrammar.g:65:1: section : mapType mapMaterial -> ^( SECTION mapType mapMaterial ) ;
    def section(self, ):

        retval = self.section_return()
        retval.start = self.input.LT(1)

        root_0 = None

        mapType3 = None

        mapMaterial4 = None


        stream_mapMaterial = RewriteRuleSubtreeStream(self.adaptor, "rule mapMaterial")
        stream_mapType = RewriteRuleSubtreeStream(self.adaptor, "rule mapType")
        try:
            try:
                # XKBGrammar.g:66:2: ( mapType mapMaterial -> ^( SECTION mapType mapMaterial ) )
                # XKBGrammar.g:66:4: mapType mapMaterial
                self.following.append(self.FOLLOW_mapType_in_section177)
                mapType3 = self.mapType()
                self.following.pop()

                stream_mapType.add(mapType3.tree)
                self.following.append(self.FOLLOW_mapMaterial_in_section179)
                mapMaterial4 = self.mapMaterial()
                self.following.pop()

                stream_mapMaterial.add(mapMaterial4.tree)
                # AST Rewrite
                # elements: mapType, mapMaterial
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
                # 67:2: -> ^( SECTION mapType mapMaterial )
                # XKBGrammar.g:67:5: ^( SECTION mapType mapMaterial )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(SECTION, "SECTION"), root_1)

                self.adaptor.addChild(root_1, stream_mapType.next())
                self.adaptor.addChild(root_1, stream_mapMaterial.next())

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

    class mapType_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mapType
    # XKBGrammar.g:70:1: mapType : ( mapOptions )+ '\"' NAME '\"' -> ^( MAPTYPE ( mapOptions )+ NAME ) ;
    def mapType(self, ):

        retval = self.mapType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal6 = None
        NAME7 = None
        char_literal8 = None
        mapOptions5 = None


        char_literal6_tree = None
        NAME7_tree = None
        char_literal8_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_31 = RewriteRuleTokenStream(self.adaptor, "token 31")
        stream_mapOptions = RewriteRuleSubtreeStream(self.adaptor, "rule mapOptions")
        try:
            try:
                # XKBGrammar.g:71:2: ( ( mapOptions )+ '\"' NAME '\"' -> ^( MAPTYPE ( mapOptions )+ NAME ) )
                # XKBGrammar.g:71:4: ( mapOptions )+ '\"' NAME '\"'
                # XKBGrammar.g:71:4: ( mapOptions )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((45 <= LA2_0 <= 50)) :
                        alt2 = 1


                    if alt2 == 1:
                        # XKBGrammar.g:71:4: mapOptions
                        self.following.append(self.FOLLOW_mapOptions_in_mapType202)
                        mapOptions5 = self.mapOptions()
                        self.following.pop()

                        stream_mapOptions.add(mapOptions5.tree)


                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1


                char_literal6 = self.input.LT(1)
                self.match(self.input, 31, self.FOLLOW_31_in_mapType205)

                stream_31.add(char_literal6)
                NAME7 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_mapType207)

                stream_NAME.add(NAME7)
                char_literal8 = self.input.LT(1)
                self.match(self.input, 31, self.FOLLOW_31_in_mapType209)

                stream_31.add(char_literal8)
                # AST Rewrite
                # elements: mapOptions, NAME
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
                # 72:2: -> ^( MAPTYPE ( mapOptions )+ NAME )
                # XKBGrammar.g:72:5: ^( MAPTYPE ( mapOptions )+ NAME )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPTYPE, "MAPTYPE"), root_1)

                # XKBGrammar.g:72:15: ( mapOptions )+
                if not (stream_mapOptions.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_mapOptions.hasNext():
                    self.adaptor.addChild(root_1, stream_mapOptions.next())


                stream_mapOptions.reset()
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

    # $ANTLR end mapType

    class mapMaterial_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mapMaterial
    # XKBGrammar.g:75:1: mapMaterial : '{' ( line_include | line_name ';' | line_keytype ';' | line_key ';' )+ '}' ';' ;
    def mapMaterial(self, ):

        retval = self.mapMaterial_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal9 = None
        char_literal12 = None
        char_literal14 = None
        char_literal16 = None
        char_literal17 = None
        char_literal18 = None
        line_include10 = None

        line_name11 = None

        line_keytype13 = None

        line_key15 = None


        char_literal9_tree = None
        char_literal12_tree = None
        char_literal14_tree = None
        char_literal16_tree = None
        char_literal17_tree = None
        char_literal18_tree = None

        try:
            try:
                # XKBGrammar.g:76:2: ( '{' ( line_include | line_name ';' | line_keytype ';' | line_key ';' )+ '}' ';' )
                # XKBGrammar.g:76:4: '{' ( line_include | line_name ';' | line_keytype ';' | line_key ';' )+ '}' ';'
                root_0 = self.adaptor.nil()

                char_literal9 = self.input.LT(1)
                self.match(self.input, 32, self.FOLLOW_32_in_mapMaterial233)


                char_literal9_tree = self.adaptor.createWithPayload(char_literal9)
                self.adaptor.addChild(root_0, char_literal9_tree)

                # XKBGrammar.g:77:2: ( line_include | line_name ';' | line_keytype ';' | line_key ';' )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 5
                    LA3 = self.input.LA(1)
                    if LA3 == 35:
                        alt3 = 1
                    elif LA3 == 36:
                        alt3 = 2
                    elif LA3 == 40:
                        alt3 = 3
                    elif LA3 == 41:
                        alt3 = 4

                    if alt3 == 1:
                        # XKBGrammar.g:77:4: line_include
                        self.following.append(self.FOLLOW_line_include_in_mapMaterial239)
                        line_include10 = self.line_include()
                        self.following.pop()

                        self.adaptor.addChild(root_0, line_include10.tree)


                    elif alt3 == 2:
                        # XKBGrammar.g:78:4: line_name ';'
                        self.following.append(self.FOLLOW_line_name_in_mapMaterial245)
                        line_name11 = self.line_name()
                        self.following.pop()

                        self.adaptor.addChild(root_0, line_name11.tree)
                        char_literal12 = self.input.LT(1)
                        self.match(self.input, 33, self.FOLLOW_33_in_mapMaterial247)



                    elif alt3 == 3:
                        # XKBGrammar.g:79:4: line_keytype ';'
                        self.following.append(self.FOLLOW_line_keytype_in_mapMaterial253)
                        line_keytype13 = self.line_keytype()
                        self.following.pop()

                        self.adaptor.addChild(root_0, line_keytype13.tree)
                        char_literal14 = self.input.LT(1)
                        self.match(self.input, 33, self.FOLLOW_33_in_mapMaterial255)



                    elif alt3 == 4:
                        # XKBGrammar.g:80:4: line_key ';'
                        self.following.append(self.FOLLOW_line_key_in_mapMaterial261)
                        line_key15 = self.line_key()
                        self.following.pop()

                        self.adaptor.addChild(root_0, line_key15.tree)
                        char_literal16 = self.input.LT(1)
                        self.match(self.input, 33, self.FOLLOW_33_in_mapMaterial263)



                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


                char_literal17 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_mapMaterial270)


                char_literal17_tree = self.adaptor.createWithPayload(char_literal17)
                self.adaptor.addChild(root_0, char_literal17_tree)

                char_literal18 = self.input.LT(1)
                self.match(self.input, 33, self.FOLLOW_33_in_mapMaterial272)


                char_literal18_tree = self.adaptor.createWithPayload(char_literal18)
                self.adaptor.addChild(root_0, char_literal18_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end mapMaterial

    class line_include_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start line_include
    # XKBGrammar.g:84:1: line_include : 'include' '\"' NAME '\"' -> ^( TOKEN_INCLUDE NAME ) ;
    def line_include(self, ):

        retval = self.line_include_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal19 = None
        char_literal20 = None
        NAME21 = None
        char_literal22 = None

        string_literal19_tree = None
        char_literal20_tree = None
        NAME21_tree = None
        char_literal22_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_31 = RewriteRuleTokenStream(self.adaptor, "token 31")
        stream_35 = RewriteRuleTokenStream(self.adaptor, "token 35")

        try:
            try:
                # XKBGrammar.g:85:2: ( 'include' '\"' NAME '\"' -> ^( TOKEN_INCLUDE NAME ) )
                # XKBGrammar.g:85:4: 'include' '\"' NAME '\"'
                string_literal19 = self.input.LT(1)
                self.match(self.input, 35, self.FOLLOW_35_in_line_include283)

                stream_35.add(string_literal19)
                char_literal20 = self.input.LT(1)
                self.match(self.input, 31, self.FOLLOW_31_in_line_include285)

                stream_31.add(char_literal20)
                NAME21 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_include287)

                stream_NAME.add(NAME21)
                char_literal22 = self.input.LT(1)
                self.match(self.input, 31, self.FOLLOW_31_in_line_include289)

                stream_31.add(char_literal22)
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
                # 86:2: -> ^( TOKEN_INCLUDE NAME )
                # XKBGrammar.g:86:5: ^( TOKEN_INCLUDE NAME )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_INCLUDE, "TOKEN_INCLUDE"), root_1)

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

    # $ANTLR end line_include

    class line_name_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start line_name
    # XKBGrammar.g:89:1: line_name : 'name' '[' n1= NAME ']' '=' '\"' n2= NAME '\"' -> ^( TOKEN_NAME $n1 $n2) ;
    def line_name(self, ):

        retval = self.line_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        n1 = None
        n2 = None
        string_literal23 = None
        char_literal24 = None
        char_literal25 = None
        char_literal26 = None
        char_literal27 = None
        char_literal28 = None

        n1_tree = None
        n2_tree = None
        string_literal23_tree = None
        char_literal24_tree = None
        char_literal25_tree = None
        char_literal26_tree = None
        char_literal27_tree = None
        char_literal28_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_31 = RewriteRuleTokenStream(self.adaptor, "token 31")
        stream_36 = RewriteRuleTokenStream(self.adaptor, "token 36")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")

        try:
            try:
                # XKBGrammar.g:90:2: ( 'name' '[' n1= NAME ']' '=' '\"' n2= NAME '\"' -> ^( TOKEN_NAME $n1 $n2) )
                # XKBGrammar.g:90:4: 'name' '[' n1= NAME ']' '=' '\"' n2= NAME '\"'
                string_literal23 = self.input.LT(1)
                self.match(self.input, 36, self.FOLLOW_36_in_line_name309)

                stream_36.add(string_literal23)
                char_literal24 = self.input.LT(1)
                self.match(self.input, 37, self.FOLLOW_37_in_line_name311)

                stream_37.add(char_literal24)
                n1 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_name315)

                stream_NAME.add(n1)
                char_literal25 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_line_name317)

                stream_38.add(char_literal25)
                char_literal26 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_line_name319)

                stream_39.add(char_literal26)
                char_literal27 = self.input.LT(1)
                self.match(self.input, 31, self.FOLLOW_31_in_line_name321)

                stream_31.add(char_literal27)
                n2 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_name325)

                stream_NAME.add(n2)
                char_literal28 = self.input.LT(1)
                self.match(self.input, 31, self.FOLLOW_31_in_line_name327)

                stream_31.add(char_literal28)
                # AST Rewrite
                # elements: n2, n1
                # token labels: n1, n2
                # rule labels: retval
                # token list labels: 
                # rule list labels: 

                retval.tree = root_0
                stream_n1 = RewriteRuleTokenStream(self.adaptor, "token n1", n1)
                stream_n2 = RewriteRuleTokenStream(self.adaptor, "token n2", n2)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                root_0 = self.adaptor.nil()
                # 91:2: -> ^( TOKEN_NAME $n1 $n2)
                # XKBGrammar.g:91:5: ^( TOKEN_NAME $n1 $n2)
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_NAME, "TOKEN_NAME"), root_1)

                self.adaptor.addChild(root_1, stream_n1.next())
                self.adaptor.addChild(root_1, stream_n2.next())

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
    # XKBGrammar.g:94:1: line_keytype : 'key.type' '[' n1= NAME ']' '=' '\"' n2= NAME '\"' -> ^( TOKEN_KEY_TYPE $n1 $n2) ;
    def line_keytype(self, ):

        retval = self.line_keytype_return()
        retval.start = self.input.LT(1)

        root_0 = None

        n1 = None
        n2 = None
        string_literal29 = None
        char_literal30 = None
        char_literal31 = None
        char_literal32 = None
        char_literal33 = None
        char_literal34 = None

        n1_tree = None
        n2_tree = None
        string_literal29_tree = None
        char_literal30_tree = None
        char_literal31_tree = None
        char_literal32_tree = None
        char_literal33_tree = None
        char_literal34_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_40 = RewriteRuleTokenStream(self.adaptor, "token 40")
        stream_31 = RewriteRuleTokenStream(self.adaptor, "token 31")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")

        try:
            try:
                # XKBGrammar.g:95:2: ( 'key.type' '[' n1= NAME ']' '=' '\"' n2= NAME '\"' -> ^( TOKEN_KEY_TYPE $n1 $n2) )
                # XKBGrammar.g:95:4: 'key.type' '[' n1= NAME ']' '=' '\"' n2= NAME '\"'
                string_literal29 = self.input.LT(1)
                self.match(self.input, 40, self.FOLLOW_40_in_line_keytype351)

                stream_40.add(string_literal29)
                char_literal30 = self.input.LT(1)
                self.match(self.input, 37, self.FOLLOW_37_in_line_keytype353)

                stream_37.add(char_literal30)
                n1 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype357)

                stream_NAME.add(n1)
                char_literal31 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_line_keytype359)

                stream_38.add(char_literal31)
                char_literal32 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_line_keytype361)

                stream_39.add(char_literal32)
                char_literal33 = self.input.LT(1)
                self.match(self.input, 31, self.FOLLOW_31_in_line_keytype363)

                stream_31.add(char_literal33)
                n2 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype367)

                stream_NAME.add(n2)
                char_literal34 = self.input.LT(1)
                self.match(self.input, 31, self.FOLLOW_31_in_line_keytype369)

                stream_31.add(char_literal34)
                # AST Rewrite
                # elements: n2, n1
                # token labels: n1, n2
                # rule labels: retval
                # token list labels: 
                # rule list labels: 

                retval.tree = root_0
                stream_n1 = RewriteRuleTokenStream(self.adaptor, "token n1", n1)
                stream_n2 = RewriteRuleTokenStream(self.adaptor, "token n2", n2)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                root_0 = self.adaptor.nil()
                # 96:2: -> ^( TOKEN_KEY_TYPE $n1 $n2)
                # XKBGrammar.g:96:5: ^( TOKEN_KEY_TYPE $n1 $n2)
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_KEY_TYPE, "TOKEN_KEY_TYPE"), root_1)

                self.adaptor.addChild(root_1, stream_n1.next())
                self.adaptor.addChild(root_1, stream_n2.next())

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
    # XKBGrammar.g:99:1: line_key : 'key' keycode keysyms -> ^( TOKEN_KEY keycode keysyms ) ;
    def line_key(self, ):

        retval = self.line_key_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal35 = None
        keycode36 = None

        keysyms37 = None


        string_literal35_tree = None
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_keysyms = RewriteRuleSubtreeStream(self.adaptor, "rule keysyms")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        try:
            try:
                # XKBGrammar.g:100:2: ( 'key' keycode keysyms -> ^( TOKEN_KEY keycode keysyms ) )
                # XKBGrammar.g:100:4: 'key' keycode keysyms
                string_literal35 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_line_key394)

                stream_41.add(string_literal35)
                self.following.append(self.FOLLOW_keycode_in_line_key396)
                keycode36 = self.keycode()
                self.following.pop()

                stream_keycode.add(keycode36.tree)
                self.following.append(self.FOLLOW_keysyms_in_line_key398)
                keysyms37 = self.keysyms()
                self.following.pop()

                stream_keysyms.add(keysyms37.tree)
                # AST Rewrite
                # elements: keycode, keysyms
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
                # 101:2: -> ^( TOKEN_KEY keycode keysyms )
                # XKBGrammar.g:101:5: ^( TOKEN_KEY keycode keysyms )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_KEY, "TOKEN_KEY"), root_1)

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
    # XKBGrammar.g:104:1: keycode : '<' NAME '>' -> ^( KEYCODE NAME ) ;
    def keycode(self, ):

        retval = self.keycode_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal38 = None
        NAME39 = None
        char_literal40 = None

        char_literal38_tree = None
        NAME39_tree = None
        char_literal40_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_42 = RewriteRuleTokenStream(self.adaptor, "token 42")

        try:
            try:
                # XKBGrammar.g:105:2: ( '<' NAME '>' -> ^( KEYCODE NAME ) )
                # XKBGrammar.g:105:4: '<' NAME '>'
                char_literal38 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_keycode422)

                stream_42.add(char_literal38)
                NAME39 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode424)

                stream_NAME.add(NAME39)
                char_literal40 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_keycode426)

                stream_43.add(char_literal40)
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
                # 106:2: -> ^( KEYCODE NAME )
                # XKBGrammar.g:106:5: ^( KEYCODE NAME )
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

            self.tree = None


    # $ANTLR start keysyms
    # XKBGrammar.g:109:1: keysyms : '{' '[' keysym+= NAME ( ',' keysym+= NAME )* ']' '}' -> ^( KEYSYMS ( $keysym)+ ) ;
    def keysyms(self, ):

        retval = self.keysyms_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal41 = None
        char_literal42 = None
        char_literal43 = None
        char_literal44 = None
        char_literal45 = None
        keysym = None
        list_keysym = None

        char_literal41_tree = None
        char_literal42_tree = None
        char_literal43_tree = None
        char_literal44_tree = None
        char_literal45_tree = None
        keysym_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_44 = RewriteRuleTokenStream(self.adaptor, "token 44")
        stream_32 = RewriteRuleTokenStream(self.adaptor, "token 32")
        stream_34 = RewriteRuleTokenStream(self.adaptor, "token 34")
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")

        try:
            try:
                # XKBGrammar.g:110:2: ( '{' '[' keysym+= NAME ( ',' keysym+= NAME )* ']' '}' -> ^( KEYSYMS ( $keysym)+ ) )
                # XKBGrammar.g:110:4: '{' '[' keysym+= NAME ( ',' keysym+= NAME )* ']' '}'
                char_literal41 = self.input.LT(1)
                self.match(self.input, 32, self.FOLLOW_32_in_keysyms446)

                stream_32.add(char_literal41)
                char_literal42 = self.input.LT(1)
                self.match(self.input, 37, self.FOLLOW_37_in_keysyms448)

                stream_37.add(char_literal42)
                keysym = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_keysyms452)

                stream_NAME.add(keysym)
                if list_keysym is None:
                    list_keysym = []
                list_keysym.append(keysym)

                # XKBGrammar.g:110:25: ( ',' keysym+= NAME )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == 44) :
                        alt4 = 1


                    if alt4 == 1:
                        # XKBGrammar.g:110:26: ',' keysym+= NAME
                        char_literal43 = self.input.LT(1)
                        self.match(self.input, 44, self.FOLLOW_44_in_keysyms455)

                        stream_44.add(char_literal43)
                        keysym = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_keysyms459)

                        stream_NAME.add(keysym)
                        if list_keysym is None:
                            list_keysym = []
                        list_keysym.append(keysym)



                    else:
                        break #loop4


                char_literal44 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_keysyms463)

                stream_38.add(char_literal44)
                char_literal45 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_keysyms465)

                stream_34.add(char_literal45)
                # AST Rewrite
                # elements: keysym
                # token labels: 
                # rule labels: retval
                # token list labels: keysym
                # rule list labels: 

                retval.tree = root_0
                stream_keysym = RewriteRuleTokenStream(self.adaptor, "token keysym", list_keysym)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                root_0 = self.adaptor.nil()
                # 111:2: -> ^( KEYSYMS ( $keysym)+ )
                # XKBGrammar.g:111:5: ^( KEYSYMS ( $keysym)+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYSYMS, "KEYSYMS"), root_1)

                # XKBGrammar.g:111:15: ( $keysym)+
                if not (stream_keysym.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_keysym.hasNext():
                    self.adaptor.addChild(root_1, stream_keysym.next())


                stream_keysym.reset()

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

    # $ANTLR end keysyms

    class mapOptions_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mapOptions
    # XKBGrammar.g:114:1: mapOptions : ( 'default' | 'hidden' | 'partial' | 'alphanumeric_keys' | 'alternate_group' | 'xkb_symbols' );
    def mapOptions(self, ):

        retval = self.mapOptions_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set46 = None

        set46_tree = None

        try:
            try:
                # XKBGrammar.g:115:2: ( 'default' | 'hidden' | 'partial' | 'alphanumeric_keys' | 'alternate_group' | 'xkb_symbols' )
                # XKBGrammar.g:
                root_0 = self.adaptor.nil()

                set46 = self.input.LT(1)
                if (45 <= self.input.LA(1) <= 50):
                    self.input.consume();
                    self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set46))
                    self.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_mapOptions0
                        )
                    raise mse





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


 

    FOLLOW_section_in_layout160 = frozenset([45, 46, 47, 48, 49, 50])
    FOLLOW_EOF_in_layout163 = frozenset([1])
    FOLLOW_mapType_in_section177 = frozenset([32])
    FOLLOW_mapMaterial_in_section179 = frozenset([1])
    FOLLOW_mapOptions_in_mapType202 = frozenset([31, 45, 46, 47, 48, 49, 50])
    FOLLOW_31_in_mapType205 = frozenset([27])
    FOLLOW_NAME_in_mapType207 = frozenset([31])
    FOLLOW_31_in_mapType209 = frozenset([1])
    FOLLOW_32_in_mapMaterial233 = frozenset([35, 36, 40, 41])
    FOLLOW_line_include_in_mapMaterial239 = frozenset([34, 35, 36, 40, 41])
    FOLLOW_line_name_in_mapMaterial245 = frozenset([33])
    FOLLOW_33_in_mapMaterial247 = frozenset([34, 35, 36, 40, 41])
    FOLLOW_line_keytype_in_mapMaterial253 = frozenset([33])
    FOLLOW_33_in_mapMaterial255 = frozenset([34, 35, 36, 40, 41])
    FOLLOW_line_key_in_mapMaterial261 = frozenset([33])
    FOLLOW_33_in_mapMaterial263 = frozenset([34, 35, 36, 40, 41])
    FOLLOW_34_in_mapMaterial270 = frozenset([33])
    FOLLOW_33_in_mapMaterial272 = frozenset([1])
    FOLLOW_35_in_line_include283 = frozenset([31])
    FOLLOW_31_in_line_include285 = frozenset([27])
    FOLLOW_NAME_in_line_include287 = frozenset([31])
    FOLLOW_31_in_line_include289 = frozenset([1])
    FOLLOW_36_in_line_name309 = frozenset([37])
    FOLLOW_37_in_line_name311 = frozenset([27])
    FOLLOW_NAME_in_line_name315 = frozenset([38])
    FOLLOW_38_in_line_name317 = frozenset([39])
    FOLLOW_39_in_line_name319 = frozenset([31])
    FOLLOW_31_in_line_name321 = frozenset([27])
    FOLLOW_NAME_in_line_name325 = frozenset([31])
    FOLLOW_31_in_line_name327 = frozenset([1])
    FOLLOW_40_in_line_keytype351 = frozenset([37])
    FOLLOW_37_in_line_keytype353 = frozenset([27])
    FOLLOW_NAME_in_line_keytype357 = frozenset([38])
    FOLLOW_38_in_line_keytype359 = frozenset([39])
    FOLLOW_39_in_line_keytype361 = frozenset([31])
    FOLLOW_31_in_line_keytype363 = frozenset([27])
    FOLLOW_NAME_in_line_keytype367 = frozenset([31])
    FOLLOW_31_in_line_keytype369 = frozenset([1])
    FOLLOW_41_in_line_key394 = frozenset([42])
    FOLLOW_keycode_in_line_key396 = frozenset([32])
    FOLLOW_keysyms_in_line_key398 = frozenset([1])
    FOLLOW_42_in_keycode422 = frozenset([27])
    FOLLOW_NAME_in_keycode424 = frozenset([43])
    FOLLOW_43_in_keycode426 = frozenset([1])
    FOLLOW_32_in_keysyms446 = frozenset([37])
    FOLLOW_37_in_keysyms448 = frozenset([27])
    FOLLOW_NAME_in_keysyms452 = frozenset([38, 44])
    FOLLOW_44_in_keysyms455 = frozenset([27])
    FOLLOW_NAME_in_keysyms459 = frozenset([38, 44])
    FOLLOW_38_in_keysyms463 = frozenset([34])
    FOLLOW_34_in_keysyms465 = frozenset([1])
    FOLLOW_set_in_mapOptions0 = frozenset([1])

