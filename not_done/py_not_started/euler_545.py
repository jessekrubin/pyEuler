#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse Rubin ~ project Euler ~
"""
Faulhaber's Formulas
http://projecteuler.net/problem=545
The sum of the kth powers of the first n positive integers can be expressed as a polynomial of degree k+1 with rational coefficients, the Faulhaber's Formulas:
1^k + 2^k + ... + n^k = ∑_i=1^n i^k = ∑_i=1^k+1 a_i n^i = a_1 n + a_2 n^2 + ... + a_k n^k + a_k+1 n^k + 1,
where ai's are rational coefficients that can be written as reduced fractions pi/qi (if ai = 0, we shall consider qi = 1).
For example, 1^4 + 2^4 + ... + n^4 = -1/30 n + 1/3 n^3 + 1/2 n^4 + 1/5 n^5.
Define D(k) as the value of q1 for the sum of kth powers (i.e. the denominator of the reduced fraction a1).
Define F(m) as the mth value of k ≥ 1 for which D(k) = 20010.
You are given D(4) = 30 (since a1 = -1/30), D(308) = 20010, F(1) = 308, F(10) = 96404.
Find F(105).
"""

def p545():
    pass

if __name__ == '__main__':
    p545()