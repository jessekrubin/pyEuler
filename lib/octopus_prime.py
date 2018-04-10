#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
from os import path
from inspect import getfile
from bisect import bisect_right, bisect_left
from functools import lru_cache
from numpy import load, save


def prime_sieve_gen(upper_bound=None, known_primes=None):
    if known_primes is not None and max(known_primes) > 1:
        div_dict = {p**2: p for p in known_primes}
        filter_num = known_primes[-1]
        for kprime in known_primes:
            divisible_num = (filter_num // kprime) * kprime + kprime
            while divisible_num in div_dict:
                divisible_num += kprime
            div_dict[divisible_num] = kprime
        filter_num += 1
    else:
        div_dict = {}
        filter_num = 2

    while True:
        prime_div = div_dict.pop(filter_num, None)
        if prime_div:
            divisible_num = prime_div + filter_num
            while divisible_num in div_dict:
                divisible_num += prime_div
            div_dict[divisible_num] = prime_div
        else:
            div_dict[filter_num * filter_num] = filter_num
            yield filter_num
        filter_num += 1
        if upper_bound is not None and upper_bound < filter_num:
            break


@lru_cache(maxsize=None)
def is_prime(number: int) -> bool:
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


def prime_factorization(n):
    """
    Returns prime factorization as a list

    :param n:
    :return:
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


class OctopusPrime(list):
    """
    OctopusPrime, the leader of the Autobots, here to help you find primes

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

    def __init__(self, n=10, save_path=None):
        autobot = """
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
        if save_path is None:
            self.save_path = path.join(path.dirname(
                getfile(OctopusPrime)), 'primes.npy')
        else:
            self.save_path = save_path
        try:
            list.__init__(self, self._load())
            self.max_loaded = self[-1]
        except:
            list.__init__(self, list(prime_sieve_gen(upper_bound=10)))
            self.max_loaded = 0

    def __del__(self):
        if self[-1] > self.max_loaded:
            self._save()

    def __str__(self):
        info = ["__\ninfo ",

                "# primes: {}".format(len(self)),
                "save path: {}".format(self.save_path),
                "max prime: {}".format(self[-1])]
        # "max prime: {}".format(self[-1])]
        return "\n".join(info)

    def _load(self):
        return load(self.save_path)

    def _save(self):
        save(self.save_path, self)

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
        return self[bisect_right(self, lower_bound):bisect_left(self.upper_bound)]

#########
# TESTS #
#########
