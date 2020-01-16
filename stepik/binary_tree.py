from sys import stdout


def traverse(out=stdout):
    n = int(input())
    tree = [[] for _i in range(n)]
    for i in range(n):
        tree[i].extend(list(map(int, input().split())))
    in_order(tree, 0, out=out)
    out.write('\n')
    pre_order(tree, 0, out=out)
    out.write('\n')
    post_order(tree, 0, out=out)


def in_order(tree, node_idx, out=stdout):
    key = tree[node_idx][0]
    left = tree[node_idx][1]
    right = tree[node_idx][2]

    if left != -1:
        in_order(tree, left, out)
    out.write(str(key) + ' ')
    if right != -1:
        in_order(tree, right, out)


def pre_order(tree, node_idx, out):
    key = tree[node_idx][0]
    left = tree[node_idx][1]
    right = tree[node_idx][2]

    out.write(str(key) + ' ')
    if left != -1:
        pre_order(tree, left, out)
    if right != -1:
        pre_order(tree, right, out)


def post_order(tree, node_idx, out):
    key = tree[node_idx][0]
    left = tree[node_idx][1]
    right = tree[node_idx][2]

    if left != -1:
        post_order(tree, left, out)
    if right != -1:
        post_order(tree, right, out)
    out.write(str(key) + ' ')


if __name__ == '__main__':
    traverse()
