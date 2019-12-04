import unittest
from stepik.hashtable_phonebook import phonebook
from unittest.mock import patch
from io import StringIO


class TestStepikTask(unittest.TestCase):

    @patch("sys.stdin", StringIO('12\nadd 911 police\nadd 76213 Mom\n'
                                 'add 17239 Bob\nfind 76213\nfind 910\n'
                                 'find 911\ndel 910\ndel 911\nfind 911\n'
                                 'find 76213\nadd 76213 daddy\nfind 76213'))
    def test_naive(self):
        output_row = 'Mom\nnot found\npolice\nnot found\nMom\ndaddy'
        self.assertEqual(phonebook(), output_row)

    @patch("sys.stdin", StringIO('8\nfind 3839442\nadd 123456 me\n'
                                 'add 0 granny\nfind 0\nfind 123456\n'
                                 'del 0\ndel 0\nfind 0'))
    def test_second(self):
        output_row = 'not found\ngranny\nme\nnot found'
        self.assertEqual(phonebook(), output_row)


if __name__ == '__main__':
    unittest.main()

