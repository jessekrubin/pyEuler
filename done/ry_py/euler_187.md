# Solution to Python problem 187

## Solution code
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Semiprimes
Problem 187
A composite is a number containing at least two prime factors. For example,
15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two, not
necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 10**8, have precisely two, not necessarily
distinct, prime factors?
"""

from pupy.amazon_prime import prime_gen
from math import sqrt
from bisect import bisect_left
from itertools import combinations_with_replacement
from operator import truediv

try: range
except NameError: range = range


def p187a(upper_bound=10**8):
    primes = list(n for n in prime_gen(1+upper_bound//2))
    for c in combinations_with_replacement(primes, 2):
        print(c)




def p187(upper_bound=10**8):
    primes = list(n for n in prime_gen(1+upper_bound//2))
    lim_root = int(sqrt(upper_bound)+1)
    ans = 0
    for i in range(len(primes)):
        if primes[i] > lim_root: break
        ans += bisect_left(primes, truediv(upper_bound, primes[i]))-i
    return ans


if __name__ == '__main__':
    assert 10 == p187(30)
    ANSWER = p187()
    print("# composite integers with two prime factors: {}".format(ANSWER))
```

## Home made solution dependencies
