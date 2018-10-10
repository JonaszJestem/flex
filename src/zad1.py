import re

import ply.lex as lex


class SimpleFlex:
    tokens = (
        'WS',
        'BLANKLINE'
    )

    def __init__(self):
        self.word_counter = 0
        self.result = ""

    def t_WS(self, t):
        r'.*\s+.*'
        stripped = str(t.value)
        stripped = re.sub("[^\S\n]+", " ", stripped)
        t.value = stripped
        self.result += stripped
        return t

    def t_BLANKLINE(self, t):
        r'\n\s+\n'
        print("Blank line!")
        pass

    def t_newline(self, t):
        r'\n+'
        print("NEW LINE!")
        t.lexer.lineno += len(t.value)

    t_ignore = ' \t'

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def test(self, data):
        self.lexer.input(data)

        while True:
            tok = self.lexer.token()
            if not tok:
                break

        self.result += "\n" + str(self.lexer.lineno)
        self.result += "\n" + str(self.word_counter)


m = SimpleFlex()
m.build()
