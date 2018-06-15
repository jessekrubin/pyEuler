#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse Rubin ~ project Euler ~
"""
Problem Name
prob #

Prompt
"""
from itertools import *
from bib.amazon_prime import prime_gen

def is_connected(a, b):
    a = str(a)
    b = str(b)
    asl = len(a)
    bsl = len(b)
    len_dif = abs(asl-bsl)
    if len_dif==0:
        difs = 0
        for i in range(asl):
            if a[i] != b[i]: difs+=1
            if difs > 1: return False
        return True
    elif abs(bsl-asl) == 1: return b in a or a in b
    return False






assert is_connected(123, 173) == True
assert is_connected(173, 123) == True
assert is_connected(23, 123) == True
assert is_connected(123, 23) == True




from collections import defaultdict
from copy import copy




def F(n):
    primes = {p for p in prime_gen(n)}
    d = defaultdict(set)
    for p1, p2 in combinations(primes, 2):
        if is_connected(p1, p2):
            d[p1].add(p2)
            d[p2].add(p1)

    two_relatives = set()
    print(d)
    def _traverse(pn, rchain, cmax):
        if rchain[-1]==pn: return True
        possrels = list(sorted((el for el in d[rchain[-1]] if el not in rchain and el<=pn),reverse=True))
        if len(possrels)==0:
            return False


        for pr in possrels:
            if pr > cmax:
                two_relatives.add(pr)
                cmax = pr
            tc = copy(rchain)+(pr,)
            # print(tc)
            if _traverse(pn, tc, cmax):
                return True
        return False
        # print(possrels)
    for p in primes:
        if p not in two_relatives:
            _traverse(p, (2, ), 2)
        print(two_relatives)

    print(two_relatives)
    print(sum(two_relatives), sum(primes))
F(1000)

def p425():
    pass


if __name__ == '__main__':
    ANSWER = p425()
    print("ANSWER: {}".format(ANSWER))
