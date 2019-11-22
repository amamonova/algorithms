from copy import deepcopy


def find_min(array):
    min_item = array[0]

    for item in array:
        if item < min_item:
            min_item = item
    return min_item


def selection_sort(array):
    deepcopy_array = deepcopy(array)
    sorted_array = []
    while len(deepcopy_array) != 0:
        min_item = find_min(deepcopy_array)
        sorted_array.append(min_item)
        deepcopy_array.pop(deepcopy_array.index(min_item))
    return sorted_array


if __name__ == '__main__':
    print(selection_sort([42, 0, 422, 3]))
