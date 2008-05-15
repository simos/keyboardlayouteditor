# $ANTLR 3.1b1 XKBGrammar.g 2008-05-15 19:18:28

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__29=29
T__28=28
T__27=27
MAPOPTIONS=17
TOKEN_INCLUDE=11
TOKEN_XKB_SYMBOLS=10
EOF=-1
MAPTYPE=15
TOKEN_PARTIAL=6
NAME=23
MAPMATERIAL=18
KEYSYMS=21
COMMENT=25
TOKEN_DEFAULT=4
T__42=42
T__43=43
TOKEN_ALTERNATE_GROUP=9
T__40=40
T__41=41
T__46=46
T__44=44
T__45=45
SECTION=19
LINE_COMMENT=26
KEYCODE=20
TOKEN_NAME=13
VALUE=22
T__30=30
T__31=31
T__32=32
WS=24
T__33=33
T__34=34
T__35=35
TOKEN_HIDDEN=5
TOKEN_ALPHANUMERIC_KEYS=7
T__36=36
T__37=37
T__38=38
T__39=39
TOKEN_MODIFIER_KEYS=8
TOKEN_KEY=14
MAPNAME=16
TOKEN_KEY_TYPE=12

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "TOKEN_DEFAULT", "TOKEN_HIDDEN", "TOKEN_PARTIAL", "TOKEN_ALPHANUMERIC_KEYS", 
    "TOKEN_MODIFIER_KEYS", "TOKEN_ALTERNATE_GROUP", "TOKEN_XKB_SYMBOLS", 
    "TOKEN_INCLUDE", "TOKEN_KEY_TYPE", "TOKEN_NAME", "TOKEN_KEY", "MAPTYPE", 
    "MAPNAME", "MAPOPTIONS", "MAPMATERIAL", "SECTION", "KEYCODE", "KEYSYMS", 
    "VALUE", "NAME", "WS", "COMMENT", "LINE_COMMENT", "'\"'", "'{'", "';'", 
    "'}'", "'include'", "'name'", "'['", "']'", "'='", "'key.type'", "'key'", 
    "'<'", "'>'", "','", "'default'", "'hidden'", "'partial'", "'alphanumeric_keys'", 
    "'alternate_group'", "'xkb_symbols'"
]




class XKBGrammarParser(Parser):
    grammarFileName = "XKBGrammar.g"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)






                
        self.adaptor = CommonTreeAdaptor()



        


    class layout_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start layout
    # XKBGrammar.g:57:1: layout : ( section )+ EOF ;
    def layout(self, ):

        retval = self.layout_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF2 = None
        section1 = None


        EOF2_tree = None

        try:
            try:
                # XKBGrammar.g:58:2: ( ( section )+ EOF )
                # XKBGrammar.g:58:4: ( section )+ EOF
                root_0 = self.adaptor.nil()

                # XKBGrammar.g:58:4: ( section )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((41 <= LA1_0 <= 46)) :
                        alt1 = 1


                    if alt1 == 1:
                        # XKBGrammar.g:58:4: section
                        self._state.following.append(self.FOLLOW_section_in_layout144)
                        section1 = self.section()

                        self._state.following.pop()
                        self.adaptor.addChild(root_0, section1.tree)



                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                EOF2 = self.input.LT(1)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_layout147)




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self.adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
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
    # XKBGrammar.g:61:1: section : mapType mapMaterial -> ^( SECTION mapType mapMaterial ) ;
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
                # XKBGrammar.g:62:2: ( mapType mapMaterial -> ^( SECTION mapType mapMaterial ) )
                # XKBGrammar.g:62:4: mapType mapMaterial
                self._state.following.append(self.FOLLOW_mapType_in_section161)
                mapType3 = self.mapType()

                self._state.following.pop()
                stream_mapType.add(mapType3.tree)
                self._state.following.append(self.FOLLOW_mapMaterial_in_section163)
                mapMaterial4 = self.mapMaterial()

                self._state.following.pop()
                stream_mapMaterial.add(mapMaterial4.tree)
                # AST Rewrite
                # elements: mapMaterial, mapType
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
                # 63:2: -> ^( SECTION mapType mapMaterial )
                # XKBGrammar.g:63:5: ^( SECTION mapType mapMaterial )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(SECTION, "SECTION"), root_1)

                self.adaptor.addChild(root_1, stream_mapType.nextTree())
                self.adaptor.addChild(root_1, stream_mapMaterial.nextTree())

                self.adaptor.addChild(root_0, root_1)



                retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self.adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
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
    # XKBGrammar.g:66:1: mapType : ( mapOptions )+ '\"' NAME '\"' -> ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME NAME ) ) ;
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
        stream_27 = RewriteRuleTokenStream(self.adaptor, "token 27")
        stream_mapOptions = RewriteRuleSubtreeStream(self.adaptor, "rule mapOptions")
        try:
            try:
                # XKBGrammar.g:67:2: ( ( mapOptions )+ '\"' NAME '\"' -> ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME NAME ) ) )
                # XKBGrammar.g:67:4: ( mapOptions )+ '\"' NAME '\"'
                # XKBGrammar.g:67:4: ( mapOptions )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((41 <= LA2_0 <= 46)) :
                        alt2 = 1


                    if alt2 == 1:
                        # XKBGrammar.g:67:4: mapOptions
                        self._state.following.append(self.FOLLOW_mapOptions_in_mapType186)
                        mapOptions5 = self.mapOptions()

                        self._state.following.pop()
                        stream_mapOptions.add(mapOptions5.tree)



                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1


                char_literal6 = self.input.LT(1)
                self.match(self.input, 27, self.FOLLOW_27_in_mapType189) 
                stream_27.add(char_literal6)
                NAME7 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_mapType191) 
                stream_NAME.add(NAME7)
                char_literal8 = self.input.LT(1)
                self.match(self.input, 27, self.FOLLOW_27_in_mapType193) 
                stream_27.add(char_literal8)
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
                # 68:2: -> ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME NAME ) )
                # XKBGrammar.g:68:5: ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME NAME ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPTYPE, "MAPTYPE"), root_1)

                # XKBGrammar.g:68:15: ^( MAPOPTIONS ( mapOptions )+ )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPOPTIONS, "MAPOPTIONS"), root_2)

                # XKBGrammar.g:68:28: ( mapOptions )+
                if not (stream_mapOptions.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_mapOptions.hasNext():
                    self.adaptor.addChild(root_2, stream_mapOptions.nextTree())


                stream_mapOptions.reset()

                self.adaptor.addChild(root_1, root_2)
                # XKBGrammar.g:68:41: ^( MAPNAME NAME )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPNAME, "MAPNAME"), root_2)

                self.adaptor.addChild(root_2, stream_NAME.nextNode())

                self.adaptor.addChild(root_1, root_2)

                self.adaptor.addChild(root_0, root_1)



                retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self.adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
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
    # XKBGrammar.g:71:1: mapMaterial : '{' ( line_include | line_name ';' | line_keytype ';' | line_key ';' )+ '}' ';' ;
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
                # XKBGrammar.g:72:2: ( '{' ( line_include | line_name ';' | line_keytype ';' | line_key ';' )+ '}' ';' )
                # XKBGrammar.g:72:4: '{' ( line_include | line_name ';' | line_keytype ';' | line_key ';' )+ '}' ';'
                root_0 = self.adaptor.nil()

                char_literal9 = self.input.LT(1)
                self.match(self.input, 28, self.FOLLOW_28_in_mapMaterial225)

                char_literal9_tree = self.adaptor.createWithPayload(char_literal9)
                self.adaptor.addChild(root_0, char_literal9_tree)

                # XKBGrammar.g:73:2: ( line_include | line_name ';' | line_keytype ';' | line_key ';' )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 5
                    LA3 = self.input.LA(1)
                    if LA3 == 31:
                        alt3 = 1
                    elif LA3 == 32:
                        alt3 = 2
                    elif LA3 == 36:
                        alt3 = 3
                    elif LA3 == 37:
                        alt3 = 4

                    if alt3 == 1:
                        # XKBGrammar.g:73:4: line_include
                        self._state.following.append(self.FOLLOW_line_include_in_mapMaterial230)
                        line_include10 = self.line_include()

                        self._state.following.pop()
                        self.adaptor.addChild(root_0, line_include10.tree)



                    elif alt3 == 2:
                        # XKBGrammar.g:74:4: line_name ';'
                        self._state.following.append(self.FOLLOW_line_name_in_mapMaterial236)
                        line_name11 = self.line_name()

                        self._state.following.pop()
                        self.adaptor.addChild(root_0, line_name11.tree)
                        char_literal12 = self.input.LT(1)
                        self.match(self.input, 29, self.FOLLOW_29_in_mapMaterial238)



                    elif alt3 == 3:
                        # XKBGrammar.g:75:4: line_keytype ';'
                        self._state.following.append(self.FOLLOW_line_keytype_in_mapMaterial244)
                        line_keytype13 = self.line_keytype()

                        self._state.following.pop()
                        self.adaptor.addChild(root_0, line_keytype13.tree)
                        char_literal14 = self.input.LT(1)
                        self.match(self.input, 29, self.FOLLOW_29_in_mapMaterial246)



                    elif alt3 == 4:
                        # XKBGrammar.g:76:4: line_key ';'
                        self._state.following.append(self.FOLLOW_line_key_in_mapMaterial252)
                        line_key15 = self.line_key()

                        self._state.following.pop()
                        self.adaptor.addChild(root_0, line_key15.tree)
                        char_literal16 = self.input.LT(1)
                        self.match(self.input, 29, self.FOLLOW_29_in_mapMaterial254)



                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


                char_literal17 = self.input.LT(1)
                self.match(self.input, 30, self.FOLLOW_30_in_mapMaterial261)

                char_literal17_tree = self.adaptor.createWithPayload(char_literal17)
                self.adaptor.addChild(root_0, char_literal17_tree)

                char_literal18 = self.input.LT(1)
                self.match(self.input, 29, self.FOLLOW_29_in_mapMaterial263)




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self.adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
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
    # XKBGrammar.g:80:1: line_include : 'include' '\"' NAME '\"' -> ^( TOKEN_INCLUDE NAME ) ;
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
        stream_27 = RewriteRuleTokenStream(self.adaptor, "token 27")

        try:
            try:
                # XKBGrammar.g:81:2: ( 'include' '\"' NAME '\"' -> ^( TOKEN_INCLUDE NAME ) )
                # XKBGrammar.g:81:4: 'include' '\"' NAME '\"'
                string_literal19 = self.input.LT(1)
                self.match(self.input, 31, self.FOLLOW_31_in_line_include275) 
                stream_31.add(string_literal19)
                char_literal20 = self.input.LT(1)
                self.match(self.input, 27, self.FOLLOW_27_in_line_include277) 
                stream_27.add(char_literal20)
                NAME21 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_include279) 
                stream_NAME.add(NAME21)
                char_literal22 = self.input.LT(1)
                self.match(self.input, 27, self.FOLLOW_27_in_line_include281) 
                stream_27.add(char_literal22)
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
                # 82:2: -> ^( TOKEN_INCLUDE NAME )
                # XKBGrammar.g:82:5: ^( TOKEN_INCLUDE NAME )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_INCLUDE, "TOKEN_INCLUDE"), root_1)

                self.adaptor.addChild(root_1, stream_NAME.nextNode())

                self.adaptor.addChild(root_0, root_1)



                retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self.adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
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
    # XKBGrammar.g:85:1: line_name : 'name' '[' n1= NAME ']' '=' '\"' n2= NAME '\"' -> ^( TOKEN_NAME $n1 ^( VALUE $n2) ) ;
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
        stream_32 = RewriteRuleTokenStream(self.adaptor, "token 32")
        stream_35 = RewriteRuleTokenStream(self.adaptor, "token 35")
        stream_33 = RewriteRuleTokenStream(self.adaptor, "token 33")
        stream_34 = RewriteRuleTokenStream(self.adaptor, "token 34")
        stream_27 = RewriteRuleTokenStream(self.adaptor, "token 27")

        try:
            try:
                # XKBGrammar.g:86:2: ( 'name' '[' n1= NAME ']' '=' '\"' n2= NAME '\"' -> ^( TOKEN_NAME $n1 ^( VALUE $n2) ) )
                # XKBGrammar.g:86:4: 'name' '[' n1= NAME ']' '=' '\"' n2= NAME '\"'
                string_literal23 = self.input.LT(1)
                self.match(self.input, 32, self.FOLLOW_32_in_line_name301) 
                stream_32.add(string_literal23)
                char_literal24 = self.input.LT(1)
                self.match(self.input, 33, self.FOLLOW_33_in_line_name303) 
                stream_33.add(char_literal24)
                n1 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_name307) 
                stream_NAME.add(n1)
                char_literal25 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_line_name309) 
                stream_34.add(char_literal25)
                char_literal26 = self.input.LT(1)
                self.match(self.input, 35, self.FOLLOW_35_in_line_name311) 
                stream_35.add(char_literal26)
                char_literal27 = self.input.LT(1)
                self.match(self.input, 27, self.FOLLOW_27_in_line_name313) 
                stream_27.add(char_literal27)
                n2 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_name317) 
                stream_NAME.add(n2)
                char_literal28 = self.input.LT(1)
                self.match(self.input, 27, self.FOLLOW_27_in_line_name319) 
                stream_27.add(char_literal28)
                # AST Rewrite
                # elements: n1, n2
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
                # 87:2: -> ^( TOKEN_NAME $n1 ^( VALUE $n2) )
                # XKBGrammar.g:87:5: ^( TOKEN_NAME $n1 ^( VALUE $n2) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_NAME, "TOKEN_NAME"), root_1)

                self.adaptor.addChild(root_1, stream_n1.nextNode())
                # XKBGrammar.g:87:22: ^( VALUE $n2)
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(VALUE, "VALUE"), root_2)

                self.adaptor.addChild(root_2, stream_n2.nextNode())

                self.adaptor.addChild(root_1, root_2)

                self.adaptor.addChild(root_0, root_1)



                retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self.adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
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
    # XKBGrammar.g:90:1: line_keytype : 'key.type' '[' n1= NAME ']' '=' '\"' n2= NAME '\"' -> ^( TOKEN_KEY_TYPE $n1 ^( VALUE $n2) ) ;
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
        stream_35 = RewriteRuleTokenStream(self.adaptor, "token 35")
        stream_36 = RewriteRuleTokenStream(self.adaptor, "token 36")
        stream_33 = RewriteRuleTokenStream(self.adaptor, "token 33")
        stream_34 = RewriteRuleTokenStream(self.adaptor, "token 34")
        stream_27 = RewriteRuleTokenStream(self.adaptor, "token 27")

        try:
            try:
                # XKBGrammar.g:91:2: ( 'key.type' '[' n1= NAME ']' '=' '\"' n2= NAME '\"' -> ^( TOKEN_KEY_TYPE $n1 ^( VALUE $n2) ) )
                # XKBGrammar.g:91:4: 'key.type' '[' n1= NAME ']' '=' '\"' n2= NAME '\"'
                string_literal29 = self.input.LT(1)
                self.match(self.input, 36, self.FOLLOW_36_in_line_keytype347) 
                stream_36.add(string_literal29)
                char_literal30 = self.input.LT(1)
                self.match(self.input, 33, self.FOLLOW_33_in_line_keytype349) 
                stream_33.add(char_literal30)
                n1 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype353) 
                stream_NAME.add(n1)
                char_literal31 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_line_keytype355) 
                stream_34.add(char_literal31)
                char_literal32 = self.input.LT(1)
                self.match(self.input, 35, self.FOLLOW_35_in_line_keytype357) 
                stream_35.add(char_literal32)
                char_literal33 = self.input.LT(1)
                self.match(self.input, 27, self.FOLLOW_27_in_line_keytype359) 
                stream_27.add(char_literal33)
                n2 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype363) 
                stream_NAME.add(n2)
                char_literal34 = self.input.LT(1)
                self.match(self.input, 27, self.FOLLOW_27_in_line_keytype365) 
                stream_27.add(char_literal34)
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
                # 92:2: -> ^( TOKEN_KEY_TYPE $n1 ^( VALUE $n2) )
                # XKBGrammar.g:92:5: ^( TOKEN_KEY_TYPE $n1 ^( VALUE $n2) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_KEY_TYPE, "TOKEN_KEY_TYPE"), root_1)

                self.adaptor.addChild(root_1, stream_n1.nextNode())
                # XKBGrammar.g:92:26: ^( VALUE $n2)
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(VALUE, "VALUE"), root_2)

                self.adaptor.addChild(root_2, stream_n2.nextNode())

                self.adaptor.addChild(root_1, root_2)

                self.adaptor.addChild(root_0, root_1)



                retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self.adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
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
    # XKBGrammar.g:95:1: line_key : 'key' keycode keysyms -> ^( TOKEN_KEY keycode keysyms ) ;
    def line_key(self, ):

        retval = self.line_key_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal35 = None
        keycode36 = None

        keysyms37 = None


        string_literal35_tree = None
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_keysyms = RewriteRuleSubtreeStream(self.adaptor, "rule keysyms")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        try:
            try:
                # XKBGrammar.g:96:2: ( 'key' keycode keysyms -> ^( TOKEN_KEY keycode keysyms ) )
                # XKBGrammar.g:96:4: 'key' keycode keysyms
                string_literal35 = self.input.LT(1)
                self.match(self.input, 37, self.FOLLOW_37_in_line_key394) 
                stream_37.add(string_literal35)
                self._state.following.append(self.FOLLOW_keycode_in_line_key396)
                keycode36 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode36.tree)
                self._state.following.append(self.FOLLOW_keysyms_in_line_key398)
                keysyms37 = self.keysyms()

                self._state.following.pop()
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
                # 97:2: -> ^( TOKEN_KEY keycode keysyms )
                # XKBGrammar.g:97:5: ^( TOKEN_KEY keycode keysyms )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_KEY, "TOKEN_KEY"), root_1)

                self.adaptor.addChild(root_1, stream_keycode.nextTree())
                self.adaptor.addChild(root_1, stream_keysyms.nextTree())

                self.adaptor.addChild(root_0, root_1)



                retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self.adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
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
    # XKBGrammar.g:100:1: keycode : '<' NAME '>' -> ^( KEYCODE NAME ) ;
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
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")

        try:
            try:
                # XKBGrammar.g:101:2: ( '<' NAME '>' -> ^( KEYCODE NAME ) )
                # XKBGrammar.g:101:4: '<' NAME '>'
                char_literal38 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_keycode422) 
                stream_38.add(char_literal38)
                NAME39 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode424) 
                stream_NAME.add(NAME39)
                char_literal40 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_keycode426) 
                stream_39.add(char_literal40)
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
                # 102:2: -> ^( KEYCODE NAME )
                # XKBGrammar.g:102:5: ^( KEYCODE NAME )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYCODE, "KEYCODE"), root_1)

                self.adaptor.addChild(root_1, stream_NAME.nextNode())

                self.adaptor.addChild(root_0, root_1)



                retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self.adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
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
    # XKBGrammar.g:105:1: keysyms : '{' '[' keysym+= NAME ( ',' keysym+= NAME )* ']' '}' -> ^( KEYSYMS ( $keysym)+ ) ;
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
        stream_30 = RewriteRuleTokenStream(self.adaptor, "token 30")
        stream_40 = RewriteRuleTokenStream(self.adaptor, "token 40")
        stream_33 = RewriteRuleTokenStream(self.adaptor, "token 33")
        stream_34 = RewriteRuleTokenStream(self.adaptor, "token 34")
        stream_28 = RewriteRuleTokenStream(self.adaptor, "token 28")

        try:
            try:
                # XKBGrammar.g:106:2: ( '{' '[' keysym+= NAME ( ',' keysym+= NAME )* ']' '}' -> ^( KEYSYMS ( $keysym)+ ) )
                # XKBGrammar.g:106:4: '{' '[' keysym+= NAME ( ',' keysym+= NAME )* ']' '}'
                char_literal41 = self.input.LT(1)
                self.match(self.input, 28, self.FOLLOW_28_in_keysyms446) 
                stream_28.add(char_literal41)
                char_literal42 = self.input.LT(1)
                self.match(self.input, 33, self.FOLLOW_33_in_keysyms448) 
                stream_33.add(char_literal42)
                keysym = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_keysyms452) 
                stream_NAME.add(keysym)
                if list_keysym is None:
                    list_keysym = []
                list_keysym.append(keysym)

                # XKBGrammar.g:106:25: ( ',' keysym+= NAME )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == 40) :
                        alt4 = 1


                    if alt4 == 1:
                        # XKBGrammar.g:106:26: ',' keysym+= NAME
                        char_literal43 = self.input.LT(1)
                        self.match(self.input, 40, self.FOLLOW_40_in_keysyms455) 
                        stream_40.add(char_literal43)
                        keysym = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_keysyms459) 
                        stream_NAME.add(keysym)
                        if list_keysym is None:
                            list_keysym = []
                        list_keysym.append(keysym)




                    else:
                        break #loop4


                char_literal44 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_keysyms463) 
                stream_34.add(char_literal44)
                char_literal45 = self.input.LT(1)
                self.match(self.input, 30, self.FOLLOW_30_in_keysyms465) 
                stream_30.add(char_literal45)
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
                # 107:2: -> ^( KEYSYMS ( $keysym)+ )
                # XKBGrammar.g:107:5: ^( KEYSYMS ( $keysym)+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYSYMS, "KEYSYMS"), root_1)

                # XKBGrammar.g:107:15: ( $keysym)+
                if not (stream_keysym.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_keysym.hasNext():
                    self.adaptor.addChild(root_1, stream_keysym.nextNode())


                stream_keysym.reset()

                self.adaptor.addChild(root_0, root_1)



                retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self.adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
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
    # XKBGrammar.g:110:1: mapOptions : ( 'default' | 'hidden' | 'partial' | 'alphanumeric_keys' | 'alternate_group' | 'xkb_symbols' );
    def mapOptions(self, ):

        retval = self.mapOptions_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set46 = None

        set46_tree = None

        try:
            try:
                # XKBGrammar.g:111:2: ( 'default' | 'hidden' | 'partial' | 'alphanumeric_keys' | 'alternate_group' | 'xkb_symbols' )
                # XKBGrammar.g:
                root_0 = self.adaptor.nil()

                set46 = self.input.LT(1)
                if (41 <= self.input.LA(1) <= 46):
                    self.input.consume();
                    self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set46))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self.adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end mapOptions


    # Delegated rules


 

    FOLLOW_section_in_layout144 = frozenset([41, 42, 43, 44, 45, 46])
    FOLLOW_EOF_in_layout147 = frozenset([1])
    FOLLOW_mapType_in_section161 = frozenset([28])
    FOLLOW_mapMaterial_in_section163 = frozenset([1])
    FOLLOW_mapOptions_in_mapType186 = frozenset([27, 41, 42, 43, 44, 45, 46])
    FOLLOW_27_in_mapType189 = frozenset([23])
    FOLLOW_NAME_in_mapType191 = frozenset([27])
    FOLLOW_27_in_mapType193 = frozenset([1])
    FOLLOW_28_in_mapMaterial225 = frozenset([31, 32, 36, 37])
    FOLLOW_line_include_in_mapMaterial230 = frozenset([30, 31, 32, 36, 37])
    FOLLOW_line_name_in_mapMaterial236 = frozenset([29])
    FOLLOW_29_in_mapMaterial238 = frozenset([30, 31, 32, 36, 37])
    FOLLOW_line_keytype_in_mapMaterial244 = frozenset([29])
    FOLLOW_29_in_mapMaterial246 = frozenset([30, 31, 32, 36, 37])
    FOLLOW_line_key_in_mapMaterial252 = frozenset([29])
    FOLLOW_29_in_mapMaterial254 = frozenset([30, 31, 32, 36, 37])
    FOLLOW_30_in_mapMaterial261 = frozenset([29])
    FOLLOW_29_in_mapMaterial263 = frozenset([1])
    FOLLOW_31_in_line_include275 = frozenset([27])
    FOLLOW_27_in_line_include277 = frozenset([23])
    FOLLOW_NAME_in_line_include279 = frozenset([27])
    FOLLOW_27_in_line_include281 = frozenset([1])
    FOLLOW_32_in_line_name301 = frozenset([33])
    FOLLOW_33_in_line_name303 = frozenset([23])
    FOLLOW_NAME_in_line_name307 = frozenset([34])
    FOLLOW_34_in_line_name309 = frozenset([35])
    FOLLOW_35_in_line_name311 = frozenset([27])
    FOLLOW_27_in_line_name313 = frozenset([23])
    FOLLOW_NAME_in_line_name317 = frozenset([27])
    FOLLOW_27_in_line_name319 = frozenset([1])
    FOLLOW_36_in_line_keytype347 = frozenset([33])
    FOLLOW_33_in_line_keytype349 = frozenset([23])
    FOLLOW_NAME_in_line_keytype353 = frozenset([34])
    FOLLOW_34_in_line_keytype355 = frozenset([35])
    FOLLOW_35_in_line_keytype357 = frozenset([27])
    FOLLOW_27_in_line_keytype359 = frozenset([23])
    FOLLOW_NAME_in_line_keytype363 = frozenset([27])
    FOLLOW_27_in_line_keytype365 = frozenset([1])
    FOLLOW_37_in_line_key394 = frozenset([38])
    FOLLOW_keycode_in_line_key396 = frozenset([28])
    FOLLOW_keysyms_in_line_key398 = frozenset([1])
    FOLLOW_38_in_keycode422 = frozenset([23])
    FOLLOW_NAME_in_keycode424 = frozenset([39])
    FOLLOW_39_in_keycode426 = frozenset([1])
    FOLLOW_28_in_keysyms446 = frozenset([33])
    FOLLOW_33_in_keysyms448 = frozenset([23])
    FOLLOW_NAME_in_keysyms452 = frozenset([34, 40])
    FOLLOW_40_in_keysyms455 = frozenset([23])
    FOLLOW_NAME_in_keysyms459 = frozenset([34, 40])
    FOLLOW_34_in_keysyms463 = frozenset([30])
    FOLLOW_30_in_keysyms465 = frozenset([1])
    FOLLOW_set_in_mapOptions0 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("XKBGrammarLexer", XKBGrammarParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)

if __name__ == '__main__':
    main(sys.argv)
