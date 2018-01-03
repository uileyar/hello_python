#!/usr/bin/env python
# coding:utf-8

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import timeit
import math
from util import *

MAX_NUM = 10001


def is_prime(n):
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
        if is_prime(n):
            prime_count += 1
    print('{}={}'.format(prime_count, n))


def is_prime_good(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    if n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = float(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
    return True


def good(max_num=MAX_NUM):
    prime_count = 1
    n = 1
    while prime_count < max_num:
        n += 2
        if is_prime_good(n):
            prime_count += 1
    print('{}={}'.format(prime_count, n))


def primes(n):
    '''
    http://en.wikipedia.org/wiki/Sieve_of_eratosthenes
    Generate primes using the sieve algorithm
    '''
    if n == 2:
        return [2]
    elif n < 2:
        return []
    s = range(3, n+1, 2)
    mroot = n ** 0.5
    half = ((n + 1) / 2) - 1
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m * m - 3) / 2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i += 1
        m = 2 * i + 3
    return [2] + [x for x in s if x]


def best(max_num=MAX_NUM):
    list = primes(max_num*20)
    print list[max_num-1]


def main():
    print timeit.timeit(stmt=st_prime, number=1)
    print timeit.timeit(stmt=good, number=1)
    print timeit.timeit(stmt=best, number=1)

if __name__ == '__main__':
    main()
