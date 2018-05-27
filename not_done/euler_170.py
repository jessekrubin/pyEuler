#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Problem Name
prob #

Prompt
"""
from __future__ import division
from itertools import combinations, permutations
stuff = set()
def f():
    for i in range(9, 0, -1):
        for c in permutations(''.join(str(j) for j in range(9, -1, -1) if j != i)):
            for s in range(1, 9):
                i, thing, ath = (i, int(''.join(c[:s])), int(''.join(c[s:])))
                    # print(i, c)
                a = set.union(set(c for c in str(thing*i)), set(c for c in str(ath*i)))
                if len(a)==10:
                        # print(len(a))
                    stuff.add(int(str(thing*i)+str(ath*i)))
                    stuff.add(int(str(ath*i)+str(thing*i)))
                    print(max(stuff))

                    # print(a)
                    # return

f()
print(stuff)
                # i, thing, ath = (i, int(''.join(c[:s])), int(''.join(c[s:])))


# def p000():
#     pass
#
#
# if __name__ == '__main__':
#     p000()
