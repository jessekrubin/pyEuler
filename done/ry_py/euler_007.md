# Solution to Python problem 7

## Solution code
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin

"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""

from pupy.amazon_prime import prime_gen


def p007(nth_prime=10001):
    count = 0
    for p in prime_gen():
        count += 1
        if count == 10001:
            return p


if __name__ == '__main__':
    ANSWER = p007()
    print("10,001th prime is: {}".format(ANSWER))

```

## Home made solution dependencies
