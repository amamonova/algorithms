def karatsuba(x, y):
    """
    :param x: positive number
    :param y: positive number
    :return: the product of x and y

    D&C algorithm for multiplication of integers.
    """
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        m = max(len(str(x)), len(str(y)))

        xl, xr = x // 10 ** (m // 2), x % 10 ** (m // 2)
        yl, yr = y // 10 ** (m // 2), y % 10 ** (m // 2)

        p1 = karatsuba(xl, yl)
        p2 = karatsuba(xr, yr)
        p3 = karatsuba(xl + xr, yl + yr)

        return 10 ** m * p1 + p2 + 10 ** (m // 2) * (p3 - p2 - p1)


if __name__ == '__main__':
    print(karatsuba(10, 30))
