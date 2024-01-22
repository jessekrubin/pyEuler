#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Goldbach's other conjecture
Problem 46
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?.
"""

from pupy.amazon import is_prime
from math import sqrt


def p046():
    n = 3
    prime_numbers = set()
    prime_numbers.add(2)
    while True:
        if is_prime(n):
            prime_numbers.add(n)
        else:
            for p in prime_numbers:
                if sqrt(((n - p) / 2)) == int(sqrt(((n - p) / 2))):
                    break  # break if it works with the conjecture
            else:
                return n
        n += 2


if __name__ == "__main__":
    answer = p046()
    print("ANSWER: {}".format(answer))
