import sys


class Buffer:
    def __init__(self, buf_size):
        self.log = []
        self.buffer = []
        self.proc = 0
        self.size = buf_size

    def check(self, time):
        if self.buffer:
            while self.buffer and self.buffer[0] <= time:
                self.buffer.remove(self.buffer[0])
            if len(self.buffer) < self.size:
                return True
        else:
            return True
        return False

    def push(self, time, duration):
        if self.buffer:
            if time > self.buffer[-1]:
                self.log.append(time)
            else:
                self.log.append(self.buffer[-1])
        else:
            if time > self.proc:
                self.log.append(time)
                self.proc = self.log[-1] + duration
            else:
                self.log.append(self.proc)

        self.buffer.append(self.log[-1] + duration)

    def add_package(self, time, duration):
        if self.check(time):
            self.push(time, duration)
        else:
            self.log.append(-1)


def get_time(out=sys.stdout):
    size, n = list(map(int, input().split()))
    buf = Buffer(size)
    for i_ in range(n):
        arr, dur = list(map(int, input().split()))
        buf.add_package(arr, dur)
    for x in buf.log:
        out.write(str(x))
        out.write('\n')


if __name__ == '__main__':
    get_time()
