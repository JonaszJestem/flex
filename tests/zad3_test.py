from unittest import TestCase

from src.zad3 import CComment


class TestHTMLCommentRemover(TestCase):
    def setUp(self):
        self.m = CComment(False)

    def test_remove_all(self):
        given = "#include <stdio.h>\nint main()\n{\n   //char name[50];\n   int marks/*, i, num*/;\n\n  \
         printf('Enter number of students: ');\n   scanf('%d', &num);"

        expected = "#include <stdio.h>\nint main()\n{\n   \n   int marks;\n\n  \
         printf('Enter number of students: ');\n   scanf('%d', &num);"

        result = self.m.test(given)

        self.assertEqual(expected, result)

    def test_leave_docs(self):
        self.m = CComment(True)
        given = "#include <stdio.h>\nint main()\n{\n   //char name[50];\n   int marks/*, i, num*/;\n\n  \
         printf('Enter number of students: ');\n   scanf('%d', &num);"

        expected = "#include <stdio.h>\nint main()\n{\n   \n   int marks/*, i, num*/;\n\n  \
         printf('Enter number of students: ');\n   scanf('%d', &num);"

        result = self.m.test(given)

        self.assertEqual(expected, result)
