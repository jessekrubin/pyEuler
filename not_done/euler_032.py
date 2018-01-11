#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

"""
Pandigital products
Problem 32
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

from helpme import dig_list_2_int

one2nine = [i for i in range(1, 10)]
from itertools import permutations
print(one2nine)


def pandigital_product(list):
    combos = 0
    for i in range(2, 9):
        print("")
        print(list)
        for j in range(1, i):
            print("__")
            last = list[i:]
            furst = list[:j]
            second = list[j:i]
            print(furst)
            print(second)
            print(last)
            combos += 1
    print(combos)



testone = [3, 9, 1, 8, 6, 7,2,5,4]
pandigital_product(testone)
