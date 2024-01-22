# -*- coding: utf-8 -*-
# Jesse Rubin ~ Project Euler
"""
Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

from pupy.maths import fib_r


def p002(upper_bound=4000000):
    return sum(
        n for n in (fib_r(i) for i in range(40)) if n % 2 == 0 and n < upper_bound + 1
    )


if __name__ == "__main__":
    ANSWER = p002()
    print("Even fibonacci numbers less than 4,000,000: {}".format(ANSWER))
