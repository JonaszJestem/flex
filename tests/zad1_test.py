from unittest import TestCase

from src.zad1 import SimpleFlex


class TestZad1(TestCase):
    def setUp(self):
        self.m = SimpleFlex()

    def test_strip(self):
        given = "   asdfsad asdasd asdasda    "
        expected = "asdfsad asdasd asdasda\n1\n3"

        result = self.m.test(given)

        self.assertEqual(expected, result)

    def test_trim_tabs_into_space(self):
        given = "asdfsad \tasdasd   asdasda"
        expected = "asdfsad asdasd asdasda\n1\n3"

        result = self.m.test(given)

        self.assertEqual(expected, result)

    def test_strip_whitespace(self):
        given = "   asdfsad       asdasd          asdasda    "
        expected = "asdfsad asdasd asdasda\n1\n3"

        result = self.m.test(given)

        self.assertEqual(expected, result)

    def test_remove_blank_lines(self):
        given = "   asdfsad  \n  \n   asdasd          asdasda    "
        expected = "asdfsad\nasdasd asdasda\n2\n3"

        result = self.m.test(given)

        self.assertEqual(expected, result)

    def test_LineCount(self):
        self.m.test("1\n2  \n3 \n4")
        self.assertEqual(4, self.m.lexer.lineno)
