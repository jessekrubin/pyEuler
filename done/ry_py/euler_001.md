# Solution to Python problem 1

## Solution code
```python
#!/usr/local/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiples_lt(lim, div):
    mul = lim // div
    return ((mul * mul * div) + (mul * div)) // 2


def multiples_o_3_n_5(upper_bound):
    return multiples_lt(upper_bound, 3) + multiples_lt(upper_bound, 5) - multiples_lt(upper_bound, 15)


def p001(upper_bound=1000):
    return multiples_o_3_n_5(upper_bound - 1)


if __name__ == '__main__':
    answer = p001()
    print("Sum: {}".format(answer))  # Sum: 233168

```

## Home made solution dependencies
