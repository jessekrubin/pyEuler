#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Efficient exponentiation
Problem 122
The most naive way of computing n15 requires fourteen multiplications:

n × n × ... × n = n15

But using a "binary" method you can compute it in six multiplications:

n × n = n**2
n**2 × n**2 = n**4
n**4 × n**4 = n**8
n**8 × n**4 = n**12
n**12 × n**2 = n**14
n**14 × n = n**15

However it is yet possible to compute it in only five multiplications:

n × n = n**2
n**2 × n = n**3
n**3 × n**3 = n**6
n**6 × n**6 = n**12
n**12 × n**3 = n**15

We shall define m(k) to be the minimum number of multiplications to compute nk;
for example m(15) = 5.

For 1 ≤ k ≤ 200, find ∑ m(k).
"""
from itertools import chain

from bib.amazon_prime import prime_factors_gen

#
# public void Backtrack(int power, int depth) {
# if (power > limit || depth > cost[power]) return;
# cost[power] = depth;
# path[depth] = power;
# for (int i = depth; i >= 0; i--)
#     Backtrack(power + path[i], depth + 1);
# }
from collections import defaultdict
d = defaultdict(int)

from copy import copy
from bib.decorations import cash_it

def m(n):

    c = {n}
    d = {i:i*2for i in range(1, n+1)}
    print(d)

    def _bin(chain = (1,)):
        # if sum(chain)==200:
        #     print(chain, sum(chain))

        # if len(chain)-1 <= min(c):
        #     # c.add(len(chain)-1)
        #     d[len(chain)] = min(d[len(chain)], len(chain)-1)
        if sum(chain)>n:
            print(d)
        else:
            if sum(chain) in d and len(chain)-1 < d[sum(chain)]:
                d[sum(chain)]=len(chain)

            for el in reversed(chain):
                tc = copy(chain) + (el+chain[-1], )
                if tc[-1]<n+1 and len(tc)-1< min(c):
                    _bin(tc)
    _bin()
    print(d)
    print(c)
    print(sum(v for v in d.values()))

    return min(c)

# assert 5 == m(15)
m(15)
m(200)
# a = m(200)
# print(a)
# for n in range(1, 200+1):
#     print(m(n))

