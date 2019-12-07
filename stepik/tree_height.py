import sys


def get_height(out=sys.stdout):
    n, parents = int(input()), [int(i) for i in input().split()]
    a = [[] for i_ in range(n + 1)]
    for i in range(n):
        a[parents[i]] += [i]

    root, height = a[-1], 0
    while len(root):
        q, root = root, []
        for b in q:
            root += a[b]
            print(root)
        height += 1
    out.write(str(height))


if __name__ == '__main__':
    get_height()

