# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Counting primitive Pythagorean triples
Problem 540
A Pythagorean triple consists of three positive integers a,b and c satisfying a2+b2=c2.
The triple is called primitive if a,b and c are relatively prime.
Let P(n) be the number of primitive Pythagorean triples with a<b<c≤n.
For example P(20) = 3, since there are three triples: (3,4,5), (5,12,13) and (8,15,17).

You are given that P(10**6) = 159139.
Find P(3141592653589793).
"""
from itertools import count
from lib.maths import gcd_cash_muny, pytriple_gen
from math import sqrt
from tqdm import tqdm
from bisect import bisect_left


#
# def pytriple_gen(max_c, primatives_only=True):
#     """
#     primative pythagorean triples generator
#
#     thanks to 3Blue1Brown
#     special thanks to 3Blue1Brown's video on pythagorean triples
#     https://www.youtube.com/watch?v=QJYmyhnaaek&t=300s
#
#     :param max_c:
#     :return:
#     """
#
#     for real_pts in tqdm(range(2, int(sqrt(max_c)+1), 1), ascii=True):
#         for imag_pts in range(1, real_pts):
#             comp = complex(real_pts, imag_pts)
#             sqrd = comp * comp
#             real = int(sqrd.real)
#             imag = int(sqrd.imag)
#             sea = int((comp * comp.conjugate()).real)
#             triple = (imag, real, sea) if real > imag else (real, imag, sea)
#             if sea > max_c:
#                 break
#             elif gcd_cash_muny(triple[0], triple[1]) == 1:
#                 yield triple

def thing(n):
    count = 0
    for i in (pytriple_gen(n)):
        count += 1

    print(count)


(thing(20))
thing(200)
thing(1000)
(thing(10**6))
thing(3141592653589793)
# def p540():
#     # print(pytriple_gen(20))
#     print(pytriple_gen(100))
# assert 3 == pytriple_gen(20)
# assert 159139 == pytriple_gen(10**6)
# answer = pytriple_gen(3141592653589793)
# print(answer)


# p540()
# print(answer)
# ans = P(1000000)
# print(ans)
# (3 141 592 653 589 793)
