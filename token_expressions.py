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
    (r'break\n',                  'BREAK_NEWLINE'),
    (r'break\w',                'BREAK_ERROR'),
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