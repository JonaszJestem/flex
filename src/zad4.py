import ply.lex as lex


class Calculator:
    tokens = (
        'DIGIT',
        'OPERATOR'
    )

    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        self.stack = []

    def t_DIGIT(self, t):
        r'-?\d+'
        self.stack.append(int(t.value))
        pass

    def t_OPERATOR(self, t):
        r'[\+|\-|\*|\%|\/|\^]'

        if len(self.stack) < 2:
            self.abortParsing(t, "Błąd: za mała liczba argumentów")
        else:
            self.executeOperation(t.value)
        pass

    def t_WHITESPACE(self, t):
        r'\s+'
        pass

    def executeOperation(self, operator):
        first_number = self.stack.pop()
        second_number = self.stack.pop()

        result = 0

        # print(first_number, operator, second_number)

        if operator == '+':
            result = first_number + second_number
        elif operator == '-':
            result = second_number - first_number
        elif operator == '*':
            result = first_number * second_number
        elif operator == '/':
            result = second_number / first_number
        elif operator == '%':
            result = second_number % first_number
        elif operator == '^':
            result = second_number ** first_number

        self.stack.append(int(result))

    def t_error(self, t):
        self.abortParsing(t, "Błąd: zły symbol \"%s\"" % t.value[0])

    def abortParsing(self, t, message):
        t.lexer.lexpos = t.lexer.lexlen
        self.stack.clear()
        self.stack.append(message)

    def test(self, data):
        self.lexer.input(data)

        while True:
            token = self.lexer.token()
            if not token:
                break

        if len(self.stack) > 1:
            return "Błąd: za mała liczba operatorów"
        else:
            return self.stack.pop()
