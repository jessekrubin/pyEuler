#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Counting the number of "hollow" square laminae that can form one, two,
three, ... distinct arrangements
Problem 174
We shall define a square lamina to be a square outline with a square "hole" so
that the shape possesses vertical and horizontal symmetry.

Given eight tiles it is possible to form a lamina in only one way: 3x3 square
with a 1x1 hole in the middle. However, using thirty-two tiles it is possible
to form two distinct laminae.


If t represents the number of tiles used, we shall say that t = 8 is type L(1)
and t = 32 is type L(2).

Let N(n) be the number of t ≤ 1000000 such that t is type L(n); for example,
N(15) = 832.

What is ∑ N(n) for 1 ≤ n ≤ 10?
"""

from lib.maths import divisors_list

def square_lams2(upperlimit):
    divfours = [i for i in range(upperlimit+1) if i % 4 == 0 and i >4]
    total = 0
    for num in divfours:
        divs = divisors_list(num//4)
        num_lams = len(divs)//2
        if 0 < num_lams < 11:
            total += 1

    return (total)


ans = square_lams2(1000000)
print("ANSWER: {}".format(ans))

