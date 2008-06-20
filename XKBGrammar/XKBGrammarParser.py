# $ANTLR 3.1b1 XKBGrammar.g 2008-06-20 23:20:19

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
    "'['", "']'", "'='", "'key.type'", "'key'", "'<'", "'>'", "','", "'modifier_map'", 
    "'virtual_modifiers'", "'type'", "'symbols'", "'virtualMods'"
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

                    if (LA2_0 == OVERRIDE or (37 <= LA2_0 <= 38) or (42 <= LA2_0 <= 43) or (47 <= LA2_0 <= 48)) :
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
                elif LA4 == 47:
                    alt4 = 5
                elif LA4 == 48:
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
    # XKBGrammar.g:89:1: line_name : 'name' ( '[' NAME ']' )? '=' DQSTRING -> ^( TOKEN_NAME DQSTRING ) ;
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
                # XKBGrammar.g:90:2: ( 'name' ( '[' NAME ']' )? '=' DQSTRING -> ^( TOKEN_NAME DQSTRING ) )
                # XKBGrammar.g:90:4: 'name' ( '[' NAME ']' )? '=' DQSTRING
                string_literal23 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_line_name333) 
                stream_38.add(string_literal23)
                # XKBGrammar.g:90:11: ( '[' NAME ']' )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 39) :
                    alt5 = 1
                if alt5 == 1:
                    # XKBGrammar.g:90:12: '[' NAME ']'
                    char_literal24 = self.input.LT(1)
                    self.match(self.input, 39, self.FOLLOW_39_in_line_name336) 
                    stream_39.add(char_literal24)
                    NAME25 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_line_name338) 
                    stream_NAME.add(NAME25)
                    char_literal26 = self.input.LT(1)
                    self.match(self.input, 40, self.FOLLOW_40_in_line_name340) 
                    stream_40.add(char_literal26)




                char_literal27 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_line_name344) 
                stream_41.add(char_literal27)
                DQSTRING28 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_name346) 
                stream_DQSTRING.add(DQSTRING28)
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
                # 91:2: -> ^( TOKEN_NAME DQSTRING )
                # XKBGrammar.g:91:5: ^( TOKEN_NAME DQSTRING )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_NAME, "TOKEN_NAME"), root_1)

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

    # $ANTLR end line_name

    class line_keytype_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start line_keytype
    # XKBGrammar.g:94:1: line_keytype : 'key.type' ( '[' NAME ']' )? '=' DQSTRING -> ^( TOKEN_KEY_TYPE DQSTRING ) ;
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
                # XKBGrammar.g:95:2: ( 'key.type' ( '[' NAME ']' )? '=' DQSTRING -> ^( TOKEN_KEY_TYPE DQSTRING ) )
                # XKBGrammar.g:95:4: 'key.type' ( '[' NAME ']' )? '=' DQSTRING
                string_literal29 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_line_keytype366) 
                stream_42.add(string_literal29)
                # XKBGrammar.g:95:15: ( '[' NAME ']' )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 39) :
                    alt6 = 1
                if alt6 == 1:
                    # XKBGrammar.g:95:16: '[' NAME ']'
                    char_literal30 = self.input.LT(1)
                    self.match(self.input, 39, self.FOLLOW_39_in_line_keytype369) 
                    stream_39.add(char_literal30)
                    NAME31 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype371) 
                    stream_NAME.add(NAME31)
                    char_literal32 = self.input.LT(1)
                    self.match(self.input, 40, self.FOLLOW_40_in_line_keytype373) 
                    stream_40.add(char_literal32)




                char_literal33 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_line_keytype377) 
                stream_41.add(char_literal33)
                DQSTRING34 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_keytype379) 
                stream_DQSTRING.add(DQSTRING34)
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
                # 96:2: -> ^( TOKEN_KEY_TYPE DQSTRING )
                # XKBGrammar.g:96:5: ^( TOKEN_KEY_TYPE DQSTRING )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_KEY_TYPE, "TOKEN_KEY_TYPE"), root_1)

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

    # $ANTLR end line_keytype

    class line_key_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start line_key
    # XKBGrammar.g:99:1: line_key : ( OVERRIDE )? 'key' '<' NAME '>' '{' keyelements ( ',' keyelements )* '}' -> ^( TOKEN_KEY ( OVERRIDE )? ^( KEYCODEX NAME ) ( keyelements )+ ) ;
    def line_key(self, ):

        retval = self.line_key_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OVERRIDE35 = None
        string_literal36 = None
        char_literal37 = None
        NAME38 = None
        char_literal39 = None
        char_literal40 = None
        char_literal42 = None
        char_literal44 = None
        keyelements41 = None

        keyelements43 = None


        OVERRIDE35_tree = None
        string_literal36_tree = None
        char_literal37_tree = None
        NAME38_tree = None
        char_literal39_tree = None
        char_literal40_tree = None
        char_literal42_tree = None
        char_literal44_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_45 = RewriteRuleTokenStream(self.adaptor, "token 45")
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_44 = RewriteRuleTokenStream(self.adaptor, "token 44")
        stream_46 = RewriteRuleTokenStream(self.adaptor, "token 46")
        stream_35 = RewriteRuleTokenStream(self.adaptor, "token 35")
        stream_OVERRIDE = RewriteRuleTokenStream(self.adaptor, "token OVERRIDE")
        stream_34 = RewriteRuleTokenStream(self.adaptor, "token 34")
        stream_keyelements = RewriteRuleSubtreeStream(self.adaptor, "rule keyelements")
        try:
            try:
                # XKBGrammar.g:100:2: ( ( OVERRIDE )? 'key' '<' NAME '>' '{' keyelements ( ',' keyelements )* '}' -> ^( TOKEN_KEY ( OVERRIDE )? ^( KEYCODEX NAME ) ( keyelements )+ ) )
                # XKBGrammar.g:100:4: ( OVERRIDE )? 'key' '<' NAME '>' '{' keyelements ( ',' keyelements )* '}'
                # XKBGrammar.g:100:4: ( OVERRIDE )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == OVERRIDE) :
                    alt7 = 1
                if alt7 == 1:
                    # XKBGrammar.g:100:4: OVERRIDE
                    OVERRIDE35 = self.input.LT(1)
                    self.match(self.input, OVERRIDE, self.FOLLOW_OVERRIDE_in_line_key399) 
                    stream_OVERRIDE.add(OVERRIDE35)




                string_literal36 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_line_key402) 
                stream_43.add(string_literal36)
                char_literal37 = self.input.LT(1)
                self.match(self.input, 44, self.FOLLOW_44_in_line_key404) 
                stream_44.add(char_literal37)
                NAME38 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_key406) 
                stream_NAME.add(NAME38)
                char_literal39 = self.input.LT(1)
                self.match(self.input, 45, self.FOLLOW_45_in_line_key408) 
                stream_45.add(char_literal39)
                char_literal40 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_line_key410) 
                stream_34.add(char_literal40)
                self._state.following.append(self.FOLLOW_keyelements_in_line_key412)
                keyelements41 = self.keyelements()

                self._state.following.pop()
                stream_keyelements.add(keyelements41.tree)
                # XKBGrammar.g:100:49: ( ',' keyelements )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 46) :
                        alt8 = 1


                    if alt8 == 1:
                        # XKBGrammar.g:100:50: ',' keyelements
                        char_literal42 = self.input.LT(1)
                        self.match(self.input, 46, self.FOLLOW_46_in_line_key415) 
                        stream_46.add(char_literal42)
                        self._state.following.append(self.FOLLOW_keyelements_in_line_key417)
                        keyelements43 = self.keyelements()

                        self._state.following.pop()
                        stream_keyelements.add(keyelements43.tree)



                    else:
                        break #loop8


                char_literal44 = self.input.LT(1)
                self.match(self.input, 35, self.FOLLOW_35_in_line_key421) 
                stream_35.add(char_literal44)
                # AST Rewrite
                # elements: NAME, OVERRIDE, keyelements
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
                # 101:2: -> ^( TOKEN_KEY ( OVERRIDE )? ^( KEYCODEX NAME ) ( keyelements )+ )
                # XKBGrammar.g:101:5: ^( TOKEN_KEY ( OVERRIDE )? ^( KEYCODEX NAME ) ( keyelements )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_KEY, "TOKEN_KEY"), root_1)

                # XKBGrammar.g:101:17: ( OVERRIDE )?
                if stream_OVERRIDE.hasNext():
                    self.adaptor.addChild(root_1, stream_OVERRIDE.nextNode())


                stream_OVERRIDE.reset();
                # XKBGrammar.g:101:27: ^( KEYCODEX NAME )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYCODEX, "KEYCODEX"), root_2)

                self.adaptor.addChild(root_2, stream_NAME.nextNode())

                self.adaptor.addChild(root_1, root_2)
                # XKBGrammar.g:101:44: ( keyelements )+
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

        string_literal45 = None
        STATE46 = None
        char_literal47 = None
        char_literal49 = None
        char_literal51 = None
        keycode48 = None

        keycode50 = None


        string_literal45_tree = None
        STATE46_tree = None
        char_literal47_tree = None
        char_literal49_tree = None
        char_literal51_tree = None
        stream_STATE = RewriteRuleTokenStream(self.adaptor, "token STATE")
        stream_47 = RewriteRuleTokenStream(self.adaptor, "token 47")
        stream_46 = RewriteRuleTokenStream(self.adaptor, "token 46")
        stream_35 = RewriteRuleTokenStream(self.adaptor, "token 35")
        stream_34 = RewriteRuleTokenStream(self.adaptor, "token 34")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        try:
            try:
                # XKBGrammar.g:105:2: ( 'modifier_map' STATE '{' keycode ( ',' keycode )* '}' -> ^( TOKEN_MODIFIER_MAP STATE ( keycode )+ ) )
                # XKBGrammar.g:105:4: 'modifier_map' STATE '{' keycode ( ',' keycode )* '}'
                string_literal45 = self.input.LT(1)
                self.match(self.input, 47, self.FOLLOW_47_in_line_modifier_map451) 
                stream_47.add(string_literal45)
                STATE46 = self.input.LT(1)
                self.match(self.input, STATE, self.FOLLOW_STATE_in_line_modifier_map453) 
                stream_STATE.add(STATE46)
                char_literal47 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_line_modifier_map455) 
                stream_34.add(char_literal47)
                self._state.following.append(self.FOLLOW_keycode_in_line_modifier_map457)
                keycode48 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode48.tree)
                # XKBGrammar.g:105:37: ( ',' keycode )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 46) :
                        alt9 = 1


                    if alt9 == 1:
                        # XKBGrammar.g:105:38: ',' keycode
                        char_literal49 = self.input.LT(1)
                        self.match(self.input, 46, self.FOLLOW_46_in_line_modifier_map460) 
                        stream_46.add(char_literal49)
                        self._state.following.append(self.FOLLOW_keycode_in_line_modifier_map462)
                        keycode50 = self.keycode()

                        self._state.following.pop()
                        stream_keycode.add(keycode50.tree)



                    else:
                        break #loop9


                char_literal51 = self.input.LT(1)
                self.match(self.input, 35, self.FOLLOW_35_in_line_modifier_map466) 
                stream_35.add(char_literal51)
                # AST Rewrite
                # elements: keycode, STATE
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

        string_literal52 = None
        NAME53 = None
        char_literal54 = None
        NAME55 = None

        string_literal52_tree = None
        NAME53_tree = None
        char_literal54_tree = None
        NAME55_tree = None
        stream_48 = RewriteRuleTokenStream(self.adaptor, "token 48")
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_46 = RewriteRuleTokenStream(self.adaptor, "token 46")

        try:
            try:
                # XKBGrammar.g:110:2: ( 'virtual_modifiers' NAME ( ',' NAME )* -> ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ ) )
                # XKBGrammar.g:110:4: 'virtual_modifiers' NAME ( ',' NAME )*
                string_literal52 = self.input.LT(1)
                self.match(self.input, 48, self.FOLLOW_48_in_line_virtual_modifiers489) 
                stream_48.add(string_literal52)
                NAME53 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_virtual_modifiers491) 
                stream_NAME.add(NAME53)
                # XKBGrammar.g:110:29: ( ',' NAME )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == 46) :
                        alt10 = 1


                    if alt10 == 1:
                        # XKBGrammar.g:110:30: ',' NAME
                        char_literal54 = self.input.LT(1)
                        self.match(self.input, 46, self.FOLLOW_46_in_line_virtual_modifiers494) 
                        stream_46.add(char_literal54)
                        NAME55 = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_line_virtual_modifiers496) 
                        stream_NAME.add(NAME55)



                    else:
                        break #loop10


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
    # XKBGrammar.g:114:1: keycode : ( '<' NAME '>' -> ^( KEYCODEX NAME ) | NAME -> ^( KEYCODE NAME ) );
    def keycode(self, ):

        retval = self.keycode_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal56 = None
        NAME57 = None
        char_literal58 = None
        NAME59 = None

        char_literal56_tree = None
        NAME57_tree = None
        char_literal58_tree = None
        NAME59_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_45 = RewriteRuleTokenStream(self.adaptor, "token 45")
        stream_44 = RewriteRuleTokenStream(self.adaptor, "token 44")

        try:
            try:
                # XKBGrammar.g:115:2: ( '<' NAME '>' -> ^( KEYCODEX NAME ) | NAME -> ^( KEYCODE NAME ) )
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == 44) :
                    alt11 = 1
                elif (LA11_0 == NAME) :
                    alt11 = 2
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # XKBGrammar.g:115:4: '<' NAME '>'
                    char_literal56 = self.input.LT(1)
                    self.match(self.input, 44, self.FOLLOW_44_in_keycode520) 
                    stream_44.add(char_literal56)
                    NAME57 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode522) 
                    stream_NAME.add(NAME57)
                    char_literal58 = self.input.LT(1)
                    self.match(self.input, 45, self.FOLLOW_45_in_keycode524) 
                    stream_45.add(char_literal58)
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
                    # 115:17: -> ^( KEYCODEX NAME )
                    # XKBGrammar.g:115:20: ^( KEYCODEX NAME )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYCODEX, "KEYCODEX"), root_1)

                    self.adaptor.addChild(root_1, stream_NAME.nextNode())

                    self.adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                elif alt11 == 2:
                    # XKBGrammar.g:116:4: NAME
                    NAME59 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode537) 
                    stream_NAME.add(NAME59)
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
                    # 116:9: -> ^( KEYCODE NAME )
                    # XKBGrammar.g:116:12: ^( KEYCODE NAME )
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
    # XKBGrammar.g:119:1: override : 'override' ;
    def override(self, ):

        retval = self.override_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal60 = None

        string_literal60_tree = None

        try:
            try:
                # XKBGrammar.g:120:2: ( 'override' )
                # XKBGrammar.g:120:4: 'override'
                root_0 = self.adaptor.nil()

                string_literal60 = self.input.LT(1)
                self.match(self.input, OVERRIDE, self.FOLLOW_OVERRIDE_in_override556)

                string_literal60_tree = self.adaptor.createWithPayload(string_literal60)
                self.adaptor.addChild(root_0, string_literal60_tree)





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
    # XKBGrammar.g:123:1: keyelements : ( elem_keysyms | elem_keysymgroup | elem_virtualmods | elem_overlay );
    def keyelements(self, ):

        retval = self.keyelements_return()
        retval.start = self.input.LT(1)

        root_0 = None

        elem_keysyms61 = None

        elem_keysymgroup62 = None

        elem_virtualmods63 = None

        elem_overlay64 = None



        try:
            try:
                # XKBGrammar.g:124:2: ( elem_keysyms | elem_keysymgroup | elem_virtualmods | elem_overlay )
                alt12 = 4
                LA12 = self.input.LA(1)
                if LA12 == 49:
                    alt12 = 1
                elif LA12 == 39 or LA12 == 50:
                    alt12 = 2
                elif LA12 == 51:
                    alt12 = 3
                elif LA12 == NAME:
                    alt12 = 4
                else:
                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # XKBGrammar.g:124:4: elem_keysyms
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_elem_keysyms_in_keyelements567)
                    elem_keysyms61 = self.elem_keysyms()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, elem_keysyms61.tree)



                elif alt12 == 2:
                    # XKBGrammar.g:125:4: elem_keysymgroup
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_elem_keysymgroup_in_keyelements573)
                    elem_keysymgroup62 = self.elem_keysymgroup()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, elem_keysymgroup62.tree)



                elif alt12 == 3:
                    # XKBGrammar.g:126:4: elem_virtualmods
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_elem_virtualmods_in_keyelements578)
                    elem_virtualmods63 = self.elem_virtualmods()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, elem_virtualmods63.tree)



                elif alt12 == 4:
                    # XKBGrammar.g:127:4: elem_overlay
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_elem_overlay_in_keyelements583)
                    elem_overlay64 = self.elem_overlay()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, elem_overlay64.tree)



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
    # XKBGrammar.g:130:1: elem_keysyms : 'type' ( '[' NAME ']' )? '=' DQSTRING -> ^( ELEM_KEYSYMS DQSTRING ) ;
    def elem_keysyms(self, ):

        retval = self.elem_keysyms_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal65 = None
        char_literal66 = None
        NAME67 = None
        char_literal68 = None
        char_literal69 = None
        DQSTRING70 = None

        string_literal65_tree = None
        char_literal66_tree = None
        NAME67_tree = None
        char_literal68_tree = None
        char_literal69_tree = None
        DQSTRING70_tree = None
        stream_49 = RewriteRuleTokenStream(self.adaptor, "token 49")
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_40 = RewriteRuleTokenStream(self.adaptor, "token 40")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")

        try:
            try:
                # XKBGrammar.g:131:2: ( 'type' ( '[' NAME ']' )? '=' DQSTRING -> ^( ELEM_KEYSYMS DQSTRING ) )
                # XKBGrammar.g:131:4: 'type' ( '[' NAME ']' )? '=' DQSTRING
                string_literal65 = self.input.LT(1)
                self.match(self.input, 49, self.FOLLOW_49_in_elem_keysyms594) 
                stream_49.add(string_literal65)
                # XKBGrammar.g:131:11: ( '[' NAME ']' )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == 39) :
                    alt13 = 1
                if alt13 == 1:
                    # XKBGrammar.g:131:12: '[' NAME ']'
                    char_literal66 = self.input.LT(1)
                    self.match(self.input, 39, self.FOLLOW_39_in_elem_keysyms597) 
                    stream_39.add(char_literal66)
                    NAME67 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_keysyms599) 
                    stream_NAME.add(NAME67)
                    char_literal68 = self.input.LT(1)
                    self.match(self.input, 40, self.FOLLOW_40_in_elem_keysyms601) 
                    stream_40.add(char_literal68)




                char_literal69 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_elem_keysyms605) 
                stream_41.add(char_literal69)
                DQSTRING70 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_elem_keysyms607) 
                stream_DQSTRING.add(DQSTRING70)
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
                # 132:2: -> ^( ELEM_KEYSYMS DQSTRING )
                # XKBGrammar.g:132:5: ^( ELEM_KEYSYMS DQSTRING )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ELEM_KEYSYMS, "ELEM_KEYSYMS"), root_1)

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

    # $ANTLR end elem_keysyms

    class elem_keysymgroup_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start elem_keysymgroup
    # XKBGrammar.g:135:1: elem_keysymgroup : ( 'symbols' '[' NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']' -> ^( ELEM_KEYSYMGROUP ^( VALUE ( $keysym)+ ) ) ;
    def elem_keysymgroup(self, ):

        retval = self.elem_keysymgroup_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal71 = None
        char_literal72 = None
        NAME73 = None
        char_literal74 = None
        char_literal75 = None
        char_literal76 = None
        char_literal77 = None
        char_literal78 = None
        keysym = None
        list_keysym = None

        string_literal71_tree = None
        char_literal72_tree = None
        NAME73_tree = None
        char_literal74_tree = None
        char_literal75_tree = None
        char_literal76_tree = None
        char_literal77_tree = None
        char_literal78_tree = None
        keysym_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_40 = RewriteRuleTokenStream(self.adaptor, "token 40")
        stream_46 = RewriteRuleTokenStream(self.adaptor, "token 46")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")
        stream_50 = RewriteRuleTokenStream(self.adaptor, "token 50")

        try:
            try:
                # XKBGrammar.g:136:2: ( ( 'symbols' '[' NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']' -> ^( ELEM_KEYSYMGROUP ^( VALUE ( $keysym)+ ) ) )
                # XKBGrammar.g:136:4: ( 'symbols' '[' NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']'
                # XKBGrammar.g:136:4: ( 'symbols' '[' NAME ']' '=' )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == 50) :
                    alt14 = 1
                if alt14 == 1:
                    # XKBGrammar.g:136:5: 'symbols' '[' NAME ']' '='
                    string_literal71 = self.input.LT(1)
                    self.match(self.input, 50, self.FOLLOW_50_in_elem_keysymgroup628) 
                    stream_50.add(string_literal71)
                    char_literal72 = self.input.LT(1)
                    self.match(self.input, 39, self.FOLLOW_39_in_elem_keysymgroup630) 
                    stream_39.add(char_literal72)
                    NAME73 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_keysymgroup632) 
                    stream_NAME.add(NAME73)
                    char_literal74 = self.input.LT(1)
                    self.match(self.input, 40, self.FOLLOW_40_in_elem_keysymgroup634) 
                    stream_40.add(char_literal74)
                    char_literal75 = self.input.LT(1)
                    self.match(self.input, 41, self.FOLLOW_41_in_elem_keysymgroup636) 
                    stream_41.add(char_literal75)




                char_literal76 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_elem_keysymgroup640) 
                stream_39.add(char_literal76)
                keysym = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_keysymgroup644) 
                stream_NAME.add(keysym)
                if list_keysym is None:
                    list_keysym = []
                list_keysym.append(keysym)

                # XKBGrammar.g:136:51: ( ',' keysym+= NAME )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == 46) :
                        alt15 = 1


                    if alt15 == 1:
                        # XKBGrammar.g:136:52: ',' keysym+= NAME
                        char_literal77 = self.input.LT(1)
                        self.match(self.input, 46, self.FOLLOW_46_in_elem_keysymgroup647) 
                        stream_46.add(char_literal77)
                        keysym = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_keysymgroup651) 
                        stream_NAME.add(keysym)
                        if list_keysym is None:
                            list_keysym = []
                        list_keysym.append(keysym)




                    else:
                        break #loop15


                char_literal78 = self.input.LT(1)
                self.match(self.input, 40, self.FOLLOW_40_in_elem_keysymgroup655) 
                stream_40.add(char_literal78)
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
                # 137:2: -> ^( ELEM_KEYSYMGROUP ^( VALUE ( $keysym)+ ) )
                # XKBGrammar.g:137:5: ^( ELEM_KEYSYMGROUP ^( VALUE ( $keysym)+ ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ELEM_KEYSYMGROUP, "ELEM_KEYSYMGROUP"), root_1)

                # XKBGrammar.g:137:24: ^( VALUE ( $keysym)+ )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(VALUE, "VALUE"), root_2)

                # XKBGrammar.g:137:32: ( $keysym)+
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
    # XKBGrammar.g:140:1: elem_virtualmods : ( 'virtualMods' '=' NAME ) -> ^( ELEM_VIRTUALMODS NAME ) ;
    def elem_virtualmods(self, ):

        retval = self.elem_virtualmods_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal79 = None
        char_literal80 = None
        NAME81 = None

        string_literal79_tree = None
        char_literal80_tree = None
        NAME81_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_51 = RewriteRuleTokenStream(self.adaptor, "token 51")

        try:
            try:
                # XKBGrammar.g:141:2: ( ( 'virtualMods' '=' NAME ) -> ^( ELEM_VIRTUALMODS NAME ) )
                # XKBGrammar.g:141:4: ( 'virtualMods' '=' NAME )
                # XKBGrammar.g:141:4: ( 'virtualMods' '=' NAME )
                # XKBGrammar.g:141:5: 'virtualMods' '=' NAME
                string_literal79 = self.input.LT(1)
                self.match(self.input, 51, self.FOLLOW_51_in_elem_virtualmods683) 
                stream_51.add(string_literal79)
                char_literal80 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_elem_virtualmods685) 
                stream_41.add(char_literal80)
                NAME81 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_virtualmods687) 
                stream_NAME.add(NAME81)




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
                # 142:2: -> ^( ELEM_VIRTUALMODS NAME )
                # XKBGrammar.g:142:5: ^( ELEM_VIRTUALMODS NAME )
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
    # XKBGrammar.g:145:1: elem_overlay : NAME '=' keycode -> ^( OVERLAY NAME keycode ) ;
    def elem_overlay(self, ):

        retval = self.elem_overlay_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME82 = None
        char_literal83 = None
        keycode84 = None


        NAME82_tree = None
        char_literal83_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        try:
            try:
                # XKBGrammar.g:146:2: ( NAME '=' keycode -> ^( OVERLAY NAME keycode ) )
                # XKBGrammar.g:146:4: NAME '=' keycode
                NAME82 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_elem_overlay708) 
                stream_NAME.add(NAME82)
                char_literal83 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_elem_overlay710) 
                stream_41.add(char_literal83)
                self._state.following.append(self.FOLLOW_keycode_in_elem_overlay712)
                keycode84 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode84.tree)
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
                # 147:2: -> ^( OVERLAY NAME keycode )
                # XKBGrammar.g:147:5: ^( OVERLAY NAME keycode )
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
    FOLLOW_34_in_symbols189 = frozenset([26, 37, 38, 42, 43, 47, 48])
    FOLLOW_mapMaterial_in_symbols191 = frozenset([26, 35, 37, 38, 42, 43, 47, 48])
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
    FOLLOW_38_in_line_name333 = frozenset([39, 41])
    FOLLOW_39_in_line_name336 = frozenset([30])
    FOLLOW_NAME_in_line_name338 = frozenset([40])
    FOLLOW_40_in_line_name340 = frozenset([41])
    FOLLOW_41_in_line_name344 = frozenset([29])
    FOLLOW_DQSTRING_in_line_name346 = frozenset([1])
    FOLLOW_42_in_line_keytype366 = frozenset([39, 41])
    FOLLOW_39_in_line_keytype369 = frozenset([30])
    FOLLOW_NAME_in_line_keytype371 = frozenset([40])
    FOLLOW_40_in_line_keytype373 = frozenset([41])
    FOLLOW_41_in_line_keytype377 = frozenset([29])
    FOLLOW_DQSTRING_in_line_keytype379 = frozenset([1])
    FOLLOW_OVERRIDE_in_line_key399 = frozenset([43])
    FOLLOW_43_in_line_key402 = frozenset([44])
    FOLLOW_44_in_line_key404 = frozenset([30])
    FOLLOW_NAME_in_line_key406 = frozenset([45])
    FOLLOW_45_in_line_key408 = frozenset([34])
    FOLLOW_34_in_line_key410 = frozenset([30, 39, 49, 50, 51])
    FOLLOW_keyelements_in_line_key412 = frozenset([35, 46])
    FOLLOW_46_in_line_key415 = frozenset([30, 39, 49, 50, 51])
    FOLLOW_keyelements_in_line_key417 = frozenset([35, 46])
    FOLLOW_35_in_line_key421 = frozenset([1])
    FOLLOW_47_in_line_modifier_map451 = frozenset([21])
    FOLLOW_STATE_in_line_modifier_map453 = frozenset([34])
    FOLLOW_34_in_line_modifier_map455 = frozenset([30, 44])
    FOLLOW_keycode_in_line_modifier_map457 = frozenset([35, 46])
    FOLLOW_46_in_line_modifier_map460 = frozenset([30, 44])
    FOLLOW_keycode_in_line_modifier_map462 = frozenset([35, 46])
    FOLLOW_35_in_line_modifier_map466 = frozenset([1])
    FOLLOW_48_in_line_virtual_modifiers489 = frozenset([30])
    FOLLOW_NAME_in_line_virtual_modifiers491 = frozenset([1, 46])
    FOLLOW_46_in_line_virtual_modifiers494 = frozenset([30])
    FOLLOW_NAME_in_line_virtual_modifiers496 = frozenset([1, 46])
    FOLLOW_44_in_keycode520 = frozenset([30])
    FOLLOW_NAME_in_keycode522 = frozenset([45])
    FOLLOW_45_in_keycode524 = frozenset([1])
    FOLLOW_NAME_in_keycode537 = frozenset([1])
    FOLLOW_OVERRIDE_in_override556 = frozenset([1])
    FOLLOW_elem_keysyms_in_keyelements567 = frozenset([1])
    FOLLOW_elem_keysymgroup_in_keyelements573 = frozenset([1])
    FOLLOW_elem_virtualmods_in_keyelements578 = frozenset([1])
    FOLLOW_elem_overlay_in_keyelements583 = frozenset([1])
    FOLLOW_49_in_elem_keysyms594 = frozenset([39, 41])
    FOLLOW_39_in_elem_keysyms597 = frozenset([30])
    FOLLOW_NAME_in_elem_keysyms599 = frozenset([40])
    FOLLOW_40_in_elem_keysyms601 = frozenset([41])
    FOLLOW_41_in_elem_keysyms605 = frozenset([29])
    FOLLOW_DQSTRING_in_elem_keysyms607 = frozenset([1])
    FOLLOW_50_in_elem_keysymgroup628 = frozenset([39])
    FOLLOW_39_in_elem_keysymgroup630 = frozenset([30])
    FOLLOW_NAME_in_elem_keysymgroup632 = frozenset([40])
    FOLLOW_40_in_elem_keysymgroup634 = frozenset([41])
    FOLLOW_41_in_elem_keysymgroup636 = frozenset([39])
    FOLLOW_39_in_elem_keysymgroup640 = frozenset([30])
    FOLLOW_NAME_in_elem_keysymgroup644 = frozenset([40, 46])
    FOLLOW_46_in_elem_keysymgroup647 = frozenset([30])
    FOLLOW_NAME_in_elem_keysymgroup651 = frozenset([40, 46])
    FOLLOW_40_in_elem_keysymgroup655 = frozenset([1])
    FOLLOW_51_in_elem_virtualmods683 = frozenset([41])
    FOLLOW_41_in_elem_virtualmods685 = frozenset([30])
    FOLLOW_NAME_in_elem_virtualmods687 = frozenset([1])
    FOLLOW_NAME_in_elem_overlay708 = frozenset([41])
    FOLLOW_41_in_elem_overlay710 = frozenset([30, 44])
    FOLLOW_keycode_in_elem_overlay712 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("XKBGrammarLexer", XKBGrammarParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)

if __name__ == '__main__':
    main(sys.argv)
