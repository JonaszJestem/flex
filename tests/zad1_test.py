import unittest

from src.zad1 import SimpleFlex


class TestZad1(unittest.TestCase):
    def setUp(self):
        self.m = SimpleFlex()
        self.build = self.m.build()

    def test_strip(self):
        self.m.test("   asdfsad asdasd asdasda    ")
        self.assertIn("asdfsad asdasd asdasda", self.m.result)

    def test_trim_tabs_into_space(self):
        self.m.test("asdfsad \tasdasd   asdasda")
        self.assertIn("asdfsad asdasd asdasda", self.m.result)

    def test_trim_multiple_spaces(self):
        self.m.test("   asdfsad       asdasd          asdasda    ")
        self.assertIn("asdfsad asdasd asdasda", self.m.result)

    def test_remove_blank_lines(self):
        self.m.test("   asdfsad  \n"
                    "  \n   "
                    "asdasd          asdasda    ")
        self.assertIn("asdfsad asdasd asdasda", self.m.result)

    def test_LineCount(self):
        self.m.test("1\n2  \n3 \n4")
        self.assertEqual(4, self.m.lexer.lineno)
