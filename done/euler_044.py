#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

"""
Pentagon numbers
Problem 44
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten
pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference,
70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
difference are pentagonal and D = |Pk − Pj| is minimised; what is the value
of D?
"""
__sol__ = 5482660

from lib.decorations import cash_muney

@cash_muney
def pent_num(n):
    return n * (3 * n - 1) // 2


answer = None
pentagonal_numbers = set()
i = 0
while answer is None:
    i += 1
    p_k = pent_num(i)
    for p_j in pentagonal_numbers:
        if p_k - p_j in pentagonal_numbers and p_k - 2 * p_j in pentagonal_numbers:
            answer = p_k - 2 * p_j
            break
    pentagonal_numbers.add(p_k)

print("D: {}".format(answer))
def p044():
    pass

if __name__ == '__main__':
    p044()