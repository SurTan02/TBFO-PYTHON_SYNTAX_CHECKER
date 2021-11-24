from token_expressions import tex
import re

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
        self.prevStr = "" 
        self.prevTok = ""
        self.currStr = ""
        self.currTok = ""

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
                tok1 = Token(tok_type, m.group(groupname), self.pos)
                k = 0
                val =""
                

                tok = tok_type
                
                self.pos = m.end()
                if (tok == 'WHITESPACE') :
                    return ''
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