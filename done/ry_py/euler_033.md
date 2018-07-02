# Solution to Python problem 33

## Solution code
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Digit cancelling fractions_in_range
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions_in_range like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions_in_range is given in its lowest common
terms, find the value of the denominator.
"""

from fractions import Fraction
from pupy.listless import iter_product


def is_fishy_fraction(n, d):
    if n % 10 == 0 and d % 10 == 0: return False
    orig_f = Fraction(n, d)
    n1, n2 = n // 10, n % 10
    d1, d2 = d // 10, d % 10
    if n1 == n2 and d1 == d2:
        return False
    elif d2 > 0 and n2 == d1 and Fraction(n1, d2) == orig_f:
        return True
    elif d1 > 0 and n1 == d2 and Fraction(n2, d1) == orig_f:
        return True
    return False


def p033():
    fracs = {Fraction(n, d) for d in range(11, 100) for n in range(10, d) if is_fishy_fraction(n, d)}
    return iter_product(fracs).denominator


if __name__ == '__main__':
    assert is_fishy_fraction(49, 98)
    ANSWER = p033()
    print("Denominator of reduced product: {}".format(ANSWER))

```

## Home made solution dependencies
