#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
"""


def ordered_fractions(d):
    fracs = set()
    for denom in range(2, d + 1):
        fracs.add(1 / denom)
        for i in range(denom // 3, (1 + denom) // 2):
            fracs.add(i / denom)

    ordered_fracs = sorted(fracs)
    start = ordered_fracs.index(1 / 3)
    stop = ordered_fracs.index(1 / 2)
    return stop - start - 1

assert 3 == ordered_fractions(8)

def p073():
    answer = ordered_fractions(12000)
    print(answer)

if __name__ == '__main__':
    p073()
