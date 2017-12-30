#!/usr/bin/env python
# coding:utf-8

import timeit
from util import *

MAX_NUM = 10000
def sum_square_difference(max_num=MAX_NUM):
    sq1 = sq2 = 0
    for n in range(1, max_num+1):
        sq1 += n*n
        sq2 += n
    diff = sq2*sq2 - sq1
    print(diff)


def good(max_num=MAX_NUM):
    sum = max_num * (max_num + 1) / 2
    sum_sq = (2 * max_num + 1) * (max_num + 1) * max_num / 6
    print sum * sum - sum_sq


def main():
    print timeit.timeit(stmt=sum_square_difference, number=1)
    print timeit.timeit(stmt=good, number=1)

if __name__ == '__main__':
    main()
