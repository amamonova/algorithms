def dummy_search(array, search_item):
    for idx in range(len(array)):
        if array[idx] == search_item:
            return idx
    return None


def binary_search(sorted_array, item):
    first, last = 0, len(sorted_array)
    while first < last:
        mid = (first + last) // 2
        if item < sorted_array[mid]:
            last = mid
        elif item > sorted_array[mid]:
            first = mid + 1
        else:
            return mid
    return None

