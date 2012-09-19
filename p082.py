#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Project Euler 82

2D dynamic programming.
'''

from numpy import array, shape, sum


def memo(f):
    d = dict()
    def inner(*args):
        if not args in d:
            d[args] = f(*args)
        return d[args]

    return inner


def f(mat):
    @memo
    def g(row, col):
        if col == 0:
            return mat[row,col]
        return min(map(
            lambda i: g(i, col - 1) + sum(mat[min(i, row):max(i, row) + 1, col]),
            range(shape(mat)[0])
            ))

    return min(map(lambda row: g(row, shape(mat)[1] - 1), range(shape(mat)[0])))


def read(filename):
    with open(filename, 'r') as f:
        return array([[int(word) for word in line.split(',')] for line in f])


#print(f(read('p082.test.txt')))
print(f(read('p082.matrix.txt')))
