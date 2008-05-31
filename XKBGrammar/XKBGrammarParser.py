# $ANTLR 3.1b1 XKBGrammar.g 2008-05-31 21:36:47

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__66=66
T__64=64
T__65=65
T__62=62
T__63=63
MAPOPTIONS=15
TOKEN_INCLUDE=4
TOKEN_MODIFIER_MAP=9
T__61=61
EOF=-1
T__60=60
TOKEN_TYPE=8
MAPTYPE=13
TOKEN_VIRTUAL_MODIFIERS=11
T__55=55
T__56=56
T__57=57
NAME=27
T__58=58
T__51=51
T__52=52
MAPMATERIAL=16
T__53=53
T__54=54
T__59=59
KEYSYMS=20
COMMENT=29
DQSTRING=26
T__50=50
T__42=42
T__43=43
STATE=22
T__40=40
T__41=41
T__46=46
T__47=47
T__44=44
T__45=45
LINE_COMMENT=30
KEYCODE=18
T__48=48
T__49=49
TOKEN_NAME=6
VALUE=21
LAYOUT=12
T__31=31
T__32=32
WS=28
T__33=33
T__34=34
T__35=35
T__36=36
T__37=37
OVERRIDE=24
T__38=38
T__39=39
KEYSYMGROUP=23
TOKEN_SYMBOL=10
MAPNAME=14
TOKEN_KEY=7
VIRTUALMODS=25
SYMBOLS=17
TOKEN_KEY_TYPE=5
KEYCODEX=19

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "TOKEN_INCLUDE", "TOKEN_KEY_TYPE", "TOKEN_NAME", "TOKEN_KEY", "TOKEN_TYPE", 
    "TOKEN_MODIFIER_MAP", "TOKEN_SYMBOL", "TOKEN_VIRTUAL_MODIFIERS", "LAYOUT", 
    "MAPTYPE", "MAPNAME", "MAPOPTIONS", "MAPMATERIAL", "SYMBOLS", "KEYCODE", 
    "KEYCODEX", "KEYSYMS", "VALUE", "STATE", "KEYSYMGROUP", "OVERRIDE", 
    "VIRTUALMODS", "DQSTRING", "NAME", "WS", "COMMENT", "LINE_COMMENT", 
    "'{'", "'}'", "';'", "'include'", "'name'", "'['", "']'", "'='", "'key.type'", 
    "'override'", "'key'", "'modifier_map'", "','", "'virtual_modifiers'", 
    "'<'", "'>'", "'type'", "'symbols'", "'virtualMods'", "'default'", "'hidden'", 
    "'partial'", "'alphanumeric_keys'", "'keypad_keys'", "'function_keys'", 
    "'modifier_keys'", "'alternate_group'", "'xkb_symbols'", "'Shift'", 
    "'Control'", "'Lock'", "'Mod1'", "'Mod2'", "'Mod3'", "'Mod4'", "'Mod5'"
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
    # XKBGrammar.g:58:1: layout : ( symbols )+ EOF -> ^( LAYOUT ( symbols )+ ) ;
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
                # XKBGrammar.g:59:2: ( ( symbols )+ EOF -> ^( LAYOUT ( symbols )+ ) )
                # XKBGrammar.g:59:4: ( symbols )+ EOF
                # XKBGrammar.g:59:4: ( symbols )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((50 <= LA1_0 <= 58)) :
                        alt1 = 1


                    if alt1 == 1:
                        # XKBGrammar.g:59:4: symbols
                        self._state.following.append(self.FOLLOW_symbols_in_layout153)
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
                self.match(self.input, EOF, self.FOLLOW_EOF_in_layout156) 
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
                # 60:2: -> ^( LAYOUT ( symbols )+ )
                # XKBGrammar.g:60:5: ^( LAYOUT ( symbols )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(LAYOUT, "LAYOUT"), root_1)

                # XKBGrammar.g:60:14: ( symbols )+
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
    # XKBGrammar.g:63:1: symbols : mapType '{' ( mapMaterial )+ '}' ';' -> ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) ) ;
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
        stream_32 = RewriteRuleTokenStream(self.adaptor, "token 32")
        stream_31 = RewriteRuleTokenStream(self.adaptor, "token 31")
        stream_33 = RewriteRuleTokenStream(self.adaptor, "token 33")
        stream_mapMaterial = RewriteRuleSubtreeStream(self.adaptor, "rule mapMaterial")
        stream_mapType = RewriteRuleSubtreeStream(self.adaptor, "rule mapType")
        try:
            try:
                # XKBGrammar.g:64:2: ( mapType '{' ( mapMaterial )+ '}' ';' -> ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) ) )
                # XKBGrammar.g:64:4: mapType '{' ( mapMaterial )+ '}' ';'
                self._state.following.append(self.FOLLOW_mapType_in_symbols179)
                mapType3 = self.mapType()

                self._state.following.pop()
                stream_mapType.add(mapType3.tree)
                char_literal4 = self.input.LT(1)
                self.match(self.input, 31, self.FOLLOW_31_in_symbols181) 
                stream_31.add(char_literal4)
                # XKBGrammar.g:64:16: ( mapMaterial )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((34 <= LA2_0 <= 35) or (39 <= LA2_0 <= 42) or LA2_0 == 44) :
                        alt2 = 1


                    if alt2 == 1:
                        # XKBGrammar.g:64:16: mapMaterial
                        self._state.following.append(self.FOLLOW_mapMaterial_in_symbols183)
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
                self.match(self.input, 32, self.FOLLOW_32_in_symbols186) 
                stream_32.add(char_literal6)
                char_literal7 = self.input.LT(1)
                self.match(self.input, 33, self.FOLLOW_33_in_symbols188) 
                stream_33.add(char_literal7)
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
                # 65:2: -> ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) )
                # XKBGrammar.g:65:5: ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(SYMBOLS, "SYMBOLS"), root_1)

                self.adaptor.addChild(root_1, stream_mapType.nextTree())
                # XKBGrammar.g:65:23: ^( MAPMATERIAL ( mapMaterial )+ )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPMATERIAL, "MAPMATERIAL"), root_2)

                # XKBGrammar.g:65:37: ( mapMaterial )+
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
    # XKBGrammar.g:68:1: mapType : ( mapOptions )+ DQSTRING -> ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME DQSTRING ) ) ;
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
                # XKBGrammar.g:69:2: ( ( mapOptions )+ DQSTRING -> ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME DQSTRING ) ) )
                # XKBGrammar.g:69:4: ( mapOptions )+ DQSTRING
                # XKBGrammar.g:69:4: ( mapOptions )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((50 <= LA3_0 <= 58)) :
                        alt3 = 1


                    if alt3 == 1:
                        # XKBGrammar.g:69:4: mapOptions
                        self._state.following.append(self.FOLLOW_mapOptions_in_mapType216)
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
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_mapType219) 
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
                # 70:2: -> ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME DQSTRING ) )
                # XKBGrammar.g:70:5: ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME DQSTRING ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPTYPE, "MAPTYPE"), root_1)

                # XKBGrammar.g:70:15: ^( MAPOPTIONS ( mapOptions )+ )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPOPTIONS, "MAPOPTIONS"), root_2)

                # XKBGrammar.g:70:28: ( mapOptions )+
                if not (stream_mapOptions.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_mapOptions.hasNext():
                    self.adaptor.addChild(root_2, stream_mapOptions.nextTree())


                stream_mapOptions.reset()

                self.adaptor.addChild(root_1, root_2)
                # XKBGrammar.g:70:41: ^( MAPNAME DQSTRING )
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
    # XKBGrammar.g:73:1: mapMaterial : ( line_include | line_name ';' | line_keytype ';' | line_key ';' | line_modifier_map ';' | line_virtual_modifiers ';' );
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
                # XKBGrammar.g:74:2: ( line_include | line_name ';' | line_keytype ';' | line_key ';' | line_modifier_map ';' | line_virtual_modifiers ';' )
                alt4 = 6
                LA4 = self.input.LA(1)
                if LA4 == 34:
                    alt4 = 1
                elif LA4 == 35:
                    alt4 = 2
                elif LA4 == 39:
                    alt4 = 3
                elif LA4 == 40 or LA4 == 41:
                    alt4 = 4
                elif LA4 == 42:
                    alt4 = 5
                elif LA4 == 44:
                    alt4 = 6
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # XKBGrammar.g:74:4: line_include
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_include_in_mapMaterial251)
                    line_include10 = self.line_include()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_include10.tree)



                elif alt4 == 2:
                    # XKBGrammar.g:75:4: line_name ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_name_in_mapMaterial257)
                    line_name11 = self.line_name()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_name11.tree)
                    char_literal12 = self.input.LT(1)
                    self.match(self.input, 33, self.FOLLOW_33_in_mapMaterial259)



                elif alt4 == 3:
                    # XKBGrammar.g:76:4: line_keytype ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_keytype_in_mapMaterial265)
                    line_keytype13 = self.line_keytype()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_keytype13.tree)
                    char_literal14 = self.input.LT(1)
                    self.match(self.input, 33, self.FOLLOW_33_in_mapMaterial267)



                elif alt4 == 4:
                    # XKBGrammar.g:77:4: line_key ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_key_in_mapMaterial273)
                    line_key15 = self.line_key()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_key15.tree)
                    char_literal16 = self.input.LT(1)
                    self.match(self.input, 33, self.FOLLOW_33_in_mapMaterial275)



                elif alt4 == 5:
                    # XKBGrammar.g:78:4: line_modifier_map ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_modifier_map_in_mapMaterial281)
                    line_modifier_map17 = self.line_modifier_map()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_modifier_map17.tree)
                    char_literal18 = self.input.LT(1)
                    self.match(self.input, 33, self.FOLLOW_33_in_mapMaterial283)



                elif alt4 == 6:
                    # XKBGrammar.g:79:4: line_virtual_modifiers ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_virtual_modifiers_in_mapMaterial289)
                    line_virtual_modifiers19 = self.line_virtual_modifiers()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_virtual_modifiers19.tree)
                    char_literal20 = self.input.LT(1)
                    self.match(self.input, 33, self.FOLLOW_33_in_mapMaterial291)



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
    # XKBGrammar.g:82:1: line_include : 'include' DQSTRING -> ^( TOKEN_INCLUDE DQSTRING ) ;
    def line_include(self, ):

        retval = self.line_include_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal21 = None
        DQSTRING22 = None

        string_literal21_tree = None
        DQSTRING22_tree = None
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")
        stream_34 = RewriteRuleTokenStream(self.adaptor, "token 34")

        try:
            try:
                # XKBGrammar.g:83:2: ( 'include' DQSTRING -> ^( TOKEN_INCLUDE DQSTRING ) )
                # XKBGrammar.g:83:4: 'include' DQSTRING
                string_literal21 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_line_include304) 
                stream_34.add(string_literal21)
                DQSTRING22 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_include306) 
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
                # 84:2: -> ^( TOKEN_INCLUDE DQSTRING )
                # XKBGrammar.g:84:5: ^( TOKEN_INCLUDE DQSTRING )
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
    # XKBGrammar.g:87:1: line_name : 'name' '[' n1= NAME ']' '=' n2= DQSTRING -> ^( TOKEN_NAME $n1 ^( VALUE $n2) ) ;
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
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")

        try:
            try:
                # XKBGrammar.g:88:2: ( 'name' '[' n1= NAME ']' '=' n2= DQSTRING -> ^( TOKEN_NAME $n1 ^( VALUE $n2) ) )
                # XKBGrammar.g:88:4: 'name' '[' n1= NAME ']' '=' n2= DQSTRING
                string_literal23 = self.input.LT(1)
                self.match(self.input, 35, self.FOLLOW_35_in_line_name326) 
                stream_35.add(string_literal23)
                char_literal24 = self.input.LT(1)
                self.match(self.input, 36, self.FOLLOW_36_in_line_name328) 
                stream_36.add(char_literal24)
                n1 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_name332) 
                stream_NAME.add(n1)
                char_literal25 = self.input.LT(1)
                self.match(self.input, 37, self.FOLLOW_37_in_line_name334) 
                stream_37.add(char_literal25)
                char_literal26 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_line_name336) 
                stream_38.add(char_literal26)
                n2 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_name340) 
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
                # 89:2: -> ^( TOKEN_NAME $n1 ^( VALUE $n2) )
                # XKBGrammar.g:89:5: ^( TOKEN_NAME $n1 ^( VALUE $n2) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_NAME, "TOKEN_NAME"), root_1)

                self.adaptor.addChild(root_1, stream_n1.nextNode())
                # XKBGrammar.g:89:22: ^( VALUE $n2)
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
    # XKBGrammar.g:92:1: line_keytype : 'key.type' '[' n1= NAME ']' '=' n2= DQSTRING -> ^( TOKEN_KEY_TYPE $n1 ^( VALUE $n2) ) ;
    def line_keytype(self, ):

        retval = self.line_keytype_return()
        retval.start = self.input.LT(1)

        root_0 = None

        n1 = None
        n2 = None
        string_literal27 = None
        char_literal28 = None
        char_literal29 = None
        char_literal30 = None

        n1_tree = None
        n2_tree = None
        string_literal27_tree = None
        char_literal28_tree = None
        char_literal29_tree = None
        char_literal30_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")
        stream_36 = RewriteRuleTokenStream(self.adaptor, "token 36")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")

        try:
            try:
                # XKBGrammar.g:93:2: ( 'key.type' '[' n1= NAME ']' '=' n2= DQSTRING -> ^( TOKEN_KEY_TYPE $n1 ^( VALUE $n2) ) )
                # XKBGrammar.g:93:4: 'key.type' '[' n1= NAME ']' '=' n2= DQSTRING
                string_literal27 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_line_keytype368) 
                stream_39.add(string_literal27)
                char_literal28 = self.input.LT(1)
                self.match(self.input, 36, self.FOLLOW_36_in_line_keytype370) 
                stream_36.add(char_literal28)
                n1 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype374) 
                stream_NAME.add(n1)
                char_literal29 = self.input.LT(1)
                self.match(self.input, 37, self.FOLLOW_37_in_line_keytype376) 
                stream_37.add(char_literal29)
                char_literal30 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_line_keytype378) 
                stream_38.add(char_literal30)
                n2 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_keytype382) 
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
                # 94:2: -> ^( TOKEN_KEY_TYPE $n1 ^( VALUE $n2) )
                # XKBGrammar.g:94:5: ^( TOKEN_KEY_TYPE $n1 ^( VALUE $n2) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_KEY_TYPE, "TOKEN_KEY_TYPE"), root_1)

                self.adaptor.addChild(root_1, stream_n1.nextNode())
                # XKBGrammar.g:94:26: ^( VALUE $n2)
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
    # XKBGrammar.g:97:1: line_key : (override= 'override' )? 'key' keycode keysyms -> ^( TOKEN_KEY ( ^( OVERRIDE $override) )? keycode keysyms ) ;
    def line_key(self, ):

        retval = self.line_key_return()
        retval.start = self.input.LT(1)

        root_0 = None

        override = None
        string_literal31 = None
        keycode32 = None

        keysyms33 = None


        override_tree = None
        string_literal31_tree = None
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_40 = RewriteRuleTokenStream(self.adaptor, "token 40")
        stream_keysyms = RewriteRuleSubtreeStream(self.adaptor, "rule keysyms")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        try:
            try:
                # XKBGrammar.g:98:2: ( (override= 'override' )? 'key' keycode keysyms -> ^( TOKEN_KEY ( ^( OVERRIDE $override) )? keycode keysyms ) )
                # XKBGrammar.g:98:4: (override= 'override' )? 'key' keycode keysyms
                # XKBGrammar.g:98:12: (override= 'override' )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 40) :
                    alt5 = 1
                if alt5 == 1:
                    # XKBGrammar.g:98:12: override= 'override'
                    override = self.input.LT(1)
                    self.match(self.input, 40, self.FOLLOW_40_in_line_key412) 
                    stream_40.add(override)




                string_literal31 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_line_key415) 
                stream_41.add(string_literal31)
                self._state.following.append(self.FOLLOW_keycode_in_line_key417)
                keycode32 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode32.tree)
                self._state.following.append(self.FOLLOW_keysyms_in_line_key419)
                keysyms33 = self.keysyms()

                self._state.following.pop()
                stream_keysyms.add(keysyms33.tree)
                # AST Rewrite
                # elements: override, keysyms, keycode
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
                # 99:2: -> ^( TOKEN_KEY ( ^( OVERRIDE $override) )? keycode keysyms )
                # XKBGrammar.g:99:5: ^( TOKEN_KEY ( ^( OVERRIDE $override) )? keycode keysyms )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_KEY, "TOKEN_KEY"), root_1)

                # XKBGrammar.g:99:17: ( ^( OVERRIDE $override) )?
                if stream_override.hasNext():
                    # XKBGrammar.g:99:17: ^( OVERRIDE $override)
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
    # XKBGrammar.g:102:1: line_modifier_map : 'modifier_map' state '{' keycode ( ',' keycode )* '}' -> ^( TOKEN_MODIFIER_MAP state ( keycode )+ ) ;
    def line_modifier_map(self, ):

        retval = self.line_modifier_map_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal34 = None
        char_literal36 = None
        char_literal38 = None
        char_literal40 = None
        state35 = None

        keycode37 = None

        keycode39 = None


        string_literal34_tree = None
        char_literal36_tree = None
        char_literal38_tree = None
        char_literal40_tree = None
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_42 = RewriteRuleTokenStream(self.adaptor, "token 42")
        stream_32 = RewriteRuleTokenStream(self.adaptor, "token 32")
        stream_31 = RewriteRuleTokenStream(self.adaptor, "token 31")
        stream_state = RewriteRuleSubtreeStream(self.adaptor, "rule state")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        try:
            try:
                # XKBGrammar.g:103:2: ( 'modifier_map' state '{' keycode ( ',' keycode )* '}' -> ^( TOKEN_MODIFIER_MAP state ( keycode )+ ) )
                # XKBGrammar.g:103:4: 'modifier_map' state '{' keycode ( ',' keycode )* '}'
                string_literal34 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_line_modifier_map449) 
                stream_42.add(string_literal34)
                self._state.following.append(self.FOLLOW_state_in_line_modifier_map451)
                state35 = self.state()

                self._state.following.pop()
                stream_state.add(state35.tree)
                char_literal36 = self.input.LT(1)
                self.match(self.input, 31, self.FOLLOW_31_in_line_modifier_map453) 
                stream_31.add(char_literal36)
                self._state.following.append(self.FOLLOW_keycode_in_line_modifier_map455)
                keycode37 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode37.tree)
                # XKBGrammar.g:103:37: ( ',' keycode )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == 43) :
                        alt6 = 1


                    if alt6 == 1:
                        # XKBGrammar.g:103:38: ',' keycode
                        char_literal38 = self.input.LT(1)
                        self.match(self.input, 43, self.FOLLOW_43_in_line_modifier_map458) 
                        stream_43.add(char_literal38)
                        self._state.following.append(self.FOLLOW_keycode_in_line_modifier_map460)
                        keycode39 = self.keycode()

                        self._state.following.pop()
                        stream_keycode.add(keycode39.tree)



                    else:
                        break #loop6


                char_literal40 = self.input.LT(1)
                self.match(self.input, 32, self.FOLLOW_32_in_line_modifier_map464) 
                stream_32.add(char_literal40)
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
                # 104:2: -> ^( TOKEN_MODIFIER_MAP state ( keycode )+ )
                # XKBGrammar.g:104:5: ^( TOKEN_MODIFIER_MAP state ( keycode )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_MODIFIER_MAP, "TOKEN_MODIFIER_MAP"), root_1)

                self.adaptor.addChild(root_1, stream_state.nextTree())
                # XKBGrammar.g:104:32: ( keycode )+
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
    # XKBGrammar.g:107:1: line_virtual_modifiers : 'virtual_modifiers' NAME ( ',' NAME )* -> ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ ) ;
    def line_virtual_modifiers(self, ):

        retval = self.line_virtual_modifiers_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal41 = None
        NAME42 = None
        char_literal43 = None
        NAME44 = None

        string_literal41_tree = None
        NAME42_tree = None
        char_literal43_tree = None
        NAME44_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_44 = RewriteRuleTokenStream(self.adaptor, "token 44")

        try:
            try:
                # XKBGrammar.g:108:2: ( 'virtual_modifiers' NAME ( ',' NAME )* -> ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ ) )
                # XKBGrammar.g:108:4: 'virtual_modifiers' NAME ( ',' NAME )*
                string_literal41 = self.input.LT(1)
                self.match(self.input, 44, self.FOLLOW_44_in_line_virtual_modifiers487) 
                stream_44.add(string_literal41)
                NAME42 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_virtual_modifiers489) 
                stream_NAME.add(NAME42)
                # XKBGrammar.g:108:29: ( ',' NAME )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 43) :
                        alt7 = 1


                    if alt7 == 1:
                        # XKBGrammar.g:108:30: ',' NAME
                        char_literal43 = self.input.LT(1)
                        self.match(self.input, 43, self.FOLLOW_43_in_line_virtual_modifiers492) 
                        stream_43.add(char_literal43)
                        NAME44 = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_line_virtual_modifiers494) 
                        stream_NAME.add(NAME44)



                    else:
                        break #loop7


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
                # 109:2: -> ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ )
                # XKBGrammar.g:109:5: ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_VIRTUAL_MODIFIERS, "TOKEN_VIRTUAL_MODIFIERS"), root_1)

                # XKBGrammar.g:109:31: ( NAME )+
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
    # XKBGrammar.g:112:1: keycode : ( NAME -> ^( KEYCODE NAME ) | '<' NAME '>' -> ^( KEYCODEX NAME ) );
    def keycode(self, ):

        retval = self.keycode_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME45 = None
        char_literal46 = None
        NAME47 = None
        char_literal48 = None

        NAME45_tree = None
        char_literal46_tree = None
        NAME47_tree = None
        char_literal48_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_45 = RewriteRuleTokenStream(self.adaptor, "token 45")
        stream_46 = RewriteRuleTokenStream(self.adaptor, "token 46")

        try:
            try:
                # XKBGrammar.g:113:2: ( NAME -> ^( KEYCODE NAME ) | '<' NAME '>' -> ^( KEYCODEX NAME ) )
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == NAME) :
                    alt8 = 1
                elif (LA8_0 == 45) :
                    alt8 = 2
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # XKBGrammar.g:113:4: NAME
                    NAME45 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode518) 
                    stream_NAME.add(NAME45)
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
                    # 113:9: -> ^( KEYCODE NAME )
                    # XKBGrammar.g:113:12: ^( KEYCODE NAME )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYCODE, "KEYCODE"), root_1)

                    self.adaptor.addChild(root_1, stream_NAME.nextNode())

                    self.adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                elif alt8 == 2:
                    # XKBGrammar.g:114:4: '<' NAME '>'
                    char_literal46 = self.input.LT(1)
                    self.match(self.input, 45, self.FOLLOW_45_in_keycode531) 
                    stream_45.add(char_literal46)
                    NAME47 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode533) 
                    stream_NAME.add(NAME47)
                    char_literal48 = self.input.LT(1)
                    self.match(self.input, 46, self.FOLLOW_46_in_keycode535) 
                    stream_46.add(char_literal48)
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
                    # 114:17: -> ^( KEYCODEX NAME )
                    # XKBGrammar.g:114:20: ^( KEYCODEX NAME )
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
    # XKBGrammar.g:117:1: keysyms : '{' ( 'type' '[' tn1= NAME ']' '=' tn2= DQSTRING ',' )* keysymgroup ( ',' keysymgroup )* '}' -> ^( KEYSYMS ( ^( TOKEN_TYPE $tn1 $tn2) )* ( keysymgroup )+ ) ;
    def keysyms(self, ):

        retval = self.keysyms_return()
        retval.start = self.input.LT(1)

        root_0 = None

        tn1 = None
        tn2 = None
        char_literal49 = None
        string_literal50 = None
        char_literal51 = None
        char_literal52 = None
        char_literal53 = None
        char_literal54 = None
        char_literal56 = None
        char_literal58 = None
        keysymgroup55 = None

        keysymgroup57 = None


        tn1_tree = None
        tn2_tree = None
        char_literal49_tree = None
        string_literal50_tree = None
        char_literal51_tree = None
        char_literal52_tree = None
        char_literal53_tree = None
        char_literal54_tree = None
        char_literal56_tree = None
        char_literal58_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_47 = RewriteRuleTokenStream(self.adaptor, "token 47")
        stream_32 = RewriteRuleTokenStream(self.adaptor, "token 32")
        stream_31 = RewriteRuleTokenStream(self.adaptor, "token 31")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")
        stream_36 = RewriteRuleTokenStream(self.adaptor, "token 36")
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")
        stream_keysymgroup = RewriteRuleSubtreeStream(self.adaptor, "rule keysymgroup")
        try:
            try:
                # XKBGrammar.g:118:2: ( '{' ( 'type' '[' tn1= NAME ']' '=' tn2= DQSTRING ',' )* keysymgroup ( ',' keysymgroup )* '}' -> ^( KEYSYMS ( ^( TOKEN_TYPE $tn1 $tn2) )* ( keysymgroup )+ ) )
                # XKBGrammar.g:118:4: '{' ( 'type' '[' tn1= NAME ']' '=' tn2= DQSTRING ',' )* keysymgroup ( ',' keysymgroup )* '}'
                char_literal49 = self.input.LT(1)
                self.match(self.input, 31, self.FOLLOW_31_in_keysyms554) 
                stream_31.add(char_literal49)
                # XKBGrammar.g:118:8: ( 'type' '[' tn1= NAME ']' '=' tn2= DQSTRING ',' )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 47) :
                        alt9 = 1


                    if alt9 == 1:
                        # XKBGrammar.g:118:9: 'type' '[' tn1= NAME ']' '=' tn2= DQSTRING ','
                        string_literal50 = self.input.LT(1)
                        self.match(self.input, 47, self.FOLLOW_47_in_keysyms557) 
                        stream_47.add(string_literal50)
                        char_literal51 = self.input.LT(1)
                        self.match(self.input, 36, self.FOLLOW_36_in_keysyms559) 
                        stream_36.add(char_literal51)
                        tn1 = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_keysyms563) 
                        stream_NAME.add(tn1)
                        char_literal52 = self.input.LT(1)
                        self.match(self.input, 37, self.FOLLOW_37_in_keysyms565) 
                        stream_37.add(char_literal52)
                        char_literal53 = self.input.LT(1)
                        self.match(self.input, 38, self.FOLLOW_38_in_keysyms567) 
                        stream_38.add(char_literal53)
                        tn2 = self.input.LT(1)
                        self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_keysyms571) 
                        stream_DQSTRING.add(tn2)
                        char_literal54 = self.input.LT(1)
                        self.match(self.input, 43, self.FOLLOW_43_in_keysyms573) 
                        stream_43.add(char_literal54)



                    else:
                        break #loop9


                self._state.following.append(self.FOLLOW_keysymgroup_in_keysyms577)
                keysymgroup55 = self.keysymgroup()

                self._state.following.pop()
                stream_keysymgroup.add(keysymgroup55.tree)
                # XKBGrammar.g:118:68: ( ',' keysymgroup )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == 43) :
                        alt10 = 1


                    if alt10 == 1:
                        # XKBGrammar.g:118:69: ',' keysymgroup
                        char_literal56 = self.input.LT(1)
                        self.match(self.input, 43, self.FOLLOW_43_in_keysyms580) 
                        stream_43.add(char_literal56)
                        self._state.following.append(self.FOLLOW_keysymgroup_in_keysyms582)
                        keysymgroup57 = self.keysymgroup()

                        self._state.following.pop()
                        stream_keysymgroup.add(keysymgroup57.tree)



                    else:
                        break #loop10


                char_literal58 = self.input.LT(1)
                self.match(self.input, 32, self.FOLLOW_32_in_keysyms586) 
                stream_32.add(char_literal58)
                # AST Rewrite
                # elements: keysymgroup, tn2, tn1
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
                # 119:2: -> ^( KEYSYMS ( ^( TOKEN_TYPE $tn1 $tn2) )* ( keysymgroup )+ )
                # XKBGrammar.g:119:5: ^( KEYSYMS ( ^( TOKEN_TYPE $tn1 $tn2) )* ( keysymgroup )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYSYMS, "KEYSYMS"), root_1)

                # XKBGrammar.g:119:15: ( ^( TOKEN_TYPE $tn1 $tn2) )*
                while stream_tn2.hasNext() or stream_tn1.hasNext():
                    # XKBGrammar.g:119:15: ^( TOKEN_TYPE $tn1 $tn2)
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_TYPE, "TOKEN_TYPE"), root_2)

                    self.adaptor.addChild(root_2, stream_tn1.nextNode())
                    self.adaptor.addChild(root_2, stream_tn2.nextNode())

                    self.adaptor.addChild(root_1, root_2)


                stream_tn2.reset();
                stream_tn1.reset();
                # XKBGrammar.g:119:40: ( keysymgroup )+
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
    # XKBGrammar.g:122:1: keysymgroup : ( 'symbols' '[' st1= NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']' -> ^( KEYSYMGROUP ( ^( TOKEN_SYMBOL $st1) )? ( $keysym)+ ) ;
    def keysymgroup(self, ):

        retval = self.keysymgroup_return()
        retval.start = self.input.LT(1)

        root_0 = None

        st1 = None
        string_literal59 = None
        char_literal60 = None
        char_literal61 = None
        char_literal62 = None
        char_literal63 = None
        char_literal64 = None
        char_literal65 = None
        keysym = None
        list_keysym = None

        st1_tree = None
        string_literal59_tree = None
        char_literal60_tree = None
        char_literal61_tree = None
        char_literal62_tree = None
        char_literal63_tree = None
        char_literal64_tree = None
        char_literal65_tree = None
        keysym_tree = None
        stream_48 = RewriteRuleTokenStream(self.adaptor, "token 48")
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_36 = RewriteRuleTokenStream(self.adaptor, "token 36")
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")

        try:
            try:
                # XKBGrammar.g:123:2: ( ( 'symbols' '[' st1= NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']' -> ^( KEYSYMGROUP ( ^( TOKEN_SYMBOL $st1) )? ( $keysym)+ ) )
                # XKBGrammar.g:123:4: ( 'symbols' '[' st1= NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']'
                # XKBGrammar.g:123:4: ( 'symbols' '[' st1= NAME ']' '=' )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == 48) :
                    alt11 = 1
                if alt11 == 1:
                    # XKBGrammar.g:123:5: 'symbols' '[' st1= NAME ']' '='
                    string_literal59 = self.input.LT(1)
                    self.match(self.input, 48, self.FOLLOW_48_in_keysymgroup619) 
                    stream_48.add(string_literal59)
                    char_literal60 = self.input.LT(1)
                    self.match(self.input, 36, self.FOLLOW_36_in_keysymgroup621) 
                    stream_36.add(char_literal60)
                    st1 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keysymgroup625) 
                    stream_NAME.add(st1)
                    char_literal61 = self.input.LT(1)
                    self.match(self.input, 37, self.FOLLOW_37_in_keysymgroup627) 
                    stream_37.add(char_literal61)
                    char_literal62 = self.input.LT(1)
                    self.match(self.input, 38, self.FOLLOW_38_in_keysymgroup629) 
                    stream_38.add(char_literal62)




                char_literal63 = self.input.LT(1)
                self.match(self.input, 36, self.FOLLOW_36_in_keysymgroup633) 
                stream_36.add(char_literal63)
                keysym = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_keysymgroup637) 
                stream_NAME.add(keysym)
                if list_keysym is None:
                    list_keysym = []
                list_keysym.append(keysym)

                # XKBGrammar.g:123:55: ( ',' keysym+= NAME )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == 43) :
                        alt12 = 1


                    if alt12 == 1:
                        # XKBGrammar.g:123:56: ',' keysym+= NAME
                        char_literal64 = self.input.LT(1)
                        self.match(self.input, 43, self.FOLLOW_43_in_keysymgroup640) 
                        stream_43.add(char_literal64)
                        keysym = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_keysymgroup644) 
                        stream_NAME.add(keysym)
                        if list_keysym is None:
                            list_keysym = []
                        list_keysym.append(keysym)




                    else:
                        break #loop12


                char_literal65 = self.input.LT(1)
                self.match(self.input, 37, self.FOLLOW_37_in_keysymgroup648) 
                stream_37.add(char_literal65)
                # AST Rewrite
                # elements: keysym, st1
                # token labels: st1
                # rule labels: retval
                # token list labels: keysym
                # rule list labels: 

                retval.tree = root_0
                stream_st1 = RewriteRuleTokenStream(self.adaptor, "token st1", st1)
                stream_keysym = RewriteRuleTokenStream(self.adaptor, "token keysym", list_keysym)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                root_0 = self.adaptor.nil()
                # 124:2: -> ^( KEYSYMGROUP ( ^( TOKEN_SYMBOL $st1) )? ( $keysym)+ )
                # XKBGrammar.g:124:5: ^( KEYSYMGROUP ( ^( TOKEN_SYMBOL $st1) )? ( $keysym)+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYSYMGROUP, "KEYSYMGROUP"), root_1)

                # XKBGrammar.g:124:19: ( ^( TOKEN_SYMBOL $st1) )?
                if stream_st1.hasNext():
                    # XKBGrammar.g:124:19: ^( TOKEN_SYMBOL $st1)
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_SYMBOL, "TOKEN_SYMBOL"), root_2)

                    self.adaptor.addChild(root_2, stream_st1.nextNode())

                    self.adaptor.addChild(root_1, root_2)


                stream_st1.reset();
                # XKBGrammar.g:124:41: ( $keysym)+
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

    class virtualmods_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start virtualmods
    # XKBGrammar.g:127:1: virtualmods : 'virtualMods' '=' NAME -> ^( VIRTUALMODS NAME ) ;
    def virtualmods(self, ):

        retval = self.virtualmods_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal66 = None
        char_literal67 = None
        NAME68 = None

        string_literal66_tree = None
        char_literal67_tree = None
        NAME68_tree = None
        stream_49 = RewriteRuleTokenStream(self.adaptor, "token 49")
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")

        try:
            try:
                # XKBGrammar.g:128:2: ( 'virtualMods' '=' NAME -> ^( VIRTUALMODS NAME ) )
                # XKBGrammar.g:128:4: 'virtualMods' '=' NAME
                string_literal66 = self.input.LT(1)
                self.match(self.input, 49, self.FOLLOW_49_in_virtualmods678) 
                stream_49.add(string_literal66)
                char_literal67 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_virtualmods680) 
                stream_38.add(char_literal67)
                NAME68 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_virtualmods682) 
                stream_NAME.add(NAME68)
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
                # 129:2: -> ^( VIRTUALMODS NAME )
                # XKBGrammar.g:129:5: ^( VIRTUALMODS NAME )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VIRTUALMODS, "VIRTUALMODS"), root_1)

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

    # $ANTLR end virtualmods

    class mapOptions_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start mapOptions
    # XKBGrammar.g:132:1: mapOptions : ( 'default' | 'hidden' | 'partial' | 'alphanumeric_keys' | 'keypad_keys' | 'function_keys' | 'modifier_keys' | 'alternate_group' | 'xkb_symbols' );
    def mapOptions(self, ):

        retval = self.mapOptions_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set69 = None

        set69_tree = None

        try:
            try:
                # XKBGrammar.g:133:2: ( 'default' | 'hidden' | 'partial' | 'alphanumeric_keys' | 'keypad_keys' | 'function_keys' | 'modifier_keys' | 'alternate_group' | 'xkb_symbols' )
                # XKBGrammar.g:
                root_0 = self.adaptor.nil()

                set69 = self.input.LT(1)
                if (50 <= self.input.LA(1) <= 58):
                    self.input.consume();
                    self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set69))
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
    # XKBGrammar.g:144:1: state : ( 'Shift' | 'Control' | 'Lock' | 'Mod1' | 'Mod2' | 'Mod3' | 'Mod4' | 'Mod5' );
    def state(self, ):

        retval = self.state_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set70 = None

        set70_tree = None

        try:
            try:
                # XKBGrammar.g:145:2: ( 'Shift' | 'Control' | 'Lock' | 'Mod1' | 'Mod2' | 'Mod3' | 'Mod4' | 'Mod5' )
                # XKBGrammar.g:
                root_0 = self.adaptor.nil()

                set70 = self.input.LT(1)
                if (59 <= self.input.LA(1) <= 66):
                    self.input.consume();
                    self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set70))
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


 

    FOLLOW_symbols_in_layout153 = frozenset([50, 51, 52, 53, 54, 55, 56, 57, 58])
    FOLLOW_EOF_in_layout156 = frozenset([1])
    FOLLOW_mapType_in_symbols179 = frozenset([31])
    FOLLOW_31_in_symbols181 = frozenset([34, 35, 39, 40, 41, 42, 44])
    FOLLOW_mapMaterial_in_symbols183 = frozenset([32, 34, 35, 39, 40, 41, 42, 44])
    FOLLOW_32_in_symbols186 = frozenset([33])
    FOLLOW_33_in_symbols188 = frozenset([1])
    FOLLOW_mapOptions_in_mapType216 = frozenset([26, 50, 51, 52, 53, 54, 55, 56, 57, 58])
    FOLLOW_DQSTRING_in_mapType219 = frozenset([1])
    FOLLOW_line_include_in_mapMaterial251 = frozenset([1])
    FOLLOW_line_name_in_mapMaterial257 = frozenset([33])
    FOLLOW_33_in_mapMaterial259 = frozenset([1])
    FOLLOW_line_keytype_in_mapMaterial265 = frozenset([33])
    FOLLOW_33_in_mapMaterial267 = frozenset([1])
    FOLLOW_line_key_in_mapMaterial273 = frozenset([33])
    FOLLOW_33_in_mapMaterial275 = frozenset([1])
    FOLLOW_line_modifier_map_in_mapMaterial281 = frozenset([33])
    FOLLOW_33_in_mapMaterial283 = frozenset([1])
    FOLLOW_line_virtual_modifiers_in_mapMaterial289 = frozenset([33])
    FOLLOW_33_in_mapMaterial291 = frozenset([1])
    FOLLOW_34_in_line_include304 = frozenset([26])
    FOLLOW_DQSTRING_in_line_include306 = frozenset([1])
    FOLLOW_35_in_line_name326 = frozenset([36])
    FOLLOW_36_in_line_name328 = frozenset([27])
    FOLLOW_NAME_in_line_name332 = frozenset([37])
    FOLLOW_37_in_line_name334 = frozenset([38])
    FOLLOW_38_in_line_name336 = frozenset([26])
    FOLLOW_DQSTRING_in_line_name340 = frozenset([1])
    FOLLOW_39_in_line_keytype368 = frozenset([36])
    FOLLOW_36_in_line_keytype370 = frozenset([27])
    FOLLOW_NAME_in_line_keytype374 = frozenset([37])
    FOLLOW_37_in_line_keytype376 = frozenset([38])
    FOLLOW_38_in_line_keytype378 = frozenset([26])
    FOLLOW_DQSTRING_in_line_keytype382 = frozenset([1])
    FOLLOW_40_in_line_key412 = frozenset([41])
    FOLLOW_41_in_line_key415 = frozenset([27, 45])
    FOLLOW_keycode_in_line_key417 = frozenset([31])
    FOLLOW_keysyms_in_line_key419 = frozenset([1])
    FOLLOW_42_in_line_modifier_map449 = frozenset([59, 60, 61, 62, 63, 64, 65, 66])
    FOLLOW_state_in_line_modifier_map451 = frozenset([31])
    FOLLOW_31_in_line_modifier_map453 = frozenset([27, 45])
    FOLLOW_keycode_in_line_modifier_map455 = frozenset([32, 43])
    FOLLOW_43_in_line_modifier_map458 = frozenset([27, 45])
    FOLLOW_keycode_in_line_modifier_map460 = frozenset([32, 43])
    FOLLOW_32_in_line_modifier_map464 = frozenset([1])
    FOLLOW_44_in_line_virtual_modifiers487 = frozenset([27])
    FOLLOW_NAME_in_line_virtual_modifiers489 = frozenset([1, 43])
    FOLLOW_43_in_line_virtual_modifiers492 = frozenset([27])
    FOLLOW_NAME_in_line_virtual_modifiers494 = frozenset([1, 43])
    FOLLOW_NAME_in_keycode518 = frozenset([1])
    FOLLOW_45_in_keycode531 = frozenset([27])
    FOLLOW_NAME_in_keycode533 = frozenset([46])
    FOLLOW_46_in_keycode535 = frozenset([1])
    FOLLOW_31_in_keysyms554 = frozenset([36, 47, 48])
    FOLLOW_47_in_keysyms557 = frozenset([36])
    FOLLOW_36_in_keysyms559 = frozenset([27])
    FOLLOW_NAME_in_keysyms563 = frozenset([37])
    FOLLOW_37_in_keysyms565 = frozenset([38])
    FOLLOW_38_in_keysyms567 = frozenset([26])
    FOLLOW_DQSTRING_in_keysyms571 = frozenset([43])
    FOLLOW_43_in_keysyms573 = frozenset([36, 47, 48])
    FOLLOW_keysymgroup_in_keysyms577 = frozenset([32, 43])
    FOLLOW_43_in_keysyms580 = frozenset([36, 47, 48])
    FOLLOW_keysymgroup_in_keysyms582 = frozenset([32, 43])
    FOLLOW_32_in_keysyms586 = frozenset([1])
    FOLLOW_48_in_keysymgroup619 = frozenset([36])
    FOLLOW_36_in_keysymgroup621 = frozenset([27])
    FOLLOW_NAME_in_keysymgroup625 = frozenset([37])
    FOLLOW_37_in_keysymgroup627 = frozenset([38])
    FOLLOW_38_in_keysymgroup629 = frozenset([36])
    FOLLOW_36_in_keysymgroup633 = frozenset([27])
    FOLLOW_NAME_in_keysymgroup637 = frozenset([37, 43])
    FOLLOW_43_in_keysymgroup640 = frozenset([27])
    FOLLOW_NAME_in_keysymgroup644 = frozenset([37, 43])
    FOLLOW_37_in_keysymgroup648 = frozenset([1])
    FOLLOW_49_in_virtualmods678 = frozenset([38])
    FOLLOW_38_in_virtualmods680 = frozenset([27])
    FOLLOW_NAME_in_virtualmods682 = frozenset([1])
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
