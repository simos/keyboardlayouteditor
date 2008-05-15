# $ANTLR 3.1b1 XKBGrammar.g 2008-05-15 22:34:00

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__29=29
T__28=28
MAPOPTIONS=17
TOKEN_INCLUDE=11
TOKEN_XKB_SYMBOLS=10
EOF=-1
MAPTYPE=15
TOKEN_PARTIAL=6
NAME=24
MAPMATERIAL=18
KEYSYMS=21
COMMENT=26
TOKEN_DEFAULT=4
DQSTRING=23
T__42=42
T__43=43
TOKEN_ALTERNATE_GROUP=9
T__40=40
T__41=41
T__46=46
T__44=44
T__45=45
SECTION=19
LINE_COMMENT=27
KEYCODE=20
TOKEN_NAME=13
VALUE=22
T__30=30
T__31=31
T__32=32
WS=25
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
    "VALUE", "DQSTRING", "NAME", "WS", "COMMENT", "LINE_COMMENT", "'{'", 
    "'}'", "';'", "'include'", "'name'", "'['", "']'", "'='", "'key.type'", 
    "'key'", "'<'", "'>'", "','", "'default'", "'hidden'", "'partial'", 
    "'alphanumeric_keys'", "'alternate_group'", "'xkb_symbols'"
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
    # XKBGrammar.g:61:1: section : mapType '{' ( mapMaterial )+ '}' ';' -> ^( SECTION mapType ^( MAPMATERIAL ( mapMaterial )+ ) ) ;
    def section(self, ):

        retval = self.section_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal4 = None
        char_literal6 = None
        char_literal7 = None
        mapType3 = None

        mapMaterial5 = None


        char_literal4_tree = None
        char_literal6_tree = None
        char_literal7_tree = None
        stream_30 = RewriteRuleTokenStream(self.adaptor, "token 30")
        stream_28 = RewriteRuleTokenStream(self.adaptor, "token 28")
        stream_29 = RewriteRuleTokenStream(self.adaptor, "token 29")
        stream_mapMaterial = RewriteRuleSubtreeStream(self.adaptor, "rule mapMaterial")
        stream_mapType = RewriteRuleSubtreeStream(self.adaptor, "rule mapType")
        try:
            try:
                # XKBGrammar.g:62:2: ( mapType '{' ( mapMaterial )+ '}' ';' -> ^( SECTION mapType ^( MAPMATERIAL ( mapMaterial )+ ) ) )
                # XKBGrammar.g:62:4: mapType '{' ( mapMaterial )+ '}' ';'
                self._state.following.append(self.FOLLOW_mapType_in_section161)
                mapType3 = self.mapType()

                self._state.following.pop()
                stream_mapType.add(mapType3.tree)
                char_literal4 = self.input.LT(1)
                self.match(self.input, 28, self.FOLLOW_28_in_section163) 
                stream_28.add(char_literal4)
                # XKBGrammar.g:62:16: ( mapMaterial )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((31 <= LA2_0 <= 32) or (36 <= LA2_0 <= 37)) :
                        alt2 = 1


                    if alt2 == 1:
                        # XKBGrammar.g:62:16: mapMaterial
                        self._state.following.append(self.FOLLOW_mapMaterial_in_section165)
                        mapMaterial5 = self.mapMaterial()

                        self._state.following.pop()
                        stream_mapMaterial.add(mapMaterial5.tree)



                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1


                char_literal6 = self.input.LT(1)
                self.match(self.input, 29, self.FOLLOW_29_in_section168) 
                stream_29.add(char_literal6)
                char_literal7 = self.input.LT(1)
                self.match(self.input, 30, self.FOLLOW_30_in_section170) 
                stream_30.add(char_literal7)
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
                # 63:2: -> ^( SECTION mapType ^( MAPMATERIAL ( mapMaterial )+ ) )
                # XKBGrammar.g:63:5: ^( SECTION mapType ^( MAPMATERIAL ( mapMaterial )+ ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(SECTION, "SECTION"), root_1)

                self.adaptor.addChild(root_1, stream_mapType.nextTree())
                # XKBGrammar.g:63:23: ^( MAPMATERIAL ( mapMaterial )+ )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPMATERIAL, "MAPMATERIAL"), root_2)

                # XKBGrammar.g:63:37: ( mapMaterial )+
                if not (stream_mapMaterial.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_mapMaterial.hasNext():
                    self.adaptor.addChild(root_2, stream_mapMaterial.nextTree())


                stream_mapMaterial.reset()

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

    # $ANTLR end section

    class mapType_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start mapType
    # XKBGrammar.g:66:1: mapType : ( mapOptions )+ DQSTRING -> ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME DQSTRING ) ) ;
    def mapType(self, ):

        retval = self.mapType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DQSTRING9 = None
        mapOptions8 = None


        DQSTRING9_tree = None
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")
        stream_mapOptions = RewriteRuleSubtreeStream(self.adaptor, "rule mapOptions")
        try:
            try:
                # XKBGrammar.g:67:2: ( ( mapOptions )+ DQSTRING -> ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME DQSTRING ) ) )
                # XKBGrammar.g:67:4: ( mapOptions )+ DQSTRING
                # XKBGrammar.g:67:4: ( mapOptions )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((41 <= LA3_0 <= 46)) :
                        alt3 = 1


                    if alt3 == 1:
                        # XKBGrammar.g:67:4: mapOptions
                        self._state.following.append(self.FOLLOW_mapOptions_in_mapType198)
                        mapOptions8 = self.mapOptions()

                        self._state.following.pop()
                        stream_mapOptions.add(mapOptions8.tree)



                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


                DQSTRING9 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_mapType201) 
                stream_DQSTRING.add(DQSTRING9)
                # AST Rewrite
                # elements: mapOptions, DQSTRING
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
                # 68:2: -> ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME DQSTRING ) )
                # XKBGrammar.g:68:5: ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME DQSTRING ) )
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
                # XKBGrammar.g:68:41: ^( MAPNAME DQSTRING )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPNAME, "MAPNAME"), root_2)

                self.adaptor.addChild(root_2, stream_DQSTRING.nextNode())

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
    # XKBGrammar.g:71:1: mapMaterial : ( line_include | line_name ';' | line_keytype ';' | line_key ';' );
    def mapMaterial(self, ):

        retval = self.mapMaterial_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal12 = None
        char_literal14 = None
        char_literal16 = None
        line_include10 = None

        line_name11 = None

        line_keytype13 = None

        line_key15 = None


        char_literal12_tree = None
        char_literal14_tree = None
        char_literal16_tree = None

        try:
            try:
                # XKBGrammar.g:72:2: ( line_include | line_name ';' | line_keytype ';' | line_key ';' )
                alt4 = 4
                LA4 = self.input.LA(1)
                if LA4 == 31:
                    alt4 = 1
                elif LA4 == 32:
                    alt4 = 2
                elif LA4 == 36:
                    alt4 = 3
                elif LA4 == 37:
                    alt4 = 4
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # XKBGrammar.g:72:4: line_include
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_include_in_mapMaterial233)
                    line_include10 = self.line_include()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_include10.tree)



                elif alt4 == 2:
                    # XKBGrammar.g:73:4: line_name ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_name_in_mapMaterial239)
                    line_name11 = self.line_name()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_name11.tree)
                    char_literal12 = self.input.LT(1)
                    self.match(self.input, 30, self.FOLLOW_30_in_mapMaterial241)



                elif alt4 == 3:
                    # XKBGrammar.g:74:4: line_keytype ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_keytype_in_mapMaterial247)
                    line_keytype13 = self.line_keytype()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_keytype13.tree)
                    char_literal14 = self.input.LT(1)
                    self.match(self.input, 30, self.FOLLOW_30_in_mapMaterial249)



                elif alt4 == 4:
                    # XKBGrammar.g:75:4: line_key ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_key_in_mapMaterial255)
                    line_key15 = self.line_key()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_key15.tree)
                    char_literal16 = self.input.LT(1)
                    self.match(self.input, 30, self.FOLLOW_30_in_mapMaterial257)



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
    # XKBGrammar.g:78:1: line_include : 'include' DQSTRING -> ^( TOKEN_INCLUDE DQSTRING ) ;
    def line_include(self, ):

        retval = self.line_include_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal17 = None
        DQSTRING18 = None

        string_literal17_tree = None
        DQSTRING18_tree = None
        stream_31 = RewriteRuleTokenStream(self.adaptor, "token 31")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")

        try:
            try:
                # XKBGrammar.g:79:2: ( 'include' DQSTRING -> ^( TOKEN_INCLUDE DQSTRING ) )
                # XKBGrammar.g:79:4: 'include' DQSTRING
                string_literal17 = self.input.LT(1)
                self.match(self.input, 31, self.FOLLOW_31_in_line_include269) 
                stream_31.add(string_literal17)
                DQSTRING18 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_include271) 
                stream_DQSTRING.add(DQSTRING18)
                # AST Rewrite
                # elements: DQSTRING
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
                # 80:2: -> ^( TOKEN_INCLUDE DQSTRING )
                # XKBGrammar.g:80:5: ^( TOKEN_INCLUDE DQSTRING )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_INCLUDE, "TOKEN_INCLUDE"), root_1)

                self.adaptor.addChild(root_1, stream_DQSTRING.nextNode())

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
    # XKBGrammar.g:83:1: line_name : 'name' '[' n1= NAME ']' '=' n2= DQSTRING -> ^( TOKEN_NAME $n1 ^( VALUE $n2) ) ;
    def line_name(self, ):

        retval = self.line_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        n1 = None
        n2 = None
        string_literal19 = None
        char_literal20 = None
        char_literal21 = None
        char_literal22 = None

        n1_tree = None
        n2_tree = None
        string_literal19_tree = None
        char_literal20_tree = None
        char_literal21_tree = None
        char_literal22_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_32 = RewriteRuleTokenStream(self.adaptor, "token 32")
        stream_35 = RewriteRuleTokenStream(self.adaptor, "token 35")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")
        stream_33 = RewriteRuleTokenStream(self.adaptor, "token 33")
        stream_34 = RewriteRuleTokenStream(self.adaptor, "token 34")

        try:
            try:
                # XKBGrammar.g:84:2: ( 'name' '[' n1= NAME ']' '=' n2= DQSTRING -> ^( TOKEN_NAME $n1 ^( VALUE $n2) ) )
                # XKBGrammar.g:84:4: 'name' '[' n1= NAME ']' '=' n2= DQSTRING
                string_literal19 = self.input.LT(1)
                self.match(self.input, 32, self.FOLLOW_32_in_line_name291) 
                stream_32.add(string_literal19)
                char_literal20 = self.input.LT(1)
                self.match(self.input, 33, self.FOLLOW_33_in_line_name293) 
                stream_33.add(char_literal20)
                n1 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_name297) 
                stream_NAME.add(n1)
                char_literal21 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_line_name299) 
                stream_34.add(char_literal21)
                char_literal22 = self.input.LT(1)
                self.match(self.input, 35, self.FOLLOW_35_in_line_name301) 
                stream_35.add(char_literal22)
                n2 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_name305) 
                stream_DQSTRING.add(n2)
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
                # 85:2: -> ^( TOKEN_NAME $n1 ^( VALUE $n2) )
                # XKBGrammar.g:85:5: ^( TOKEN_NAME $n1 ^( VALUE $n2) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_NAME, "TOKEN_NAME"), root_1)

                self.adaptor.addChild(root_1, stream_n1.nextNode())
                # XKBGrammar.g:85:22: ^( VALUE $n2)
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
    # XKBGrammar.g:88:1: line_keytype : 'key.type' '[' n1= NAME ']' '=' n2= DQSTRING -> ^( TOKEN_KEY_TYPE $n1 ^( VALUE $n2) ) ;
    def line_keytype(self, ):

        retval = self.line_keytype_return()
        retval.start = self.input.LT(1)

        root_0 = None

        n1 = None
        n2 = None
        string_literal23 = None
        char_literal24 = None
        char_literal25 = None
        char_literal26 = None

        n1_tree = None
        n2_tree = None
        string_literal23_tree = None
        char_literal24_tree = None
        char_literal25_tree = None
        char_literal26_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_35 = RewriteRuleTokenStream(self.adaptor, "token 35")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")
        stream_36 = RewriteRuleTokenStream(self.adaptor, "token 36")
        stream_33 = RewriteRuleTokenStream(self.adaptor, "token 33")
        stream_34 = RewriteRuleTokenStream(self.adaptor, "token 34")

        try:
            try:
                # XKBGrammar.g:89:2: ( 'key.type' '[' n1= NAME ']' '=' n2= DQSTRING -> ^( TOKEN_KEY_TYPE $n1 ^( VALUE $n2) ) )
                # XKBGrammar.g:89:4: 'key.type' '[' n1= NAME ']' '=' n2= DQSTRING
                string_literal23 = self.input.LT(1)
                self.match(self.input, 36, self.FOLLOW_36_in_line_keytype333) 
                stream_36.add(string_literal23)
                char_literal24 = self.input.LT(1)
                self.match(self.input, 33, self.FOLLOW_33_in_line_keytype335) 
                stream_33.add(char_literal24)
                n1 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype339) 
                stream_NAME.add(n1)
                char_literal25 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_line_keytype341) 
                stream_34.add(char_literal25)
                char_literal26 = self.input.LT(1)
                self.match(self.input, 35, self.FOLLOW_35_in_line_keytype343) 
                stream_35.add(char_literal26)
                n2 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_keytype347) 
                stream_DQSTRING.add(n2)
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
                # 90:2: -> ^( TOKEN_KEY_TYPE $n1 ^( VALUE $n2) )
                # XKBGrammar.g:90:5: ^( TOKEN_KEY_TYPE $n1 ^( VALUE $n2) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_KEY_TYPE, "TOKEN_KEY_TYPE"), root_1)

                self.adaptor.addChild(root_1, stream_n1.nextNode())
                # XKBGrammar.g:90:26: ^( VALUE $n2)
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
    # XKBGrammar.g:93:1: line_key : 'key' keycode keysyms -> ^( TOKEN_KEY keycode keysyms ) ;
    def line_key(self, ):

        retval = self.line_key_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal27 = None
        keycode28 = None

        keysyms29 = None


        string_literal27_tree = None
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_keysyms = RewriteRuleSubtreeStream(self.adaptor, "rule keysyms")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        try:
            try:
                # XKBGrammar.g:94:2: ( 'key' keycode keysyms -> ^( TOKEN_KEY keycode keysyms ) )
                # XKBGrammar.g:94:4: 'key' keycode keysyms
                string_literal27 = self.input.LT(1)
                self.match(self.input, 37, self.FOLLOW_37_in_line_key376) 
                stream_37.add(string_literal27)
                self._state.following.append(self.FOLLOW_keycode_in_line_key378)
                keycode28 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode28.tree)
                self._state.following.append(self.FOLLOW_keysyms_in_line_key380)
                keysyms29 = self.keysyms()

                self._state.following.pop()
                stream_keysyms.add(keysyms29.tree)
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
                # 95:2: -> ^( TOKEN_KEY keycode keysyms )
                # XKBGrammar.g:95:5: ^( TOKEN_KEY keycode keysyms )
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
    # XKBGrammar.g:98:1: keycode : '<' NAME '>' -> ^( KEYCODE NAME ) ;
    def keycode(self, ):

        retval = self.keycode_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal30 = None
        NAME31 = None
        char_literal32 = None

        char_literal30_tree = None
        NAME31_tree = None
        char_literal32_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")

        try:
            try:
                # XKBGrammar.g:99:2: ( '<' NAME '>' -> ^( KEYCODE NAME ) )
                # XKBGrammar.g:99:4: '<' NAME '>'
                char_literal30 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_keycode404) 
                stream_38.add(char_literal30)
                NAME31 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode406) 
                stream_NAME.add(NAME31)
                char_literal32 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_keycode408) 
                stream_39.add(char_literal32)
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
                # 100:2: -> ^( KEYCODE NAME )
                # XKBGrammar.g:100:5: ^( KEYCODE NAME )
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
    # XKBGrammar.g:103:1: keysyms : '{' '[' keysym+= NAME ( ',' keysym+= NAME )* ']' '}' -> ^( KEYSYMS ( $keysym)+ ) ;
    def keysyms(self, ):

        retval = self.keysyms_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal33 = None
        char_literal34 = None
        char_literal35 = None
        char_literal36 = None
        char_literal37 = None
        keysym = None
        list_keysym = None

        char_literal33_tree = None
        char_literal34_tree = None
        char_literal35_tree = None
        char_literal36_tree = None
        char_literal37_tree = None
        keysym_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_40 = RewriteRuleTokenStream(self.adaptor, "token 40")
        stream_33 = RewriteRuleTokenStream(self.adaptor, "token 33")
        stream_34 = RewriteRuleTokenStream(self.adaptor, "token 34")
        stream_28 = RewriteRuleTokenStream(self.adaptor, "token 28")
        stream_29 = RewriteRuleTokenStream(self.adaptor, "token 29")

        try:
            try:
                # XKBGrammar.g:104:2: ( '{' '[' keysym+= NAME ( ',' keysym+= NAME )* ']' '}' -> ^( KEYSYMS ( $keysym)+ ) )
                # XKBGrammar.g:104:4: '{' '[' keysym+= NAME ( ',' keysym+= NAME )* ']' '}'
                char_literal33 = self.input.LT(1)
                self.match(self.input, 28, self.FOLLOW_28_in_keysyms428) 
                stream_28.add(char_literal33)
                char_literal34 = self.input.LT(1)
                self.match(self.input, 33, self.FOLLOW_33_in_keysyms430) 
                stream_33.add(char_literal34)
                keysym = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_keysyms434) 
                stream_NAME.add(keysym)
                if list_keysym is None:
                    list_keysym = []
                list_keysym.append(keysym)

                # XKBGrammar.g:104:25: ( ',' keysym+= NAME )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == 40) :
                        alt5 = 1


                    if alt5 == 1:
                        # XKBGrammar.g:104:26: ',' keysym+= NAME
                        char_literal35 = self.input.LT(1)
                        self.match(self.input, 40, self.FOLLOW_40_in_keysyms437) 
                        stream_40.add(char_literal35)
                        keysym = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_keysyms441) 
                        stream_NAME.add(keysym)
                        if list_keysym is None:
                            list_keysym = []
                        list_keysym.append(keysym)




                    else:
                        break #loop5


                char_literal36 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_keysyms445) 
                stream_34.add(char_literal36)
                char_literal37 = self.input.LT(1)
                self.match(self.input, 29, self.FOLLOW_29_in_keysyms447) 
                stream_29.add(char_literal37)
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
                # 105:2: -> ^( KEYSYMS ( $keysym)+ )
                # XKBGrammar.g:105:5: ^( KEYSYMS ( $keysym)+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYSYMS, "KEYSYMS"), root_1)

                # XKBGrammar.g:105:15: ( $keysym)+
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
    # XKBGrammar.g:108:1: mapOptions : ( 'default' | 'hidden' | 'partial' | 'alphanumeric_keys' | 'alternate_group' | 'xkb_symbols' );
    def mapOptions(self, ):

        retval = self.mapOptions_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set38 = None

        set38_tree = None

        try:
            try:
                # XKBGrammar.g:109:2: ( 'default' | 'hidden' | 'partial' | 'alphanumeric_keys' | 'alternate_group' | 'xkb_symbols' )
                # XKBGrammar.g:
                root_0 = self.adaptor.nil()

                set38 = self.input.LT(1)
                if (41 <= self.input.LA(1) <= 46):
                    self.input.consume();
                    self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set38))
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
    FOLLOW_28_in_section163 = frozenset([31, 32, 36, 37])
    FOLLOW_mapMaterial_in_section165 = frozenset([29, 31, 32, 36, 37])
    FOLLOW_29_in_section168 = frozenset([30])
    FOLLOW_30_in_section170 = frozenset([1])
    FOLLOW_mapOptions_in_mapType198 = frozenset([23, 41, 42, 43, 44, 45, 46])
    FOLLOW_DQSTRING_in_mapType201 = frozenset([1])
    FOLLOW_line_include_in_mapMaterial233 = frozenset([1])
    FOLLOW_line_name_in_mapMaterial239 = frozenset([30])
    FOLLOW_30_in_mapMaterial241 = frozenset([1])
    FOLLOW_line_keytype_in_mapMaterial247 = frozenset([30])
    FOLLOW_30_in_mapMaterial249 = frozenset([1])
    FOLLOW_line_key_in_mapMaterial255 = frozenset([30])
    FOLLOW_30_in_mapMaterial257 = frozenset([1])
    FOLLOW_31_in_line_include269 = frozenset([23])
    FOLLOW_DQSTRING_in_line_include271 = frozenset([1])
    FOLLOW_32_in_line_name291 = frozenset([33])
    FOLLOW_33_in_line_name293 = frozenset([24])
    FOLLOW_NAME_in_line_name297 = frozenset([34])
    FOLLOW_34_in_line_name299 = frozenset([35])
    FOLLOW_35_in_line_name301 = frozenset([23])
    FOLLOW_DQSTRING_in_line_name305 = frozenset([1])
    FOLLOW_36_in_line_keytype333 = frozenset([33])
    FOLLOW_33_in_line_keytype335 = frozenset([24])
    FOLLOW_NAME_in_line_keytype339 = frozenset([34])
    FOLLOW_34_in_line_keytype341 = frozenset([35])
    FOLLOW_35_in_line_keytype343 = frozenset([23])
    FOLLOW_DQSTRING_in_line_keytype347 = frozenset([1])
    FOLLOW_37_in_line_key376 = frozenset([38])
    FOLLOW_keycode_in_line_key378 = frozenset([28])
    FOLLOW_keysyms_in_line_key380 = frozenset([1])
    FOLLOW_38_in_keycode404 = frozenset([24])
    FOLLOW_NAME_in_keycode406 = frozenset([39])
    FOLLOW_39_in_keycode408 = frozenset([1])
    FOLLOW_28_in_keysyms428 = frozenset([33])
    FOLLOW_33_in_keysyms430 = frozenset([24])
    FOLLOW_NAME_in_keysyms434 = frozenset([34, 40])
    FOLLOW_40_in_keysyms437 = frozenset([24])
    FOLLOW_NAME_in_keysyms441 = frozenset([34, 40])
    FOLLOW_34_in_keysyms445 = frozenset([29])
    FOLLOW_29_in_keysyms447 = frozenset([1])
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
