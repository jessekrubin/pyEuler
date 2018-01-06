#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Digit cancelling fractions
Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

list_of_toops = [(j, i) for i in range(10, 100) for j in range(10, i)]
# print(list_thing)


def both_digs(n):
    return n // 10, n % 10


def is_fishy_fraction(toop):
    og_fracking = toop[0] / toop[1]
    a, b = both_digs(toop[0])
    c, d = both_digs(toop[1])
    if toop[0] % 10 == 0:
        return False
    if a == c:
        return og_fracking == float(b / d)
    if a == d:
        return og_fracking == float(b / c)
    if b == c:
        try:
            return og_fracking == float(a / d)
        except ZeroDivisionError:
            pass

    if b == d:
        return og_fracking == float(a / c)
    return False


well_we_know_this_is_one = (49, 98)
test = is_fishy_fraction(well_we_know_this_is_one)
# print(test)


def div_toop(toop):
    return float(toop[0] / toop[1])


thingsy = [toop for toop in list_of_toops if is_fishy_fraction(toop)]

print(thingsy)
product = 1
for i in map(div_toop, thingsy):
    print(i)
    product *= i
numProd = 1
denProd = 1
for thing in thingsy:
    numProd *= thing[0]
    denProd *= thing[1]

print(numProd + " - " + numProd / 387296)
print(denProd + " - " + denProd / 387296)
