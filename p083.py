#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Project Euler 83

Dijkstra.
'''

import operator
from numpy import array, shape


def dijkstra(g, source, target, weight):
    d = [None for i in range(vertex_count(g))]
    closed = [False for i in range(vertex_count(g))]
    d[source] = 0
    result = 0
    while True:
        u = None
        acc = None
        for i in range(vertex_count(g)):
            if not closed[i] and not d[i] is None:
                if acc is None or d[i] < acc:
                    acc = d[i]
                    u = i
        assert not u is None
        if u == target:
            result = acc
            break
        closed[u] = True
        for e in out_edges(g, u):
            v = edge_target(g, e)
            w = weight(e)
            if not closed[v] and (d[v] is None or acc + w < d[v]):
                d[v] = acc + w
    return result


def vertex_count(g):
    return len(g)


def edge_target(g, e):
    return g[e[0]][e[1]]


def out_edges(g, u):
    return [(u, v) for v in range(len(g[u]))]


def make_graph(mat):
    def index(row, col):
        return row * col_count(mat) + col

    n = row_count(mat) * col_count(mat)
    g = [[] for i in range(n)]
    for row in range(row_count(mat)):
        for col in range(col_count(mat)):
            u = index(row, col)
            if row > 0:
                g[u].append(index(row - 1, col))
            if col > 0:
                g[u].append(index(row, col - 1))
            if row < row_count(mat) - 1:
                g[u].append(index(row + 1, col))
            if col < col_count(mat) - 1:
                g[u].append(index(row, col + 1))
    return g


def solve(mat):
    g = make_graph(mat)

    def weight(e):
        def unindex(v):
            return v // col_count(mat), v % col_count(mat)
        return mat[unindex(edge_target(g, e))]

    return mat[0, 0] + dijkstra(g, 0, vertex_count(g) - 1, weight)


def row_count(mat):
    return shape(mat)[0]


def col_count(mat):
    return shape(mat)[1]


def read(filename):
    with open(filename, 'r') as f:
        return array([[int(word) for word in line.split(',')] for line in f])


#print(solve(read('p083.test.txt')))
print(solve(read('p083.matrix.txt')))
