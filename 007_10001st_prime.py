#!/usr/bin/env python
# coding:utf-8

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import timeit
import math
from util import *

MAX_NUM = 10001


def is_prime_my(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def st_prime(max_num=MAX_NUM):
    prime_count = 1
    n = 1
    while prime_count < max_num:
        n += 2
        if is_prime_my(n):
            prime_count += 1
    print('{}={}'.format(prime_count, n))


def good(max_num=MAX_NUM):
    prime_count = 1
    n = 1
    while prime_count < max_num:
        n += 2
        if is_prime(n):
            prime_count += 1
    print('{}={}'.format(prime_count, n))


def best(max_num=MAX_NUM):
    prime_list = primes(max_num*20)
    print prime_list[max_num-1]


def main():
    print timeit.timeit(stmt=st_prime, number=1)
    print timeit.timeit(stmt=good, number=1)
    print timeit.timeit(stmt=best, number=1)

if __name__ == '__main__':
    main()
