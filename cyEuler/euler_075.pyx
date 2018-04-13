#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Singular integer right triangles
Problem 75
It turns out that 12 cm is the smallest length of wire that can be bent to
form an integer sided right angle triangle in exactly one way, but there are
many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
integer sided right angle triangle, and other lengths allow more than one
solution to be found; for example, using 120 cm it is possible to form
exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of
L ≤ 1,500,000 can exactly one integer sided right angle triangle
be formed?
"""

from math import sqrt, gcd
from itertools import count
from collections import defaultdict
from tqdm import tqdm
import bisect

# def triangles(limit):
#     L = limit
#     L += 1
#     range_lim = int(sqrt(L))+2
#     tri_perims = [0] * (L+1)
#     squares2 = [i**2 for i in range(0, L//2)]
#     nsq = len(squares2)
#     print("found squares")
#     max_square = squares2[-1]
#     for a in tqdm(range(1, nsq-2)):
#         asq = squares2[a]
#
#         bind = bisect.bisect_left(squares2, max_square-asq)
#         # print(max_square, asq, bind)
#         for b in range(a+1, bind):
#         # for b in range(a+1, nsq-1):
#             csq = asq + squares2[b]
#             if csq > max_square:
#                 break
#             ind = bisect.bisect_left(squares2, csq)
#             if squares2[ind] == csq:
#                 per = a+b+ind
#                 if per < L:
#                     tri_perims[per] += 1
#                 # print("___")
#                 # print("a", (a))
#                 # print("b", (b))
#                 # print("c", ind)
#                 # print("perimeter", per)
#
#     county = sum(1 for i in tri_perims if i ==1)
#     print(county)
#     return(county)

def triangles(limit):
    L = limit
    L += 1
    range_lim = int(sqrt(L))+2
    tri_perims = {}
    squares2 = [i**2 for i in range(0, L//2)]
    nsq = len(squares2)
    print("found squares")
    max_square = squares2[-1]
    county = 0
    for a in tqdm(range(1, nsq-2)):
        asq = squares2[a]
        bind = bisect.bisect_left(squares2, max_square-asq)
        for b in range(a+1, bind):
            csq = asq + squares2[b]
            if csq > max_square:
                break
            ind = bisect.bisect_left(squares2, csq)
            if squares2[ind] == csq:
                per = a+b+ind
                if per < L:
                    tri_perims[per] = tri_perims.get(per, 0) + 1
                # print("___")
                # print("a", (a))
                # print("b", (b))
                # print("c", ind)
                # print("perimeter", per)

        if a in tri_perims:
            if tri_perims[a] == 1:
                county += 1
            del tri_perims[a]


    county += sum(1 for k, v in tri_perims.items() if v ==1)
    print(county)
    return(county)

# triangles(30)

assert 16 == triangles(150)
assert 11 == triangles(100)


ans = (triangles(1500000))
print(ans)


# for t in range(len(tri_perims)):
#     if tri_perims[t]==1:
#         print(t)
#     elif tri_perims[t] > 1:
#         print("AKSDJF")
#         print(t)


# triangles = {}
# for a in tqdm(range(1, 1+L)):
#     for b in range(1, a, 1):
#         c_sq = (a*a) + (b*b)
#         if c_sq in squares and gcd(a, b) == 1:
#             per = a+b+squares[c_sq]
#             triangles[per] = triangles.get(per, 0) + 1
#
# print(triangles)
# ones = [k for k, v in triangles.items() if v == 1]
# print(ones)

# print("")
# triangles = {}
# for a in tqdm(range(1, L//2)):
#     for b in range(1, a):
#         # if gcd(a, b) == 1:
#         # print("___")
#         # print(a, b)
#         c_sq = (a*a) + (b*b)
#         if c_sq in squares:
#             # print("HERM")
#             per = a+b+squares[c_sq]
#             triangles[per] = triangles.get(per, 0) + 1
#
# print(triangles)
# ones = [k for k, v in triangles.items() if v == 1]
# print(ones)

# triangles = {}
# for a in tqdm(range(1, L//2)):
#     for b in range(1, a, 2):
#         # if gcd(a, b) == 1:
#         # print("___")
#         # print(a, b)
#         c_sq = (a*a) + (b*b)
#         if c_sq in squares:
#             # print("HERM")
#             per = a+b+squares[c_sq]
#             triangles[per] = triangles.get(per, 0) + 1
#
# print(triangles)
# print(triangles)

# perimeter=120
# num_triangles = 0
# for b in range(1, perimeter // 2):
#     a = (2 * b * perimeter - perimeter ** 2) / (2 * (b - perimeter))
#
#     if a % 1:
#         continue
#     a = int(a)
#     if a < b:
#         if a ** 2 + b ** 2 == (perimeter - a - b) ** 2:
#             num_triangles += 1
#






























