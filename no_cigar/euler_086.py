# -*- coding: utf-8 -*-
# ~ Jesse Rubin ~ project Euler ~
"""
Cuboid route
http://projecteuler.net/problem=86
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a
fly, F, sits in the opposite corner. By travelling on the surfaces of the room
the shortest "straight line" distance from S to F is 10 and the path is shown
on the diagram.

However, there are up to three "shortest" path candidates for any given cuboid
and the shortest route doesn't always have integer length. It can be shown that
there are exactly 2060 distinct cuboids, ignoring rotations, with integer
dimensions, up to a maximum size of M by M by M, for which the shortest route
has integer length when M = 100. This is the least value of M for which the
number of solutions first exceeds two thousand; the number of solutions
when M = 99 is 1975. Find the least value of M such that the number of
solutions first exceeds one million.
"""
from __future__ import division
from bib.maths import pytriple_gen, Vuple
from math import sqrt


def cuboid_routes(m):
    total = 0
    maxhp = sqrt(1 + (5 * (m**2)))
    for p in pytriple_gen(maxhp):
        trip = Vuple(p)
        while trip[0] <= m:
            cubs = set()
            for i in range(1, trip[0]):
                c = tuple(sorted([i, trip[0] - i, trip[1]]))
                if max(c) <= m:
                    cubs.add(c)
            if trip[1] - trip[0] <= trip[0]:
                for i in range(trip[1] - trip[0], (trip[1] // 2) + 2):
                    cubs.add(tuple(sorted([trip[0], trip[1] - i, i])))
            total += len(cubs)
            trip += Vuple(p)
    return total


assert 1975 == cuboid_routes(99)
assert 2060 == cuboid_routes(100)

# a = cuboid_routes(1816)
# print(a)
# a = cuboid_routes(1817)
# print(a)
# # a = cuboid_routes(1818) #ANSWER
# print(a)
# a = cuboid_routes(1819)
# print(a)
# a = cuboid_routes(1820)
# print(a)
# # for mm in count(100):
# #     ans = (cuboid_routes(mm))
# #     print(ans, mm)
# #     if ans > 1000000:
# #         break
#
#


def p086():
    pass


if __name__ == "__main__":
    p086()
