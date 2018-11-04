from unittest import TestCase

from src.zad2 import HTMLCommentRemover


class TestHTMLCommentRemover(TestCase):
    def setUp(self):
        self.m = HTMLCommentRemover()

    def test_single_comment(self):
        given = "<html>beuiahbeau <!-- afeaogeuaeajhgioav efkjeanbfauighea \n\n\t --> gaeojeganeagaoueh</html>"
        expected = "<html>beuiahbeau  gaeojeganeagaoueh</html>"

        result = self.m.test(given)

        self.assertEqual(expected, result)

    def test_double_comment(self):
        given = "<html>beuiahbeau <!-- afeaogeuaeajhgioav efkjeanbfauighea \n\n\t --> gaeojeganeagaoueh <br>beuiahbeau <!-- afeaogeuaeajhgioav efkjeanbfauighea \n\n\t --> </br></html>"
        expected = "<html>beuiahbeau  gaeojeganeagaoueh <br>beuiahbeau  </br></html>"

        result = self.m.test(given)

        self.assertEqual(expected, result)

    def test_nested_comment(self):
        given = "<html>beuiahbeau <!-- afeaogeuaeajhgioav efkjeanbfauighea \n\n\t gaeojeganeagaoueh <br>beuiahbeau <!-- afeaogeuaeajhgioav efkjeanbfauighea \n\n\t --> </br></html>"
        expected = "<html>beuiahbeau  </br></html>"

        result = self.m.test(given)

        self.assertEqual(expected, result)
