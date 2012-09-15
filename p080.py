#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Project Euler 80
use integer rather than float
'''

from itertools import takewhile
from math import sqrt


def total(n):
    def inner(n, root):
        def last(seq):
            return list(seq)[-1]

        if len(str(root)) == 100:
            return sum(map(int, str(root)))
        return inner(n * 100, last(takewhile(
            lambda r: r * r <= n * 100,
            map(lambda n: n + root * 10, range(10))
            )))

    return sum(map(lambda n: inner(n, int(sqrt(n))), range(1, n)))


# remove rational numbers 1 + 2 + ... + 9
print(total(100) - 45)
