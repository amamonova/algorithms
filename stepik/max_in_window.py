import sys


class StackWithMax:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    def push(self, x):
        self.main_stack.append(x)
        if len(self.main_stack) == 1:
            self.max_stack.append(x)
            return

        if x > self.max_stack[-1]:
            self.max_stack.append(x)
        else:
            self.max_stack.append(self.max_stack[-1])

    def get_max(self):
        return self.max_stack[-1]

    def pop(self):
        self.max_stack.pop()
        return self.main_stack.pop()

    def is_empty(self):
        if self.main_stack:
            return False
        return True


class Queue(object):
    def __init__(self):
        self.put_stack = StackWithMax()
        self.out_stack = StackWithMax()

    def enqueue(self, item):
        self.put_stack.push(item)

    def dequeue(self):
        if self.out_stack.is_empty():
            while not self.put_stack.is_empty():
                self.out_stack.push(self.put_stack.pop())
        return self.out_stack.pop()

    def get_max(self):
        if self.out_stack.is_empty():
            return self.put_stack.get_max()
        elif self.put_stack.is_empty():
            return self.out_stack.get_max()
        else:
            return max(self.put_stack.get_max(),
                       self.out_stack.get_max())

    def pprint(self):
        print(f'out: {self.out_stack.main_stack}')
        print(f'in: {self.put_stack.main_stack}')


def find_max(out=sys.stdout):
    n = int(input())
    array = [int(x) for x in input().split()]
    win_size = int(input())
    q = Queue()
    for el in array[:win_size]:
        q.enqueue(el)

    out.write(str(q.get_max()))
    out.write(' ')

    for idx in range(n - win_size):
        q.enqueue(array[win_size + idx])
        q.dequeue()
        q.get_max()
        out.write(str(q.get_max()))
        out.write(' ')


if __name__ == '__main__':
    find_max()  



