# $ANTLR 3.1b1 XKBGrammar.g 2008-05-21 02:16:01

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__29=29
T__28=28
MAPOPTIONS=13
TOKEN_INCLUDE=4
TOKEN_MODIFIER_MAP=9
EOF=-1
TOKEN_TYPE=8
MAPTYPE=11
T__55=55
T__56=56
T__57=57
NAME=24
T__58=58
T__51=51
T__52=52
MAPMATERIAL=14
T__53=53
T__54=54
T__59=59
KEYSYMS=18
COMMENT=26
DQSTRING=23
T__50=50
T__42=42
T__43=43
STATE=20
T__40=40
T__41=41
T__46=46
T__47=47
T__44=44
SECTION=15
T__45=45
LINE_COMMENT=27
KEYCODE=16
T__48=48
T__49=49
TOKEN_NAME=6
VALUE=19
LAYOUT=10
T__30=30
T__31=31
T__32=32
WS=25
T__33=33
T__34=34
T__35=35
T__36=36
T__37=37
OVERRIDE=22
T__38=38
T__39=39
KEYSYMGROUP=21
MAPNAME=12
TOKEN_KEY=7
TOKEN_KEY_TYPE=5
KEYCODEX=17

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "TOKEN_INCLUDE", "TOKEN_KEY_TYPE", "TOKEN_NAME", "TOKEN_KEY", "TOKEN_TYPE", 
    "TOKEN_MODIFIER_MAP", "LAYOUT", "MAPTYPE", "MAPNAME", "MAPOPTIONS", 
    "MAPMATERIAL", "SECTION", "KEYCODE", "KEYCODEX", "KEYSYMS", "VALUE", 
    "STATE", "KEYSYMGROUP", "OVERRIDE", "DQSTRING", "NAME", "WS", "COMMENT", 
    "LINE_COMMENT", "'{'", "'}'", "';'", "'include'", "'name'", "'['", "']'", 
    "'='", "'key.type'", "'override'", "'key'", "'modifier_map'", "','", 
    "'<'", "'>'", "'type'", "'default'", "'hidden'", "'partial'", "'alphanumeric_keys'", 
    "'keypad_keys'", "'modifier_keys'", "'alternate_group'", "'xkb_symbols'", 
    "'Shift'", "'Control'", "'Lock'", "'Mod1'", "'Mod2'", "'Mod3'", "'Mod4'", 
    "'Mod5'"
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
    # XKBGrammar.g:55:1: layout : ( section )+ EOF -> ^( LAYOUT ( section )+ ) ;
    def layout(self, ):

        retval = self.layout_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF2 = None
        section1 = None


        EOF2_tree = None
        stream_EOF = RewriteRuleTokenStream(self.adaptor, "token EOF")
        stream_section = RewriteRuleSubtreeStream(self.adaptor, "rule section")
        try:
            try:
                # XKBGrammar.g:56:2: ( ( section )+ EOF -> ^( LAYOUT ( section )+ ) )
                # XKBGrammar.g:56:4: ( section )+ EOF
                # XKBGrammar.g:56:4: ( section )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((44 <= LA1_0 <= 51)) :
                        alt1 = 1


                    if alt1 == 1:
                        # XKBGrammar.g:56:4: section
                        self._state.following.append(self.FOLLOW_section_in_layout141)
                        section1 = self.section()

                        self._state.following.pop()
                        stream_section.add(section1.tree)



                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                EOF2 = self.input.LT(1)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_layout144) 
                stream_EOF.add(EOF2)
                # AST Rewrite
                # elements: section
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
                # 57:2: -> ^( LAYOUT ( section )+ )
                # XKBGrammar.g:57:5: ^( LAYOUT ( section )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(LAYOUT, "LAYOUT"), root_1)

                # XKBGrammar.g:57:14: ( section )+
                if not (stream_section.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_section.hasNext():
                    self.adaptor.addChild(root_1, stream_section.nextTree())


                stream_section.reset()

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

    # $ANTLR end layout

    class section_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start section
    # XKBGrammar.g:60:1: section : mapType '{' ( mapMaterial )+ '}' ';' -> ^( SECTION mapType ^( MAPMATERIAL ( mapMaterial )+ ) ) ;
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
                # XKBGrammar.g:61:2: ( mapType '{' ( mapMaterial )+ '}' ';' -> ^( SECTION mapType ^( MAPMATERIAL ( mapMaterial )+ ) ) )
                # XKBGrammar.g:61:4: mapType '{' ( mapMaterial )+ '}' ';'
                self._state.following.append(self.FOLLOW_mapType_in_section167)
                mapType3 = self.mapType()

                self._state.following.pop()
                stream_mapType.add(mapType3.tree)
                char_literal4 = self.input.LT(1)
                self.match(self.input, 28, self.FOLLOW_28_in_section169) 
                stream_28.add(char_literal4)
                # XKBGrammar.g:61:16: ( mapMaterial )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((31 <= LA2_0 <= 32) or (36 <= LA2_0 <= 39)) :
                        alt2 = 1


                    if alt2 == 1:
                        # XKBGrammar.g:61:16: mapMaterial
                        self._state.following.append(self.FOLLOW_mapMaterial_in_section171)
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
                self.match(self.input, 29, self.FOLLOW_29_in_section174) 
                stream_29.add(char_literal6)
                char_literal7 = self.input.LT(1)
                self.match(self.input, 30, self.FOLLOW_30_in_section176) 
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
                # 62:2: -> ^( SECTION mapType ^( MAPMATERIAL ( mapMaterial )+ ) )
                # XKBGrammar.g:62:5: ^( SECTION mapType ^( MAPMATERIAL ( mapMaterial )+ ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(SECTION, "SECTION"), root_1)

                self.adaptor.addChild(root_1, stream_mapType.nextTree())
                # XKBGrammar.g:62:23: ^( MAPMATERIAL ( mapMaterial )+ )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPMATERIAL, "MAPMATERIAL"), root_2)

                # XKBGrammar.g:62:37: ( mapMaterial )+
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
    # XKBGrammar.g:65:1: mapType : ( mapOptions )+ DQSTRING -> ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME DQSTRING ) ) ;
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
                # XKBGrammar.g:66:2: ( ( mapOptions )+ DQSTRING -> ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME DQSTRING ) ) )
                # XKBGrammar.g:66:4: ( mapOptions )+ DQSTRING
                # XKBGrammar.g:66:4: ( mapOptions )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((44 <= LA3_0 <= 51)) :
                        alt3 = 1


                    if alt3 == 1:
                        # XKBGrammar.g:66:4: mapOptions
                        self._state.following.append(self.FOLLOW_mapOptions_in_mapType204)
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
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_mapType207) 
                stream_DQSTRING.add(DQSTRING9)
                # AST Rewrite
                # elements: DQSTRING, mapOptions
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
                # 67:2: -> ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME DQSTRING ) )
                # XKBGrammar.g:67:5: ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME DQSTRING ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPTYPE, "MAPTYPE"), root_1)

                # XKBGrammar.g:67:15: ^( MAPOPTIONS ( mapOptions )+ )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPOPTIONS, "MAPOPTIONS"), root_2)

                # XKBGrammar.g:67:28: ( mapOptions )+
                if not (stream_mapOptions.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_mapOptions.hasNext():
                    self.adaptor.addChild(root_2, stream_mapOptions.nextTree())


                stream_mapOptions.reset()

                self.adaptor.addChild(root_1, root_2)
                # XKBGrammar.g:67:41: ^( MAPNAME DQSTRING )
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
    # XKBGrammar.g:70:1: mapMaterial : ( line_include | line_name ';' | line_keytype ';' | line_key ';' | line_modifier_map ';' );
    def mapMaterial(self, ):

        retval = self.mapMaterial_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal12 = None
        char_literal14 = None
        char_literal16 = None
        char_literal18 = None
        line_include10 = None

        line_name11 = None

        line_keytype13 = None

        line_key15 = None

        line_modifier_map17 = None


        char_literal12_tree = None
        char_literal14_tree = None
        char_literal16_tree = None
        char_literal18_tree = None

        try:
            try:
                # XKBGrammar.g:71:2: ( line_include | line_name ';' | line_keytype ';' | line_key ';' | line_modifier_map ';' )
                alt4 = 5
                LA4 = self.input.LA(1)
                if LA4 == 31:
                    alt4 = 1
                elif LA4 == 32:
                    alt4 = 2
                elif LA4 == 36:
                    alt4 = 3
                elif LA4 == 37 or LA4 == 38:
                    alt4 = 4
                elif LA4 == 39:
                    alt4 = 5
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # XKBGrammar.g:71:4: line_include
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_include_in_mapMaterial239)
                    line_include10 = self.line_include()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_include10.tree)



                elif alt4 == 2:
                    # XKBGrammar.g:72:4: line_name ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_name_in_mapMaterial245)
                    line_name11 = self.line_name()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_name11.tree)
                    char_literal12 = self.input.LT(1)
                    self.match(self.input, 30, self.FOLLOW_30_in_mapMaterial247)



                elif alt4 == 3:
                    # XKBGrammar.g:73:4: line_keytype ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_keytype_in_mapMaterial253)
                    line_keytype13 = self.line_keytype()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_keytype13.tree)
                    char_literal14 = self.input.LT(1)
                    self.match(self.input, 30, self.FOLLOW_30_in_mapMaterial255)



                elif alt4 == 4:
                    # XKBGrammar.g:74:4: line_key ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_key_in_mapMaterial261)
                    line_key15 = self.line_key()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_key15.tree)
                    char_literal16 = self.input.LT(1)
                    self.match(self.input, 30, self.FOLLOW_30_in_mapMaterial263)



                elif alt4 == 5:
                    # XKBGrammar.g:75:4: line_modifier_map ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_modifier_map_in_mapMaterial269)
                    line_modifier_map17 = self.line_modifier_map()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_modifier_map17.tree)
                    char_literal18 = self.input.LT(1)
                    self.match(self.input, 30, self.FOLLOW_30_in_mapMaterial271)



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

        string_literal19 = None
        DQSTRING20 = None

        string_literal19_tree = None
        DQSTRING20_tree = None
        stream_31 = RewriteRuleTokenStream(self.adaptor, "token 31")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")

        try:
            try:
                # XKBGrammar.g:79:2: ( 'include' DQSTRING -> ^( TOKEN_INCLUDE DQSTRING ) )
                # XKBGrammar.g:79:4: 'include' DQSTRING
                string_literal19 = self.input.LT(1)
                self.match(self.input, 31, self.FOLLOW_31_in_line_include283) 
                stream_31.add(string_literal19)
                DQSTRING20 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_include285) 
                stream_DQSTRING.add(DQSTRING20)
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
        string_literal21 = None
        char_literal22 = None
        char_literal23 = None
        char_literal24 = None

        n1_tree = None
        n2_tree = None
        string_literal21_tree = None
        char_literal22_tree = None
        char_literal23_tree = None
        char_literal24_tree = None
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
                string_literal21 = self.input.LT(1)
                self.match(self.input, 32, self.FOLLOW_32_in_line_name305) 
                stream_32.add(string_literal21)
                char_literal22 = self.input.LT(1)
                self.match(self.input, 33, self.FOLLOW_33_in_line_name307) 
                stream_33.add(char_literal22)
                n1 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_name311) 
                stream_NAME.add(n1)
                char_literal23 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_line_name313) 
                stream_34.add(char_literal23)
                char_literal24 = self.input.LT(1)
                self.match(self.input, 35, self.FOLLOW_35_in_line_name315) 
                stream_35.add(char_literal24)
                n2 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_name319) 
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
        string_literal25 = None
        char_literal26 = None
        char_literal27 = None
        char_literal28 = None

        n1_tree = None
        n2_tree = None
        string_literal25_tree = None
        char_literal26_tree = None
        char_literal27_tree = None
        char_literal28_tree = None
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
                string_literal25 = self.input.LT(1)
                self.match(self.input, 36, self.FOLLOW_36_in_line_keytype347) 
                stream_36.add(string_literal25)
                char_literal26 = self.input.LT(1)
                self.match(self.input, 33, self.FOLLOW_33_in_line_keytype349) 
                stream_33.add(char_literal26)
                n1 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype353) 
                stream_NAME.add(n1)
                char_literal27 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_line_keytype355) 
                stream_34.add(char_literal27)
                char_literal28 = self.input.LT(1)
                self.match(self.input, 35, self.FOLLOW_35_in_line_keytype357) 
                stream_35.add(char_literal28)
                n2 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_keytype361) 
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
    # XKBGrammar.g:93:1: line_key : (override= 'override' )? 'key' keycode keysyms -> ^( TOKEN_KEY ( ^( OVERRIDE $override) )? keycode keysyms ) ;
    def line_key(self, ):

        retval = self.line_key_return()
        retval.start = self.input.LT(1)

        root_0 = None

        override = None
        string_literal29 = None
        keycode30 = None

        keysyms31 = None


        override_tree = None
        string_literal29_tree = None
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")
        stream_keysyms = RewriteRuleSubtreeStream(self.adaptor, "rule keysyms")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        try:
            try:
                # XKBGrammar.g:94:2: ( (override= 'override' )? 'key' keycode keysyms -> ^( TOKEN_KEY ( ^( OVERRIDE $override) )? keycode keysyms ) )
                # XKBGrammar.g:94:4: (override= 'override' )? 'key' keycode keysyms
                # XKBGrammar.g:94:12: (override= 'override' )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 37) :
                    alt5 = 1
                if alt5 == 1:
                    # XKBGrammar.g:94:12: override= 'override'
                    override = self.input.LT(1)
                    self.match(self.input, 37, self.FOLLOW_37_in_line_key391) 
                    stream_37.add(override)




                string_literal29 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_line_key394) 
                stream_38.add(string_literal29)
                self._state.following.append(self.FOLLOW_keycode_in_line_key396)
                keycode30 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode30.tree)
                self._state.following.append(self.FOLLOW_keysyms_in_line_key398)
                keysyms31 = self.keysyms()

                self._state.following.pop()
                stream_keysyms.add(keysyms31.tree)
                # AST Rewrite
                # elements: keycode, override, keysyms
                # token labels: override
                # rule labels: retval
                # token list labels: 
                # rule list labels: 

                retval.tree = root_0
                stream_override = RewriteRuleTokenStream(self.adaptor, "token override", override)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                root_0 = self.adaptor.nil()
                # 95:2: -> ^( TOKEN_KEY ( ^( OVERRIDE $override) )? keycode keysyms )
                # XKBGrammar.g:95:5: ^( TOKEN_KEY ( ^( OVERRIDE $override) )? keycode keysyms )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_KEY, "TOKEN_KEY"), root_1)

                # XKBGrammar.g:95:17: ( ^( OVERRIDE $override) )?
                if stream_override.hasNext():
                    # XKBGrammar.g:95:17: ^( OVERRIDE $override)
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(OVERRIDE, "OVERRIDE"), root_2)

                    self.adaptor.addChild(root_2, stream_override.nextNode())

                    self.adaptor.addChild(root_1, root_2)


                stream_override.reset();
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

    class line_modifier_map_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start line_modifier_map
    # XKBGrammar.g:98:1: line_modifier_map : 'modifier_map' state '{' keycode ( ',' keycode )* '}' -> ^( TOKEN_MODIFIER_MAP state ( keycode )+ ) ;
    def line_modifier_map(self, ):

        retval = self.line_modifier_map_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal32 = None
        char_literal34 = None
        char_literal36 = None
        char_literal38 = None
        state33 = None

        keycode35 = None

        keycode37 = None


        string_literal32_tree = None
        char_literal34_tree = None
        char_literal36_tree = None
        char_literal38_tree = None
        stream_40 = RewriteRuleTokenStream(self.adaptor, "token 40")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")
        stream_28 = RewriteRuleTokenStream(self.adaptor, "token 28")
        stream_29 = RewriteRuleTokenStream(self.adaptor, "token 29")
        stream_state = RewriteRuleSubtreeStream(self.adaptor, "rule state")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        try:
            try:
                # XKBGrammar.g:99:2: ( 'modifier_map' state '{' keycode ( ',' keycode )* '}' -> ^( TOKEN_MODIFIER_MAP state ( keycode )+ ) )
                # XKBGrammar.g:99:4: 'modifier_map' state '{' keycode ( ',' keycode )* '}'
                string_literal32 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_line_modifier_map428) 
                stream_39.add(string_literal32)
                self._state.following.append(self.FOLLOW_state_in_line_modifier_map430)
                state33 = self.state()

                self._state.following.pop()
                stream_state.add(state33.tree)
                char_literal34 = self.input.LT(1)
                self.match(self.input, 28, self.FOLLOW_28_in_line_modifier_map432) 
                stream_28.add(char_literal34)
                self._state.following.append(self.FOLLOW_keycode_in_line_modifier_map434)
                keycode35 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode35.tree)
                # XKBGrammar.g:99:37: ( ',' keycode )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == 40) :
                        alt6 = 1


                    if alt6 == 1:
                        # XKBGrammar.g:99:38: ',' keycode
                        char_literal36 = self.input.LT(1)
                        self.match(self.input, 40, self.FOLLOW_40_in_line_modifier_map437) 
                        stream_40.add(char_literal36)
                        self._state.following.append(self.FOLLOW_keycode_in_line_modifier_map439)
                        keycode37 = self.keycode()

                        self._state.following.pop()
                        stream_keycode.add(keycode37.tree)



                    else:
                        break #loop6


                char_literal38 = self.input.LT(1)
                self.match(self.input, 29, self.FOLLOW_29_in_line_modifier_map443) 
                stream_29.add(char_literal38)
                # AST Rewrite
                # elements: keycode, state
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
                # 100:2: -> ^( TOKEN_MODIFIER_MAP state ( keycode )+ )
                # XKBGrammar.g:100:5: ^( TOKEN_MODIFIER_MAP state ( keycode )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_MODIFIER_MAP, "TOKEN_MODIFIER_MAP"), root_1)

                self.adaptor.addChild(root_1, stream_state.nextTree())
                # XKBGrammar.g:100:32: ( keycode )+
                if not (stream_keycode.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_keycode.hasNext():
                    self.adaptor.addChild(root_1, stream_keycode.nextTree())


                stream_keycode.reset()

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

    # $ANTLR end line_modifier_map

    class keycode_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start keycode
    # XKBGrammar.g:103:1: keycode : ( NAME -> ^( KEYCODE NAME ) | '<' NAME '>' -> ^( KEYCODEX NAME ) );
    def keycode(self, ):

        retval = self.keycode_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME39 = None
        char_literal40 = None
        NAME41 = None
        char_literal42 = None

        NAME39_tree = None
        char_literal40_tree = None
        NAME41_tree = None
        char_literal42_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_42 = RewriteRuleTokenStream(self.adaptor, "token 42")
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")

        try:
            try:
                # XKBGrammar.g:104:2: ( NAME -> ^( KEYCODE NAME ) | '<' NAME '>' -> ^( KEYCODEX NAME ) )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == NAME) :
                    alt7 = 1
                elif (LA7_0 == 41) :
                    alt7 = 2
                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # XKBGrammar.g:104:4: NAME
                    NAME39 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode467) 
                    stream_NAME.add(NAME39)
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
                    # 104:9: -> ^( KEYCODE NAME )
                    # XKBGrammar.g:104:12: ^( KEYCODE NAME )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYCODE, "KEYCODE"), root_1)

                    self.adaptor.addChild(root_1, stream_NAME.nextNode())

                    self.adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                elif alt7 == 2:
                    # XKBGrammar.g:105:4: '<' NAME '>'
                    char_literal40 = self.input.LT(1)
                    self.match(self.input, 41, self.FOLLOW_41_in_keycode480) 
                    stream_41.add(char_literal40)
                    NAME41 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode482) 
                    stream_NAME.add(NAME41)
                    char_literal42 = self.input.LT(1)
                    self.match(self.input, 42, self.FOLLOW_42_in_keycode484) 
                    stream_42.add(char_literal42)
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
                    # 105:17: -> ^( KEYCODEX NAME )
                    # XKBGrammar.g:105:20: ^( KEYCODEX NAME )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYCODEX, "KEYCODEX"), root_1)

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
    # XKBGrammar.g:108:1: keysyms : '{' ( 'type' '[' tn1= NAME ']' '=' tn2= DQSTRING ',' )? keysymgroup ( ',' keysymgroup )* '}' -> ^( KEYSYMS ( ^( TOKEN_TYPE $tn1 $tn2) )? ( keysymgroup )+ ) ;
    def keysyms(self, ):

        retval = self.keysyms_return()
        retval.start = self.input.LT(1)

        root_0 = None

        tn1 = None
        tn2 = None
        char_literal43 = None
        string_literal44 = None
        char_literal45 = None
        char_literal46 = None
        char_literal47 = None
        char_literal48 = None
        char_literal50 = None
        char_literal52 = None
        keysymgroup49 = None

        keysymgroup51 = None


        tn1_tree = None
        tn2_tree = None
        char_literal43_tree = None
        string_literal44_tree = None
        char_literal45_tree = None
        char_literal46_tree = None
        char_literal47_tree = None
        char_literal48_tree = None
        char_literal50_tree = None
        char_literal52_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_40 = RewriteRuleTokenStream(self.adaptor, "token 40")
        stream_35 = RewriteRuleTokenStream(self.adaptor, "token 35")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")
        stream_33 = RewriteRuleTokenStream(self.adaptor, "token 33")
        stream_34 = RewriteRuleTokenStream(self.adaptor, "token 34")
        stream_28 = RewriteRuleTokenStream(self.adaptor, "token 28")
        stream_29 = RewriteRuleTokenStream(self.adaptor, "token 29")
        stream_keysymgroup = RewriteRuleSubtreeStream(self.adaptor, "rule keysymgroup")
        try:
            try:
                # XKBGrammar.g:109:2: ( '{' ( 'type' '[' tn1= NAME ']' '=' tn2= DQSTRING ',' )? keysymgroup ( ',' keysymgroup )* '}' -> ^( KEYSYMS ( ^( TOKEN_TYPE $tn1 $tn2) )? ( keysymgroup )+ ) )
                # XKBGrammar.g:109:4: '{' ( 'type' '[' tn1= NAME ']' '=' tn2= DQSTRING ',' )? keysymgroup ( ',' keysymgroup )* '}'
                char_literal43 = self.input.LT(1)
                self.match(self.input, 28, self.FOLLOW_28_in_keysyms503) 
                stream_28.add(char_literal43)
                # XKBGrammar.g:109:8: ( 'type' '[' tn1= NAME ']' '=' tn2= DQSTRING ',' )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == 43) :
                    alt8 = 1
                if alt8 == 1:
                    # XKBGrammar.g:109:9: 'type' '[' tn1= NAME ']' '=' tn2= DQSTRING ','
                    string_literal44 = self.input.LT(1)
                    self.match(self.input, 43, self.FOLLOW_43_in_keysyms506) 
                    stream_43.add(string_literal44)
                    char_literal45 = self.input.LT(1)
                    self.match(self.input, 33, self.FOLLOW_33_in_keysyms508) 
                    stream_33.add(char_literal45)
                    tn1 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keysyms512) 
                    stream_NAME.add(tn1)
                    char_literal46 = self.input.LT(1)
                    self.match(self.input, 34, self.FOLLOW_34_in_keysyms514) 
                    stream_34.add(char_literal46)
                    char_literal47 = self.input.LT(1)
                    self.match(self.input, 35, self.FOLLOW_35_in_keysyms516) 
                    stream_35.add(char_literal47)
                    tn2 = self.input.LT(1)
                    self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_keysyms520) 
                    stream_DQSTRING.add(tn2)
                    char_literal48 = self.input.LT(1)
                    self.match(self.input, 40, self.FOLLOW_40_in_keysyms522) 
                    stream_40.add(char_literal48)




                self._state.following.append(self.FOLLOW_keysymgroup_in_keysyms526)
                keysymgroup49 = self.keysymgroup()

                self._state.following.pop()
                stream_keysymgroup.add(keysymgroup49.tree)
                # XKBGrammar.g:109:68: ( ',' keysymgroup )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 40) :
                        alt9 = 1


                    if alt9 == 1:
                        # XKBGrammar.g:109:69: ',' keysymgroup
                        char_literal50 = self.input.LT(1)
                        self.match(self.input, 40, self.FOLLOW_40_in_keysyms529) 
                        stream_40.add(char_literal50)
                        self._state.following.append(self.FOLLOW_keysymgroup_in_keysyms531)
                        keysymgroup51 = self.keysymgroup()

                        self._state.following.pop()
                        stream_keysymgroup.add(keysymgroup51.tree)



                    else:
                        break #loop9


                char_literal52 = self.input.LT(1)
                self.match(self.input, 29, self.FOLLOW_29_in_keysyms535) 
                stream_29.add(char_literal52)
                # AST Rewrite
                # elements: keysymgroup, tn1, tn2
                # token labels: tn1, tn2
                # rule labels: retval
                # token list labels: 
                # rule list labels: 

                retval.tree = root_0
                stream_tn1 = RewriteRuleTokenStream(self.adaptor, "token tn1", tn1)
                stream_tn2 = RewriteRuleTokenStream(self.adaptor, "token tn2", tn2)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                root_0 = self.adaptor.nil()
                # 110:2: -> ^( KEYSYMS ( ^( TOKEN_TYPE $tn1 $tn2) )? ( keysymgroup )+ )
                # XKBGrammar.g:110:5: ^( KEYSYMS ( ^( TOKEN_TYPE $tn1 $tn2) )? ( keysymgroup )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYSYMS, "KEYSYMS"), root_1)

                # XKBGrammar.g:110:15: ( ^( TOKEN_TYPE $tn1 $tn2) )?
                if stream_tn1.hasNext() or stream_tn2.hasNext():
                    # XKBGrammar.g:110:15: ^( TOKEN_TYPE $tn1 $tn2)
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_TYPE, "TOKEN_TYPE"), root_2)

                    self.adaptor.addChild(root_2, stream_tn1.nextNode())
                    self.adaptor.addChild(root_2, stream_tn2.nextNode())

                    self.adaptor.addChild(root_1, root_2)


                stream_tn1.reset();
                stream_tn2.reset();
                # XKBGrammar.g:110:40: ( keysymgroup )+
                if not (stream_keysymgroup.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_keysymgroup.hasNext():
                    self.adaptor.addChild(root_1, stream_keysymgroup.nextTree())


                stream_keysymgroup.reset()

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

    class keysymgroup_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start keysymgroup
    # XKBGrammar.g:113:1: keysymgroup : '[' keysym+= NAME ( ',' keysym+= NAME )* ']' -> ^( KEYSYMGROUP ( $keysym)+ ) ;
    def keysymgroup(self, ):

        retval = self.keysymgroup_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal53 = None
        char_literal54 = None
        char_literal55 = None
        keysym = None
        list_keysym = None

        char_literal53_tree = None
        char_literal54_tree = None
        char_literal55_tree = None
        keysym_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_40 = RewriteRuleTokenStream(self.adaptor, "token 40")
        stream_33 = RewriteRuleTokenStream(self.adaptor, "token 33")
        stream_34 = RewriteRuleTokenStream(self.adaptor, "token 34")

        try:
            try:
                # XKBGrammar.g:114:2: ( '[' keysym+= NAME ( ',' keysym+= NAME )* ']' -> ^( KEYSYMGROUP ( $keysym)+ ) )
                # XKBGrammar.g:114:4: '[' keysym+= NAME ( ',' keysym+= NAME )* ']'
                char_literal53 = self.input.LT(1)
                self.match(self.input, 33, self.FOLLOW_33_in_keysymgroup567) 
                stream_33.add(char_literal53)
                keysym = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_keysymgroup571) 
                stream_NAME.add(keysym)
                if list_keysym is None:
                    list_keysym = []
                list_keysym.append(keysym)

                # XKBGrammar.g:114:21: ( ',' keysym+= NAME )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == 40) :
                        alt10 = 1


                    if alt10 == 1:
                        # XKBGrammar.g:114:22: ',' keysym+= NAME
                        char_literal54 = self.input.LT(1)
                        self.match(self.input, 40, self.FOLLOW_40_in_keysymgroup574) 
                        stream_40.add(char_literal54)
                        keysym = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_keysymgroup578) 
                        stream_NAME.add(keysym)
                        if list_keysym is None:
                            list_keysym = []
                        list_keysym.append(keysym)




                    else:
                        break #loop10


                char_literal55 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_keysymgroup582) 
                stream_34.add(char_literal55)
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
                # 115:2: -> ^( KEYSYMGROUP ( $keysym)+ )
                # XKBGrammar.g:115:5: ^( KEYSYMGROUP ( $keysym)+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYSYMGROUP, "KEYSYMGROUP"), root_1)

                # XKBGrammar.g:115:19: ( $keysym)+
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

    # $ANTLR end keysymgroup

    class mapOptions_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start mapOptions
    # XKBGrammar.g:118:1: mapOptions : ( 'default' | 'hidden' | 'partial' | 'alphanumeric_keys' | 'keypad_keys' | 'modifier_keys' | 'alternate_group' | 'xkb_symbols' );
    def mapOptions(self, ):

        retval = self.mapOptions_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set56 = None

        set56_tree = None

        try:
            try:
                # XKBGrammar.g:119:2: ( 'default' | 'hidden' | 'partial' | 'alphanumeric_keys' | 'keypad_keys' | 'modifier_keys' | 'alternate_group' | 'xkb_symbols' )
                # XKBGrammar.g:
                root_0 = self.adaptor.nil()

                set56 = self.input.LT(1)
                if (44 <= self.input.LA(1) <= 51):
                    self.input.consume();
                    self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set56))
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

    class state_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start state
    # XKBGrammar.g:129:1: state : ( 'Shift' | 'Control' | 'Lock' | 'Mod1' | 'Mod2' | 'Mod3' | 'Mod4' | 'Mod5' );
    def state(self, ):

        retval = self.state_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set57 = None

        set57_tree = None

        try:
            try:
                # XKBGrammar.g:130:2: ( 'Shift' | 'Control' | 'Lock' | 'Mod1' | 'Mod2' | 'Mod3' | 'Mod4' | 'Mod5' )
                # XKBGrammar.g:
                root_0 = self.adaptor.nil()

                set57 = self.input.LT(1)
                if (52 <= self.input.LA(1) <= 59):
                    self.input.consume();
                    self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set57))
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

    # $ANTLR end state


    # Delegated rules


 

    FOLLOW_section_in_layout141 = frozenset([44, 45, 46, 47, 48, 49, 50, 51])
    FOLLOW_EOF_in_layout144 = frozenset([1])
    FOLLOW_mapType_in_section167 = frozenset([28])
    FOLLOW_28_in_section169 = frozenset([31, 32, 36, 37, 38, 39])
    FOLLOW_mapMaterial_in_section171 = frozenset([29, 31, 32, 36, 37, 38, 39])
    FOLLOW_29_in_section174 = frozenset([30])
    FOLLOW_30_in_section176 = frozenset([1])
    FOLLOW_mapOptions_in_mapType204 = frozenset([23, 44, 45, 46, 47, 48, 49, 50, 51])
    FOLLOW_DQSTRING_in_mapType207 = frozenset([1])
    FOLLOW_line_include_in_mapMaterial239 = frozenset([1])
    FOLLOW_line_name_in_mapMaterial245 = frozenset([30])
    FOLLOW_30_in_mapMaterial247 = frozenset([1])
    FOLLOW_line_keytype_in_mapMaterial253 = frozenset([30])
    FOLLOW_30_in_mapMaterial255 = frozenset([1])
    FOLLOW_line_key_in_mapMaterial261 = frozenset([30])
    FOLLOW_30_in_mapMaterial263 = frozenset([1])
    FOLLOW_line_modifier_map_in_mapMaterial269 = frozenset([30])
    FOLLOW_30_in_mapMaterial271 = frozenset([1])
    FOLLOW_31_in_line_include283 = frozenset([23])
    FOLLOW_DQSTRING_in_line_include285 = frozenset([1])
    FOLLOW_32_in_line_name305 = frozenset([33])
    FOLLOW_33_in_line_name307 = frozenset([24])
    FOLLOW_NAME_in_line_name311 = frozenset([34])
    FOLLOW_34_in_line_name313 = frozenset([35])
    FOLLOW_35_in_line_name315 = frozenset([23])
    FOLLOW_DQSTRING_in_line_name319 = frozenset([1])
    FOLLOW_36_in_line_keytype347 = frozenset([33])
    FOLLOW_33_in_line_keytype349 = frozenset([24])
    FOLLOW_NAME_in_line_keytype353 = frozenset([34])
    FOLLOW_34_in_line_keytype355 = frozenset([35])
    FOLLOW_35_in_line_keytype357 = frozenset([23])
    FOLLOW_DQSTRING_in_line_keytype361 = frozenset([1])
    FOLLOW_37_in_line_key391 = frozenset([38])
    FOLLOW_38_in_line_key394 = frozenset([24, 41])
    FOLLOW_keycode_in_line_key396 = frozenset([28])
    FOLLOW_keysyms_in_line_key398 = frozenset([1])
    FOLLOW_39_in_line_modifier_map428 = frozenset([52, 53, 54, 55, 56, 57, 58, 59])
    FOLLOW_state_in_line_modifier_map430 = frozenset([28])
    FOLLOW_28_in_line_modifier_map432 = frozenset([24, 41])
    FOLLOW_keycode_in_line_modifier_map434 = frozenset([29, 40])
    FOLLOW_40_in_line_modifier_map437 = frozenset([24, 41])
    FOLLOW_keycode_in_line_modifier_map439 = frozenset([29, 40])
    FOLLOW_29_in_line_modifier_map443 = frozenset([1])
    FOLLOW_NAME_in_keycode467 = frozenset([1])
    FOLLOW_41_in_keycode480 = frozenset([24])
    FOLLOW_NAME_in_keycode482 = frozenset([42])
    FOLLOW_42_in_keycode484 = frozenset([1])
    FOLLOW_28_in_keysyms503 = frozenset([33, 43])
    FOLLOW_43_in_keysyms506 = frozenset([33])
    FOLLOW_33_in_keysyms508 = frozenset([24])
    FOLLOW_NAME_in_keysyms512 = frozenset([34])
    FOLLOW_34_in_keysyms514 = frozenset([35])
    FOLLOW_35_in_keysyms516 = frozenset([23])
    FOLLOW_DQSTRING_in_keysyms520 = frozenset([40])
    FOLLOW_40_in_keysyms522 = frozenset([33, 43])
    FOLLOW_keysymgroup_in_keysyms526 = frozenset([29, 40])
    FOLLOW_40_in_keysyms529 = frozenset([33, 43])
    FOLLOW_keysymgroup_in_keysyms531 = frozenset([29, 40])
    FOLLOW_29_in_keysyms535 = frozenset([1])
    FOLLOW_33_in_keysymgroup567 = frozenset([24])
    FOLLOW_NAME_in_keysymgroup571 = frozenset([34, 40])
    FOLLOW_40_in_keysymgroup574 = frozenset([24])
    FOLLOW_NAME_in_keysymgroup578 = frozenset([34, 40])
    FOLLOW_34_in_keysymgroup582 = frozenset([1])
    FOLLOW_set_in_mapOptions0 = frozenset([1])
    FOLLOW_set_in_state0 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("XKBGrammarLexer", XKBGrammarParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)

if __name__ == '__main__':
    main(sys.argv)
