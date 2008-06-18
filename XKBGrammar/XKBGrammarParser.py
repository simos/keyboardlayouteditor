# $ANTLR 3.1b1 XKBGrammar.g 2008-06-18 23:27:42

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
MAPOPTIONS=16
OVERLAY=27
TOKEN_INCLUDE=4
ELEM_VIRTUALMODS=24
ELEM_KEYSYMS=23
TOKEN_MODIFIER_MAP=9
EOF=-1
TOKEN_TYPE=8
MAPTYPE=14
TOKEN_VIRTUAL_MODIFIERS=11
NAME=30
T__51=51
MAPMATERIAL=17
MAPOPTS=28
COMMENT=32
DQSTRING=29
T__50=50
T__42=42
T__43=43
T__40=40
STATE=21
T__41=41
T__46=46
T__47=47
T__44=44
T__45=45
LINE_COMMENT=33
KEYCODE=18
T__48=48
T__49=49
TOKEN_NAME=6
VALUE=20
LAYOUT=12
WS=31
T__34=34
T__35=35
T__36=36
T__37=37
OVERRIDE=26
T__38=38
T__39=39
TOKEN_SYMBOL=10
ELEM_KEYSYMGROUP=22
TOKEN_KEY=7
MAPNAME=15
SYMBOLS=13
KEYELEMENTS=25
TOKEN_KEY_TYPE=5
KEYCODEX=19

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "TOKEN_INCLUDE", "TOKEN_KEY_TYPE", "TOKEN_NAME", "TOKEN_KEY", "TOKEN_TYPE", 
    "TOKEN_MODIFIER_MAP", "TOKEN_SYMBOL", "TOKEN_VIRTUAL_MODIFIERS", "LAYOUT", 
    "SYMBOLS", "MAPTYPE", "MAPNAME", "MAPOPTIONS", "MAPMATERIAL", "KEYCODE", 
    "KEYCODEX", "VALUE", "STATE", "ELEM_KEYSYMGROUP", "ELEM_KEYSYMS", "ELEM_VIRTUALMODS", 
    "KEYELEMENTS", "OVERRIDE", "OVERLAY", "MAPOPTS", "DQSTRING", "NAME", 
    "WS", "COMMENT", "LINE_COMMENT", "'{'", "'}'", "';'", "'include'", "'name'", 
    "'['", "']'", "'='", "'key.type'", "'key'", "','", "'modifier_map'", 
    "'virtual_modifiers'", "'<'", "'>'", "'type'", "'symbols'", "'virtualMods'"
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
    # XKBGrammar.g:60:1: layout : ( symbols )+ EOF -> ^( LAYOUT ( symbols )+ ) ;
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
                # XKBGrammar.g:61:2: ( ( symbols )+ EOF -> ^( LAYOUT ( symbols )+ ) )
                # XKBGrammar.g:61:4: ( symbols )+ EOF
                # XKBGrammar.g:61:4: ( symbols )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == MAPOPTS) :
                        alt1 = 1


                    if alt1 == 1:
                        # XKBGrammar.g:61:4: symbols
                        self._state.following.append(self.FOLLOW_symbols_in_layout161)
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
                self.match(self.input, EOF, self.FOLLOW_EOF_in_layout164) 
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
                # 62:2: -> ^( LAYOUT ( symbols )+ )
                # XKBGrammar.g:62:5: ^( LAYOUT ( symbols )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(LAYOUT, "LAYOUT"), root_1)

                # XKBGrammar.g:62:14: ( symbols )+
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
    # XKBGrammar.g:65:1: symbols : mapType '{' ( mapMaterial )+ '}' ';' -> ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) ) ;
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
        stream_35 = RewriteRuleTokenStream(self.adaptor, "token 35")
        stream_36 = RewriteRuleTokenStream(self.adaptor, "token 36")
        stream_34 = RewriteRuleTokenStream(self.adaptor, "token 34")
        stream_mapMaterial = RewriteRuleSubtreeStream(self.adaptor, "rule mapMaterial")
        stream_mapType = RewriteRuleSubtreeStream(self.adaptor, "rule mapType")
        try:
            try:
                # XKBGrammar.g:66:2: ( mapType '{' ( mapMaterial )+ '}' ';' -> ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) ) )
                # XKBGrammar.g:66:4: mapType '{' ( mapMaterial )+ '}' ';'
                self._state.following.append(self.FOLLOW_mapType_in_symbols187)
                mapType3 = self.mapType()

                self._state.following.pop()
                stream_mapType.add(mapType3.tree)
                char_literal4 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_symbols189) 
                stream_34.add(char_literal4)
                # XKBGrammar.g:66:16: ( mapMaterial )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == OVERRIDE or (37 <= LA2_0 <= 38) or (42 <= LA2_0 <= 43) or (45 <= LA2_0 <= 46)) :
                        alt2 = 1


                    if alt2 == 1:
                        # XKBGrammar.g:66:16: mapMaterial
                        self._state.following.append(self.FOLLOW_mapMaterial_in_symbols191)
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
                self.match(self.input, 35, self.FOLLOW_35_in_symbols194) 
                stream_35.add(char_literal6)
                char_literal7 = self.input.LT(1)
                self.match(self.input, 36, self.FOLLOW_36_in_symbols196) 
                stream_36.add(char_literal7)
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
                # 67:2: -> ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) )
                # XKBGrammar.g:67:5: ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(SYMBOLS, "SYMBOLS"), root_1)

                self.adaptor.addChild(root_1, stream_mapType.nextTree())
                # XKBGrammar.g:67:23: ^( MAPMATERIAL ( mapMaterial )+ )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPMATERIAL, "MAPMATERIAL"), root_2)

                # XKBGrammar.g:67:37: ( mapMaterial )+
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
    # XKBGrammar.g:70:1: mapType : ( MAPOPTS )+ DQSTRING -> ^( MAPTYPE ^( MAPOPTIONS ( MAPOPTS )+ ) ^( MAPNAME DQSTRING ) ) ;
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
                # XKBGrammar.g:71:2: ( ( MAPOPTS )+ DQSTRING -> ^( MAPTYPE ^( MAPOPTIONS ( MAPOPTS )+ ) ^( MAPNAME DQSTRING ) ) )
                # XKBGrammar.g:71:4: ( MAPOPTS )+ DQSTRING
                # XKBGrammar.g:71:4: ( MAPOPTS )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == MAPOPTS) :
                        alt3 = 1


                    if alt3 == 1:
                        # XKBGrammar.g:71:4: MAPOPTS
                        MAPOPTS8 = self.input.LT(1)
                        self.match(self.input, MAPOPTS, self.FOLLOW_MAPOPTS_in_mapType224) 
                        stream_MAPOPTS.add(MAPOPTS8)



                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


                DQSTRING9 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_mapType227) 
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
                # 72:2: -> ^( MAPTYPE ^( MAPOPTIONS ( MAPOPTS )+ ) ^( MAPNAME DQSTRING ) )
                # XKBGrammar.g:72:5: ^( MAPTYPE ^( MAPOPTIONS ( MAPOPTS )+ ) ^( MAPNAME DQSTRING ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPTYPE, "MAPTYPE"), root_1)

                # XKBGrammar.g:72:15: ^( MAPOPTIONS ( MAPOPTS )+ )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPOPTIONS, "MAPOPTIONS"), root_2)

                # XKBGrammar.g:72:28: ( MAPOPTS )+
                if not (stream_MAPOPTS.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_MAPOPTS.hasNext():
                    self.adaptor.addChild(root_2, stream_MAPOPTS.nextNode())


                stream_MAPOPTS.reset()

                self.adaptor.addChild(root_1, root_2)
                # XKBGrammar.g:72:38: ^( MAPNAME DQSTRING )
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
    # XKBGrammar.g:75:1: mapMaterial : ( line_include | line_name ';' | line_keytype ';' | line_key ';' | line_modifier_map ';' | line_virtual_modifiers ';' );
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
                # XKBGrammar.g:76:2: ( line_include | line_name ';' | line_keytype ';' | line_key ';' | line_modifier_map ';' | line_virtual_modifiers ';' )
                alt4 = 6
                LA4 = self.input.LA(1)
                if LA4 == 37:
                    alt4 = 1
                elif LA4 == 38:
                    alt4 = 2
                elif LA4 == 42:
                    alt4 = 3
                elif LA4 == OVERRIDE or LA4 == 43:
                    alt4 = 4
                elif LA4 == 45:
                    alt4 = 5
                elif LA4 == 46:
                    alt4 = 6
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # XKBGrammar.g:76:4: line_include
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_include_in_mapMaterial259)
                    line_include10 = self.line_include()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_include10.tree)



                elif alt4 == 2:
                    # XKBGrammar.g:77:4: line_name ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_name_in_mapMaterial265)
                    line_name11 = self.line_name()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_name11.tree)
                    char_literal12 = self.input.LT(1)
                    self.match(self.input, 36, self.FOLLOW_36_in_mapMaterial267)



                elif alt4 == 3:
                    # XKBGrammar.g:78:4: line_keytype ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_keytype_in_mapMaterial273)
                    line_keytype13 = self.line_keytype()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_keytype13.tree)
                    char_literal14 = self.input.LT(1)
                    self.match(self.input, 36, self.FOLLOW_36_in_mapMaterial275)



                elif alt4 == 4:
                    # XKBGrammar.g:79:4: line_key ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_key_in_mapMaterial281)
                    line_key15 = self.line_key()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_key15.tree)
                    char_literal16 = self.input.LT(1)
                    self.match(self.input, 36, self.FOLLOW_36_in_mapMaterial283)



                elif alt4 == 5:
                    # XKBGrammar.g:80:4: line_modifier_map ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_modifier_map_in_mapMaterial289)
                    line_modifier_map17 = self.line_modifier_map()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_modifier_map17.tree)
                    char_literal18 = self.input.LT(1)
                    self.match(self.input, 36, self.FOLLOW_36_in_mapMaterial291)



                elif alt4 == 6:
                    # XKBGrammar.g:81:4: line_virtual_modifiers ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_virtual_modifiers_in_mapMaterial297)
                    line_virtual_modifiers19 = self.line_virtual_modifiers()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_virtual_modifiers19.tree)
                    char_literal20 = self.input.LT(1)
                    self.match(self.input, 36, self.FOLLOW_36_in_mapMaterial299)



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
    # XKBGrammar.g:84:1: line_include : 'include' DQSTRING -> ^( TOKEN_INCLUDE DQSTRING ) ;
    def line_include(self, ):

        retval = self.line_include_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal21 = None
        DQSTRING22 = None

        string_literal21_tree = None
        DQSTRING22_tree = None
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")

        try:
            try:
                # XKBGrammar.g:85:2: ( 'include' DQSTRING -> ^( TOKEN_INCLUDE DQSTRING ) )
                # XKBGrammar.g:85:4: 'include' DQSTRING
                string_literal21 = self.input.LT(1)
                self.match(self.input, 37, self.FOLLOW_37_in_line_include311) 
                stream_37.add(string_literal21)
                DQSTRING22 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_include313) 
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
                # 86:2: -> ^( TOKEN_INCLUDE DQSTRING )
                # XKBGrammar.g:86:5: ^( TOKEN_INCLUDE DQSTRING )
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
    # XKBGrammar.g:89:1: line_name : 'name' '[' NAME ']' '=' DQSTRING -> ^( TOKEN_NAME NAME ^( VALUE DQSTRING ) ) ;
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
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_40 = RewriteRuleTokenStream(self.adaptor, "token 40")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")

        try:
            try:
                # XKBGrammar.g:90:2: ( 'name' '[' NAME ']' '=' DQSTRING -> ^( TOKEN_NAME NAME ^( VALUE DQSTRING ) ) )
                # XKBGrammar.g:90:4: 'name' '[' NAME ']' '=' DQSTRING
                string_literal23 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_line_name333) 
                stream_38.add(string_literal23)
                char_literal24 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_line_name335) 
                stream_39.add(char_literal24)
                NAME25 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_name337) 
                stream_NAME.add(NAME25)
                char_literal26 = self.input.LT(1)
                self.match(self.input, 40, self.FOLLOW_40_in_line_name339) 
                stream_40.add(char_literal26)
                char_literal27 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_line_name341) 
                stream_41.add(char_literal27)
                DQSTRING28 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_name343) 
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
                # 91:2: -> ^( TOKEN_NAME NAME ^( VALUE DQSTRING ) )
                # XKBGrammar.g:91:5: ^( TOKEN_NAME NAME ^( VALUE DQSTRING ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_NAME, "TOKEN_NAME"), root_1)

                self.adaptor.addChild(root_1, stream_NAME.nextNode())
                # XKBGrammar.g:91:23: ^( VALUE DQSTRING )
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
    # XKBGrammar.g:94:1: line_keytype : 'key.type' ( '[' NAME ']' )? '=' DQSTRING -> ^( TOKEN_KEY_TYPE ( NAME )? ^( VALUE DQSTRING ) ) ;
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
        stream_42 = RewriteRuleTokenStream(self.adaptor, "token 42")
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_40 = RewriteRuleTokenStream(self.adaptor, "token 40")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")

        try:
            try:
                # XKBGrammar.g:95:2: ( 'key.type' ( '[' NAME ']' )? '=' DQSTRING -> ^( TOKEN_KEY_TYPE ( NAME )? ^( VALUE DQSTRING ) ) )
                # XKBGrammar.g:95:4: 'key.type' ( '[' NAME ']' )? '=' DQSTRING
                string_literal29 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_line_keytype369) 
                stream_42.add(string_literal29)
                # XKBGrammar.g:95:15: ( '[' NAME ']' )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 39) :
                    alt5 = 1
                if alt5 == 1:
                    # XKBGrammar.g:95:16: '[' NAME ']'
                    char_literal30 = self.input.LT(1)
                    self.match(self.input, 39, self.FOLLOW_39_in_line_keytype372) 
                    stream_39.add(char_literal30)
                    NAME31 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype374) 
                    stream_NAME.add(NAME31)
                    char_literal32 = self.input.LT(1)
                    self.match(self.input, 40, self.FOLLOW_40_in_line_keytype376) 
                    stream_40.add(char_literal32)




                char_literal33 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_line_keytype380) 
                stream_41.add(char_literal33)
                DQSTRING34 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_keytype382) 
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
                # 96:2: -> ^( TOKEN_KEY_TYPE ( NAME )? ^( VALUE DQSTRING ) )
                # XKBGrammar.g:96:5: ^( TOKEN_KEY_TYPE ( NAME )? ^( VALUE DQSTRING ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_KEY_TYPE, "TOKEN_KEY_TYPE"), root_1)

                # XKBGrammar.g:96:22: ( NAME )?
                if stream_NAME.hasNext():
                    self.adaptor.addChild(root_1, stream_NAME.nextNode())


                stream_NAME.reset();
                # XKBGrammar.g:96:28: ^( VALUE DQSTRING )
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
    # XKBGrammar.g:99:1: line_key : ( OVERRIDE )? 'key' keycode '{' keyelements ( ',' keyelements )* '}' -> ^( TOKEN_KEY ( OVERRIDE )? keycode ( keyelements )+ ) ;
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
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_44 = RewriteRuleTokenStream(self.adaptor, "token 44")
        stream_35 = RewriteRuleTokenStream(self.adaptor, "token 35")
        stream_OVERRIDE = RewriteRuleTokenStream(self.adaptor, "token OVERRIDE")
        stream_34 = RewriteRuleTokenStream(self.adaptor, "token 34")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        stream_keyelements = RewriteRuleSubtreeStream(self.adaptor, "rule keyelements")
        try:
            try:
                # XKBGrammar.g:100:2: ( ( OVERRIDE )? 'key' keycode '{' keyelements ( ',' keyelements )* '}' -> ^( TOKEN_KEY ( OVERRIDE )? keycode ( keyelements )+ ) )
                # XKBGrammar.g:100:4: ( OVERRIDE )? 'key' keycode '{' keyelements ( ',' keyelements )* '}'
                # XKBGrammar.g:100:4: ( OVERRIDE )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == OVERRIDE) :
                    alt6 = 1
                if alt6 == 1:
                    # XKBGrammar.g:100:4: OVERRIDE
                    OVERRIDE35 = self.input.LT(1)
                    self.match(self.input, OVERRIDE, self.FOLLOW_OVERRIDE_in_line_key409) 
                    stream_OVERRIDE.add(OVERRIDE35)




                string_literal36 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_line_key412) 
                stream_43.add(string_literal36)
                self._state.following.append(self.FOLLOW_keycode_in_line_key414)
                keycode37 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode37.tree)
                char_literal38 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_line_key416) 
                stream_34.add(char_literal38)
                self._state.following.append(self.FOLLOW_keyelements_in_line_key418)
                keyelements39 = self.keyelements()

                self._state.following.pop()
                stream_keyelements.add(keyelements39.tree)
                # XKBGrammar.g:100:44: ( ',' keyelements )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 44) :
                        alt7 = 1


                    if alt7 == 1:
                        # XKBGrammar.g:100:45: ',' keyelements
                        char_literal40 = self.input.LT(1)
                        self.match(self.input, 44, self.FOLLOW_44_in_line_key421) 
                        stream_44.add(char_literal40)
                        self._state.following.append(self.FOLLOW_keyelements_in_line_key423)
                        keyelements41 = self.keyelements()

                        self._state.following.pop()
                        stream_keyelements.add(keyelements41.tree)



                    else:
                        break #loop7


                char_literal42 = self.input.LT(1)
                self.match(self.input, 35, self.FOLLOW_35_in_line_key427) 
                stream_35.add(char_literal42)
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
                # 101:2: -> ^( TOKEN_KEY ( OVERRIDE )? keycode ( keyelements )+ )
                # XKBGrammar.g:101:5: ^( TOKEN_KEY ( OVERRIDE )? keycode ( keyelements )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_KEY, "TOKEN_KEY"), root_1)

                # XKBGrammar.g:101:17: ( OVERRIDE )?
                if stream_OVERRIDE.hasNext():
                    self.adaptor.addChild(root_1, stream_OVERRIDE.nextNode())


                stream_OVERRIDE.reset();
                self.adaptor.addChild(root_1, stream_keycode.nextTree())
                # XKBGrammar.g:101:35: ( keyelements )+
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
    # XKBGrammar.g:104:1: line_modifier_map : 'modifier_map' STATE '{' keycode ( ',' keycode )* '}' -> ^( TOKEN_MODIFIER_MAP STATE ( keycode )+ ) ;
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
        stream_45 = RewriteRuleTokenStream(self.adaptor, "token 45")
        stream_44 = RewriteRuleTokenStream(self.adaptor, "token 44")
        stream_35 = RewriteRuleTokenStream(self.adaptor, "token 35")
        stream_34 = RewriteRuleTokenStream(self.adaptor, "token 34")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        try:
            try:
                # XKBGrammar.g:105:2: ( 'modifier_map' STATE '{' keycode ( ',' keycode )* '}' -> ^( TOKEN_MODIFIER_MAP STATE ( keycode )+ ) )
                # XKBGrammar.g:105:4: 'modifier_map' STATE '{' keycode ( ',' keycode )* '}'
                string_literal43 = self.input.LT(1)
                self.match(self.input, 45, self.FOLLOW_45_in_line_modifier_map453) 
                stream_45.add(string_literal43)
                STATE44 = self.input.LT(1)
                self.match(self.input, STATE, self.FOLLOW_STATE_in_line_modifier_map455) 
                stream_STATE.add(STATE44)
                char_literal45 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_line_modifier_map457) 
                stream_34.add(char_literal45)
                self._state.following.append(self.FOLLOW_keycode_in_line_modifier_map459)
                keycode46 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode46.tree)
                # XKBGrammar.g:105:37: ( ',' keycode )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 44) :
                        alt8 = 1


                    if alt8 == 1:
                        # XKBGrammar.g:105:38: ',' keycode
                        char_literal47 = self.input.LT(1)
                        self.match(self.input, 44, self.FOLLOW_44_in_line_modifier_map462) 
                        stream_44.add(char_literal47)
                        self._state.following.append(self.FOLLOW_keycode_in_line_modifier_map464)
                        keycode48 = self.keycode()

                        self._state.following.pop()
                        stream_keycode.add(keycode48.tree)



                    else:
                        break #loop8


                char_literal49 = self.input.LT(1)
                self.match(self.input, 35, self.FOLLOW_35_in_line_modifier_map468) 
                stream_35.add(char_literal49)
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
                # 106:2: -> ^( TOKEN_MODIFIER_MAP STATE ( keycode )+ )
                # XKBGrammar.g:106:5: ^( TOKEN_MODIFIER_MAP STATE ( keycode )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_MODIFIER_MAP, "TOKEN_MODIFIER_MAP"), root_1)

                self.adaptor.addChild(root_1, stream_STATE.nextNode())
                # XKBGrammar.g:106:32: ( keycode )+
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
    # XKBGrammar.g:109:1: line_virtual_modifiers : 'virtual_modifiers' NAME ( ',' NAME )* -> ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ ) ;
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
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_44 = RewriteRuleTokenStream(self.adaptor, "token 44")
        stream_46 = RewriteRuleTokenStream(self.adaptor, "token 46")

        try:
            try:
                # XKBGrammar.g:110:2: ( 'virtual_modifiers' NAME ( ',' NAME )* -> ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ ) )
                # XKBGrammar.g:110:4: 'virtual_modifiers' NAME ( ',' NAME )*
                string_literal50 = self.input.LT(1)
                self.match(self.input, 46, self.FOLLOW_46_in_line_virtual_modifiers491) 
                stream_46.add(string_literal50)
                NAME51 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_virtual_modifiers493) 
                stream_NAME.add(NAME51)
                # XKBGrammar.g:110:29: ( ',' NAME )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 44) :
                        alt9 = 1


                    if alt9 == 1:
                        # XKBGrammar.g:110:30: ',' NAME
                        char_literal52 = self.input.LT(1)
                        self.match(self.input, 44, self.FOLLOW_44_in_line_virtual_modifiers496) 
                        stream_44.add(char_literal52)
                        NAME53 = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_line_virtual_modifiers498) 
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
                # 111:2: -> ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ )
                # XKBGrammar.g:111:5: ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_VIRTUAL_MODIFIERS, "TOKEN_VIRTUAL_MODIFIERS"), root_1)

                # XKBGrammar.g:111:31: ( NAME )+
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
    # XKBGrammar.g:114:1: keycode : '<' NAME '>' -> ^( KEYCODE NAME ) ;
    def keycode(self, ):

        retval = self.keycode_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal54 = None
        NAME55 = None
        char_literal56 = None

        char_literal54_tree = None
        NAME55_tree = None
        char_literal56_tree = None
        stream_48 = RewriteRuleTokenStream(self.adaptor, "token 48")
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_47 = RewriteRuleTokenStream(self.adaptor, "token 47")

        try:
            try:
                # XKBGrammar.g:115:2: ( '<' NAME '>' -> ^( KEYCODE NAME ) )
                # XKBGrammar.g:115:4: '<' NAME '>'
                char_literal54 = self.input.LT(1)
                self.match(self.input, 47, self.FOLLOW_47_in_keycode522) 
                stream_47.add(char_literal54)
                NAME55 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode524) 
                stream_NAME.add(NAME55)
                char_literal56 = self.input.LT(1)
                self.match(self.input, 48, self.FOLLOW_48_in_keycode526) 
                stream_48.add(char_literal56)
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
                # 115:17: -> ^( KEYCODE NAME )
                # XKBGrammar.g:115:20: ^( KEYCODE NAME )
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

    class override_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start override
    # XKBGrammar.g:118:1: override : 'override' ;
    def override(self, ):

        retval = self.override_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal57 = None

        string_literal57_tree = None

        try:
            try:
                # XKBGrammar.g:119:2: ( 'override' )
                # XKBGrammar.g:119:4: 'override'
                root_0 = self.adaptor.nil()

                string_literal57 = self.input.LT(1)
                self.match(self.input, OVERRIDE, self.FOLLOW_OVERRIDE_in_override545)

                string_literal57_tree = self.adaptor.createWithPayload(string_literal57)
                self.adaptor.addChild(root_0, string_literal57_tree)





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
    # XKBGrammar.g:122:1: keyelements : ( elem_keysyms | elem_keysymgroup | elem_virtualmods | elem_overlay );
    def keyelements(self, ):

        retval = self.keyelements_return()
        retval.start = self.input.LT(1)

        root_0 = None

        elem_keysyms58 = None

        elem_keysymgroup59 = None

        elem_virtualmods60 = None

        elem_overlay61 = None



        try:
            try:
                # XKBGrammar.g:123:2: ( elem_keysyms | elem_keysymgroup | elem_virtualmods | elem_overlay )
                alt10 = 4
                LA10 = self.input.LA(1)
                if LA10 == 49:
                    alt10 = 1
                elif LA10 == 39 or LA10 == 50:
                    alt10 = 2
                elif LA10 == 51:
                    alt10 = 3
                elif LA10 == NAME:
                    alt10 = 4
                else:
                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # XKBGrammar.g:123:4: elem_keysyms
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_elem_keysyms_in_keyelements556)
                    elem_keysyms58 = self.elem_keysyms()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, elem_keysyms58.tree)



                elif alt10 == 2:
                    # XKBGrammar.g:124:4: elem_keysymgroup
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_elem_keysymgroup_in_keyelements562)
                    elem_keysymgroup59 = self.elem_keysymgroup()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, elem_keysymgroup59.tree)



                elif alt10 == 3:
                    # XKBGrammar.g:125:4: elem_virtualmods
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_elem_virtualmods_in_keyelements567)
                    elem_virtualmods60 = self.elem_virtualmods()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, elem_virtualmods60.tree)



                elif alt10 == 4:
                    # XKBGrammar.g:126:4: elem_overlay
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_elem_overlay_in_keyelements572)
                    elem_overlay61 = self.elem_overlay()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, elem_overlay61.tree)



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
    # XKBGrammar.g:129:1: elem_keysyms : 'type' ( '[' NAME ']' )? '=' DQSTRING -> ^( ELEM_KEYSYMS ^( TOKEN_TYPE ( NAME )? DQSTRING ) ) ;
    def elem_keysyms(self, ):

        retval = self.elem_keysyms_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal62 = None
        char_literal63 = None
        NAME64 = None
        char_literal65 = None
        char_literal66 = None
        DQSTRING67 = None

        string_literal62_tree = None
        char_literal63_tree = None
        NAME64_tree = None
        char_literal65_tree = None
        char_literal66_tree = None
        DQSTRING67_tree = None
        stream_49 = RewriteRuleTokenStream(self.adaptor, "token 49")
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_40 = RewriteRuleTokenStream(self.adaptor, "token 40")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")

        try:
            try:
                # XKBGrammar.g:130:2: ( 'type' ( '[' NAME ']' )? '=' DQSTRING -> ^( ELEM_KEYSYMS ^( TOKEN_TYPE ( NAME )? DQSTRING ) ) )
                # XKBGrammar.g:130:4: 'type' ( '[' NAME ']' )? '=' DQSTRING
                string_literal62 = self.input.LT(1)
                self.match(self.input, 49, self.FOLLOW_49_in_elem_keysyms583) 
                stream_49.add(string_literal62)
                # XKBGrammar.g:130:11: ( '[' NAME ']' )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == 39) :
                    alt11 = 1
                if alt11 == 1:
                    # XKBGrammar.g:130:12: '[' NAME ']'
                    char_literal63 = self.input.LT(1)
                    self.match(self.input, 39, self.FOLLOW_39_in_elem_keysyms586) 
                    stream_39.add(char_literal63)
                    NAME64 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_keysyms588) 
                    stream_NAME.add(NAME64)
                    char_literal65 = self.input.LT(1)
                    self.match(self.input, 40, self.FOLLOW_40_in_elem_keysyms590) 
                    stream_40.add(char_literal65)




                char_literal66 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_elem_keysyms594) 
                stream_41.add(char_literal66)
                DQSTRING67 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_elem_keysyms596) 
                stream_DQSTRING.add(DQSTRING67)
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
                # 131:2: -> ^( ELEM_KEYSYMS ^( TOKEN_TYPE ( NAME )? DQSTRING ) )
                # XKBGrammar.g:131:5: ^( ELEM_KEYSYMS ^( TOKEN_TYPE ( NAME )? DQSTRING ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ELEM_KEYSYMS, "ELEM_KEYSYMS"), root_1)

                # XKBGrammar.g:131:20: ^( TOKEN_TYPE ( NAME )? DQSTRING )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_TYPE, "TOKEN_TYPE"), root_2)

                # XKBGrammar.g:131:33: ( NAME )?
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
    # XKBGrammar.g:134:1: elem_keysymgroup : ( 'symbols' '[' group= NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']' -> ^( ELEM_KEYSYMGROUP ( $group)? ^( VALUE ( $keysym)+ ) ) ;
    def elem_keysymgroup(self, ):

        retval = self.elem_keysymgroup_return()
        retval.start = self.input.LT(1)

        root_0 = None

        group = None
        string_literal68 = None
        char_literal69 = None
        char_literal70 = None
        char_literal71 = None
        char_literal72 = None
        char_literal73 = None
        char_literal74 = None
        keysym = None
        list_keysym = None

        group_tree = None
        string_literal68_tree = None
        char_literal69_tree = None
        char_literal70_tree = None
        char_literal71_tree = None
        char_literal72_tree = None
        char_literal73_tree = None
        char_literal74_tree = None
        keysym_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_44 = RewriteRuleTokenStream(self.adaptor, "token 44")
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_40 = RewriteRuleTokenStream(self.adaptor, "token 40")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")
        stream_50 = RewriteRuleTokenStream(self.adaptor, "token 50")

        try:
            try:
                # XKBGrammar.g:135:2: ( ( 'symbols' '[' group= NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']' -> ^( ELEM_KEYSYMGROUP ( $group)? ^( VALUE ( $keysym)+ ) ) )
                # XKBGrammar.g:135:4: ( 'symbols' '[' group= NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']'
                # XKBGrammar.g:135:4: ( 'symbols' '[' group= NAME ']' '=' )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == 50) :
                    alt12 = 1
                if alt12 == 1:
                    # XKBGrammar.g:135:5: 'symbols' '[' group= NAME ']' '='
                    string_literal68 = self.input.LT(1)
                    self.match(self.input, 50, self.FOLLOW_50_in_elem_keysymgroup624) 
                    stream_50.add(string_literal68)
                    char_literal69 = self.input.LT(1)
                    self.match(self.input, 39, self.FOLLOW_39_in_elem_keysymgroup626) 
                    stream_39.add(char_literal69)
                    group = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_keysymgroup630) 
                    stream_NAME.add(group)
                    char_literal70 = self.input.LT(1)
                    self.match(self.input, 40, self.FOLLOW_40_in_elem_keysymgroup632) 
                    stream_40.add(char_literal70)
                    char_literal71 = self.input.LT(1)
                    self.match(self.input, 41, self.FOLLOW_41_in_elem_keysymgroup634) 
                    stream_41.add(char_literal71)




                char_literal72 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_elem_keysymgroup638) 
                stream_39.add(char_literal72)
                keysym = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_keysymgroup642) 
                stream_NAME.add(keysym)
                if list_keysym is None:
                    list_keysym = []
                list_keysym.append(keysym)

                # XKBGrammar.g:135:57: ( ',' keysym+= NAME )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == 44) :
                        alt13 = 1


                    if alt13 == 1:
                        # XKBGrammar.g:135:58: ',' keysym+= NAME
                        char_literal73 = self.input.LT(1)
                        self.match(self.input, 44, self.FOLLOW_44_in_elem_keysymgroup645) 
                        stream_44.add(char_literal73)
                        keysym = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_keysymgroup649) 
                        stream_NAME.add(keysym)
                        if list_keysym is None:
                            list_keysym = []
                        list_keysym.append(keysym)




                    else:
                        break #loop13


                char_literal74 = self.input.LT(1)
                self.match(self.input, 40, self.FOLLOW_40_in_elem_keysymgroup653) 
                stream_40.add(char_literal74)
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
                # 136:2: -> ^( ELEM_KEYSYMGROUP ( $group)? ^( VALUE ( $keysym)+ ) )
                # XKBGrammar.g:136:5: ^( ELEM_KEYSYMGROUP ( $group)? ^( VALUE ( $keysym)+ ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ELEM_KEYSYMGROUP, "ELEM_KEYSYMGROUP"), root_1)

                # XKBGrammar.g:136:24: ( $group)?
                if stream_group.hasNext():
                    self.adaptor.addChild(root_1, stream_group.nextNode())


                stream_group.reset();
                # XKBGrammar.g:136:32: ^( VALUE ( $keysym)+ )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(VALUE, "VALUE"), root_2)

                # XKBGrammar.g:136:40: ( $keysym)+
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
    # XKBGrammar.g:139:1: elem_virtualmods : ( 'virtualMods' '=' NAME ) -> ^( ELEM_VIRTUALMODS NAME ) ;
    def elem_virtualmods(self, ):

        retval = self.elem_virtualmods_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal75 = None
        char_literal76 = None
        NAME77 = None

        string_literal75_tree = None
        char_literal76_tree = None
        NAME77_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_51 = RewriteRuleTokenStream(self.adaptor, "token 51")

        try:
            try:
                # XKBGrammar.g:140:2: ( ( 'virtualMods' '=' NAME ) -> ^( ELEM_VIRTUALMODS NAME ) )
                # XKBGrammar.g:140:4: ( 'virtualMods' '=' NAME )
                # XKBGrammar.g:140:4: ( 'virtualMods' '=' NAME )
                # XKBGrammar.g:140:5: 'virtualMods' '=' NAME
                string_literal75 = self.input.LT(1)
                self.match(self.input, 51, self.FOLLOW_51_in_elem_virtualmods685) 
                stream_51.add(string_literal75)
                char_literal76 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_elem_virtualmods687) 
                stream_41.add(char_literal76)
                NAME77 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_virtualmods689) 
                stream_NAME.add(NAME77)




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
                # 141:2: -> ^( ELEM_VIRTUALMODS NAME )
                # XKBGrammar.g:141:5: ^( ELEM_VIRTUALMODS NAME )
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

    class elem_overlay_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start elem_overlay
    # XKBGrammar.g:144:1: elem_overlay : NAME '=' keycode -> ^( OVERLAY NAME keycode ) ;
    def elem_overlay(self, ):

        retval = self.elem_overlay_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME78 = None
        char_literal79 = None
        keycode80 = None


        NAME78_tree = None
        char_literal79_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        try:
            try:
                # XKBGrammar.g:145:2: ( NAME '=' keycode -> ^( OVERLAY NAME keycode ) )
                # XKBGrammar.g:145:4: NAME '=' keycode
                NAME78 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_overlay710) 
                stream_NAME.add(NAME78)
                char_literal79 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_elem_overlay712) 
                stream_41.add(char_literal79)
                self._state.following.append(self.FOLLOW_keycode_in_elem_overlay714)
                keycode80 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode80.tree)
                # AST Rewrite
                # elements: keycode, NAME
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
                # 146:2: -> ^( OVERLAY NAME keycode )
                # XKBGrammar.g:146:5: ^( OVERLAY NAME keycode )
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


 

    FOLLOW_symbols_in_layout161 = frozenset([28])
    FOLLOW_EOF_in_layout164 = frozenset([1])
    FOLLOW_mapType_in_symbols187 = frozenset([34])
    FOLLOW_34_in_symbols189 = frozenset([26, 37, 38, 42, 43, 45, 46])
    FOLLOW_mapMaterial_in_symbols191 = frozenset([26, 35, 37, 38, 42, 43, 45, 46])
    FOLLOW_35_in_symbols194 = frozenset([36])
    FOLLOW_36_in_symbols196 = frozenset([1])
    FOLLOW_MAPOPTS_in_mapType224 = frozenset([28, 29])
    FOLLOW_DQSTRING_in_mapType227 = frozenset([1])
    FOLLOW_line_include_in_mapMaterial259 = frozenset([1])
    FOLLOW_line_name_in_mapMaterial265 = frozenset([36])
    FOLLOW_36_in_mapMaterial267 = frozenset([1])
    FOLLOW_line_keytype_in_mapMaterial273 = frozenset([36])
    FOLLOW_36_in_mapMaterial275 = frozenset([1])
    FOLLOW_line_key_in_mapMaterial281 = frozenset([36])
    FOLLOW_36_in_mapMaterial283 = frozenset([1])
    FOLLOW_line_modifier_map_in_mapMaterial289 = frozenset([36])
    FOLLOW_36_in_mapMaterial291 = frozenset([1])
    FOLLOW_line_virtual_modifiers_in_mapMaterial297 = frozenset([36])
    FOLLOW_36_in_mapMaterial299 = frozenset([1])
    FOLLOW_37_in_line_include311 = frozenset([29])
    FOLLOW_DQSTRING_in_line_include313 = frozenset([1])
    FOLLOW_38_in_line_name333 = frozenset([39])
    FOLLOW_39_in_line_name335 = frozenset([30])
    FOLLOW_NAME_in_line_name337 = frozenset([40])
    FOLLOW_40_in_line_name339 = frozenset([41])
    FOLLOW_41_in_line_name341 = frozenset([29])
    FOLLOW_DQSTRING_in_line_name343 = frozenset([1])
    FOLLOW_42_in_line_keytype369 = frozenset([39, 41])
    FOLLOW_39_in_line_keytype372 = frozenset([30])
    FOLLOW_NAME_in_line_keytype374 = frozenset([40])
    FOLLOW_40_in_line_keytype376 = frozenset([41])
    FOLLOW_41_in_line_keytype380 = frozenset([29])
    FOLLOW_DQSTRING_in_line_keytype382 = frozenset([1])
    FOLLOW_OVERRIDE_in_line_key409 = frozenset([43])
    FOLLOW_43_in_line_key412 = frozenset([47])
    FOLLOW_keycode_in_line_key414 = frozenset([34])
    FOLLOW_34_in_line_key416 = frozenset([30, 39, 49, 50, 51])
    FOLLOW_keyelements_in_line_key418 = frozenset([35, 44])
    FOLLOW_44_in_line_key421 = frozenset([30, 39, 49, 50, 51])
    FOLLOW_keyelements_in_line_key423 = frozenset([35, 44])
    FOLLOW_35_in_line_key427 = frozenset([1])
    FOLLOW_45_in_line_modifier_map453 = frozenset([21])
    FOLLOW_STATE_in_line_modifier_map455 = frozenset([34])
    FOLLOW_34_in_line_modifier_map457 = frozenset([47])
    FOLLOW_keycode_in_line_modifier_map459 = frozenset([35, 44])
    FOLLOW_44_in_line_modifier_map462 = frozenset([47])
    FOLLOW_keycode_in_line_modifier_map464 = frozenset([35, 44])
    FOLLOW_35_in_line_modifier_map468 = frozenset([1])
    FOLLOW_46_in_line_virtual_modifiers491 = frozenset([30])
    FOLLOW_NAME_in_line_virtual_modifiers493 = frozenset([1, 44])
    FOLLOW_44_in_line_virtual_modifiers496 = frozenset([30])
    FOLLOW_NAME_in_line_virtual_modifiers498 = frozenset([1, 44])
    FOLLOW_47_in_keycode522 = frozenset([30])
    FOLLOW_NAME_in_keycode524 = frozenset([48])
    FOLLOW_48_in_keycode526 = frozenset([1])
    FOLLOW_OVERRIDE_in_override545 = frozenset([1])
    FOLLOW_elem_keysyms_in_keyelements556 = frozenset([1])
    FOLLOW_elem_keysymgroup_in_keyelements562 = frozenset([1])
    FOLLOW_elem_virtualmods_in_keyelements567 = frozenset([1])
    FOLLOW_elem_overlay_in_keyelements572 = frozenset([1])
    FOLLOW_49_in_elem_keysyms583 = frozenset([39, 41])
    FOLLOW_39_in_elem_keysyms586 = frozenset([30])
    FOLLOW_NAME_in_elem_keysyms588 = frozenset([40])
    FOLLOW_40_in_elem_keysyms590 = frozenset([41])
    FOLLOW_41_in_elem_keysyms594 = frozenset([29])
    FOLLOW_DQSTRING_in_elem_keysyms596 = frozenset([1])
    FOLLOW_50_in_elem_keysymgroup624 = frozenset([39])
    FOLLOW_39_in_elem_keysymgroup626 = frozenset([30])
    FOLLOW_NAME_in_elem_keysymgroup630 = frozenset([40])
    FOLLOW_40_in_elem_keysymgroup632 = frozenset([41])
    FOLLOW_41_in_elem_keysymgroup634 = frozenset([39])
    FOLLOW_39_in_elem_keysymgroup638 = frozenset([30])
    FOLLOW_NAME_in_elem_keysymgroup642 = frozenset([40, 44])
    FOLLOW_44_in_elem_keysymgroup645 = frozenset([30])
    FOLLOW_NAME_in_elem_keysymgroup649 = frozenset([40, 44])
    FOLLOW_40_in_elem_keysymgroup653 = frozenset([1])
    FOLLOW_51_in_elem_virtualmods685 = frozenset([41])
    FOLLOW_41_in_elem_virtualmods687 = frozenset([30])
    FOLLOW_NAME_in_elem_virtualmods689 = frozenset([1])
    FOLLOW_NAME_in_elem_overlay710 = frozenset([41])
    FOLLOW_41_in_elem_overlay712 = frozenset([47])
    FOLLOW_keycode_in_elem_overlay714 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("XKBGrammarLexer", XKBGrammarParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)

if __name__ == '__main__':
    main(sys.argv)
