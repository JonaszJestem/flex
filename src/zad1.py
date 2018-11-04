import ply.lex as lex


class SimpleFlex:
    tokens = (
        'WHITESPACE',
        'NEWLINE',
        'WORD',
        'WHITESPACE_BEGINNING',
        'WHITESPACE_END'
    )

    def __init__(self, **kwargs):
        self.word_counter = 0
        self.lexer = lex.lex(module=self, **kwargs)

    def t_WHITESPACE_BEGINNING(self, t):
        r'(^[^\S\n]+)'
        pass

    def t_WHITESPACE_END(self, t):
        r'([^\S\n]+\Z)'
        pass

    def t_WHITESPACE(self, t):
        r'\s+'
        if "\n" in t.value:
            t.value = "\n"
            t.lexer.lineno += 1
            return t
        t.value = " "
        return t

    def t_NEWLINE(self, t):
        r'([^\S\n]*\n+[^\S\n]*)+'
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
        result = ""

        while True:
            token = self.lexer.token()
            if not token:
                break
            result += token.value

        result += "\n" + str(self.lexer.lineno) + "\n" + str(self.word_counter)
        return result
