from datetime import datetime
import time


class Timer:
    """Context manager for timing"""

    def __init__(self):
        self.start, self.final = None, None

    def __enter__(self):
        self.start = datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.final = datetime.now()
        self.delta = (self.final - self.start).total_seconds()


if __name__ == '__main__':
    def foo():
        time.sleep(1)
    t = Timer()
    with t:
        foo()
    print(t.delta)
