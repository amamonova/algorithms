import unittest
from sorting import selection_sort


class TestSort(unittest.TestCase):
    def test_empty(self):
        self.assertListEqual(selection_sort([]), [],
                             'Selection sort. Should be empty list.')

    def test_single(self):
        self.assertListEqual(selection_sort([42]), [42],
                             'Selection sort. Should be [42]')

    def test_sorted_array(self):
        self.assertListEqual(selection_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5],
                             'Selection sort. Should be [1, 2, 3, 4, 5]')

    def test_array(self):
        array = [42, 0, 422, 3]
        array_with_duplicates = [42, 42, 10, 0, 1, 2]
        reversed_array = [422, 42, 0]

        self.assertListEqual(selection_sort(array), sorted(array),
                             'Selection sort.')

        self.assertListEqual(selection_sort(array_with_duplicates),
                             sorted(array_with_duplicates),
                             'Selection sort. Wrong answer for '
                             'array with duplicates')

        self.assertListEqual(selection_sort(reversed_array),
                             sorted(reversed_array),
                             'Selection sort. Wrong answer for reversed array')


if __name__ == '__main__':
    unittest.main()
