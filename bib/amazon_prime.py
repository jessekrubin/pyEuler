#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - Biblioteca
from bisect import bisect_right, bisect
from itertools import count
from math import sqrt

from bib import xrange
from bib.maths import divisors_gen
from bib.decorations import cash_it


def prime_gen(plim=0, kprimes=None):
    """Infinite (within reason) prime number generator

    My big modification is the pdiv_dictionary() function that recreats the
    dictionary of divisors so that you can continue to generate prime numbers
    from a (sorted) list of prime numbers.

    Based on:
        eratosthenes by David Eppstein, UC Irvine, 28 Feb 2002
        http://code.activestate.com/recipes/117119/ and the thread at the url

    Args:
        plim (int): prime_limit; default=0 makes for an infinite generator
        kprimes (iter): known_primes as an iterable

    Yields:
        (int): prime numbers

    Examples:
        >>> list(prime_gen(50))
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        >>> list(prime_gen(10))
        [2, 3, 5, 7]
    """

    if kprimes is None: kprimes = [2, 3, 5, 7, 11]

    def _dictionary():
        """Recreates the prime divisors dictionary used by the generator"""
        div_dict = {}
        for pdiv in kprimes:
            multiple = kprimes[-1] // pdiv * pdiv
            if multiple % 2 == 0: multiple += pdiv
            else: multiple += 2 * pdiv
            while multiple in div_dict: multiple += pdiv * 2
            div_dict[multiple] = pdiv
        return div_dict

    # [1]
    # See if the upper bound is greater than the known primes
    if 0 < plim <= kprimes[-1]:
        for p in kprimes:
            if p <= plim:
                yield p
        return  # return bc we are done

    # [2]
    # Recreate the prime divisibility dictionary using kprimes;
    # Set start and yield first 4 primes
    divz = _dictionary()
    start = kprimes[-1] + 2  # max prime + 2 (make sure it is odd)
    if start == 13: yield 2; yield 3; yield 5; yield 7; yield 11
    # use count or range depending on if generator is infinite
    it = count(start, 2) if plim == 0 else xrange(start, plim, 2)
    for num in it:
        prime_div = divz.pop(num, None)
        if prime_div:
            multiple = (2 * prime_div) + num
            while multiple in divz: multiple += (2 * prime_div)
            divz[multiple] = prime_div
        else:
            divz[num * num] = num
            yield num


def prime_factorization_gen(n):
    """generates all numbers in the prime factorization of n

    Args:
        n (int): number to be factored

    Yields:
        (int): prime factors w/ repeats

    Examples:
        >>> list(prime_factorization_gen(12))
        [2, 2, 3]
        >>> list(prime_factorization_gen(16))
        [2, 2, 2, 2]

    """
    for factor in prime_factors_gen(n):
        if n <= 1: break
        while n % factor == 0:
            n //= factor
            yield factor


def prime_factors_gen(n):
    """prime factors generator

    Args:
        n (int): number to be factorized

    Yields:
        (int): prime factors w/o repeats

    Examples:
        >>> list(prime_factors_gen(12))
        [2, 3]
        >>> list(prime_factors_gen(16))
        [2]

    """
    return (p for p in divisors_gen(n) if is_prime(p))


@cash_it
def is_prime(number):
    """Checks if a number is prime

    Args:
        number (int): number to check if is prime

    Returns:
        (bool): True if number is prime
        (bool): False if number is not prime

    Examples:
        >>> is_prime(37)
        True
        >>> is_prime(100)
        False
        >>> is_prime(89)
        True
    """
    if number == 2 or number == 3: return True
    if number < 2 or number % 2 == 0: return False
    if number < 9: return True
    if number % 3 == 0: return False
    for step in xrange(5, int(sqrt(number)) + 1, 6):
        if step >= number: break
        if number % step == 0: return False
        if number % (step + 2) == 0: return False
    return True


class OctopusPrime(list):
    """OctopusPrime, the 8-leg autobot, here to help you find PRIMES"""

    def __init__(self, plim=100):
        """______OCTOPUS_PRIME ACTIVATE______
           ░░░░░░░▄▄▄▄█████████████▄▄▄░░░░░░░
           ████▄▀████████▀▀▀▀▀▀████████▀▄████
           ▀████░▀██████▄▄░░░░▄▄██████▀░████▀
           ░███▀▀█▄▄░▀▀██████████▀▀░▄▄█▀▀███░
           ░████▄▄▄▀▀█▄░░░▀▀▀▀░░░▄█▀▀▄▄▄████░
           ░░██▄▄░▀▀████░██▄▄██░████▀▀░▄▄██░░
           ░░░▀████▄▄▄██░██████░██▄▄▄████▀░░░
           ░░██▄▀▀▀▀▀▀▀▀░░████░░▀▀▀▀▀▀▀▀▄██░░
           ░░░██░░░░░░░░░░████░░░░░░░░░░██░░░
           ░░░███▄▄░░░░▄█░████░█▄░░░░▄▄███░░░
           ░░░███████░███░████░███░███████░░░
           ░░░███████░███░▀▀▀▀░███░███████░░░
           ░░░███████░████████████░███████░░░
           ░░░░▀█████░███░▄▄▄▄░███░█████▀░░░░
           ░░░░░░░░▀▀░██▀▄████▄░██░▀▀░░░░░░░░
           ░░░░░░░░░░░░▀░██████░▀░░░░░░░░░░░░

        Args:
            plim (int): starting max limit to generate primes below
        """
        list.__init__(self, list(prime_gen(plim=plim)))
        self.max_loaded = self[-1]

    def _transform(self, n=None):
        """TRANSFORM / grow the list"""
        n = n if n is not None else self[-1] * 10
        self.extend(list(prime_gen(plim=n, kprimes=self)))

    def __contains__(self, item):
        if self[bisect(self, item) - 1] == item: return True
        return False

    def primes_below(self, upper_bound):
        """Lists primes, p, such that  p < upper_bound

        Args:
            upper_bound (int): exclusive upper bound

        Returns:
            (list): primes less than upper_bound

        """
        return self.primes_between(1, upper_bound)

    def primes_between(self, lower_bound, upper_bound):
        """Lists primes, p, such that, lower_bound < p < upper_bound

        Args:
            lower_bound (int): exclusive lower bound
            upper_bound (int): exclusive upper bound

        Returns:
            (list): primes between lower_bound and upper_bound

        """
        if upper_bound > self[-1]: self._transform(upper_bound)
        return self[bisect_right(self, lower_bound):bisect(self, upper_bound)]
