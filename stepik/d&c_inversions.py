def inversions_num_naive(array):
    count = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if i < j and array[i] > array[j]:
                count += 1
    return count


def merge_sort_inversions(arr):
    if len(arr) == 1:
        return arr, 0

    m = len(arr) // 2
    left_arr = arr[:m]
    right_array = arr[m:]

    left_arr, left_inv = merge_sort_inversions(left_arr)
    right_array, right_inv = merge_sort_inversions(right_array)

    result = []
    i = 0
    j = 0
    inversions = 0 + left_inv + right_inv

    while i < len(left_arr) and j < len(right_array):
        if left_arr[i] <= right_array[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_array[j])
            j += 1
            inversions += (len(left_arr) - i)

    result += left_arr[i:]
    result += right_array[j:]

    return result, inversions


if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    print(merge_sort_inversions(array)[1])
