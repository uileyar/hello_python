#!/usr/bin/env python
# coding:utf-8

from util import *


@spend_time
def multiples_1(max_count):
    count = 0
    for step in [3, 5]:
        for n in range(0, max_count, step):
            count += n
    for n in range(0, max_count, 3*5):
        count -= n
    print count


@spend_time
def multiples_1_bad(max_count):
    count = 0
    for n in range(0, max_count):
        if n % 3 == 0 or n % 5 == 0:
            count += n
    print count


@spend_time
def multiples_1_best(max_count):
    max_count = max_count - 1

    def mcp1(n, m_count):
        fl = float(m_count / n)
        return int(n * fl * (fl + 1) / 2)
    count = mcp1(3, max_count) + mcp1(5, max_count) - mcp1(15, max_count)
    print count


def main():
    max_count = 100000000
    multiples_1_best(max_count)
    multiples_1(max_count)
    #multiples_1_bad(max_count)
    pass


if __name__ == '__main__':
    main()
