#!/usr/bin/env python
# coding:utf-8

import timeit
import math
from util import *

MAX_NUM = 2000000


def summation_of_primes(max_num=MAX_NUM):
    total = 2 + 3
    n = 5
    while n <= max_num:
        if is_prime(n):
            total += n
        n += 2
        if n < max_num and is_prime(n):
            total += n
        n += 4
    print('{}={}'.format(n, total))


def best(max_num=MAX_NUM):
    total = n = 0
    prime_list = primes(max_num)
    for n in prime_list:
        if n < max_num:
            total += n
    print('{}={}'.format(n, total))


def main():
    print timeit.timeit(stmt=best, number=1)
    print timeit.timeit(stmt=summation_of_primes, number=1)


if __name__ == '__main__':
    main()
