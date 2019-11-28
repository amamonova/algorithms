from bisect import bisect_left, bisect_right
from sys import stdin, stdout


if __name__ == "__main__":
    begins, ends = [], []
    n, m = [int(x) for x in stdin.readline().split()]
    for i in range(n):
        current = stdin.readline().split()
        begins.append(int(current[0]))
        ends.append(int(current[1]))
    dots = [int(x) for x in stdin.readline().split()]

    results = []
    begins = sorted(begins)
    ends = sorted(ends)

    for dot in dots:
        m_beg = bisect_right(begins, dot)
        m_end = bisect_left(ends, dot)
        stdout.write(str(m_beg - m_end) + ' ')
