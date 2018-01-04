#!/usr/bin/env python
# coding:utf-8

import timeit
import math
from util import *


def special_pythagorean_triplet(num=1000):
    for a in range(1, num // 3):
        for b in range(a + 1, num // 2):
            c = num - a - b
            if c < b:
                break
            if a**2 + b**2 == c**2:
                print('{}*{}*{}={}'.format(a, b, c, a * b * c))
                return


def good(n=1000):
    # n is a + b + c where a**2+b**2=c**2
    sq = map(lambda x: x * x, range(0, n / 2 + 1))
    j, t = divmod(n, 2)
    t = 0
    for i in range(1, n / 4):
        while True:
            t += 1  # just an iteration counter
            c = ((sq[i] + sq[j]) ** 0.5)
            d = i + j + c
            if d > n:
                j -= 1
            elif d == n:
                print(i, j, c, i * j * c, t)
                return
            else:
                break


def special_pythagorean_triplet2(t=1000):
    for m in range(int(math.sqrt(t) / 2), int(math.sqrt(t / 2))):
        n = t / (2 * m) - m
        if m > n > 0 and n.is_integer():
            a, b, c = 2 * m * n, m * m - n * n, m * m + n * n
            return int(a * b * c)


def main():
    print timeit.timeit(stmt=good, number=1)
    print timeit.timeit(stmt=special_pythagorean_triplet, number=1)


if __name__ == '__main__':
    main()
