#!/usr/bin/env python
# coding:utf-8

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import timeit
from util import *

MAX_NUM = 20


def _parse_num(num_list, num, parse_list):
    for k in num_list:
        if k >= num:
            break
        if num % k == 0:
            pk = num / k
            parse_list.append(k)
            return _parse_num(num_list, pk, parse_list)
    parse_list.append(num)


def smallest_multiple(max_num=MAX_NUM):
    smallest_num = 1
    num_list = []
    for n in range(2, max_num + 1):
        num_list.append(n)
    parse_list = {}
    for num in num_list:
        parse_list[num] = []
        _parse_num(num_list, num, parse_list[num])
    # print(parse_list)
    for num in num_list:
        count = 0
        for k, v in parse_list.items():
            c_max = 0
            for vv in v:
                if vv == num:
                    c_max += 1
            count = max(c_max, count)
        if count > 0:
            # print('{}={}'.format(num, count))
            smallest_num *= num**count
    print('self ={}'.format(smallest_num))


def good(max_num=MAX_NUM):
    i = 1
    for k in (range(1, max_num)):
        if i % k > 0:
            for j in range(1, max_num):
                if (i * j) % k == 0:
                    i *= j
                    break
    print('good ={}'.format(i))


def gcd(a, b):
    while b: a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


def PE1(max_num=MAX_NUM):
    ans = 1
    for i in xrange(2, max_num + 1):
        ans = lcm(i, ans)
    print('PE1 ={}'.format(ans))


#from common import primeSieve
from math import sqrt, log


def PE2(max_num=MAX_NUM):
    primes = primeSieve(max_num + 1)  # returns list of all primes <=N
    sqrtN = sqrt(max_num)
    ans = 1
    for p in primes:
        if p <= sqrtN:
            ans *= p ** (int(log(max_num) / log(p)))
        else:
            ans *= p


def main():
    print timeit.timeit(stmt=smallest_multiple, number=1)
    print timeit.timeit(stmt=good, number=1)
    print timeit.timeit(stmt=PE1, number=1)
    #print timeit.timeit(stmt=PE2, number=1)


if __name__ == '__main__':
    main()
