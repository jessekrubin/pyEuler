# Solution to Python problem 80

## Solution code
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Square root digital expansion
Problem 80
It is well known that if the square root of a natural number is not an integer,
then it is irrational. The decimal expansion of such square roots is infinite
without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the
first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums
of the first one hundred decimal digits for all the irrational square roots.
"""

from decimal import getcontext, Decimal

getcontext().prec = 102


def sum_root_dig(n):
    return sum(int(c) for c in str(Decimal(n).sqrt()).replace('.', '')[0:100])


def p080():
    return sum(sum_root_dig(n) for n in range(1, 101)
               if n not in {i * i for i in range(1, 11)})


if __name__ == '__main__':
    assert 475 == sum_root_dig(2)
    ANSWER = p080()
    print("ANSWER: {}".format(ANSWER))
```

## Home made solution dependencies
