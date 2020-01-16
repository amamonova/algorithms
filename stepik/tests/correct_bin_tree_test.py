import unittest
from unittest.mock import patch
from io import StringIO
from stepik.correct_bin_tree_test import check


class TestStepikCorrBinTree(unittest.TestCase):
    @patch('sys.stdin', StringIO('3\n2 1 2\n1 -1 -1\n3 -1 -1'))
    def test_first(self):
        out = StringIO()
        check(out=out)
        self.assertEqual(out.getvalue().strip(), 'CORRECT')

    @patch('sys.stdin', StringIO('3\n1 1 2\n2 -1 -1\n3 -1 -1'))
    def test_second(self):
        out = StringIO()
        check(out=out)
        self.assertEqual(out.getvalue().strip(), 'INCORRECT')

    @patch('sys.stdin', StringIO('0'))
    def test_third(self):
        out = StringIO()
        check(out=out)
        self.assertEqual(out.getvalue().strip(), 'CORRECT')

    @patch('sys.stdin', StringIO('5\n1 -1 1\n2 -1 2\n3 -1 3\n4 -1 4\n5 -1 -1'))
    def test_fourth(self):
        out = StringIO()
        check(out=out)
        self.assertEqual(out.getvalue().strip(), 'CORRECT')

    @patch('sys.stdin', StringIO('7\n4 1 2\n2 3 4\n6 5 6\n1 -1 -1\n'
                                 '3 -1 -1\n5 -1 -1\n7 -1 -1'))
    def test_fifth(self):
        out = StringIO()
        check(out=out)
        self.assertEqual(out.getvalue().strip(), 'CORRECT')

    @patch('sys.stdin', StringIO('4\n4 1 -1\n2 2 3\n1 -1 -1\n5 -1 -1'))
    def test_six(self):
        out = StringIO()
        check(out=out)
        self.assertEqual(out.getvalue().strip(), 'INCORRECT')




