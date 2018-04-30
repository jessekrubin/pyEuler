#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Cubic permutations
Problem 62
The cube, 41063625 (3453), can be permuted to produce two other cubes:
56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits
are cube.
"""
__sol__ = None

from itertools import count
from lib.listless import digits_list, dig_list_2_int

def cubic_perms(n_perms):
    cubed_dict = {}
    for i in count(100):
        ccc = dig_list_2_int(sorted(digits_list(i**3), reverse=True))
        if ccc in cubed_dict:
            cubed_dict[ccc].append(i)
            if len(cubed_dict[ccc]) > n_perms - 1:
                # print(cubed_dict[ccc])
                return cubed_dict[ccc][0]**3
        else:
            cubed_dict.setdefault(ccc, []).append(i)


print("Answer:", cubic_perms(3)) # 41063625
print("Answer:", cubic_perms(5)) # 127035954683







































def p062():
    pass

if __name__ == '__main__':
    p062()