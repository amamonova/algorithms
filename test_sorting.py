import unittest
from sorting import selection_sort, quick_sort, insertion_sort, merge_sort, \
    quick_sort2


class TestSort(unittest.TestCase):
    def setUp(self):
        self.sort_funcs = [selection_sort, quick_sort, insertion_sort,
                           merge_sort, quick_sort2]

    def empty_test(self, sort_func):
        self.assertListEqual(sort_func([]), [],
                             f'Fail in {sort_func.__name__.upper()}. '
                             'Selection sort. Should be empty list.')

    def single_test(self, sort_func):
        self.assertListEqual(sort_func([42]), [42],
                             f'Fail in {sort_func.__name__.upper()}. '
                             'Selection sort. Should be [42]')

    def sorted_array_test(self, sort_func):
        self.assertListEqual(sort_func([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5],
                             f'Fail in {sort_func.__name__.upper()}. '
                             'Selection sort. Should be [1, 2, 3, 4, 5]')

    def array_test(self, sort_func):
        array = [42, 0, 422, 3]
        array_with_duplicates = [42, 42, 10, 0, 1, 2]
        reversed_array = [422, 42, 0]

        self.assertListEqual(sort_func(array), sorted(array),
                             f'Fail in {sort_func.__name__.upper()}. '
                             'Simple check.')

        self.assertListEqual(sort_func(array_with_duplicates),
                             sorted(array_with_duplicates),
                             f'Fail in {sort_func.__name__.upper()}. '
                             'Wrong answer for array with duplicates.')

        self.assertListEqual(sort_func(reversed_array),
                             sorted(reversed_array),
                             f'Fail in {sort_func.__name__.upper()}. '
                             'Wrong answer for reversed array.')

    def test_sort(self):
        for s_f in self.sort_funcs:
            self.empty_test(s_f)
            self.single_test(s_f)
            self.sorted_array_test(s_f)
            self.array_test(s_f)


if __name__ == '__main__':
    unittest.main()
