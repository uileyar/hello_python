#!/usr/bin/env python
# coding:utf-8

import timeit
from util import *


def largest_palindrome_product():
    max_count = 0
    for n in range(100, 999):
        for m in range(100, 999):
            flag = True
            k = str(m * n)
            for i in range(0, len(k) / 2):
                if k[i] != k[-(i + 1)]:
                    flag = False
                    break
            if flag:
                max_count = max(max_count, int(k))
    print(max_count)


def main():
    print timeit.timeit(stmt=largest_palindrome_product, number=1)


if __name__ == '__main__':
    main()
