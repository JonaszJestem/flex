from unittest import TestCase

from src.zad4 import Calculator


class TestZad1(TestCase):
    def setUp(self):
        self.m = Calculator()

    def test_1(self):
        given = "2 3+4*"
        expected = 20

        result = self.m.test(given)

        self.assertEqual(expected, result)

    def test_2(self):
        given = "1 2 3 4 + * -"
        expected = -13

        result = self.m.test(given)

        self.assertEqual(expected, result)

    def test_3(self):
        given = "-1 2 -3 4 + * -"
        expected = -3

        result = self.m.test(given)

        self.assertEqual(expected, result)

    def test_4(self):
        given = "8 -7 6 -5 4 * -3 % / - +"
        expected = 4

        result = self.m.test(given)

        self.assertEqual(expected, result)

    def test_5(self):
        given = "2 3 2 ^ ^"
        expected = 512

        result = self.m.test(given)

        self.assertEqual(expected, result)

    def test_6(self):
        given = "2 3 +*"
        expected = "Błąd: za mała liczba argumentów"

        result = self.m.test(given)

        self.assertEqual(expected, result)

    def test_7(self):
        given = "2 3 4 +"
        expected = "Błąd: za mała liczba operatorów"

        result = self.m.test(given)

        self.assertEqual(expected, result)

    def test_8(self):
        given = "2.4 3+"
        expected = "Błąd: zły symbol \".\""

        result = self.m.test(given)

        self.assertEqual(expected, result)
