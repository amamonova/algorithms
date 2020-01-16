from sys import stdout
from io import StringIO
from stepik.binary_tree import in_order


def check(out=stdout):
    flag = False
    n = int(input())
    if n == 0:
        out.write('CORRECT')
        return
    tree = [[] for _i in range(n)]
    for i in range(n):
        tree[i].extend(list(map(int, input().split())))

    res_out = StringIO()
    in_order(tree, 0, res_out)
    res_out = res_out.getvalue().strip()
    res = [int(x) for x in res_out.split()]

    for i in range(len(res)-1):
        if res[i] < res[i+1]:
            flag = True
        else:
            flag = False
            break
    if flag:
        out.write('CORRECT')
    else:
        out.write('INCORRECT')


if __name__ == '__main__':
    check()
