#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
"""

from math import factorial

stuff = [i for i in range(1, 10)]*3
print(stuff)
a = factorial(18)  # there are 18! perms of stuff

# for each permutation there are 8 possible places to sub in zeros
print(a)

ans = 227485267000992000

print(227485267000992000)
print(ans//a)
print(ans/a)
b = 17*16

print(b)
print(b/35)

print(a)

# for i in permutations(stuff):
#     num_perms += 1
#
# print(num_perms)
