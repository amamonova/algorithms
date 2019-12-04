import unittest
from mock import patch
from stepik.pattern_matching import find

from io import StringIO


class TestStepikPatternProblem(unittest.TestCase):
    @patch('sys.stdin', StringIO('aba\nabacaba'))
    def test_first(self):
        output_row = '0 4'
        self.assertEqual(find(), output_row)

    @patch('sys.stdin', StringIO('Test\ntestTesttesT'))
    def test_second(self):
        output_row = '4'
        self.assertEqual(find(), output_row)

    @patch('sys.stdin', StringIO('aaaaa\nbaaaaaaa'))
    def test_third(self):
        output_row = '1 2 3'
        self.assertEqual(find(), output_row)


if __name__ == '__main__':
    unittest.main()
