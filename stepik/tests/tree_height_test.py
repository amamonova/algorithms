from io import StringIO
import unittest
from mock import patch

from stepik.tree_height import get_height


class TestStepikTreeHeight(unittest.TestCase):
    @patch('sys.stdin', StringIO('5\n4 -1 4 1 1'))
    def test_first(self):
        out = StringIO()
        get_height(out=out)
        self.assertEqual(out.getvalue().strip(), '3')

    @patch('sys.stdin', StringIO('5\n-1 0 4 0 3'))
    def test_second(self):
        out = StringIO()
        get_height(out=out)
        self.assertEqual(out.getvalue().strip(), '4')


if __name__ == '__main__':
    unittest.main()
