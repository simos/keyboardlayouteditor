grammar XKBGrammar;

options
{
	language = Python;
	output = AST;
}

tokens
{
	// attributes
	TOKEN_DEFAULT 			= 'default';
	TOKEN_HIDDEN 			= 'hidden';
	TOKEN_PARTIAL 			= 'partial';
	TOKEN_ALPHANUMERIC_KEYS 	= 'alphanumeric_keys';
	TOKEN_MODIFIER_KEYS 		= 'modifier_keys';
	TOKEN_ALTERNATE_GROUP 		= 'alternate_group';
	TOKEN_XKB_SYMBOLS 		= 'xkb_symbols';

	// Keywords
	TOKEN_INCLUDE 			= 'include';
	TOKEN_KEY_TYPE			= 'key.type';
	TOKEN_NAME 			= 'name';		
	TOKEN_KEY 			= 'key';
	TOKEN_MODIFIER_MAP		= 'modifier_map';

	// Punctuators
	LBRACKET			= '[';
	RBRACKET			= ']';
	LCURLY				= '{';
	RCURLY				= '}';
	COMMA				= ',';
	DQUOTE				= '"';
	MINUS				= '-';
	PLUS				= '+';
	SEMICOLON			= ';';
	EQUAL				= '=';
	LOWERTHAN			= '<';
	GREATERTHAN			= '>';
	// HYPHEN			= '-';
	// SPACE			= ' ';
	// UNDERSCORE			= '_';
	DOT				= '.';
	
	ATTRIBUTES;
	ATTRIBUTE;
	INCLUDE;
	NAME;
	KEY;
	KEYTYPE;
	SECTION;
	SECTIONNAME;
}

layout 	: section* EOF! 
	;
	
section
	: 
	preamble sectionmaterial
	{ print '}' }
	-> ^(SECTION)
 	;

preamble :	attribute_xkb+ sectionname=quotedstring
	{ print '%(sname)s {' % { "sname": $sectionname.text } }
	;

quotedstring returns [value]
	: DQUOTE sectionname+=~(DQUOTE)+ DQUOTE 
{ 
qstring = ['"']
for elem in $sectionname:
	qstring.append(elem.getText())
qstring.append('"')
$value = "".join(qstring)
}
	;

sectionmaterial
	: LCURLY (line_include 
	| line_name 
	| line_keytype 
	| line_key 
//	| line_modifiermap
	| line_comment)+ RCURLY SEMICOLON
	;

line_comment
	:	COMMENT { skip(); } ;

line_include
	//: KEYWORD_INCLUDE DQUOTE NAME_INCLUDE DQUOTE COMMENT*
	: TOKEN_INCLUDE include=quotedstring 
	{ print '\tinclude %(inc)s' % { "inc": $include.text } }
	;

line_name
	: TOKEN_NAME LBRACKET name=NAME RBRACKET EQUAL nameval=quotedstring SEMICOLON
	{ print '\tname[\%(name)s] = %(nameval)s;' % {  "name": $name.text, "nameval": $nameval.text } }
	;

line_keytype
	: TOKEN_KEY_TYPE LBRACKET keytype=NAME RBRACKET EQUAL DQUOTE keytypevalue=NAME DQUOTE SEMICOLON
	{ print '\tkey.type[\%(kt)s] = \"%(ktv)s\";' % {  "kt": $keytype.text, "ktv": $keytypevalue.text } }
	;
	
// line_modifiermap
//	: TOKEN_MODIFIER_MAP mapname=NAME mapsyms SEMICOLON
//	{ print "\tmodifier_map \%(mapname)s %(mapsyms)s ;" % {  "mapname": $mapname.text, "mapsyms": $mapsyms.text } }
//	;

line_key
	: TOKEN_KEY keycode keysyms SEMICOLON
	{ print "\tkey \%(keycode)s %(keysyms)s ;" % {  "keycode": $keycode.text, "keysyms": $keysyms.text } }
	;
	
keycode	
	: LOWERTHAN NAME GREATERTHAN 
	-> ^(INCLUDE NAME)
	;

keysyms	
	: LCURLY LBRACKET (NAME|NAME_KEYSYM) (COMMA (NAME|NAME_KEYSYM))* RBRACKET RCURLY  
	;

// mapsyms	
//	: LCURLY LBRACKET (NAME|keycode) (COMMA (NAME|keycode))* RBRACKET RCURLY  
//	;

attribute_xkb
	: TOKEN_DEFAULT 	{ print "default", }
	| TOKEN_HIDDEN 		{ print "hidden", }
	| TOKEN_PARTIAL 	{ print "partial", }	
	| TOKEN_ALPHANUMERIC_KEYS { print "alphanumeric_keys", } 	
//	| TOKEN_MODIFIER_KEYS 	{ print "modifier_keys", }
	| TOKEN_ALTERNATE_GROUP { print "alternate_group", }
	| TOKEN_XKB_SYMBOLS     { print "xkb_symbols", }
	-> ^(ATTRIBUTES ATTRIBUTE)
	;

/*
ATTRIBUTE_XKB
	: 'default' 
	| 'hidden'
	| 'partial' 
	| 'alphanumeric_keys'
	| 'modifier_keys'
	| 'alternate_group' 
	| 'xkb_symbols'
	;
*/

NAME
	: ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'_'|'0'..'9')*
        ;

NAME_INCLUDE
	: ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'_'|'('|')'|'0'..'9')*
        ;

NAME_KEYSYM
	: ('0'..'9'|'a'..'z'|'A'..'Z')('a'..'z'|'A'..'Z'|'_'|'0'..'9')*
        ;

NAME_GROUP
	: ('0'..'9'|'a'..'z'|'A'..'Z')('a'..'z'|'A'..'Z'|'_'|'-'|'.'|'0'..'9')*
        ;

COMMENT	: '//' (~('\n'|'\r'))* 
	{ $channel = HIDDEN; }
	;

WS      :       ('\t'|' '|NEWLINE)+ 
	{ $channel=HIDDEN; }
	;

fragment NEWLINE
        :       '\r'|'\n'
	;

