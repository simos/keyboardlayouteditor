# $ANTLR 3.1b1 XKBGrammar.g 2008-06-04 20:51:54

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
T__66=66
T__67=67
T__64=64
T__65=65
T__62=62
T__63=63
MAPOPTIONS=16
TOKEN_INCLUDE=4
TOKEN_MODIFIER_MAP=9
T__61=61
EOF=-1
T__60=60
TOKEN_TYPE=8
MAPTYPE=14
TOKEN_VIRTUAL_MODIFIERS=11
T__55=55
T__56=56
T__57=57
NAME=28
T__58=58
T__51=51
T__52=52
MAPMATERIAL=17
T__53=53
T__54=54
T__59=59
KEYSYMS=20
COMMENT=30
DQSTRING=27
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
LINE_COMMENT=31
KEYCODE=18
T__48=48
T__49=49
TOKEN_NAME=6
VALUE=21
LAYOUT=12
T__32=32
WS=29
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
MAPNAME=15
TOKEN_KEY=7
VIRTUALMODS=25
SYMBOLS=13
KEYELEMENTS=26
TOKEN_KEY_TYPE=5
KEYCODEX=19

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "TOKEN_INCLUDE", "TOKEN_KEY_TYPE", "TOKEN_NAME", "TOKEN_KEY", "TOKEN_TYPE", 
    "TOKEN_MODIFIER_MAP", "TOKEN_SYMBOL", "TOKEN_VIRTUAL_MODIFIERS", "LAYOUT", 
    "SYMBOLS", "MAPTYPE", "MAPNAME", "MAPOPTIONS", "MAPMATERIAL", "KEYCODE", 
    "KEYCODEX", "KEYSYMS", "VALUE", "STATE", "KEYSYMGROUP", "OVERRIDE", 
    "VIRTUALMODS", "KEYELEMENTS", "DQSTRING", "NAME", "WS", "COMMENT", "LINE_COMMENT", 
    "'{'", "'}'", "';'", "'include'", "'name'", "'['", "']'", "'='", "'key.type'", 
    "'override'", "'key'", "','", "'modifier_map'", "'virtual_modifiers'", 
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
    # XKBGrammar.g:59:1: layout : ( symbols )+ EOF -> ^( LAYOUT ( symbols )+ ) ;
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
                # XKBGrammar.g:60:2: ( ( symbols )+ EOF -> ^( LAYOUT ( symbols )+ ) )
                # XKBGrammar.g:60:4: ( symbols )+ EOF
                # XKBGrammar.g:60:4: ( symbols )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((51 <= LA1_0 <= 59)) :
                        alt1 = 1


                    if alt1 == 1:
                        # XKBGrammar.g:60:4: symbols
                        self._state.following.append(self.FOLLOW_symbols_in_layout157)
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
                self.match(self.input, EOF, self.FOLLOW_EOF_in_layout160) 
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
                # 61:2: -> ^( LAYOUT ( symbols )+ )
                # XKBGrammar.g:61:5: ^( LAYOUT ( symbols )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(LAYOUT, "LAYOUT"), root_1)

                # XKBGrammar.g:61:14: ( symbols )+
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
    # XKBGrammar.g:64:1: symbols : mapType '{' ( mapMaterial )+ '}' ';' -> ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) ) ;
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
        stream_33 = RewriteRuleTokenStream(self.adaptor, "token 33")
        stream_34 = RewriteRuleTokenStream(self.adaptor, "token 34")
        stream_mapMaterial = RewriteRuleSubtreeStream(self.adaptor, "rule mapMaterial")
        stream_mapType = RewriteRuleSubtreeStream(self.adaptor, "rule mapType")
        try:
            try:
                # XKBGrammar.g:65:2: ( mapType '{' ( mapMaterial )+ '}' ';' -> ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) ) )
                # XKBGrammar.g:65:4: mapType '{' ( mapMaterial )+ '}' ';'
                self._state.following.append(self.FOLLOW_mapType_in_symbols183)
                mapType3 = self.mapType()

                self._state.following.pop()
                stream_mapType.add(mapType3.tree)
                char_literal4 = self.input.LT(1)
                self.match(self.input, 32, self.FOLLOW_32_in_symbols185) 
                stream_32.add(char_literal4)
                # XKBGrammar.g:65:16: ( mapMaterial )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((35 <= LA2_0 <= 36) or (40 <= LA2_0 <= 42) or (44 <= LA2_0 <= 45)) :
                        alt2 = 1


                    if alt2 == 1:
                        # XKBGrammar.g:65:16: mapMaterial
                        self._state.following.append(self.FOLLOW_mapMaterial_in_symbols187)
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
                self.match(self.input, 33, self.FOLLOW_33_in_symbols190) 
                stream_33.add(char_literal6)
                char_literal7 = self.input.LT(1)
                self.match(self.input, 34, self.FOLLOW_34_in_symbols192) 
                stream_34.add(char_literal7)
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
                # 66:2: -> ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) )
                # XKBGrammar.g:66:5: ^( SYMBOLS mapType ^( MAPMATERIAL ( mapMaterial )+ ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(SYMBOLS, "SYMBOLS"), root_1)

                self.adaptor.addChild(root_1, stream_mapType.nextTree())
                # XKBGrammar.g:66:23: ^( MAPMATERIAL ( mapMaterial )+ )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPMATERIAL, "MAPMATERIAL"), root_2)

                # XKBGrammar.g:66:37: ( mapMaterial )+
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
    # XKBGrammar.g:69:1: mapType : ( mapOptions )+ DQSTRING -> ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME DQSTRING ) ) ;
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
                # XKBGrammar.g:70:2: ( ( mapOptions )+ DQSTRING -> ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME DQSTRING ) ) )
                # XKBGrammar.g:70:4: ( mapOptions )+ DQSTRING
                # XKBGrammar.g:70:4: ( mapOptions )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((51 <= LA3_0 <= 59)) :
                        alt3 = 1


                    if alt3 == 1:
                        # XKBGrammar.g:70:4: mapOptions
                        self._state.following.append(self.FOLLOW_mapOptions_in_mapType220)
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
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_mapType223) 
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
                # 71:2: -> ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME DQSTRING ) )
                # XKBGrammar.g:71:5: ^( MAPTYPE ^( MAPOPTIONS ( mapOptions )+ ) ^( MAPNAME DQSTRING ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPTYPE, "MAPTYPE"), root_1)

                # XKBGrammar.g:71:15: ^( MAPOPTIONS ( mapOptions )+ )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MAPOPTIONS, "MAPOPTIONS"), root_2)

                # XKBGrammar.g:71:28: ( mapOptions )+
                if not (stream_mapOptions.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_mapOptions.hasNext():
                    self.adaptor.addChild(root_2, stream_mapOptions.nextTree())


                stream_mapOptions.reset()

                self.adaptor.addChild(root_1, root_2)
                # XKBGrammar.g:71:41: ^( MAPNAME DQSTRING )
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
    # XKBGrammar.g:74:1: mapMaterial : ( line_include | line_name ';' | line_keytype ';' | line_key ';' | line_modifier_map ';' | line_virtual_modifiers ';' );
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
                # XKBGrammar.g:75:2: ( line_include | line_name ';' | line_keytype ';' | line_key ';' | line_modifier_map ';' | line_virtual_modifiers ';' )
                alt4 = 6
                LA4 = self.input.LA(1)
                if LA4 == 35:
                    alt4 = 1
                elif LA4 == 36:
                    alt4 = 2
                elif LA4 == 40:
                    alt4 = 3
                elif LA4 == 41 or LA4 == 42:
                    alt4 = 4
                elif LA4 == 44:
                    alt4 = 5
                elif LA4 == 45:
                    alt4 = 6
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # XKBGrammar.g:75:4: line_include
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_include_in_mapMaterial255)
                    line_include10 = self.line_include()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_include10.tree)



                elif alt4 == 2:
                    # XKBGrammar.g:76:4: line_name ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_name_in_mapMaterial261)
                    line_name11 = self.line_name()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_name11.tree)
                    char_literal12 = self.input.LT(1)
                    self.match(self.input, 34, self.FOLLOW_34_in_mapMaterial263)



                elif alt4 == 3:
                    # XKBGrammar.g:77:4: line_keytype ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_keytype_in_mapMaterial269)
                    line_keytype13 = self.line_keytype()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_keytype13.tree)
                    char_literal14 = self.input.LT(1)
                    self.match(self.input, 34, self.FOLLOW_34_in_mapMaterial271)



                elif alt4 == 4:
                    # XKBGrammar.g:78:4: line_key ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_key_in_mapMaterial277)
                    line_key15 = self.line_key()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_key15.tree)
                    char_literal16 = self.input.LT(1)
                    self.match(self.input, 34, self.FOLLOW_34_in_mapMaterial279)



                elif alt4 == 5:
                    # XKBGrammar.g:79:4: line_modifier_map ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_modifier_map_in_mapMaterial285)
                    line_modifier_map17 = self.line_modifier_map()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_modifier_map17.tree)
                    char_literal18 = self.input.LT(1)
                    self.match(self.input, 34, self.FOLLOW_34_in_mapMaterial287)



                elif alt4 == 6:
                    # XKBGrammar.g:80:4: line_virtual_modifiers ';'
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_line_virtual_modifiers_in_mapMaterial293)
                    line_virtual_modifiers19 = self.line_virtual_modifiers()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, line_virtual_modifiers19.tree)
                    char_literal20 = self.input.LT(1)
                    self.match(self.input, 34, self.FOLLOW_34_in_mapMaterial295)



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
    # XKBGrammar.g:83:1: line_include : 'include' DQSTRING -> ^( TOKEN_INCLUDE DQSTRING ) ;
    def line_include(self, ):

        retval = self.line_include_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal21 = None
        DQSTRING22 = None

        string_literal21_tree = None
        DQSTRING22_tree = None
        stream_35 = RewriteRuleTokenStream(self.adaptor, "token 35")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")

        try:
            try:
                # XKBGrammar.g:84:2: ( 'include' DQSTRING -> ^( TOKEN_INCLUDE DQSTRING ) )
                # XKBGrammar.g:84:4: 'include' DQSTRING
                string_literal21 = self.input.LT(1)
                self.match(self.input, 35, self.FOLLOW_35_in_line_include307) 
                stream_35.add(string_literal21)
                DQSTRING22 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_include309) 
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
                # 85:2: -> ^( TOKEN_INCLUDE DQSTRING )
                # XKBGrammar.g:85:5: ^( TOKEN_INCLUDE DQSTRING )
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
    # XKBGrammar.g:88:1: line_name : 'name' '[' n1= NAME ']' '=' n2= DQSTRING -> ^( TOKEN_NAME $n1 ^( VALUE $n2) ) ;
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
        stream_36 = RewriteRuleTokenStream(self.adaptor, "token 36")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")

        try:
            try:
                # XKBGrammar.g:89:2: ( 'name' '[' n1= NAME ']' '=' n2= DQSTRING -> ^( TOKEN_NAME $n1 ^( VALUE $n2) ) )
                # XKBGrammar.g:89:4: 'name' '[' n1= NAME ']' '=' n2= DQSTRING
                string_literal23 = self.input.LT(1)
                self.match(self.input, 36, self.FOLLOW_36_in_line_name329) 
                stream_36.add(string_literal23)
                char_literal24 = self.input.LT(1)
                self.match(self.input, 37, self.FOLLOW_37_in_line_name331) 
                stream_37.add(char_literal24)
                n1 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_name335) 
                stream_NAME.add(n1)
                char_literal25 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_line_name337) 
                stream_38.add(char_literal25)
                char_literal26 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_line_name339) 
                stream_39.add(char_literal26)
                n2 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_name343) 
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
                # 90:2: -> ^( TOKEN_NAME $n1 ^( VALUE $n2) )
                # XKBGrammar.g:90:5: ^( TOKEN_NAME $n1 ^( VALUE $n2) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_NAME, "TOKEN_NAME"), root_1)

                self.adaptor.addChild(root_1, stream_n1.nextNode())
                # XKBGrammar.g:90:22: ^( VALUE $n2)
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
    # XKBGrammar.g:93:1: line_keytype : 'key.type' ( '[' NAME ']' )? '=' DQSTRING -> ^( TOKEN_KEY_TYPE ( NAME )? ^( VALUE DQSTRING ) ) ;
    def line_keytype(self, ):

        retval = self.line_keytype_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal27 = None
        char_literal28 = None
        NAME29 = None
        char_literal30 = None
        char_literal31 = None
        DQSTRING32 = None

        string_literal27_tree = None
        char_literal28_tree = None
        NAME29_tree = None
        char_literal30_tree = None
        char_literal31_tree = None
        DQSTRING32_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_40 = RewriteRuleTokenStream(self.adaptor, "token 40")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")

        try:
            try:
                # XKBGrammar.g:94:2: ( 'key.type' ( '[' NAME ']' )? '=' DQSTRING -> ^( TOKEN_KEY_TYPE ( NAME )? ^( VALUE DQSTRING ) ) )
                # XKBGrammar.g:94:4: 'key.type' ( '[' NAME ']' )? '=' DQSTRING
                string_literal27 = self.input.LT(1)
                self.match(self.input, 40, self.FOLLOW_40_in_line_keytype371) 
                stream_40.add(string_literal27)
                # XKBGrammar.g:94:15: ( '[' NAME ']' )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 37) :
                    alt5 = 1
                if alt5 == 1:
                    # XKBGrammar.g:94:16: '[' NAME ']'
                    char_literal28 = self.input.LT(1)
                    self.match(self.input, 37, self.FOLLOW_37_in_line_keytype374) 
                    stream_37.add(char_literal28)
                    NAME29 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_line_keytype376) 
                    stream_NAME.add(NAME29)
                    char_literal30 = self.input.LT(1)
                    self.match(self.input, 38, self.FOLLOW_38_in_line_keytype378) 
                    stream_38.add(char_literal30)




                char_literal31 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_line_keytype382) 
                stream_39.add(char_literal31)
                DQSTRING32 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_line_keytype384) 
                stream_DQSTRING.add(DQSTRING32)
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
                # 95:2: -> ^( TOKEN_KEY_TYPE ( NAME )? ^( VALUE DQSTRING ) )
                # XKBGrammar.g:95:5: ^( TOKEN_KEY_TYPE ( NAME )? ^( VALUE DQSTRING ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_KEY_TYPE, "TOKEN_KEY_TYPE"), root_1)

                # XKBGrammar.g:95:22: ( NAME )?
                if stream_NAME.hasNext():
                    self.adaptor.addChild(root_1, stream_NAME.nextNode())


                stream_NAME.reset();
                # XKBGrammar.g:95:28: ^( VALUE DQSTRING )
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
    # XKBGrammar.g:98:1: line_key : (override= 'override' )? 'key' keycode '{' keyelements ( ',' keyelements )* '}' -> ^( TOKEN_KEY ( ^( OVERRIDE $override) )? keycode ( keyelements )+ ) ;
    def line_key(self, ):

        retval = self.line_key_return()
        retval.start = self.input.LT(1)

        root_0 = None

        override = None
        string_literal33 = None
        char_literal35 = None
        char_literal37 = None
        char_literal39 = None
        keycode34 = None

        keyelements36 = None

        keyelements38 = None


        override_tree = None
        string_literal33_tree = None
        char_literal35_tree = None
        char_literal37_tree = None
        char_literal39_tree = None
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_42 = RewriteRuleTokenStream(self.adaptor, "token 42")
        stream_32 = RewriteRuleTokenStream(self.adaptor, "token 32")
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_33 = RewriteRuleTokenStream(self.adaptor, "token 33")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        stream_keyelements = RewriteRuleSubtreeStream(self.adaptor, "rule keyelements")
        try:
            try:
                # XKBGrammar.g:99:2: ( (override= 'override' )? 'key' keycode '{' keyelements ( ',' keyelements )* '}' -> ^( TOKEN_KEY ( ^( OVERRIDE $override) )? keycode ( keyelements )+ ) )
                # XKBGrammar.g:99:4: (override= 'override' )? 'key' keycode '{' keyelements ( ',' keyelements )* '}'
                # XKBGrammar.g:99:12: (override= 'override' )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 41) :
                    alt6 = 1
                if alt6 == 1:
                    # XKBGrammar.g:99:12: override= 'override'
                    override = self.input.LT(1)
                    self.match(self.input, 41, self.FOLLOW_41_in_line_key413) 
                    stream_41.add(override)




                string_literal33 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_line_key416) 
                stream_42.add(string_literal33)
                self._state.following.append(self.FOLLOW_keycode_in_line_key418)
                keycode34 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode34.tree)
                char_literal35 = self.input.LT(1)
                self.match(self.input, 32, self.FOLLOW_32_in_line_key420) 
                stream_32.add(char_literal35)
                self._state.following.append(self.FOLLOW_keyelements_in_line_key422)
                keyelements36 = self.keyelements()

                self._state.following.pop()
                stream_keyelements.add(keyelements36.tree)
                # XKBGrammar.g:99:55: ( ',' keyelements )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 43) :
                        alt7 = 1


                    if alt7 == 1:
                        # XKBGrammar.g:99:56: ',' keyelements
                        char_literal37 = self.input.LT(1)
                        self.match(self.input, 43, self.FOLLOW_43_in_line_key425) 
                        stream_43.add(char_literal37)
                        self._state.following.append(self.FOLLOW_keyelements_in_line_key427)
                        keyelements38 = self.keyelements()

                        self._state.following.pop()
                        stream_keyelements.add(keyelements38.tree)



                    else:
                        break #loop7


                char_literal39 = self.input.LT(1)
                self.match(self.input, 33, self.FOLLOW_33_in_line_key431) 
                stream_33.add(char_literal39)
                # AST Rewrite
                # elements: keyelements, keycode, override
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
                # 100:2: -> ^( TOKEN_KEY ( ^( OVERRIDE $override) )? keycode ( keyelements )+ )
                # XKBGrammar.g:100:5: ^( TOKEN_KEY ( ^( OVERRIDE $override) )? keycode ( keyelements )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_KEY, "TOKEN_KEY"), root_1)

                # XKBGrammar.g:100:17: ( ^( OVERRIDE $override) )?
                if stream_override.hasNext():
                    # XKBGrammar.g:100:17: ^( OVERRIDE $override)
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(OVERRIDE, "OVERRIDE"), root_2)

                    self.adaptor.addChild(root_2, stream_override.nextNode())

                    self.adaptor.addChild(root_1, root_2)


                stream_override.reset();
                self.adaptor.addChild(root_1, stream_keycode.nextTree())
                # XKBGrammar.g:100:48: ( keyelements )+
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
    # XKBGrammar.g:103:1: line_modifier_map : 'modifier_map' state '{' keycode ( ',' keycode )* '}' -> ^( TOKEN_MODIFIER_MAP state ( keycode )+ ) ;
    def line_modifier_map(self, ):

        retval = self.line_modifier_map_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal40 = None
        char_literal42 = None
        char_literal44 = None
        char_literal46 = None
        state41 = None

        keycode43 = None

        keycode45 = None


        string_literal40_tree = None
        char_literal42_tree = None
        char_literal44_tree = None
        char_literal46_tree = None
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_44 = RewriteRuleTokenStream(self.adaptor, "token 44")
        stream_32 = RewriteRuleTokenStream(self.adaptor, "token 32")
        stream_33 = RewriteRuleTokenStream(self.adaptor, "token 33")
        stream_state = RewriteRuleSubtreeStream(self.adaptor, "rule state")
        stream_keycode = RewriteRuleSubtreeStream(self.adaptor, "rule keycode")
        try:
            try:
                # XKBGrammar.g:104:2: ( 'modifier_map' state '{' keycode ( ',' keycode )* '}' -> ^( TOKEN_MODIFIER_MAP state ( keycode )+ ) )
                # XKBGrammar.g:104:4: 'modifier_map' state '{' keycode ( ',' keycode )* '}'
                string_literal40 = self.input.LT(1)
                self.match(self.input, 44, self.FOLLOW_44_in_line_modifier_map462) 
                stream_44.add(string_literal40)
                self._state.following.append(self.FOLLOW_state_in_line_modifier_map464)
                state41 = self.state()

                self._state.following.pop()
                stream_state.add(state41.tree)
                char_literal42 = self.input.LT(1)
                self.match(self.input, 32, self.FOLLOW_32_in_line_modifier_map466) 
                stream_32.add(char_literal42)
                self._state.following.append(self.FOLLOW_keycode_in_line_modifier_map468)
                keycode43 = self.keycode()

                self._state.following.pop()
                stream_keycode.add(keycode43.tree)
                # XKBGrammar.g:104:37: ( ',' keycode )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 43) :
                        alt8 = 1


                    if alt8 == 1:
                        # XKBGrammar.g:104:38: ',' keycode
                        char_literal44 = self.input.LT(1)
                        self.match(self.input, 43, self.FOLLOW_43_in_line_modifier_map471) 
                        stream_43.add(char_literal44)
                        self._state.following.append(self.FOLLOW_keycode_in_line_modifier_map473)
                        keycode45 = self.keycode()

                        self._state.following.pop()
                        stream_keycode.add(keycode45.tree)



                    else:
                        break #loop8


                char_literal46 = self.input.LT(1)
                self.match(self.input, 33, self.FOLLOW_33_in_line_modifier_map477) 
                stream_33.add(char_literal46)
                # AST Rewrite
                # elements: state, keycode
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
                # 105:2: -> ^( TOKEN_MODIFIER_MAP state ( keycode )+ )
                # XKBGrammar.g:105:5: ^( TOKEN_MODIFIER_MAP state ( keycode )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_MODIFIER_MAP, "TOKEN_MODIFIER_MAP"), root_1)

                self.adaptor.addChild(root_1, stream_state.nextTree())
                # XKBGrammar.g:105:32: ( keycode )+
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
    # XKBGrammar.g:108:1: line_virtual_modifiers : 'virtual_modifiers' NAME ( ',' NAME )* -> ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ ) ;
    def line_virtual_modifiers(self, ):

        retval = self.line_virtual_modifiers_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal47 = None
        NAME48 = None
        char_literal49 = None
        NAME50 = None

        string_literal47_tree = None
        NAME48_tree = None
        char_literal49_tree = None
        NAME50_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_45 = RewriteRuleTokenStream(self.adaptor, "token 45")

        try:
            try:
                # XKBGrammar.g:109:2: ( 'virtual_modifiers' NAME ( ',' NAME )* -> ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ ) )
                # XKBGrammar.g:109:4: 'virtual_modifiers' NAME ( ',' NAME )*
                string_literal47 = self.input.LT(1)
                self.match(self.input, 45, self.FOLLOW_45_in_line_virtual_modifiers500) 
                stream_45.add(string_literal47)
                NAME48 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_line_virtual_modifiers502) 
                stream_NAME.add(NAME48)
                # XKBGrammar.g:109:29: ( ',' NAME )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 43) :
                        alt9 = 1


                    if alt9 == 1:
                        # XKBGrammar.g:109:30: ',' NAME
                        char_literal49 = self.input.LT(1)
                        self.match(self.input, 43, self.FOLLOW_43_in_line_virtual_modifiers505) 
                        stream_43.add(char_literal49)
                        NAME50 = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_line_virtual_modifiers507) 
                        stream_NAME.add(NAME50)



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
                # 110:2: -> ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ )
                # XKBGrammar.g:110:5: ^( TOKEN_VIRTUAL_MODIFIERS ( NAME )+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_VIRTUAL_MODIFIERS, "TOKEN_VIRTUAL_MODIFIERS"), root_1)

                # XKBGrammar.g:110:31: ( NAME )+
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
    # XKBGrammar.g:113:1: keycode : ( NAME -> ^( KEYCODE NAME ) | '<' NAME '>' -> ^( KEYCODEX NAME ) );
    def keycode(self, ):

        retval = self.keycode_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME51 = None
        char_literal52 = None
        NAME53 = None
        char_literal54 = None

        NAME51_tree = None
        char_literal52_tree = None
        NAME53_tree = None
        char_literal54_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_47 = RewriteRuleTokenStream(self.adaptor, "token 47")
        stream_46 = RewriteRuleTokenStream(self.adaptor, "token 46")

        try:
            try:
                # XKBGrammar.g:114:2: ( NAME -> ^( KEYCODE NAME ) | '<' NAME '>' -> ^( KEYCODEX NAME ) )
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == NAME) :
                    alt10 = 1
                elif (LA10_0 == 46) :
                    alt10 = 2
                else:
                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae

                if alt10 == 1:
                    # XKBGrammar.g:114:4: NAME
                    NAME51 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode531) 
                    stream_NAME.add(NAME51)
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
                    # 114:9: -> ^( KEYCODE NAME )
                    # XKBGrammar.g:114:12: ^( KEYCODE NAME )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYCODE, "KEYCODE"), root_1)

                    self.adaptor.addChild(root_1, stream_NAME.nextNode())

                    self.adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                elif alt10 == 2:
                    # XKBGrammar.g:115:4: '<' NAME '>'
                    char_literal52 = self.input.LT(1)
                    self.match(self.input, 46, self.FOLLOW_46_in_keycode544) 
                    stream_46.add(char_literal52)
                    NAME53 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keycode546) 
                    stream_NAME.add(NAME53)
                    char_literal54 = self.input.LT(1)
                    self.match(self.input, 47, self.FOLLOW_47_in_keycode548) 
                    stream_47.add(char_literal54)
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

    class keyelements_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start keyelements
    # XKBGrammar.g:118:1: keyelements : ( keysyms | virtualmods | keysymgroup );
    def keyelements(self, ):

        retval = self.keyelements_return()
        retval.start = self.input.LT(1)

        root_0 = None

        keysyms55 = None

        virtualmods56 = None

        keysymgroup57 = None



        try:
            try:
                # XKBGrammar.g:119:2: ( keysyms | virtualmods | keysymgroup )
                alt11 = 3
                LA11 = self.input.LA(1)
                if LA11 == 48:
                    alt11 = 1
                elif LA11 == 50:
                    alt11 = 2
                elif LA11 == 37 or LA11 == 49:
                    alt11 = 3
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # XKBGrammar.g:119:4: keysyms
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_keysyms_in_keyelements567)
                    keysyms55 = self.keysyms()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, keysyms55.tree)



                elif alt11 == 2:
                    # XKBGrammar.g:120:4: virtualmods
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_virtualmods_in_keyelements573)
                    virtualmods56 = self.virtualmods()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, virtualmods56.tree)



                elif alt11 == 3:
                    # XKBGrammar.g:121:4: keysymgroup
                    root_0 = self.adaptor.nil()

                    self._state.following.append(self.FOLLOW_keysymgroup_in_keyelements578)
                    keysymgroup57 = self.keysymgroup()

                    self._state.following.pop()
                    self.adaptor.addChild(root_0, keysymgroup57.tree)



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

    class keysyms_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start keysyms
    # XKBGrammar.g:124:1: keysyms : 'type' ( '[' NAME ']' )? '=' DQSTRING -> ^( KEYSYMS ^( TOKEN_TYPE ( NAME )? DQSTRING ) ) ;
    def keysyms(self, ):

        retval = self.keysyms_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal58 = None
        char_literal59 = None
        NAME60 = None
        char_literal61 = None
        char_literal62 = None
        DQSTRING63 = None

        string_literal58_tree = None
        char_literal59_tree = None
        NAME60_tree = None
        char_literal61_tree = None
        char_literal62_tree = None
        DQSTRING63_tree = None
        stream_48 = RewriteRuleTokenStream(self.adaptor, "token 48")
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_DQSTRING = RewriteRuleTokenStream(self.adaptor, "token DQSTRING")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")

        try:
            try:
                # XKBGrammar.g:125:2: ( 'type' ( '[' NAME ']' )? '=' DQSTRING -> ^( KEYSYMS ^( TOKEN_TYPE ( NAME )? DQSTRING ) ) )
                # XKBGrammar.g:125:4: 'type' ( '[' NAME ']' )? '=' DQSTRING
                string_literal58 = self.input.LT(1)
                self.match(self.input, 48, self.FOLLOW_48_in_keysyms589) 
                stream_48.add(string_literal58)
                # XKBGrammar.g:125:11: ( '[' NAME ']' )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == 37) :
                    alt12 = 1
                if alt12 == 1:
                    # XKBGrammar.g:125:12: '[' NAME ']'
                    char_literal59 = self.input.LT(1)
                    self.match(self.input, 37, self.FOLLOW_37_in_keysyms592) 
                    stream_37.add(char_literal59)
                    NAME60 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keysyms594) 
                    stream_NAME.add(NAME60)
                    char_literal61 = self.input.LT(1)
                    self.match(self.input, 38, self.FOLLOW_38_in_keysyms596) 
                    stream_38.add(char_literal61)




                char_literal62 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_keysyms600) 
                stream_39.add(char_literal62)
                DQSTRING63 = self.input.LT(1)
                self.match(self.input, DQSTRING, self.FOLLOW_DQSTRING_in_keysyms602) 
                stream_DQSTRING.add(DQSTRING63)
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
                # 126:2: -> ^( KEYSYMS ^( TOKEN_TYPE ( NAME )? DQSTRING ) )
                # XKBGrammar.g:126:5: ^( KEYSYMS ^( TOKEN_TYPE ( NAME )? DQSTRING ) )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYSYMS, "KEYSYMS"), root_1)

                # XKBGrammar.g:126:15: ^( TOKEN_TYPE ( NAME )? DQSTRING )
                root_2 = self.adaptor.nil()
                root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_TYPE, "TOKEN_TYPE"), root_2)

                # XKBGrammar.g:126:28: ( NAME )?
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

    # $ANTLR end keysyms

    class keysymgroup_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None




    # $ANTLR start keysymgroup
    # XKBGrammar.g:129:1: keysymgroup : ( 'symbols' '[' st1= NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']' -> ^( KEYSYMGROUP ( ^( TOKEN_SYMBOL $st1) )? ( $keysym)+ ) ;
    def keysymgroup(self, ):

        retval = self.keysymgroup_return()
        retval.start = self.input.LT(1)

        root_0 = None

        st1 = None
        string_literal64 = None
        char_literal65 = None
        char_literal66 = None
        char_literal67 = None
        char_literal68 = None
        char_literal69 = None
        char_literal70 = None
        keysym = None
        list_keysym = None

        st1_tree = None
        string_literal64_tree = None
        char_literal65_tree = None
        char_literal66_tree = None
        char_literal67_tree = None
        char_literal68_tree = None
        char_literal69_tree = None
        char_literal70_tree = None
        keysym_tree = None
        stream_49 = RewriteRuleTokenStream(self.adaptor, "token 49")
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")

        try:
            try:
                # XKBGrammar.g:130:2: ( ( 'symbols' '[' st1= NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']' -> ^( KEYSYMGROUP ( ^( TOKEN_SYMBOL $st1) )? ( $keysym)+ ) )
                # XKBGrammar.g:130:4: ( 'symbols' '[' st1= NAME ']' '=' )? '[' keysym+= NAME ( ',' keysym+= NAME )* ']'
                # XKBGrammar.g:130:4: ( 'symbols' '[' st1= NAME ']' '=' )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == 49) :
                    alt13 = 1
                if alt13 == 1:
                    # XKBGrammar.g:130:5: 'symbols' '[' st1= NAME ']' '='
                    string_literal64 = self.input.LT(1)
                    self.match(self.input, 49, self.FOLLOW_49_in_keysymgroup630) 
                    stream_49.add(string_literal64)
                    char_literal65 = self.input.LT(1)
                    self.match(self.input, 37, self.FOLLOW_37_in_keysymgroup632) 
                    stream_37.add(char_literal65)
                    st1 = self.input.LT(1)
                    self.match(self.input, NAME, self.FOLLOW_NAME_in_keysymgroup636) 
                    stream_NAME.add(st1)
                    char_literal66 = self.input.LT(1)
                    self.match(self.input, 38, self.FOLLOW_38_in_keysymgroup638) 
                    stream_38.add(char_literal66)
                    char_literal67 = self.input.LT(1)
                    self.match(self.input, 39, self.FOLLOW_39_in_keysymgroup640) 
                    stream_39.add(char_literal67)




                char_literal68 = self.input.LT(1)
                self.match(self.input, 37, self.FOLLOW_37_in_keysymgroup644) 
                stream_37.add(char_literal68)
                keysym = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_keysymgroup648) 
                stream_NAME.add(keysym)
                if list_keysym is None:
                    list_keysym = []
                list_keysym.append(keysym)

                # XKBGrammar.g:130:55: ( ',' keysym+= NAME )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == 43) :
                        alt14 = 1


                    if alt14 == 1:
                        # XKBGrammar.g:130:56: ',' keysym+= NAME
                        char_literal69 = self.input.LT(1)
                        self.match(self.input, 43, self.FOLLOW_43_in_keysymgroup651) 
                        stream_43.add(char_literal69)
                        keysym = self.input.LT(1)
                        self.match(self.input, NAME, self.FOLLOW_NAME_in_keysymgroup655) 
                        stream_NAME.add(keysym)
                        if list_keysym is None:
                            list_keysym = []
                        list_keysym.append(keysym)




                    else:
                        break #loop14


                char_literal70 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_keysymgroup659) 
                stream_38.add(char_literal70)
                # AST Rewrite
                # elements: st1, keysym
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
                # 131:2: -> ^( KEYSYMGROUP ( ^( TOKEN_SYMBOL $st1) )? ( $keysym)+ )
                # XKBGrammar.g:131:5: ^( KEYSYMGROUP ( ^( TOKEN_SYMBOL $st1) )? ( $keysym)+ )
                root_1 = self.adaptor.nil()
                root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(KEYSYMGROUP, "KEYSYMGROUP"), root_1)

                # XKBGrammar.g:131:19: ( ^( TOKEN_SYMBOL $st1) )?
                if stream_st1.hasNext():
                    # XKBGrammar.g:131:19: ^( TOKEN_SYMBOL $st1)
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(TOKEN_SYMBOL, "TOKEN_SYMBOL"), root_2)

                    self.adaptor.addChild(root_2, stream_st1.nextNode())

                    self.adaptor.addChild(root_1, root_2)


                stream_st1.reset();
                # XKBGrammar.g:131:41: ( $keysym)+
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
    # XKBGrammar.g:134:1: virtualmods : 'virtualMods' '=' NAME -> ^( VIRTUALMODS NAME ) ;
    def virtualmods(self, ):

        retval = self.virtualmods_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal71 = None
        char_literal72 = None
        NAME73 = None

        string_literal71_tree = None
        char_literal72_tree = None
        NAME73_tree = None
        stream_NAME = RewriteRuleTokenStream(self.adaptor, "token NAME")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")
        stream_50 = RewriteRuleTokenStream(self.adaptor, "token 50")

        try:
            try:
                # XKBGrammar.g:135:2: ( 'virtualMods' '=' NAME -> ^( VIRTUALMODS NAME ) )
                # XKBGrammar.g:135:4: 'virtualMods' '=' NAME
                string_literal71 = self.input.LT(1)
                self.match(self.input, 50, self.FOLLOW_50_in_virtualmods689) 
                stream_50.add(string_literal71)
                char_literal72 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_virtualmods691) 
                stream_39.add(char_literal72)
                NAME73 = self.input.LT(1)
                self.match(self.input, NAME, self.FOLLOW_NAME_in_virtualmods693) 
                stream_NAME.add(NAME73)
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
                # 136:2: -> ^( VIRTUALMODS NAME )
                # XKBGrammar.g:136:5: ^( VIRTUALMODS NAME )
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
    # XKBGrammar.g:139:1: mapOptions : ( 'default' | 'hidden' | 'partial' | 'alphanumeric_keys' | 'keypad_keys' | 'function_keys' | 'modifier_keys' | 'alternate_group' | 'xkb_symbols' );
    def mapOptions(self, ):

        retval = self.mapOptions_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set74 = None

        set74_tree = None

        try:
            try:
                # XKBGrammar.g:140:2: ( 'default' | 'hidden' | 'partial' | 'alphanumeric_keys' | 'keypad_keys' | 'function_keys' | 'modifier_keys' | 'alternate_group' | 'xkb_symbols' )
                # XKBGrammar.g:
                root_0 = self.adaptor.nil()

                set74 = self.input.LT(1)
                if (51 <= self.input.LA(1) <= 59):
                    self.input.consume();
                    self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set74))
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
    # XKBGrammar.g:151:1: state : ( 'Shift' | 'Control' | 'Lock' | 'Mod1' | 'Mod2' | 'Mod3' | 'Mod4' | 'Mod5' );
    def state(self, ):

        retval = self.state_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set75 = None

        set75_tree = None

        try:
            try:
                # XKBGrammar.g:152:2: ( 'Shift' | 'Control' | 'Lock' | 'Mod1' | 'Mod2' | 'Mod3' | 'Mod4' | 'Mod5' )
                # XKBGrammar.g:
                root_0 = self.adaptor.nil()

                set75 = self.input.LT(1)
                if (60 <= self.input.LA(1) <= 67):
                    self.input.consume();
                    self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set75))
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


 

    FOLLOW_symbols_in_layout157 = frozenset([51, 52, 53, 54, 55, 56, 57, 58, 59])
    FOLLOW_EOF_in_layout160 = frozenset([1])
    FOLLOW_mapType_in_symbols183 = frozenset([32])
    FOLLOW_32_in_symbols185 = frozenset([35, 36, 40, 41, 42, 44, 45])
    FOLLOW_mapMaterial_in_symbols187 = frozenset([33, 35, 36, 40, 41, 42, 44, 45])
    FOLLOW_33_in_symbols190 = frozenset([34])
    FOLLOW_34_in_symbols192 = frozenset([1])
    FOLLOW_mapOptions_in_mapType220 = frozenset([27, 51, 52, 53, 54, 55, 56, 57, 58, 59])
    FOLLOW_DQSTRING_in_mapType223 = frozenset([1])
    FOLLOW_line_include_in_mapMaterial255 = frozenset([1])
    FOLLOW_line_name_in_mapMaterial261 = frozenset([34])
    FOLLOW_34_in_mapMaterial263 = frozenset([1])
    FOLLOW_line_keytype_in_mapMaterial269 = frozenset([34])
    FOLLOW_34_in_mapMaterial271 = frozenset([1])
    FOLLOW_line_key_in_mapMaterial277 = frozenset([34])
    FOLLOW_34_in_mapMaterial279 = frozenset([1])
    FOLLOW_line_modifier_map_in_mapMaterial285 = frozenset([34])
    FOLLOW_34_in_mapMaterial287 = frozenset([1])
    FOLLOW_line_virtual_modifiers_in_mapMaterial293 = frozenset([34])
    FOLLOW_34_in_mapMaterial295 = frozenset([1])
    FOLLOW_35_in_line_include307 = frozenset([27])
    FOLLOW_DQSTRING_in_line_include309 = frozenset([1])
    FOLLOW_36_in_line_name329 = frozenset([37])
    FOLLOW_37_in_line_name331 = frozenset([28])
    FOLLOW_NAME_in_line_name335 = frozenset([38])
    FOLLOW_38_in_line_name337 = frozenset([39])
    FOLLOW_39_in_line_name339 = frozenset([27])
    FOLLOW_DQSTRING_in_line_name343 = frozenset([1])
    FOLLOW_40_in_line_keytype371 = frozenset([37, 39])
    FOLLOW_37_in_line_keytype374 = frozenset([28])
    FOLLOW_NAME_in_line_keytype376 = frozenset([38])
    FOLLOW_38_in_line_keytype378 = frozenset([39])
    FOLLOW_39_in_line_keytype382 = frozenset([27])
    FOLLOW_DQSTRING_in_line_keytype384 = frozenset([1])
    FOLLOW_41_in_line_key413 = frozenset([42])
    FOLLOW_42_in_line_key416 = frozenset([28, 46])
    FOLLOW_keycode_in_line_key418 = frozenset([32])
    FOLLOW_32_in_line_key420 = frozenset([37, 48, 49, 50])
    FOLLOW_keyelements_in_line_key422 = frozenset([33, 43])
    FOLLOW_43_in_line_key425 = frozenset([37, 48, 49, 50])
    FOLLOW_keyelements_in_line_key427 = frozenset([33, 43])
    FOLLOW_33_in_line_key431 = frozenset([1])
    FOLLOW_44_in_line_modifier_map462 = frozenset([60, 61, 62, 63, 64, 65, 66, 67])
    FOLLOW_state_in_line_modifier_map464 = frozenset([32])
    FOLLOW_32_in_line_modifier_map466 = frozenset([28, 46])
    FOLLOW_keycode_in_line_modifier_map468 = frozenset([33, 43])
    FOLLOW_43_in_line_modifier_map471 = frozenset([28, 46])
    FOLLOW_keycode_in_line_modifier_map473 = frozenset([33, 43])
    FOLLOW_33_in_line_modifier_map477 = frozenset([1])
    FOLLOW_45_in_line_virtual_modifiers500 = frozenset([28])
    FOLLOW_NAME_in_line_virtual_modifiers502 = frozenset([1, 43])
    FOLLOW_43_in_line_virtual_modifiers505 = frozenset([28])
    FOLLOW_NAME_in_line_virtual_modifiers507 = frozenset([1, 43])
    FOLLOW_NAME_in_keycode531 = frozenset([1])
    FOLLOW_46_in_keycode544 = frozenset([28])
    FOLLOW_NAME_in_keycode546 = frozenset([47])
    FOLLOW_47_in_keycode548 = frozenset([1])
    FOLLOW_keysyms_in_keyelements567 = frozenset([1])
    FOLLOW_virtualmods_in_keyelements573 = frozenset([1])
    FOLLOW_keysymgroup_in_keyelements578 = frozenset([1])
    FOLLOW_48_in_keysyms589 = frozenset([37, 39])
    FOLLOW_37_in_keysyms592 = frozenset([28])
    FOLLOW_NAME_in_keysyms594 = frozenset([38])
    FOLLOW_38_in_keysyms596 = frozenset([39])
    FOLLOW_39_in_keysyms600 = frozenset([27])
    FOLLOW_DQSTRING_in_keysyms602 = frozenset([1])
    FOLLOW_49_in_keysymgroup630 = frozenset([37])
    FOLLOW_37_in_keysymgroup632 = frozenset([28])
    FOLLOW_NAME_in_keysymgroup636 = frozenset([38])
    FOLLOW_38_in_keysymgroup638 = frozenset([39])
    FOLLOW_39_in_keysymgroup640 = frozenset([37])
    FOLLOW_37_in_keysymgroup644 = frozenset([28])
    FOLLOW_NAME_in_keysymgroup648 = frozenset([38, 43])
    FOLLOW_43_in_keysymgroup651 = frozenset([28])
    FOLLOW_NAME_in_keysymgroup655 = frozenset([38, 43])
    FOLLOW_38_in_keysymgroup659 = frozenset([1])
    FOLLOW_50_in_virtualmods689 = frozenset([39])
    FOLLOW_39_in_virtualmods691 = frozenset([28])
    FOLLOW_NAME_in_virtualmods693 = frozenset([1])
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
