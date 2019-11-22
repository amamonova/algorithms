import unittest
from searches import dummy_search, binary_search


class TestSearch(unittest.TestCase):
    def test_dummy_search(self):
        self.assertEqual(dummy_search([0, 1, 2, 3, 5, 6], 3), 3,
                         'Simple checker. Should be 3')
        self.assertEqual(dummy_search([1], 1), 0,
                         'Single item checker. Should be 0')
        self.assertEqual(dummy_search([0, 3, 10], 5), None,
                         'None checker. Should be None')
        self.assertEqual(dummy_search([2, 4, 100], 2), 0,
                         'First item checker. Should be 2')
        self.assertEqual(dummy_search([2, 4, 100], 100), 2,
                         'Last item checker. Should be 2')
        self.assertEqual(dummy_search([], 100), None,
                         'Empty checker. Should be None')

    def test_binary_search(self):
        self.assertEqual(binary_search([0, 1, 2, 3, 5, 6], 3), 3,
                         'Simple checker. Should be 3')
        self.assertEqual(binary_search([1], 1), 0,
                         'Single item checker. Should be 0')
        self.assertEqual(binary_search([0, 3, 10], 5), None,
                         'None checker. Should be None')
        self.assertEqual(binary_search([2, 4, 100], 2), 0,
                         'First item checker. Should be 2')
        self.assertEqual(binary_search([2, 4, 100], 100), 2,
                         'Last item checker. Should be 2')
        self.assertEqual(binary_search([], 100), None,
                         'Empty checker. Should be None')


if __name__ == '__main__':
    unittest.main()

