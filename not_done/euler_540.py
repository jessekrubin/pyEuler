#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Almost equilateral triangles
Problem 94
It is easily proved that no equilateral triangle exists with integral length
sides and integral area. However, the almost equilateral triangle 5-5-6 has
an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two
sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles w/ integral
side lengths and area and whose perimeters do not exceed one billion
(1,000,000,000).
"""
from math import sqrt, gcd
from itertools import count
from tqdm import tqdm
from bisect import bisect_left


# def p(n):
#     """
#     generates primative pythagorean triples w/ help frum 3Blue1Brown
#     special thanks to 3Blue1Brown's video on pythagorean triples
#     https://www.youtube.com/watch?v=QJYmyhnaaek&t=300s
#     """
#     print(n)
#     squares = [i*i for i in range(1, n+1)]
#     print("squares made")
#     total = 0
#     for reals in range(2, n, 2):
#         # if reals%10000 == 0:
#         #     print(reals)
#         for imaginaries in count(1):
#             sqrd = complex(reals, imaginaries)**2
#             real = abs(int(sqrd.real))
#             imaginary = int(sqrd.imag)
#             hypsq = (real * real) + (imaginary * imaginary)
#
#             hypotenuse = int(sqrt((real * real) + (imaginary * imaginary)))
#             print(100)
#             print(hypotenuse, bisect_left(squares, hypsq))
#             print(squares[bisect_left(squares, hypotenuse)])
#             print(len(squares))
#             if hypotenuse > n:
#                 break
#             if gcd(real, imaginary) == 1 and hypotenuse <= n:
#                 total += 1

def p(n):
    """
    generates primative pythagorean triples w/ help frum 3Blue1Brown
    special thanks to 3Blue1Brown's video on pythagorean triples
    https://www.youtube.com/watch?v=QJYmyhnaaek&t=300s
    """
    print(n)
    squares = [i*i for i in range(n+1)]
    print("squares made")
    total = 0
    for reals in range(2, n, 2):
        # if reals%10000 == 0:
        #     print(reals)
        for imaginaries in count(1):
            sqrd = complex(reals, imaginaries)**2
            real = int(sqrd.real)
            imaginary = int(sqrd.imag)
            hypsq = (real * real) + (imaginary * imaginary)
            hypotenuse = int(sqrt(hypsq))
            # print(100)
            # print(hypotenuse, bisect_left(squares, hypsq))
            # print(squares[bisect_left(squares, hypotenuse)])
            # print(len(squares))
            if hypotenuse > n:
                break
            if gcd(real, imaginary) == 1 and hypotenuse <= n:
                # total += 1
                print(complex(reals, imaginaries))
                print(complex(reals, imaginaries)*complex(reals, imaginaries))
                print(complex(reals, imaginaries).conjugate()*complex(reals, imaginaries))
                print(real, imaginary, hypotenuse)
                # yield (real, imaginary, hypotenuse)
    # for i in pytriples_gen(n):
    #     total += 1
    print(total)
    return total

def p540():
    print(p(20))
    # assert 3 == p(20)
    # assert 159139 == p(10**6)
    # answer = p(3141592653589793)
    # print(answer)

p540()
# print(answer)
# ans = P(1000000)
# print(ans)


