# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from bib.amazon_prime import pfactors_gen


def p003():
    return max(pfactors_gen(600851475143))


if __name__ == '__main__':
    ANSWER = p003()
    print("Largest prime factor of 600851475143: {}".format(ANSWER))  # 6857


