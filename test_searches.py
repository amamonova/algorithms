import unittest
from searches import dummy_search, binary_search


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.search_functions = [dummy_search, binary_search]

    def search_test(self, search_func):
        self.assertEqual(search_func([0, 1, 2, 3, 5, 6], 3), 3,
                         f'Fail in {search_func.__name__.upper()}. '
                         'Simple checker. Should be 3.')
        self.assertEqual(search_func([1], 1), 0,
                         f'Fail in {search_func.__name__.upper()}. '
                         'Single item checker. Should be 0')
        self.assertEqual(search_func([0, 3, 10], 5), None,
                         f'Fail in {search_func.__name__.upper()}. '
                         'None checker. Should be None')
        self.assertEqual(search_func([2, 4, 100], 2), 0,
                         f'Fail in {search_func.__name__.upper()}. '
                         'First item checker. Should be 2')
        self.assertEqual(search_func([2, 4, 100], 100), 2,
                         f'Fail in {search_func.__name__.upper()}. '
                         'Last item checker. Should be 2')
        self.assertEqual(search_func([], 100), None,
                         f'Fail in {search_func.__name__.upper()}. '
                         'Empty checker. Should be None')

    def test_searches(self):
        for s_f in self.search_functions:
            self.search_test(s_f)


if __name__ == '__main__':
    unittest.main()

