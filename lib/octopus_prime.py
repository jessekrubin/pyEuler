#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler

from bisect import bisect_right, bisect_left
from itertools import chain, count
from lib.decorations import cash_muney
from lib.maths import expo


def prime_sieve_gen(upper_bound=0, known_primes=[2, 5, 7, 11]):
    """
    infinite (within reason) prime number generator

    My big modification is the pdiv_dictionary() function that recreats the
    dictionary of divisors so that you can continue to generate prime numbers
    from a (sorted) list of prime numbers.

    BASED ON:
        eratosthenes by David Eppstein, UC Irvine, 28 Feb 2002
        http://code.activestate.com/recipes/117119/
        and
        the thread at that url


    :param upper_bound:
    :param known_primes:
    :return:
    """

    def pdiv_dictionary():
        """
        Recreates the prime divisors dictionary used by the generator
        """
        div_dict = {}
        for pdiv in known_primes:  # for each prime
            multiple = known_primes[-1] // pdiv * pdiv
            if multiple % 2 == 0:
                multiple += pdiv
            else:
                multiple += 2 * pdiv
            while multiple in div_dict: multiple += pdiv * 2
            div_dict[multiple] = pdiv
        return div_dict

    # recreate the dictionary of divisors if a list of primes numbers was given
    # as a parameter. 15, is the next thing div 3 beyond 11, and othewise we
    # look to the squares
    divz = {15: 3, 25: 5, 49: 7, 121: 11} if known_primes[-1] == 11 else pdiv_dictionary()
    start = known_primes[-1] + 2
    if start == 13: yield 2; yield 3; yield 5; yield 7; yield 11
    for num in count(start, 2):
        if 0 < upper_bound < num: break  # stop at upper bound
        prime_div = divz.pop(num, None)
        if prime_div:
            multiple = (2 * prime_div) + num
            while multiple in divz: multiple += (2 * prime_div)
            divz[multiple] = prime_div
        else:
            divz[num * num] = num
            yield num


def pfactorization_gen(n):
    return (n for n in chain.from_iterable([p] * expo(p, n) for p in pfactors_gen(n)))


def pfactors_gen(n):
    """
    Returns prime factorization as a list

    :param n:
    :return:
    """
    return (p for p in prime_sieve_gen(int(n ** (1 / 2) + 1)) if n % p == 0)


@cash_muney
def is_prime(number):
    """
    Returns True if number is prime

    >>> is_prime(37)
    True
    >>> is_prime(100)
    False
    >>> is_prime(89)
    True
    """
    if number == 2 or number == 3:
        return True
    if number < 2 or number % 2 == 0:
        return False
    if number < 9:
        return True
    if number % 3 == 0:
        return False
    r = int(number ** 0.5)
    step = 5
    while step <= r:
        if number % step == 0:
            return False
        if number % (step + 2) == 0:
            return False
        step += 6
    return True


class OctopusPrime(list):
    """
    OctopusPrime, the leader of the Autobots, here to help you find primes

    ______OCTOPUS_PRIME ACTIVATE______
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

    """

    def __init__(self, n=10, savings_n_loads=True, save_path=None):
        list.__init__(self, list(prime_sieve_gen(upper_bound=n)))
        self.max_loaded = self[-1]

    def transform(self, n=None):
        n = n if n is not None else self[-1] * 10
        self.extend(list(prime_sieve_gen(upper_bound=n, known_primes=self)))

    def is_prime(self, number):
        if number > self[-1]:
            self.transform(number + 1)
        if number in self:
            return True
        else:
            return False

    def primes_below(self, upper_bound):
        return self.primes_between(1, upper_bound)

    def primes_between(self, lower_bound, upper_bound):
        if upper_bound > self[-1]:
            self.transform(upper_bound)
        return self[bisect_right(self, lower_bound):bisect_left(self, upper_bound)]
