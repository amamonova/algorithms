from io import StringIO
import unittest
from mock import patch
from stepik.max_in_window import find_max


class TestStepikMaxWindow(unittest.TestCase):

    @patch('sys.stdin', StringIO('8\n2 7 3 1 5 2 6 2\n4'))
    def test_first(self):
        out = StringIO()
        find_max(out=out)
        output = out.getvalue().strip()
        self.assertEqual(output, '7 7 5 6 6')

    @patch('sys.stdin', StringIO('3\n2 1 5\n1'))
    def test_second(self):
        out = StringIO()
        find_max(out=out)
        output = out.getvalue().strip()
        self.assertEqual(output, '2 1 5')

    @patch('sys.stdin', StringIO('3\n2 3 9\n3'))
    def test_third(self):
        out = StringIO()
        find_max(out=out)
        output = out.getvalue().strip()
        self.assertEqual(output, '9')


if __name__ == '__main__':
    unittest.main()
