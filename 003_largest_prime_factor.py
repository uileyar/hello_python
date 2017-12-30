#!/usr/bin/env python
# coding:utf-8

import timeit
from util import *


def largest_prime_factor(number=600851475143):
    i = 2
    while i < number/2:
        if number % i == 0:
            print('{}'.format(i))
            largest_prime_factor(number/i)
            return
        i += 1
    print number


def main():
    print timeit.timeit(stmt=largest_prime_factor, number=1)


if __name__ == '__main__':
    main()
