# Solution to Python problem 32

## Solution code
```python
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

from pupy.listless import int_from_digits
from itertools import permutations


def pandigital_product(list):
    """
    >>> pandigital_product([3, 9, 1, 8, 6, 7, 2, 5, 4])
    True
    """
    for i in range(2, 9):
        for j in range(1, i):
            last = list[i:]
            furst = list[:j]
            second = list[j:i]
            if int_from_digits(furst) * int_from_digits(second) == int_from_digits(last):
                return int_from_digits(last)
    return 0


def p032():
    one2nine = [i for i in range(1, 10)]
    pandigital_lists = [i for i in permutations(one2nine)]
    products = set()
    for pandigit in pandigital_lists:
        products.add(pandigital_product(pandigit))
    return sum(products)


if __name__ == '__main__':
    ans = p032()
    print("Sum of products: {}".format(ans))

```

## Home made solution dependencies
