#!/usr/bin/env python
# coding:utf-8

import timeit
from util import *

MAX_COUNT = 4000000


def fibonacci_1(max_count=MAX_COUNT):
    count = 0
    k = begin = 1
    while k < max_count:
        k, begin = begin, begin + k
        if k & 1 == 0:
            count += k
    print count


def main():
    print timeit.timeit(stmt=fibonacci_1, number=1)


if __name__ == '__main__':
    main()
