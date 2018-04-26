#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from lib.octopus_prime import pfactors_gen

answer = max(pfactors_gen(600851475143))
print("largest prime factor of 600851475143 is: {}".format(answer))  # 6857
