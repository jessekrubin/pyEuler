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

from itertools import count
from bib.listless import digits_list, int_from_digits


def cubic_perms(n_perms):
    cubed_dict = {}
    for i in count(100):
        ccc = int_from_digits(sorted(digits_list(i**3), reverse=True))
        if ccc in cubed_dict:
            cubed_dict[ccc].append(i)
            if len(cubed_dict[ccc]) > n_perms - 1:
                # print(cubed_dict[ccc])
                return cubed_dict[ccc][0] ** 3
        else:
            cubed_dict.setdefault(ccc, []).append(i)


def p062():
    return cubic_perms(5)


if __name__ == '__main__':
    assert cubic_perms(3) == 41063625
    ans = p062()
    print("Answer: {}".format(ans))  # 127035954683