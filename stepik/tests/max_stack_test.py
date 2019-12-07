from io import StringIO
import unittest
from mock import patch

from stepik.max_stack import get_max


class TestStepikMaxStack(unittest.TestCase):
    @patch('sys.stdin', StringIO('3\npush 1\npush 7\npop'))
    def test_first(self):
        out = StringIO()
        get_max(out=out)
        self.assertEqual(out.getvalue().strip(), '')

    @patch('sys.stdin', StringIO('5\npush 2\npush 1\nmax\npop\nmax'))
    def test_second(self):
        out = StringIO()
        get_max(out=out)
        self.assertEqual(out.getvalue().strip(), '2\n2')

    @patch('sys.stdin', StringIO('6\npush 7\npush 1\npush 7\nmax\npop\nmax'))
    def test_third(self):
        out = StringIO()
        get_max(out=out)
        self.assertEqual(out.getvalue().strip(), '7\n7')

    @patch('sys.stdin', StringIO('5\npush 1\npush 2\nmax\npop\nmax'))
    def test_fourth(self):
        out = StringIO()
        get_max(out=out)
        self.assertEqual(out.getvalue().strip(), '2\n1')

    @patch('sys.stdin', StringIO('10\npush 2\npush 3\npush 9\npush 7\n'
                                 'push 2\nmax\nmax\nmax\npop\nmax'))
    def test_fifth(self):
        out = StringIO()
        get_max(out=out)
        self.assertEqual(out.getvalue().strip(), '9 9 9 9'.replace(' ', '\n'))


if __name__ == '__main__':
    unittest.main()
