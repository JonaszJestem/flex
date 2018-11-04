import ply.lex as lex


class HTMLCommentRemover:
    tokens = (
        'HTML',
    )

    states = (
        ('comment', 'exclusive'),
    )

    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        self.html = []
        self.html_start = 0

    def t_comment(self, t):
        r'<!--'
        self.html.append((self.html_start, t.lexer.lexpos - 4))
        t.lexer.begin("comment")
        pass

    def t_comment_end(self, t):
        r'-->'
        self.html_start = t.lexer.lexpos
        t.lexer.begin("INITIAL")
        pass

    def t_comment_error(self, t):
        t.lexer.skip(1)
        pass

    def t_error(self, t):
        t.lexer.skip(1)
        pass

    def t_eof(self, t):
        self.html.append((self.html_start, self.lexer.lexpos))

    def test(self, data):
        self.lexer.input(data)

        while True:
            token = self.lexer.token()
            if not token:
                break

        result = ""
        for (start, end) in self.html:
            result += data[start:end]
        return result
