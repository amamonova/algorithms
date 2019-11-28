from copy import deepcopy
import random


def find_min(array):
    min_item = array[0]

    for item in array:
        if item < min_item:
            min_item = item
    return min_item


def selection_sort(array):
    deepcopy_array = deepcopy(array)
    sorted_array = []
    while len(deepcopy_array):
        min_item = find_min(deepcopy_array)
        sorted_array.append(min_item)
        deepcopy_array.pop(deepcopy_array.index(min_item))
    return sorted_array


def insertion_sort(array):
    for idx in range(1, len(array)):
        j = idx
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array


def merge(left_arr, right_arr):
    result = []
    left_pointer, right_pointer = 0, 0

    while left_pointer < len(left_arr) and \
            right_pointer < len(right_arr):
        if left_arr[left_pointer] < right_arr[right_pointer]:
            result.append(left_arr[left_pointer])
            left_pointer += 1
        else:
            result.append(right_arr[right_pointer])
            right_pointer += 1
    result += right_arr[right_pointer:]
    result += left_arr[left_pointer:]
    return result


def merge_sort(array):
    if len(array) <= 1:
        return array
    m = len(array) // 2
    left = merge_sort(array[:m])
    right = merge_sort(array[m:])
    return merge(left, right)


def quick_sort(array):
    if len(array) < 2:
        return array
    pivot_idx = random.choice(range(len(array)))
    less_array = [x for x in array if x < array[pivot_idx]]
    greater_array = [x for x in array if x > array[pivot_idx]]
    equal_array = [x for x in array if x == array[pivot_idx]]
    return quick_sort(less_array) + equal_array + quick_sort(greater_array)


def partition(array, left, right):
    pivot_idx = left
    for i in range(left, right):
        if array[i] < array[right]:
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
            pivot_idx += 1
    array[right], array[pivot_idx] = array[pivot_idx], array[right]
    return pivot_idx


def inner_quick_sort2(array, left, right):
    if right > left:
        pivot = partition(array, left, right)
        inner_quick_sort2(array, left, pivot-1)
        inner_quick_sort2(array, pivot+1, right)
    return array


def quick_sort2(array):
    return inner_quick_sort2(array, 0, len(array)-1)


if __name__ == '__main__':
    print(quick_sort2([42, 0, 422, 3]))