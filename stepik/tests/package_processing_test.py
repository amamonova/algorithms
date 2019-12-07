from io import StringIO
import unittest
from mock import patch

from stepik.package_processing import get_time


class TestStepikHandler(unittest.TestCase):
    @patch('sys.stdin', StringIO('1 0'))
    def test_first(self):
        out = StringIO()
        get_time(out=out)
        self.assertEqual(out.getvalue().strip(), '')

    @patch('sys.stdin', StringIO('1 1\n0 0'))
    def test_second(self):
        out = StringIO()
        get_time(out=out)
        self.assertEqual(out.getvalue().strip(), '0')

    @patch('sys.stdin', StringIO('1 2\n0 1\n0 1'))
    def test_third(self):
        out = StringIO()
        get_time(out=out)
        self.assertEqual(out.getvalue().strip(), '0\n-1')

    @patch('sys.stdin', StringIO('1 2\n0 1\n1 1'))
    def test_fourth(self):
        out = StringIO()
        get_time(out=out)
        self.assertEqual(out.getvalue().strip(), '0\n1')

    @patch('sys.stdin', StringIO('2 8\n0 0\n0 0\n0 0\n1 0\n'
                                 '1 0\n1 1\n1 2\n1 3'))
    def test_fifth(self):
        out = StringIO()
        get_time(out=out)
        self.assertEqual(out.getvalue().strip(), '0 0 0 1 '
                                                 '1 1 2 -1'.replace(' ', '\n'))


if __name__ == '__main__':
    unittest.main()
