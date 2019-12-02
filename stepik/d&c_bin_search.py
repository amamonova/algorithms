def bin_search(array, item):
    left = 0
    right = len(array) - 1
    while right >= left:
        med = (right + left) // 2
        if item == array[med]:
            return med + 1
        elif item < array[med]:
            right = med - 1
        elif item > array[med]:
            left = med + 1
    return -1


if __name__ == '__main__':
    row1 = list(map(int, input().split()))[1:]
    row2 = list(map(int, input().split()))[1:]
    print(*[bin_search(row1, x) for x in row2])

