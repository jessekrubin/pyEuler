#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse Rubin ~ project Euler ~
"""
Best Approximations by Quadratic Integers
http://projecteuler.net/problem=591
Given a non-square integer d, any real x can be approximated arbitrarily close by quadratic integers a+b√(d), where a,b are integers. For example, the following inequalities approximate π with precision 10^-13:
4375636191520√(2)-6188084046055 < π < 721133315582√(2)-1019836515172 
We call BQA_d(x,n) the quadratic integer closest to x with the absolute values of a,b not exceeding n. We also define the integral part of a quadratic integer as I_d(a+b√(d)) = a.
You are given that:
BQA_2(π,10) = 6 - 2√(2)
BQA_5(π,100)=26√(5)-55
BQA_7(π,10^6)=560323 - 211781√(7)
I_2(BQA_2(π,10^13))=-6188084046055Find the sum of |I_d(BQA_d(π,10^13))| for all  non-square positive integers less than 100.
"""

def p591():
    pass

if __name__ == '__main__':
    p591()