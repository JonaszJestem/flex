import ply.lex as lex


class CComment:
    tokens = (
        'CODE',
        'DOCS'
    )

    states = (
        ('comment', 'exclusive'),
        ('documentation', 'exclusive'),
    )

    def __init__(self, *args):
        self.lexer = lex.lex(module=self)
        self.code = []
        self.code_start = 0
        self.leave_docs = args[0]

    def t_comment(self, t):
        r'\/\/'
        self.code.append((self.code_start, t.lexer.lexpos - 2))
        t.lexer.begin("comment")
        pass

    def t_comment_end(self, t):
        r'\n'
        self.code_start = t.lexer.lexpos - 1
        t.lexer.begin("INITIAL")
        pass

    def t_comment_error(self, t):
        t.lexer.skip(1)
        pass

    def t_DOCS(self, t):
        r'\/\*'
        if not self.leave_docs:
            self.code.append((self.code_start, t.lexer.lexpos - 2))
            t.lexer.begin("documentation")
        pass

    def t_documentation_end(self, t):
        r'\*\/'
        self.code_start = t.lexer.lexpos
        t.lexer.begin("INITIAL")
        pass

    def t_documentation_error(self, t):
        t.lexer.skip(1)
        pass

    def t_error(self, t):
        t.lexer.skip(1)
        pass

    def t_eof(self, t):
        self.code.append((self.code_start, self.lexer.lexpos))

    def test(self, data):
        self.lexer.input(data)

        while True:
            token = self.lexer.token()
            if not token:
                break

        result = ""
        for (start, end) in self.code:
            result += data[start:end]
        return result
