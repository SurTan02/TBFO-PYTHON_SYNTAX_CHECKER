
#from token_expressions import tex
import re
import os

class Token(object):
    def __init__(self, type, value, posistion):
        self.type = type
        self.value = value
        self. position = posistion

    def __str__(self):
         return '%s(%s) at %s' % (self.type, self.value, self.position)

class Lexer(object):
    def __init__(self, rules, skip_whitespace=True):
        index = 1
        holder = []
        self.group_type = {}

        for regex, type in rules:
            groupname = 'GROUP%s' % index
            holder.append('(?P<%s>%s)' % (groupname, regex))
            self.group_type[groupname] = type
            index += 1
        
        self.regex = re.compile('|'.join(holder))
        self.skip_whitespace = skip_whitespace
        self.re_ws_skip = re.compile('\S')

    def input(self, buf):
        self.buf = buf
        self.pos = 0
        
    def token(self):
        if self.pos >= len(self.buf):
            return None
        else:
            if self.skip_whitespace:
                m = self.re_ws_skip.search(self.buf, self.pos)

                if m:
                    self.pos = m.start()
                else:
                    return None

            m = self.regex.match(self.buf, self.pos)
            if m:
                groupname = m.lastgroup
                tok_type = self.group_type[groupname]
                tok = Token(tok_type, m.group(groupname), self.pos)
                self.pos = m.end()
                return tok

            # if we're here, no rule matched
            raise LexerError(self.pos)

    def tokens(self):
        while 1:
            tok = self.token()
            if tok is None: break
            yield tok
 

    
class LexerError(Exception):
    def __init__(self, pos):
        self.pos = pos

file_path = './checkfile.txt'
f = open("checkfile.txt", encoding="utf8")
text = f.read()

tex = [
    (r'\=',                   'ASSIGNMENT'),
    (r'\(',                    'LP'),
    (r'\)',                    'RP'),
    (r'\[',                      'LSB'),
    (r'\]',                     'RSB'),
    (r'\*\*',                   'POWER'),
    (r';',                     'SEMICOLON'),
    (r'\+',                    'PLUS'),
    (r'-',                     'MINUS'),
    (r'\*',                    'MULTIPLY'),
    (r'\/',                     'DIVIDE'),
    (r':',                      'COLON'),
    (r'abs',                    'ABS'),
    (r'round',                  'ROUND'),
    (r'pow',                    'POW'),

    (r'\"\"\"',                 'TRIPLEQUOTE'),
    (r'\'\'\'',                 'TRIPLEQUOTE'),
     (r'\#.*',                  'COMMENT'),
    (r'\".*\"',                  'STRING'),
    (r'\'.*\'',                 'STRING'),
    (r'\.',                     'WITH_METHOD'),
     (r'\d+',                   'INTEGER'),
    (r'\d+.+\d',                'FLOAT'),
    (r'[a-zA-Z_]+[\da-zA-Z_0-9]*','IDENTIFIER'),

    (r'<=',                    'LESS_OR_EQUAL_THAN'),
    (r'<',                     'LESS_THAN'),
    (r'>=',                    'GREATER_OR_EQUAL_THAN'),
    (r'>',                     'GREATER_THAN'),
    (r'==',                    'EQUALS'),
    (r'!=',                    'NOT_EQUAL'),

    (r'str',                    'STR'),
    (r'int',                    'INT'),
    (r'float',                  'TO_FLOAT'),

    (r'\n',                     'NEWLINE'),
    (r'and',                   'AND'),
    (r'\sor\s',                 'OR'),
    (r'not',                   'NOT'),
    (r'if\(',                    'IF_LP'),
    (r'if\s',                    'IF'),
    (r'elif\(',                    'ELIF_LP'),
    (r'elif\s',                    'ELIF'),
    # (r'then',                  'THEN'),
    (r'else',                  'ELSE'),
    (r'while',                 'WHILE'),
    # (r'do',                    'DO'),
    # (r'end',                   'END'),
    (r'print',                 'PRINT'),
    (r'is\s',                     'IS'),
    (r'bool',                   'BOOL'),
    (r'import\s',                 'IMPORT'),
    (r'None',                   'NONE'),
    (r'False',                  'FALSE'),
    (r'True',                   'TRUE'),
    (r'as\s',                   'AS'),
    (r'break\n',                  'BREAK NEWLINE'),
    (r'break\w',                'BREAK ERROR'),
    (r'class\s',                'CLASS'),
    (r'continue\n',             'CONTINUE'),
    (r'def\s',                  'DEF'),
    (r'for\s',                  'FOR'),
    (r'from\s',                 'FROM'),
    (r'in\s',                   'IN'),
    (r'not',                    'NOT'),
    (r'pass',                   'PASS'),
    (r'raise\s',                  'RAISE'),
    (r'return\s',               'RETURN'),
    (r'while',                  'WHILE'),
    (r'with',                   'WITH'),
    (r'\w',                     'NULL'),
    
]

lexered = Lexer(tex, skip_whitespace=True)
lexered.input(text)

try:
    for tokens in lexered.tokens():
        print(tokens)
except LexerError as err:
    print('LexerError at position %s' % err.pos)
    
