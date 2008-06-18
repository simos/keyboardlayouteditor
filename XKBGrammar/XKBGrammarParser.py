# $ANTLR 3.1b1 XKBGrammar.g 2008-06-18 19:48:03

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
MAPOPTIONS=16
OVERLAY=29
TOKEN_INCLUDE=4
ELEM_VIRTUALMODS=24
ELEM_KEYSYMS=23
TOKEN_MODIFIER_MAP=9
EOF=-1
TOKEN_TYPE=8
MAPTYPE=14
TOKEN_VIRTUAL_MODIFIERS=11
T__55=55
T__56=56
T__57=57
NAME=32
T__58=58
T__51=51
T__52=52
T__53=53
MAPMATERIAL=17
T__54=54
MAPOPTS=30
COMMENT=34
DQSTRING=31
T__50=50
T__42=42
T__43=43
STATE=21
T__40=40
T__41=41
T__46=46
T__47=47
ACTIONS_SETMODS=26
T__44=44
T__45=45
LINE_COMMENT=35
KEYCODE=18
T__48=48
T__49=49
ELEM_ACTIONS=25
TOKEN_NAME=6
VALUE=20
LAYOUT=12
WS=33
T__36=36
T__37=37
OVERRIDE=28
T__38=38
T__39=39
ELEM_KEYSYMGROUP=22
TOKEN_SYMBOL=10
TOKEN_KEY=7
MAPNAME=15
SYMBOLS=13
KEYELEMENTS=27
TOKEN_KEY_TYPE=5
KEYCODEX=19

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "TOKEN_INCLUDE", "TOKEN_KEY_TYPE", "TOKEN_NAME", "TOKEN_KEY", "TOKEN_TYPE", 
    "TOKEN_MODIFIER_MAP", "TOKEN_SYMBOL", "TOKEN_VIRTUAL_MODIFIERS", "LAYOUT", 
    "SYMBOLS", "MAPTYPE", "MAPNAME", "MAPOPTIONS", "MAPMATERIAL", "KEYCODE", 
    "KEYCODEX", "VALUE", "STATE", "ELEM_KEYSYMGROUP", "ELEM_KEYSYMS", "ELEM_VIRTUALMODS", 
    "ELEM_ACTIONS", "ACTIONS_SETMODS", "KEYELEMENTS", "OVERRIDE", "OVERLAY", 
    "MAPOPTS", "DQSTRING", "NAME", "WS", "COMMENT", "LINE_COMMENT", "'{'", 
    "'}'", "';'", "'include'", "'name'", "'['", "']'", "'='", "'key.type'", 
    "'key'", "','", "'modifier_map'", "'virtual_modifiers'", "'<'", "'>'", 
    "'type'", "'symbols'", "'virtualMods'", "'actions'", "'SetMods'", "'('", 
    "'modifiers'", "')'"
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
    # XKBGrammar.g:62:1: layout : ( symbols )+ EOF -> ^( LAYOUT ( symbols )+ ) ;
    def layout(self, ):

        retval = self.layout_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF2 = None
        symbols1 = None


        EOF2_tree = None
        stream_EOF = RewriteRuleTokenStream(self.adaptor, "token EOF")
        stream_symbols = RewriteRuleSubtreeStream(self.adaptor, "rule symbols")
        try:
            try:
                # XKBGrammar.g:63:2: ( ( symbols )+ EOF -> ^( LAYOUT ( symbols )+ ) )
                # XKBGrammar.g:63:4: ( symbols )+ EOF
                # XKBGrammar.g:63:4: ( symbols )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == MAPOPTS) :
                        alt1 = 1


                    if alt1 == 1:
                        # XKBGrammar.g:63:4: symbols
                        self._state.following.append(self.FOLLOW_symbols_in_layout169)
                        symbols1 = self.symbols()

                        self._state.following.pop()
                        stream_symbols.add(symbols1.tree)



                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1


                EOF2 = self.input.LT(1)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_layout172) 
                stream_EOF.add(EOF2)
                # AST Rewrite
                # elements: symbols
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
                # 64:2: -> ^( LAYOUT ( symbols )+ )
                # XKBGrammar.g:64:5: ^( LAYOUT ( symbols )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(LAYOUT, "LAYOUT"), root_1)

                # XKBGrammar.g:64:14: ( symbols )+
                if not (stream_symbols.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_symbols.hasNext():
                    self.adaptor.addChild(root_1, stream_symbols.nextTree())


                stream_symbols.reset()

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

    class symbols_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start symbols
    # XKBGrammar.g:67:1: symbols : mapType '{' ( mapMaterial )+ '}' ';' -> ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) ) ;
    def symbols(self, ):

        retval = self.symbols_return()
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
        stream_36 = RewriteRuleTokenStream(self.adaptor, "token 36")
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")
        stream_mapMaterial = RewriteRuleSubtreeStream(self.adaptor, "rule mapMaterial")
        stream_mapType = RewriteRuleSubtreeStream(self.adaptor, "rule mapType")
        try:
            try:
                # XKBGrammar.g:68:2: ( mapType '{' ( mapMaterial )+ '}' ';' -> ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) ) )
                # XKBGrammar.g:68:4: mapType '{' ( mapMaterial )+ '}' ';'
                self._state.following.append(self.FOLLOW_mapType_in_symbols195)
                mapType3 = self.mapType()

                self._state.following.pop()
                stream_mapType.add(mapType3.tree)
                char_literal4 = self.input.LT(1)
                self.match(self.input, 36, self.FOLLOW_36_in_symbols197) 
                stream_36.add(char_literal4)
                # XKBGrammar.g:68:16: ( mapMaterial )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == OVERRIDE or (39 <= LA2_0 <= 40) or (44 <= LA2_0 <= 45) or (47 <= LA2_0 <= 48)) :
                        alt2 = 1


                    if alt2 == 1:
                        # XKBGrammar.g:68:16: mapMaterial
                        self._state.following.append(self.FOLLOW_mapMaterial_in_symbols199)
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
                self.match(self.input, 37, self.FOLLOW_37_in_symbols202) 
                stream_37.add(char_literal6)
                char_literal7 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_symbols204) 
                stream_38.add(char_literal7)
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
                # 69:2: -> ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) )
                # XKBGrammar.g:69:5: ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(SYMBOLS, "SYMBOLS"), root_1)

                self.adaptor.addChild(root_1, stream_mapType.nextTree())
                # XKBGrammar.g:69:23: ^( MAPMATERIAL ( mapMaterial )+ )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPMATERIAL, "MAPMATERIAL"), root_2)

                # XKBGrammar.g:69:37: ( mapMaterial )+
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

    # $ANTLR end symbols

    class mapType_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start mapType
    # XKBGrammar.g:72:1: mapType : ( MAPOPTS )+ DQSTRING -> ^( MAPTYPE ^( MAPOPTIONS ( MAPOPTS )+ ) ^( MAPNAME DQSTRING ) ) ;
    def mapType(self, ):

        retval = self.mapType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MAPOPTS8 = None
        DQSTRING9 = None

        MAPOPTS8_tree = None
        DQSTRING9_tree = None
        stream_MAPOPTS = RewriteRuleTokenStream(self.adaptor, "token MAPOPTS")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")

        try:
            try:
                # XKBGrammar.g:73:2: ( ( MAPOPTS )+ DQSTRING -> ^( MAPTYPE ^( MAPOPTIONS ( MAPOPTS )+ ) ^( MAPNAME DQSTRING ) ) )
                # XKBGrammar.g:73:4: ( MAPOPTS )+ DQSTRING
                # XKBGrammar.g:73:4: ( MAPOPTS )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == MAPOPTS) :
                        alt3 = 1


                    if alt3 == 1:
                        # XKBGrammar.g:73:4: MAPOPTS
                        MAPOPTS8 = self.input.LT(1)
                        self.match(self.input, MAPOPTS, self.FOLLOW_MAPOPTS_in_mapType232) 
                        stream_MAPOPTS.add(MAPOPTS8)



                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


                DQSTRING9 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_mapType235) 
                stream_DQSTRING.add(DQSTRING9)
                # AST Rewrite
                # elements: DQSTRING, MAPOPTS
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
                # 74:2: -> ^( MAPTYPE ^( MAPOPTIONS ( MAPOPTS )+ ) ^( MAPNAME DQSTRING ) )
                # XKBGrammar.g:74:5: ^( MAPTYPE ^( MAPOPTIONS ( MAPOPTS )+ ) ^( MAPNAME DQSTRING ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPTYPE, "MAPTYPE"), root_1)

                # XKBGrammar.g:74:15: ^( MAPOPTIONS ( MAPOPTS )+ )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPOPTIONS, "MAPOPTIONS"), root_2)

                # XKBGrammar.g:74:28: ( MAPOPTS )+
                if not (stream_MAPOPTS.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_MAPOPTS.hasNext():
                    self.adaptor.addChild(root_2, stream_MAPOPTS.nextNode())


                stream_MAPOPTS.reset()

                self.adaptor.addChild(root_1, root_2)
                # XKBGrammar.g:74:38: ^( MAPNAME DQSTRING )
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
    # XKBGrammar.g:77:1: mapMaterial : ( line_include | line_name ';' | line_keytype ';' | line_key ';' | line_modifier_map ';' | line_virtual_modifiers ';' );
    def mapMaterial(self, ):

        retval = self.mapMaterial_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal12 = None
        char_literal14 = None
        char_literal16 = None
        char_literal18 = None
        char_literal20 = None
        line_include10 = None

        line_name11 = None

        line_keytype13 = None

        line_key15 = None

        line_modifier_map17 = None

        line_virtual_modifiers19 = None


        char_literal12_tree = None
        char_literal14_tree = None
        char_literal16_tree = None
        char_literal18_tree = None
        char_literal20_tree = None

        try:
            try:
                # XKBGrammar.g:78:2: ( line_include | line_name ';' | line_keytype ';' | line_key ';' | line_modifier_map ';' | line_virtual_modifiers ';' )
                alt4 = 6
                LA4 = self.input.LA(1)
                if LA4 == 39:
                    alt4 = 1
                elif LA4 == 40:
                    alt4 = 2
                elif LA4 == 44:
                    alt4 = 3
                elif LA4 == OVERRIDE or LA4 == 45:
                    alt4 = 4
                elif LA4 == 47:
                    alt4 = 5
                elif LA4 == 48:
                    alt4 = 6
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # XKBGrammar.g:78:4: line_include
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_include_in_mapMaterial267)
                    line_include10 = self.line_include()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_include10.tree)



                elif alt4 == 2:
                    # XKBGrammar.g:79:4: line_name ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_name_in_mapMaterial273)
                    line_name11 = self.line_name()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_name11.tree)
                    char_literal12 = self.input.LT(1)
                    self.match(self.input, 38, self.FOLLOW_38_in_mapMaterial275)



                elif alt4 == 3:
                    # XKBGrammar.g:80:4: line_keytype ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_keytype_in_mapMaterial281)
                    line_keytype13 = self.line_keytype()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_keytype13.tree)
                    char_literal14 = self.input.LT(1)
                    self.match(self.input, 38, self.FOLLOW_38_in_mapMaterial283)



                elif alt4 == 4:
                    # XKBGrammar.g:81:4: line_key ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_key_in_mapMaterial289)
                    line_key15 = self.line_key()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_key15.tree)
                    char_literal16 = self.input.LT(1)
                    self.match(self.input, 38, self.FOLLOW_38_in_mapMaterial291)



                elif alt4 == 5:
                    # XKBGrammar.g:82:4: line_modifier_map ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_modifier_map_in_mapMaterial297)
                    line_modifier_map17 = self.line_modifier_map()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_modifier_map17.tree)
                    char_literal18 = self.input.LT(1)
                    self.match(self.input, 38, self.FOLLOW_38_in_mapMaterial299)



                elif alt4 == 6:
                    # XKBGrammar.g:83:4: line_virtual_modifiers ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_virtual_modifiers_in_mapMaterial305)
                    line_virtual_modifiers19 = self.line_virtual_modifiers()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_virtual_modifiers19.tree)
                    char_literal20 = self.input.LT(1)
                    self.match(self.input, 38, self.FOLLOW_38_in_mapMaterial307)



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
    # XKBGrammar.g:86:1: line_include : 'include' DQSTRING -> ^( TOKEN_INCLUDE DQSTRING ) ;
    def line_include(self, ):

        retval = self.line_include_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal21 = None
        DQSTRING22 = None

        string_literal21_tree = None
        DQSTRING22_tree = None
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")

        try:
            try:
                # XKBGrammar.g:87:2: ( 'include' DQSTRING -> ^( TOKEN_INCLUDE DQSTRING ) )
                # XKBGrammar.g:87:4: 'include' DQSTRING
                string_literal21 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_line_include319) 
                stream_39.add(string_literal21)
                DQSTRING22 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_include321) 
                stream_DQSTRING.add(DQSTRING22)
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
                # 88:2: -> ^( TOKEN_INCLUDE DQSTRING )
                # XKBGrammar.g:88:5: ^( TOKEN_INCLUDE DQSTRING )
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
    # XKBGrammar.g:91:1: line_name : 'name' '[' NAME ']' '=' DQSTRING -> ^( TOKEN_NAME NAME ^( VALUE DQSTRING ) ) ;
    def line_name(self, ):

        retval = self.line_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal23 = None
        char_literal24 = None
        NAME25 = None
        char_literal26 = None
        char_literal27 = None
        DQSTRING28 = None

        string_literal23_tree = None
        char_literal24_tree = None
        NAME25_tree = None
        char_literal26_tree = None
        char_literal27_tree = None
        DQSTRING28_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_42 = RewriteRuleTokenStream(self.adaptor, "token 42")
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_40 = RewriteRuleTokenStream(self.adaptor, "token 40")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")

        try:
            try:
                # XKBGrammar.g:92:2: ( 'name' '[' NAME ']' '=' DQSTRING -> ^( TOKEN_NAME NAME ^( VALUE DQSTRING ) ) )
                # XKBGrammar.g:92:4: 'name' '[' NAME ']' '=' DQSTRING
                string_literal23 = self.input.LT(1)
                self.match(self.input, 40, self.FOLLOW_40_in_line_name341) 
                stream_40.add(string_literal23)
                char_literal24 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_line_name343) 
                stream_41.add(char_literal24)
                NAME25 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_name345) 
                stream_NAME.add(NAME25)
                char_literal26 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_line_name347) 
                stream_42.add(char_literal26)
                char_literal27 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_line_name349) 
                stream_43.add(char_literal27)
                DQSTRING28 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_name351) 
                stream_DQSTRING.add(DQSTRING28)
                # AST Rewrite
                # elements: DQSTRING, NAME
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
                # 93:2: -> ^( TOKEN_NAME NAME ^( VALUE DQSTRING ) )
                # XKBGrammar.g:93:5: ^( TOKEN_NAME NAME ^( VALUE DQSTRING ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_NAME, "TOKEN_NAME"), root_1)

                self.adaptor.addChild(root_1, stream_NAME.nextNode())
                # XKBGrammar.g:93:23: ^( VALUE DQSTRING )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(VALUE, "VALUE"), root_2)

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

    # $ANTLR end line_name

    class line_keytype_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start line_keytype
    # XKBGrammar.g:96:1: line_keytype : 'key.type' ( '[' NAME ']' )? '=' DQSTRING -> ^( TOKEN_KEY_TYPE ( NAME )? ^( VALUE DQSTRING ) ) ;
    def line_keytype(self, ):

        retval = self.line_keytype_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal29 = None
        char_literal30 = None
        NAME31 = None
        char_literal32 = None
        char_literal33 = None
        DQSTRING34 = None

        string_literal29_tree = None
        char_literal30_tree = None
        NAME31_tree = None
        char_literal32_tree = None
        char_literal33_tree = None
        DQSTRING34_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_42 = RewriteRuleTokenStream(self.adaptor, "token 42")
        stream_44 = RewriteRuleTokenStream(self.adaptor, "token 44")
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")

        try:
            try:
                # XKBGrammar.g:97:2: ( 'key.type' ( '[' NAME ']' )? '=' DQSTRING -> ^( TOKEN_KEY_TYPE ( NAME )? ^( VALUE DQSTRING ) ) )
                # XKBGrammar.g:97:4: 'key.type' ( '[' NAME ']' )? '=' DQSTRING
                string_literal29 = self.input.LT(1)
                self.match(self.input, 44, self.FOLLOW_44_in_line_keytype377) 
                stream_44.add(string_literal29)
                # XKBGrammar.g:97:15: ( '[' NAME ']' )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 41) :
                    alt5 = 1
                if alt5 == 1:
                    # XKBGrammar.g:97:16: '[' NAME ']'
                    char_literal30 = self.input.LT(1)
                    self.match(self.input, 41, self.FOLLOW_41_in_line_keytype380) 
                    stream_41.add(char_literal30)
                    NAME31 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype382) 
                    stream_NAME.add(NAME31)
                    char_literal32 = self.input.LT(1)
                    self.match(self.input, 42, self.FOLLOW_42_in_line_keytype384) 
                    stream_42.add(char_literal32)




                char_literal33 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_line_keytype388) 
                stream_43.add(char_literal33)
                DQSTRING34 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_keytype390) 
                stream_DQSTRING.add(DQSTRING34)
                # AST Rewrite
                # elements: NAME, DQSTRING
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
                # 98:2: -> ^( TOKEN_KEY_TYPE ( NAME )? ^( VALUE DQSTRING ) )
                # XKBGrammar.g:98:5: ^( TOKEN_KEY_TYPE ( NAME )? ^( VALUE DQSTRING ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_KEY_TYPE, "TOKEN_KEY_TYPE"), root_1)

                # XKBGrammar.g:98:22: ( NAME )?
                if stream_NAME.hasNext():
                    self.adaptor.addChild(root_1, stream_NAME.nextNode())


                stream_NAME.reset();
                # XKBGrammar.g:98:28: ^( VALUE DQSTRING )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(VALUE, "VALUE"), root_2)

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

    # $ANTLR end line_keytype

    class line_key_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start line_key
    # XKBGrammar.g:101:1: line_key : ( OVERRIDE )? 'key' keycode '{' keyelements ( ',' keyelements )* '}' -> ^( TOKEN_KEY ( OVERRIDE )? keycode ( keyelements )+ ) ;
    def line_key(self, ):

        retval = self.line_key_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OVERRIDE35 = None
        string_literal36 = None
        char_literal38 = None
        char_literal40 = None
        char_literal42 = None
        keycode37 = None

        keyelements39 = None

        keyelements41 = None


        OVERRIDE35_tree = None
        string_literal36_tree = None
        char_literal38_tree = None
        char_literal40_tree = None
        char_literal42_tree = None
        stream_45 = RewriteRuleTokenStream(self.adaptor, "token 45")
        stream_46 = RewriteRuleTokenStream(self.adaptor, "token 46")
        stream_36 = RewriteRuleTokenStream(self.adaptor, "token 36")
        stream_OVERRIDE = RewriteRuleTokenStream(self.adaptor, "token OVERRIDE")
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        stream_keyelements = RewriteRuleSubtreeStream(self.adaptor, "rule keyelements")
        try:
            try:
                # XKBGrammar.g:102:2: ( ( OVERRIDE )? 'key' keycode '{' keyelements ( ',' keyelements )* '}' -> ^( TOKEN_KEY ( OVERRIDE )? keycode ( keyelements )+ ) )
                # XKBGrammar.g:102:4: ( OVERRIDE )? 'key' keycode '{' keyelements ( ',' keyelements )* '}'
                # XKBGrammar.g:102:4: ( OVERRIDE )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == OVERRIDE) :
                    alt6 = 1
                if alt6 == 1:
                    # XKBGrammar.g:102:4: OVERRIDE
                    OVERRIDE35 = self.input.LT(1)
                    self.match(self.input, OVERRIDE, self.FOLLOW_OVERRIDE_in_line_key417) 
                    stream_OVERRIDE.add(OVERRIDE35)




                string_literal36 = self.input.LT(1)
                self.match(self.input, 45, self.FOLLOW_45_in_line_key420) 
                stream_45.add(string_literal36)
                self._state.following.append(self.FOLLOW_keycode_in_line_key422)
                keycode37 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode37.tree)
                char_literal38 = self.input.LT(1)
                self.match(self.input, 36, self.FOLLOW_36_in_line_key424) 
                stream_36.add(char_literal38)
                self._state.following.append(self.FOLLOW_keyelements_in_line_key426)
                keyelements39 = self.keyelements()

                self._state.following.pop()
                stream_keyelements.add(keyelements39.tree)
                # XKBGrammar.g:102:44: ( ',' keyelements )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 46) :
                        alt7 = 1


                    if alt7 == 1:
                        # XKBGrammar.g:102:45: ',' keyelements
                        char_literal40 = self.input.LT(1)
                        self.match(self.input, 46, self.FOLLOW_46_in_line_key429) 
                        stream_46.add(char_literal40)
                        self._state.following.append(self.FOLLOW_keyelements_in_line_key431)
                        keyelements41 = self.keyelements()

                        self._state.following.pop()
                        stream_keyelements.add(keyelements41.tree)



                    else:
                        break #loop7


                char_literal42 = self.input.LT(1)
                self.match(self.input, 37, self.FOLLOW_37_in_line_key435) 
                stream_37.add(char_literal42)
                # AST Rewrite
                # elements: keyelements, keycode, OVERRIDE
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
                # 103:2: -> ^( TOKEN_KEY ( OVERRIDE )? keycode ( keyelements )+ )
                # XKBGrammar.g:103:5: ^( TOKEN_KEY ( OVERRIDE )? keycode ( keyelements )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_KEY, "TOKEN_KEY"), root_1)

                # XKBGrammar.g:103:17: ( OVERRIDE )?
                if stream_OVERRIDE.hasNext():
                    self.adaptor.addChild(root_1, stream_OVERRIDE.nextNode())


                stream_OVERRIDE.reset();
                self.adaptor.addChild(root_1, stream_keycode.nextTree())
                # XKBGrammar.g:103:35: ( keyelements )+
                if not (stream_keyelements.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_keyelements.hasNext():
                    self.adaptor.addChild(root_1, stream_keyelements.nextTree())


                stream_keyelements.reset()

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
    # XKBGrammar.g:106:1: line_modifier_map : 'modifier_map' STATE '{' keycode ( ',' keycode )* '}' -> ^( TOKEN_MODIFIER_MAP STATE ( keycode )+ ) ;
    def line_modifier_map(self, ):

        retval = self.line_modifier_map_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal43 = None
        STATE44 = None
        char_literal45 = None
        char_literal47 = None
        char_literal49 = None
        keycode46 = None

        keycode48 = None


        string_literal43_tree = None
        STATE44_tree = None
        char_literal45_tree = None
        char_literal47_tree = None
        char_literal49_tree = None
        stream_STATE = RewriteRuleTokenStream(self.adaptor, "token STATE")
        stream_47 = RewriteRuleTokenStream(self.adaptor, "token 47")
        stream_46 = RewriteRuleTokenStream(self.adaptor, "token 46")
        stream_36 = RewriteRuleTokenStream(self.adaptor, "token 36")
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        try:
            try:
                # XKBGrammar.g:107:2: ( 'modifier_map' STATE '{' keycode ( ',' keycode )* '}' -> ^( TOKEN_MODIFIER_MAP STATE ( keycode )+ ) )
                # XKBGrammar.g:107:4: 'modifier_map' STATE '{' keycode ( ',' keycode )* '}'
                string_literal43 = self.input.LT(1)
                self.match(self.input, 47, self.FOLLOW_47_in_line_modifier_map461) 
                stream_47.add(string_literal43)
                STATE44 = self.input.LT(1)
                self.match(self.input, STATE, self.FOLLOW_STATE_in_line_modifier_map463) 
                stream_STATE.add(STATE44)
                char_literal45 = self.input.LT(1)
                self.match(self.input, 36, self.FOLLOW_36_in_line_modifier_map465) 
                stream_36.add(char_literal45)
                self._state.following.append(self.FOLLOW_keycode_in_line_modifier_map467)
                keycode46 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode46.tree)
                # XKBGrammar.g:107:37: ( ',' keycode )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 46) :
                        alt8 = 1


                    if alt8 == 1:
                        # XKBGrammar.g:107:38: ',' keycode
                        char_literal47 = self.input.LT(1)
                        self.match(self.input, 46, self.FOLLOW_46_in_line_modifier_map470) 
                        stream_46.add(char_literal47)
                        self._state.following.append(self.FOLLOW_keycode_in_line_modifier_map472)
                        keycode48 = self.keycode()

                        self._state.following.pop()
                        stream_keycode.add(keycode48.tree)



                    else:
                        break #loop8


                char_literal49 = self.input.LT(1)
                self.match(self.input, 37, self.FOLLOW_37_in_line_modifier_map476) 
                stream_37.add(char_literal49)
                # AST Rewrite
                # elements: STATE, keycode
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
                # 108:2: -> ^( TOKEN_MODIFIER_MAP STATE ( keycode )+ )
                # XKBGrammar.g:108:5: ^( TOKEN_MODIFIER_MAP STATE ( keycode )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_MODIFIER_MAP, "TOKEN_MODIFIER_MAP"), root_1)

                self.adaptor.addChild(root_1, stream_STATE.nextNode())
                # XKBGrammar.g:108:32: ( keycode )+
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

    class line_virtual_modifiers_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start line_virtual_modifiers
    # XKBGrammar.g:111:1: line_virtual_modifiers : 'virtual_modifiers' NAME ( ',' NAME )* -> ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ ) ;
    def line_virtual_modifiers(self, ):

        retval = self.line_virtual_modifiers_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal50 = None
        NAME51 = None
        char_literal52 = None
        NAME53 = None

        string_literal50_tree = None
        NAME51_tree = None
        char_literal52_tree = None
        NAME53_tree = None
        stream_48 = RewriteRuleTokenStream(self.adaptor, "token 48")
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_46 = RewriteRuleTokenStream(self.adaptor, "token 46")

        try:
            try:
                # XKBGrammar.g:112:2: ( 'virtual_modifiers' NAME ( ',' NAME )* -> ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ ) )
                # XKBGrammar.g:112:4: 'virtual_modifiers' NAME ( ',' NAME )*
                string_literal50 = self.input.LT(1)
                self.match(self.input, 48, self.FOLLOW_48_in_line_virtual_modifiers499) 
                stream_48.add(string_literal50)
                NAME51 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_virtual_modifiers501) 
                stream_NAME.add(NAME51)
                # XKBGrammar.g:112:29: ( ',' NAME )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 46) :
                        alt9 = 1


                    if alt9 == 1:
                        # XKBGrammar.g:112:30: ',' NAME
                        char_literal52 = self.input.LT(1)
                        self.match(self.input, 46, self.FOLLOW_46_in_line_virtual_modifiers504) 
                        stream_46.add(char_literal52)
                        NAME53 = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_line_virtual_modifiers506) 
                        stream_NAME.add(NAME53)



                    else:
                        break #loop9


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
                # 113:2: -> ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ )
                # XKBGrammar.g:113:5: ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_VIRTUAL_MODIFIERS, "TOKEN_VIRTUAL_MODIFIERS"), root_1)

                # XKBGrammar.g:113:31: ( NAME )+
                if not (stream_NAME.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_NAME.hasNext():
                    self.adaptor.addChild(root_1, stream_NAME.nextNode())


                stream_NAME.reset()

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

    # $ANTLR end line_virtual_modifiers

    class keycode_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start keycode
    # XKBGrammar.g:116:1: keycode : ( NAME -> ^( KEYCODE NAME ) | '<' NAME '>' -> ^( KEYCODEX NAME ) );
    def keycode(self, ):

        retval = self.keycode_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME54 = None
        char_literal55 = None
        NAME56 = None
        char_literal57 = None

        NAME54_tree = None
        char_literal55_tree = None
        NAME56_tree = None
        char_literal57_tree = None
        stream_49 = RewriteRuleTokenStream(self.adaptor, "token 49")
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_50 = RewriteRuleTokenStream(self.adaptor, "token 50")

        try:
            try:
                # XKBGrammar.g:117:2: ( NAME -> ^( KEYCODE NAME ) | '<' NAME '>' -> ^( KEYCODEX NAME ) )
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == NAME) :
                    alt10 = 1
                elif (LA10_0 == 49) :
                    alt10 = 2
                else:
                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # XKBGrammar.g:117:4: NAME
                    NAME54 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode530) 
                    stream_NAME.add(NAME54)
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
                    # 117:9: -> ^( KEYCODE NAME )
                    # XKBGrammar.g:117:12: ^( KEYCODE NAME )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYCODE, "KEYCODE"), root_1)

                    self.adaptor.addChild(root_1, stream_NAME.nextNode())

                    self.adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                elif alt10 == 2:
                    # XKBGrammar.g:118:4: '<' NAME '>'
                    char_literal55 = self.input.LT(1)
                    self.match(self.input, 49, self.FOLLOW_49_in_keycode543) 
                    stream_49.add(char_literal55)
                    NAME56 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode545) 
                    stream_NAME.add(NAME56)
                    char_literal57 = self.input.LT(1)
                    self.match(self.input, 50, self.FOLLOW_50_in_keycode547) 
                    stream_50.add(char_literal57)
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
                    # 118:17: -> ^( KEYCODEX NAME )
                    # XKBGrammar.g:118:20: ^( KEYCODEX NAME )
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

    class override_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start override
    # XKBGrammar.g:121:1: override : 'override' ;
    def override(self, ):

        retval = self.override_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal58 = None

        string_literal58_tree = None

        try:
            try:
                # XKBGrammar.g:122:2: ( 'override' )
                # XKBGrammar.g:122:4: 'override'
                root_0 = self.adaptor.nil()

                string_literal58 = self.input.LT(1)
                self.match(self.input, OVERRIDE, self.FOLLOW_OVERRIDE_in_override566)

                string_literal58_tree = self.adaptor.createWithPayload(string_literal58)
                self.adaptor.addChild(root_0, string_literal58_tree)





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

    # $ANTLR end override

    class keyelements_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start keyelements
    # XKBGrammar.g:125:1: keyelements : ( elem_keysyms | elem_keysymgroup | elem_virtualmods | elem_actions | elem_overlay );
    def keyelements(self, ):

        retval = self.keyelements_return()
        retval.start = self.input.LT(1)

        root_0 = None

        elem_keysyms59 = None

        elem_keysymgroup60 = None

        elem_virtualmods61 = None

        elem_actions62 = None

        elem_overlay63 = None



        try:
            try:
                # XKBGrammar.g:126:2: ( elem_keysyms | elem_keysymgroup | elem_virtualmods | elem_actions | elem_overlay )
                alt11 = 5
                LA11 = self.input.LA(1)
                if LA11 == 51:
                    alt11 = 1
                elif LA11 == 41 or LA11 == 52:
                    alt11 = 2
                elif LA11 == 53:
                    alt11 = 3
                elif LA11 == 54:
                    alt11 = 4
                elif LA11 == NAME:
                    alt11 = 5
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # XKBGrammar.g:126:4: elem_keysyms
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_elem_keysyms_in_keyelements577)
                    elem_keysyms59 = self.elem_keysyms()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, elem_keysyms59.tree)



                elif alt11 == 2:
                    # XKBGrammar.g:127:4: elem_keysymgroup
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_elem_keysymgroup_in_keyelements583)
                    elem_keysymgroup60 = self.elem_keysymgroup()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, elem_keysymgroup60.tree)



                elif alt11 == 3:
                    # XKBGrammar.g:128:4: elem_virtualmods
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_elem_virtualmods_in_keyelements588)
                    elem_virtualmods61 = self.elem_virtualmods()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, elem_virtualmods61.tree)



                elif alt11 == 4:
                    # XKBGrammar.g:129:4: elem_actions
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_elem_actions_in_keyelements593)
                    elem_actions62 = self.elem_actions()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, elem_actions62.tree)



                elif alt11 == 5:
                    # XKBGrammar.g:130:4: elem_overlay
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_elem_overlay_in_keyelements598)
                    elem_overlay63 = self.elem_overlay()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, elem_overlay63.tree)



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

    # $ANTLR end keyelements

    class elem_keysyms_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start elem_keysyms
    # XKBGrammar.g:133:1: elem_keysyms : 'type' ( '[' NAME ']' )? '=' DQSTRING -> ^( ELEM_KEYSYMS ^( TOKEN_TYPE ( NAME )? DQSTRING ) ) ;
    def elem_keysyms(self, ):

        retval = self.elem_keysyms_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal64 = None
        char_literal65 = None
        NAME66 = None
        char_literal67 = None
        char_literal68 = None
        DQSTRING69 = None

        string_literal64_tree = None
        char_literal65_tree = None
        NAME66_tree = None
        char_literal67_tree = None
        char_literal68_tree = None
        DQSTRING69_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_42 = RewriteRuleTokenStream(self.adaptor, "token 42")
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_51 = RewriteRuleTokenStream(self.adaptor, "token 51")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")

        try:
            try:
                # XKBGrammar.g:134:2: ( 'type' ( '[' NAME ']' )? '=' DQSTRING -> ^( ELEM_KEYSYMS ^( TOKEN_TYPE ( NAME )? DQSTRING ) ) )
                # XKBGrammar.g:134:4: 'type' ( '[' NAME ']' )? '=' DQSTRING
                string_literal64 = self.input.LT(1)
                self.match(self.input, 51, self.FOLLOW_51_in_elem_keysyms609) 
                stream_51.add(string_literal64)
                # XKBGrammar.g:134:11: ( '[' NAME ']' )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == 41) :
                    alt12 = 1
                if alt12 == 1:
                    # XKBGrammar.g:134:12: '[' NAME ']'
                    char_literal65 = self.input.LT(1)
                    self.match(self.input, 41, self.FOLLOW_41_in_elem_keysyms612) 
                    stream_41.add(char_literal65)
                    NAME66 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_keysyms614) 
                    stream_NAME.add(NAME66)
                    char_literal67 = self.input.LT(1)
                    self.match(self.input, 42, self.FOLLOW_42_in_elem_keysyms616) 
                    stream_42.add(char_literal67)




                char_literal68 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_elem_keysyms620) 
                stream_43.add(char_literal68)
                DQSTRING69 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_elem_keysyms622) 
                stream_DQSTRING.add(DQSTRING69)
                # AST Rewrite
                # elements: DQSTRING, NAME
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
                # 135:2: -> ^( ELEM_KEYSYMS ^( TOKEN_TYPE ( NAME )? DQSTRING ) )
                # XKBGrammar.g:135:5: ^( ELEM_KEYSYMS ^( TOKEN_TYPE ( NAME )? DQSTRING ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ELEM_KEYSYMS, "ELEM_KEYSYMS"), root_1)

                # XKBGrammar.g:135:20: ^( TOKEN_TYPE ( NAME )? DQSTRING )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_TYPE, "TOKEN_TYPE"), root_2)

                # XKBGrammar.g:135:33: ( NAME )?
                if stream_NAME.hasNext():
                    self.adaptor.addChild(root_2, stream_NAME.nextNode())


                stream_NAME.reset();
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

    # $ANTLR end elem_keysyms

    class elem_keysymgroup_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start elem_keysymgroup
    # XKBGrammar.g:138:1: elem_keysymgroup : ( 'symbols' '[' group= NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']' -> ^( ELEM_KEYSYMGROUP ( $group)? ^( VALUE ( $keysym)+ ) ) ;
    def elem_keysymgroup(self, ):

        retval = self.elem_keysymgroup_return()
        retval.start = self.input.LT(1)

        root_0 = None

        group = None
        string_literal70 = None
        char_literal71 = None
        char_literal72 = None
        char_literal73 = None
        char_literal74 = None
        char_literal75 = None
        char_literal76 = None
        keysym = None
        list_keysym = None

        group_tree = None
        string_literal70_tree = None
        char_literal71_tree = None
        char_literal72_tree = None
        char_literal73_tree = None
        char_literal74_tree = None
        char_literal75_tree = None
        char_literal76_tree = None
        keysym_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_42 = RewriteRuleTokenStream(self.adaptor, "token 42")
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_46 = RewriteRuleTokenStream(self.adaptor, "token 46")
        stream_52 = RewriteRuleTokenStream(self.adaptor, "token 52")

        try:
            try:
                # XKBGrammar.g:139:2: ( ( 'symbols' '[' group= NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']' -> ^( ELEM_KEYSYMGROUP ( $group)? ^( VALUE ( $keysym)+ ) ) )
                # XKBGrammar.g:139:4: ( 'symbols' '[' group= NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']'
                # XKBGrammar.g:139:4: ( 'symbols' '[' group= NAME ']' '=' )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == 52) :
                    alt13 = 1
                if alt13 == 1:
                    # XKBGrammar.g:139:5: 'symbols' '[' group= NAME ']' '='
                    string_literal70 = self.input.LT(1)
                    self.match(self.input, 52, self.FOLLOW_52_in_elem_keysymgroup650) 
                    stream_52.add(string_literal70)
                    char_literal71 = self.input.LT(1)
                    self.match(self.input, 41, self.FOLLOW_41_in_elem_keysymgroup652) 
                    stream_41.add(char_literal71)
                    group = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_keysymgroup656) 
                    stream_NAME.add(group)
                    char_literal72 = self.input.LT(1)
                    self.match(self.input, 42, self.FOLLOW_42_in_elem_keysymgroup658) 
                    stream_42.add(char_literal72)
                    char_literal73 = self.input.LT(1)
                    self.match(self.input, 43, self.FOLLOW_43_in_elem_keysymgroup660) 
                    stream_43.add(char_literal73)




                char_literal74 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_elem_keysymgroup664) 
                stream_41.add(char_literal74)
                keysym = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_keysymgroup668) 
                stream_NAME.add(keysym)
                if list_keysym is None:
                    list_keysym = []
                list_keysym.append(keysym)

                # XKBGrammar.g:139:57: ( ',' keysym+= NAME )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == 46) :
                        alt14 = 1


                    if alt14 == 1:
                        # XKBGrammar.g:139:58: ',' keysym+= NAME
                        char_literal75 = self.input.LT(1)
                        self.match(self.input, 46, self.FOLLOW_46_in_elem_keysymgroup671) 
                        stream_46.add(char_literal75)
                        keysym = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_keysymgroup675) 
                        stream_NAME.add(keysym)
                        if list_keysym is None:
                            list_keysym = []
                        list_keysym.append(keysym)




                    else:
                        break #loop14


                char_literal76 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_elem_keysymgroup679) 
                stream_42.add(char_literal76)
                # AST Rewrite
                # elements: group, keysym
                # token labels: group
                # rule labels: retval
                # token list labels: keysym
                # rule list labels: 

                retval.tree = root_0
                stream_group = RewriteRuleTokenStream(self.adaptor, "token group", group)
                stream_keysym = RewriteRuleTokenStream(self.adaptor, "token keysym", list_keysym)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                root_0 = self.adaptor.nil()
                # 140:2: -> ^( ELEM_KEYSYMGROUP ( $group)? ^( VALUE ( $keysym)+ ) )
                # XKBGrammar.g:140:5: ^( ELEM_KEYSYMGROUP ( $group)? ^( VALUE ( $keysym)+ ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ELEM_KEYSYMGROUP, "ELEM_KEYSYMGROUP"), root_1)

                # XKBGrammar.g:140:24: ( $group)?
                if stream_group.hasNext():
                    self.adaptor.addChild(root_1, stream_group.nextNode())


                stream_group.reset();
                # XKBGrammar.g:140:32: ^( VALUE ( $keysym)+ )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(VALUE, "VALUE"), root_2)

                # XKBGrammar.g:140:40: ( $keysym)+
                if not (stream_keysym.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_keysym.hasNext():
                    self.adaptor.addChild(root_2, stream_keysym.nextNode())


                stream_keysym.reset()

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

    # $ANTLR end elem_keysymgroup

    class elem_virtualmods_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start elem_virtualmods
    # XKBGrammar.g:143:1: elem_virtualmods : ( 'virtualMods' '=' NAME ) -> ^( ELEM_VIRTUALMODS NAME ) ;
    def elem_virtualmods(self, ):

        retval = self.elem_virtualmods_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal77 = None
        char_literal78 = None
        NAME79 = None

        string_literal77_tree = None
        char_literal78_tree = None
        NAME79_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_53 = RewriteRuleTokenStream(self.adaptor, "token 53")

        try:
            try:
                # XKBGrammar.g:144:2: ( ( 'virtualMods' '=' NAME ) -> ^( ELEM_VIRTUALMODS NAME ) )
                # XKBGrammar.g:144:4: ( 'virtualMods' '=' NAME )
                # XKBGrammar.g:144:4: ( 'virtualMods' '=' NAME )
                # XKBGrammar.g:144:5: 'virtualMods' '=' NAME
                string_literal77 = self.input.LT(1)
                self.match(self.input, 53, self.FOLLOW_53_in_elem_virtualmods711) 
                stream_53.add(string_literal77)
                char_literal78 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_elem_virtualmods713) 
                stream_43.add(char_literal78)
                NAME79 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_virtualmods715) 
                stream_NAME.add(NAME79)




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
                # 145:2: -> ^( ELEM_VIRTUALMODS NAME )
                # XKBGrammar.g:145:5: ^( ELEM_VIRTUALMODS NAME )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ELEM_VIRTUALMODS, "ELEM_VIRTUALMODS"), root_1)

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

    # $ANTLR end elem_virtualmods

    class elem_actions_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start elem_actions
    # XKBGrammar.g:148:1: elem_actions : 'actions' '[' NAME ']' '=' '[' actions_setmods ( ',' actions_setmods )* ']' -> ^( ELEM_ACTIONS NAME ( actions_setmods )+ ) ;
    def elem_actions(self, ):

        retval = self.elem_actions_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal80 = None
        char_literal81 = None
        NAME82 = None
        char_literal83 = None
        char_literal84 = None
        char_literal85 = None
        char_literal87 = None
        char_literal89 = None
        actions_setmods86 = None

        actions_setmods88 = None


        string_literal80_tree = None
        char_literal81_tree = None
        NAME82_tree = None
        char_literal83_tree = None
        char_literal84_tree = None
        char_literal85_tree = None
        char_literal87_tree = None
        char_literal89_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_42 = RewriteRuleTokenStream(self.adaptor, "token 42")
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_46 = RewriteRuleTokenStream(self.adaptor, "token 46")
        stream_54 = RewriteRuleTokenStream(self.adaptor, "token 54")
        stream_actions_setmods = RewriteRuleSubtreeStream(self.adaptor, "rule actions_setmods")
        try:
            try:
                # XKBGrammar.g:149:2: ( 'actions' '[' NAME ']' '=' '[' actions_setmods ( ',' actions_setmods )* ']' -> ^( ELEM_ACTIONS NAME ( actions_setmods )+ ) )
                # XKBGrammar.g:149:4: 'actions' '[' NAME ']' '=' '[' actions_setmods ( ',' actions_setmods )* ']'
                string_literal80 = self.input.LT(1)
                self.match(self.input, 54, self.FOLLOW_54_in_elem_actions736) 
                stream_54.add(string_literal80)
                char_literal81 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_elem_actions738) 
                stream_41.add(char_literal81)
                NAME82 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_actions740) 
                stream_NAME.add(NAME82)
                char_literal83 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_elem_actions742) 
                stream_42.add(char_literal83)
                char_literal84 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_elem_actions744) 
                stream_43.add(char_literal84)
                char_literal85 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_elem_actions746) 
                stream_41.add(char_literal85)
                self._state.following.append(self.FOLLOW_actions_setmods_in_elem_actions748)
                actions_setmods86 = self.actions_setmods()

                self._state.following.pop()
                stream_actions_setmods.add(actions_setmods86.tree)
                # XKBGrammar.g:149:51: ( ',' actions_setmods )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == 46) :
                        alt15 = 1


                    if alt15 == 1:
                        # XKBGrammar.g:149:52: ',' actions_setmods
                        char_literal87 = self.input.LT(1)
                        self.match(self.input, 46, self.FOLLOW_46_in_elem_actions751) 
                        stream_46.add(char_literal87)
                        self._state.following.append(self.FOLLOW_actions_setmods_in_elem_actions753)
                        actions_setmods88 = self.actions_setmods()

                        self._state.following.pop()
                        stream_actions_setmods.add(actions_setmods88.tree)



                    else:
                        break #loop15


                char_literal89 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_elem_actions757) 
                stream_42.add(char_literal89)
                # AST Rewrite
                # elements: actions_setmods, NAME
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
                # 150:2: -> ^( ELEM_ACTIONS NAME ( actions_setmods )+ )
                # XKBGrammar.g:150:5: ^( ELEM_ACTIONS NAME ( actions_setmods )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ELEM_ACTIONS, "ELEM_ACTIONS"), root_1)

                self.adaptor.addChild(root_1, stream_NAME.nextNode())
                # XKBGrammar.g:150:25: ( actions_setmods )+
                if not (stream_actions_setmods.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_actions_setmods.hasNext():
                    self.adaptor.addChild(root_1, stream_actions_setmods.nextTree())


                stream_actions_setmods.reset()

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

    # $ANTLR end elem_actions

    class actions_setmods_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start actions_setmods
    # XKBGrammar.g:153:1: actions_setmods : 'SetMods' '(' 'modifiers' '=' (mod= STATE | mod= NAME ) ( ',' NAME )* ')' -> ^( ACTIONS_SETMODS $mod ( NAME )* ) ;
    def actions_setmods(self, ):

        retval = self.actions_setmods_return()
        retval.start = self.input.LT(1)

        root_0 = None

        mod = None
        string_literal90 = None
        char_literal91 = None
        string_literal92 = None
        char_literal93 = None
        char_literal94 = None
        NAME95 = None
        char_literal96 = None

        mod_tree = None
        string_literal90_tree = None
        char_literal91_tree = None
        string_literal92_tree = None
        char_literal93_tree = None
        char_literal94_tree = None
        NAME95_tree = None
        char_literal96_tree = None
        stream_STATE = RewriteRuleTokenStream(self.adaptor, "token STATE")
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_58 = RewriteRuleTokenStream(self.adaptor, "token 58")
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_57 = RewriteRuleTokenStream(self.adaptor, "token 57")
        stream_56 = RewriteRuleTokenStream(self.adaptor, "token 56")
        stream_55 = RewriteRuleTokenStream(self.adaptor, "token 55")
        stream_46 = RewriteRuleTokenStream(self.adaptor, "token 46")

        try:
            try:
                # XKBGrammar.g:154:2: ( 'SetMods' '(' 'modifiers' '=' (mod= STATE | mod= NAME ) ( ',' NAME )* ')' -> ^( ACTIONS_SETMODS $mod ( NAME )* ) )
                # XKBGrammar.g:154:4: 'SetMods' '(' 'modifiers' '=' (mod= STATE | mod= NAME ) ( ',' NAME )* ')'
                string_literal90 = self.input.LT(1)
                self.match(self.input, 55, self.FOLLOW_55_in_actions_setmods780) 
                stream_55.add(string_literal90)
                char_literal91 = self.input.LT(1)
                self.match(self.input, 56, self.FOLLOW_56_in_actions_setmods782) 
                stream_56.add(char_literal91)
                string_literal92 = self.input.LT(1)
                self.match(self.input, 57, self.FOLLOW_57_in_actions_setmods784) 
                stream_57.add(string_literal92)
                char_literal93 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_actions_setmods786) 
                stream_43.add(char_literal93)
                # XKBGrammar.g:154:34: (mod= STATE | mod= NAME )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == STATE) :
                    alt16 = 1
                elif (LA16_0 == NAME) :
                    alt16 = 2
                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # XKBGrammar.g:154:35: mod= STATE
                    mod = self.input.LT(1)
                    self.match(self.input, STATE, self.FOLLOW_STATE_in_actions_setmods791) 
                    stream_STATE.add(mod)



                elif alt16 == 2:
                    # XKBGrammar.g:154:47: mod= NAME
                    mod = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_actions_setmods797) 
                    stream_NAME.add(mod)




                # XKBGrammar.g:154:57: ( ',' NAME )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == 46) :
                        alt17 = 1


                    if alt17 == 1:
                        # XKBGrammar.g:154:58: ',' NAME
                        char_literal94 = self.input.LT(1)
                        self.match(self.input, 46, self.FOLLOW_46_in_actions_setmods801) 
                        stream_46.add(char_literal94)
                        NAME95 = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_actions_setmods803) 
                        stream_NAME.add(NAME95)



                    else:
                        break #loop17


                char_literal96 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_actions_setmods807) 
                stream_58.add(char_literal96)
                # AST Rewrite
                # elements: NAME, mod
                # token labels: mod
                # rule labels: retval
                # token list labels: 
                # rule list labels: 

                retval.tree = root_0
                stream_mod = RewriteRuleTokenStream(self.adaptor, "token mod", mod)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                root_0 = self.adaptor.nil()
                # 155:2: -> ^( ACTIONS_SETMODS $mod ( NAME )* )
                # XKBGrammar.g:155:5: ^( ACTIONS_SETMODS $mod ( NAME )* )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ACTIONS_SETMODS, "ACTIONS_SETMODS"), root_1)

                self.adaptor.addChild(root_1, stream_mod.nextNode())
                # XKBGrammar.g:155:28: ( NAME )*
                while stream_NAME.hasNext():
                    self.adaptor.addChild(root_1, stream_NAME.nextNode())


                stream_NAME.reset();

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

    # $ANTLR end actions_setmods

    class elem_overlay_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start elem_overlay
    # XKBGrammar.g:158:1: elem_overlay : NAME '=' keycode -> ^( OVERLAY NAME keycode ) ;
    def elem_overlay(self, ):

        retval = self.elem_overlay_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME97 = None
        char_literal98 = None
        keycode99 = None


        NAME97_tree = None
        char_literal98_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        try:
            try:
                # XKBGrammar.g:159:2: ( NAME '=' keycode -> ^( OVERLAY NAME keycode ) )
                # XKBGrammar.g:159:4: NAME '=' keycode
                NAME97 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_overlay831) 
                stream_NAME.add(NAME97)
                char_literal98 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_elem_overlay833) 
                stream_43.add(char_literal98)
                self._state.following.append(self.FOLLOW_keycode_in_elem_overlay835)
                keycode99 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode99.tree)
                # AST Rewrite
                # elements: NAME, keycode
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
                # 160:2: -> ^( OVERLAY NAME keycode )
                # XKBGrammar.g:160:5: ^( OVERLAY NAME keycode )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(OVERLAY, "OVERLAY"), root_1)

                self.adaptor.addChild(root_1, stream_NAME.nextNode())
                self.adaptor.addChild(root_1, stream_keycode.nextTree())

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

    # $ANTLR end elem_overlay


    # Delegated rules


 

    FOLLOW_symbols_in_layout169 = frozenset([30])
    FOLLOW_EOF_in_layout172 = frozenset([1])
    FOLLOW_mapType_in_symbols195 = frozenset([36])
    FOLLOW_36_in_symbols197 = frozenset([28, 39, 40, 44, 45, 47, 48])
    FOLLOW_mapMaterial_in_symbols199 = frozenset([28, 37, 39, 40, 44, 45, 47, 48])
    FOLLOW_37_in_symbols202 = frozenset([38])
    FOLLOW_38_in_symbols204 = frozenset([1])
    FOLLOW_MAPOPTS_in_mapType232 = frozenset([30, 31])
    FOLLOW_DQSTRING_in_mapType235 = frozenset([1])
    FOLLOW_line_include_in_mapMaterial267 = frozenset([1])
    FOLLOW_line_name_in_mapMaterial273 = frozenset([38])
    FOLLOW_38_in_mapMaterial275 = frozenset([1])
    FOLLOW_line_keytype_in_mapMaterial281 = frozenset([38])
    FOLLOW_38_in_mapMaterial283 = frozenset([1])
    FOLLOW_line_key_in_mapMaterial289 = frozenset([38])
    FOLLOW_38_in_mapMaterial291 = frozenset([1])
    FOLLOW_line_modifier_map_in_mapMaterial297 = frozenset([38])
    FOLLOW_38_in_mapMaterial299 = frozenset([1])
    FOLLOW_line_virtual_modifiers_in_mapMaterial305 = frozenset([38])
    FOLLOW_38_in_mapMaterial307 = frozenset([1])
    FOLLOW_39_in_line_include319 = frozenset([31])
    FOLLOW_DQSTRING_in_line_include321 = frozenset([1])
    FOLLOW_40_in_line_name341 = frozenset([41])
    FOLLOW_41_in_line_name343 = frozenset([32])
    FOLLOW_NAME_in_line_name345 = frozenset([42])
    FOLLOW_42_in_line_name347 = frozenset([43])
    FOLLOW_43_in_line_name349 = frozenset([31])
    FOLLOW_DQSTRING_in_line_name351 = frozenset([1])
    FOLLOW_44_in_line_keytype377 = frozenset([41, 43])
    FOLLOW_41_in_line_keytype380 = frozenset([32])
    FOLLOW_NAME_in_line_keytype382 = frozenset([42])
    FOLLOW_42_in_line_keytype384 = frozenset([43])
    FOLLOW_43_in_line_keytype388 = frozenset([31])
    FOLLOW_DQSTRING_in_line_keytype390 = frozenset([1])
    FOLLOW_OVERRIDE_in_line_key417 = frozenset([45])
    FOLLOW_45_in_line_key420 = frozenset([32, 49])
    FOLLOW_keycode_in_line_key422 = frozenset([36])
    FOLLOW_36_in_line_key424 = frozenset([32, 41, 51, 52, 53, 54])
    FOLLOW_keyelements_in_line_key426 = frozenset([37, 46])
    FOLLOW_46_in_line_key429 = frozenset([32, 41, 51, 52, 53, 54])
    FOLLOW_keyelements_in_line_key431 = frozenset([37, 46])
    FOLLOW_37_in_line_key435 = frozenset([1])
    FOLLOW_47_in_line_modifier_map461 = frozenset([21])
    FOLLOW_STATE_in_line_modifier_map463 = frozenset([36])
    FOLLOW_36_in_line_modifier_map465 = frozenset([32, 49])
    FOLLOW_keycode_in_line_modifier_map467 = frozenset([37, 46])
    FOLLOW_46_in_line_modifier_map470 = frozenset([32, 49])
    FOLLOW_keycode_in_line_modifier_map472 = frozenset([37, 46])
    FOLLOW_37_in_line_modifier_map476 = frozenset([1])
    FOLLOW_48_in_line_virtual_modifiers499 = frozenset([32])
    FOLLOW_NAME_in_line_virtual_modifiers501 = frozenset([1, 46])
    FOLLOW_46_in_line_virtual_modifiers504 = frozenset([32])
    FOLLOW_NAME_in_line_virtual_modifiers506 = frozenset([1, 46])
    FOLLOW_NAME_in_keycode530 = frozenset([1])
    FOLLOW_49_in_keycode543 = frozenset([32])
    FOLLOW_NAME_in_keycode545 = frozenset([50])
    FOLLOW_50_in_keycode547 = frozenset([1])
    FOLLOW_OVERRIDE_in_override566 = frozenset([1])
    FOLLOW_elem_keysyms_in_keyelements577 = frozenset([1])
    FOLLOW_elem_keysymgroup_in_keyelements583 = frozenset([1])
    FOLLOW_elem_virtualmods_in_keyelements588 = frozenset([1])
    FOLLOW_elem_actions_in_keyelements593 = frozenset([1])
    FOLLOW_elem_overlay_in_keyelements598 = frozenset([1])
    FOLLOW_51_in_elem_keysyms609 = frozenset([41, 43])
    FOLLOW_41_in_elem_keysyms612 = frozenset([32])
    FOLLOW_NAME_in_elem_keysyms614 = frozenset([42])
    FOLLOW_42_in_elem_keysyms616 = frozenset([43])
    FOLLOW_43_in_elem_keysyms620 = frozenset([31])
    FOLLOW_DQSTRING_in_elem_keysyms622 = frozenset([1])
    FOLLOW_52_in_elem_keysymgroup650 = frozenset([41])
    FOLLOW_41_in_elem_keysymgroup652 = frozenset([32])
    FOLLOW_NAME_in_elem_keysymgroup656 = frozenset([42])
    FOLLOW_42_in_elem_keysymgroup658 = frozenset([43])
    FOLLOW_43_in_elem_keysymgroup660 = frozenset([41])
    FOLLOW_41_in_elem_keysymgroup664 = frozenset([32])
    FOLLOW_NAME_in_elem_keysymgroup668 = frozenset([42, 46])
    FOLLOW_46_in_elem_keysymgroup671 = frozenset([32])
    FOLLOW_NAME_in_elem_keysymgroup675 = frozenset([42, 46])
    FOLLOW_42_in_elem_keysymgroup679 = frozenset([1])
    FOLLOW_53_in_elem_virtualmods711 = frozenset([43])
    FOLLOW_43_in_elem_virtualmods713 = frozenset([32])
    FOLLOW_NAME_in_elem_virtualmods715 = frozenset([1])
    FOLLOW_54_in_elem_actions736 = frozenset([41])
    FOLLOW_41_in_elem_actions738 = frozenset([32])
    FOLLOW_NAME_in_elem_actions740 = frozenset([42])
    FOLLOW_42_in_elem_actions742 = frozenset([43])
    FOLLOW_43_in_elem_actions744 = frozenset([41])
    FOLLOW_41_in_elem_actions746 = frozenset([55])
    FOLLOW_actions_setmods_in_elem_actions748 = frozenset([42, 46])
    FOLLOW_46_in_elem_actions751 = frozenset([55])
    FOLLOW_actions_setmods_in_elem_actions753 = frozenset([42, 46])
    FOLLOW_42_in_elem_actions757 = frozenset([1])
    FOLLOW_55_in_actions_setmods780 = frozenset([56])
    FOLLOW_56_in_actions_setmods782 = frozenset([57])
    FOLLOW_57_in_actions_setmods784 = frozenset([43])
    FOLLOW_43_in_actions_setmods786 = frozenset([21, 32])
    FOLLOW_STATE_in_actions_setmods791 = frozenset([46, 58])
    FOLLOW_NAME_in_actions_setmods797 = frozenset([46, 58])
    FOLLOW_46_in_actions_setmods801 = frozenset([32])
    FOLLOW_NAME_in_actions_setmods803 = frozenset([46, 58])
    FOLLOW_58_in_actions_setmods807 = frozenset([1])
    FOLLOW_NAME_in_elem_overlay831 = frozenset([43])
    FOLLOW_43_in_elem_overlay833 = frozenset([32, 49])
    FOLLOW_keycode_in_elem_overlay835 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("XKBGrammarLexer", XKBGrammarParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)

if __name__ == '__main__':
    main(sys.argv)
