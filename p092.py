#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
project euler 092
recurse and memo
'''

N = 10000000
memo = [0 for i in range(N)]

def f(n):
    def inner(n):
        return n if n in (1, 89) else f(sum(map(lambda s: int(s) ** 2, str(n))))
    if not memo[n]:
        memo[n] = inner(n)
    return memo[n]

count = 0
for i in range(1, N):
    if f(i) == 89:
        #print('now %d' % i)
        count += 1
print(count)
