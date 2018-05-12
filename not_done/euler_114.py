#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
"""

combs = []
from copy import copy

def block_combos(cur, total):
    print(cur, total)
    rem = total-sum(cur)
    print(rem)
    if rem<3:
        print(cur + [1]*rem)
        yield cur + [1]*rem
    for b in range(1, total):
        a = copy(cur)
        a.append(b)
        print(a)
        yield block_combos(a, total)

print(list(block_combos([], 7)))



