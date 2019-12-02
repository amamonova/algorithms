import unittest
from stepik.chaining import chain
from unittest.mock import patch
from io import StringIO


class TestStepikChaining(unittest.TestCase):

    @patch("sys.stdin", StringIO('5\n12\nadd world\nadd HellO\ncheck 4\n'
                                 'find World\nfind world\ndel world\n'
                                 'check 4\ndel HellO\nadd luck\nadd GooD\n'
                                 'check 2\ndel good'))
    def test_first(self):
        output_row = 'HellO world\nno\nyes\nHellO\nGooD luck'
        self.assertEqual(chain(), output_row)

    @patch("sys.stdin", StringIO('4\n8\nadd test\nadd test\nfind test\n'
                                 'del test\nfind test\nfind Test\n'
                                 'add Test\nfind Test'))
    def test_second(self):
        output_row = 'yes\nno\nno\nyes'
        self.assertEqual(chain(), output_row)

    @patch('sys.stdin', StringIO('3\n12\ncheck 0\nfind help\nadd help\n'
                                 'add del\nadd add\nfind add\nfind del\n'
                                 'del del\nfind del\ncheck 0\ncheck 1\n'
                                 'check 2'))
    def test_third(self):
        output_row = '\nno\nyes\nyes\nno\n\nadd help\n'


if __name__ == '__main__':
    unittest.main()

