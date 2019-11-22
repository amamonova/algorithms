def rec_sum(array):
    if len(array) == 0:
        return 0
    return array[0] + rec_sum(array[1:])


def rec_len(array):
    if len(array) == 0:
        return 0
    return 1 + rec_len(array[1:])


def rec_max(array):
    if len(array) == 1:
        return array[0]
    else:
        cur_max = rec_max(array[1:])
        return array[0] if array[0] > cur_max else cur_max


if __name__ == '__main__':
    print(rec_len([0, 1]))
    print(rec_max([5, 22, 3]))
