import ply.lex as lex


class SimpleFlex:
    tokens = (
        'WHITESPACE',
        'NEWLINE',
        'WORD',
        'WHITESPACE_BEGINNING_OR_END'
    )

    def __init__(self, **kwargs):
        self.word_counter = 0
        self.lexer = lex.lex(module=self, **kwargs)

    def t_WHITESPACE_BEGINNING_OR_END(self, t):
        r'^[^\S\n]+|[^\S\n]+$'
        t.value = " "
        pass

    def t_WHITESPACE(self, t):
        r'[^\S\n]+'
        t.value = " "
        return t

    def t_NEWLINE(self, t):
        r'\n+'
        t.value = "\n"
        t.lexer.lineno += 1
        return t

    def t_WORD(self, t):
        r'\S+'
        self.word_counter += 1
        return t

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def test(self, data):
        self.lexer.input(data)

        while True:
            token = self.lexer.token()
            if not token:
                break
            print(token.value, end='')
        print()
        print(self.lexer.lineno)
        print(self.word_counter)
