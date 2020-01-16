import unittest
from stepik.binary_tree import traverse
from unittest.mock import patch
from io import StringIO


class TestStepikBinTree(unittest.TestCase):
    @patch('sys.stdin', StringIO('10\n0 7 2\n10 -1 -1\n20 -1 6\n30 8 9\n'
                                 '40 3 -1\n50 -1 -1\n60 1 -1\n70 5 4\n'
                                 '80 -1 -1\n90 -1 -1'))
    def test_first(self):
        out = StringIO()
        traverse(out=out)
        self.assertEqual(out.getvalue().strip(),
                         '50 70 80 30 90 40 0 20 10 60'
                         '\n0 70 50 40 30 80 90 20 60 10'
                         '\n50 80 90 30 40 70 10 60 20 0')

    @patch('sys.stdin', StringIO('5\n4 1 2\n2 3 4\n5 -1 -1\n1 -1 -1\n3 -1 -1'))
    def test_second(self):
        out = StringIO()
        traverse(out=out)
        self.assertEqual(out.getvalue().strip(), '1 2 3 4 5\n4 2 1 3 5\n'
                                                 '1 3 2 5 4')


if __name__ == '__main__':
    unittest.main()
