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
from itertools import count
from lib.maths import gcd_cash_muny
from math import sqrt
from tqdm import tqdm
from bisect import bisect_left

# def pytriplets_gen(n):
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


# def pytriplets_gen(max_c):
#     """
#     generates primative pythagorean triples w/ help frum 3Blue1Brown
#     special thanks to 3Blue1Brown's video on pythagorean triples
#     https://www.youtube.com/watch?v=QJYmyhnaaek&t=300s
#     """
#     print(max_c)
#     squares = [i * i for i in range(max_c + 1)]
#     print("squares made")
#
#     prims = []
#     total = 0
#     for reals in range(2, max_c, 1):
#         # if reals%10000 == 0:
#         #     print(reals)
#         # for imaginaries in count(1):
#         for imaginaries in range(1, reals):
#             complexnum = complex(reals, imaginaries)
#             sqrd = complexnum * complexnum
#             real = abs(int(sqrd.real))
#             imaginary = int(sqrd.imag)
#             hypsq = (real * real) + (imaginary * imaginary)
#             # hypotenuse = int(sqrt(hypsq)) # retired in favor of bisect
#             sea_sqrt = bisect_left(squares, hypsq)
#             sea = int((complexnum*complexnum.conjugate()).real)
#             # print(100)
#             # print(len(squares))
#             if sea_sqrt > max_c:
#                 break
#             if gcd_cash_muny(real, imaginary) == 1 and sea_sqrt <= max_c:
#                 # total += 1
#                 print("___")
#                 print(sea_sqrt, bisect_left(squares, hypsq))
#                 print("complex", complex(reals, imaginaries))
#                 print("complex conj", complex(reals, imaginaries).conjugate())
#                 print("complex squared",
#                       complex(reals, imaginaries) * complex(reals, imaginaries))
#                 print( "conj times complex",
#                        complex(reals, imaginaries).conjugate() * complex(
#                            reals, imaginaries))
#                 print(real, imaginary, sea_sqrt)
#                 print(real, imaginary, sea)
#                 primative = []
#                 if real > imaginary:
#                     primative = tuple([imaginary, real, sea])
#                 else:
#                     primative = tuple([real, imaginary, sea])
#                 prims.append(primative)
#                 # print(sum((real, imaginary, sea_sqrt)))
#                 # yield (real, imaginary, hypotenuse)
#     # for i in pytriples_gen(n):
#     #     total += 1
#     print(total)
#     print(len(prims))
#     print(prims)
#     return total

def pytriplets_gen(max_c):
    """
    generates primative pythagorean triples w/ help frum 3Blue1Brown
    special thanks to 3Blue1Brown's video on pythagorean triples
    https://www.youtube.com/watch?v=QJYmyhnaaek&t=300s
    """
    for real_pts in range(2, max_c, 1):
        for imag_pts in range(1, real_pts):
            contrived_n = complex(real_pts, imag_pts)
            sqrd = contrived_n * contrived_n
            real = abs(int(sqrd.real))
            imag = int(sqrd.imag)
            sea = int((contrived_n*contrived_n.conjugate()).real)
            if sea > max_c:
                break
            if gcd_cash_muny(real, imag) == 1 and sea <= max_c:
                # total += 1
                # print("___")
                # print(sea_sqrt, bisect_left(squares, hypsq))
                # print("complex", complex(reals, imaginaries))
                # print("complex conj", complex(reals, imaginaries).conjugate())
                # print("complex squared",
                #     complex(reals, imaginaries) * complex(reals, imaginaries))
                # print( "conj times complex",
                #     complex(reals, imaginaries).conjugate() * complex(
                #         reals, imaginaries))
                # print(real, imaginary, sea_sqrt)
                # print(real, imaginary, sea)
                if real > imag:
                    yield (imag, real, sea)
                else:
                    yield (real, imag, sea)

underhund = set(triplet for triplet in pytriplets_gen(100))
print(underhund)

# def test_prime
should_be = set([(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
                 (20, 21, 29), (9, 40, 41), (12, 35, 37), (11, 60, 61),
                 (28, 45, 53), (33, 56, 65), (13, 84, 85), (16, 63, 65),
                 (48, 55, 73), (39, 80, 89), (36, 77, 85), (65, 72, 97)])

print(underhund == should_be)
primatives = [[3, 4, 5], [5, 12, 13], [8, 15, 17],
              [7, 24, 25], [20, 21, 29], [12, 35, 37],
              [9, 40, 41], [28, 45, 53], [11, 60, 61],
              [16, 63, 65], [33, 56, 65], [48, 55, 73],
              [13, 84, 85], [36, 77, 85], [39, 80, 89],
              [65, 72, 97]]

non_primative = [[6, 8, 10], [9, 12, 15], [12, 16, 20], [15, 20, 25],
                 [10, 24, 26], [18, 24, 30], [16, 30, 34], [21, 28, 35],
                 [15, 36, 39], [24, 32, 40], [27, 36, 45], [14, 48, 50],
                 [30, 40, 50], [24, 45, 51], [20, 48, 52], [33, 44, 55],
                 [40, 42, 58], [36, 48, 60], [25, 60, 65], [39, 52, 65],
                 [32, 60, 68], [42, 56, 70], [24, 70, 74], [21, 72, 75],
                 [45, 60, 75], [30, 72, 78], [48, 64, 80], [18, 80, 82],
                 [40, 75, 85], [51, 68, 85], [60, 63, 87], [54, 72, 90],
                 [35, 84, 91], [57, 76, 95]]

print("____")
def testing(a, b):
    comp = complex(a, b)
    print("complex", comp)
    print("complex sq", comp**2)
    print("complex sq", comp*comp.conjugate())

testing(1, 2)
testing(2, 1)

# def p540():
#     # print(pytriplets_gen(20))
#     print(pytriplets_gen(100))
    # assert 3 == pytriplets_gen(20)
    # assert 159139 == pytriplets_gen(10**6)
    # answer = pytriplets_gen(3141592653589793)
    # print(answer)


# p540()
# print(answer)
# ans = P(1000000)
# print(ans)
