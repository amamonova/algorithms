import sys


class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []
        self.len_stack = 0

    def top(self, stack):
        return stack[-1]

    def push(self, item):
        if not self.len_stack:
            self.max_stack.append(item)
        else:
            if self.top(self.max_stack) < item:
                self.max_stack.append(item)
            else:
                self.max_stack.append(self.top(self.max_stack))
        self.stack.append(item)
        self.len_stack += 1

    def pop(self):
        del self.stack[-1]
        del self.max_stack[-1]
        self.len_stack -= 1

    def max(self):
        return self.top(self.max_stack)


def get_max(out=sys.stdout):
    n = int(input())
    s = Stack()

    for i_ in range(n):
        line = input().split()
        if len(line) == 2:
            command, item = line
            s.push(int(item))
        else:
            command = line[0]
            if command == 'max':
                out.write(str(s.max()))
                out.write('\n')
            elif command == 'pop':
                s.pop()


if __name__ == '__main__':
    get_max()
