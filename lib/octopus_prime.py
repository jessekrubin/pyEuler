#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
from lib.decorations import json_cash
from os import path, getcwd, pardir
from json import load, dump
import inspect
import os



def primes_below(upperbound):
    return list(n for n in prime_sieve_gen(upperbound))


def prime_sieve_gen(upper_bound=None, known_primes=None):
    if known_primes is not None:
        D = { p**2 : [p] for p in known_primes}
        q = known_primes[-1]
        for n in known_primes:
            thing = ((q//n)*n)+n
            D.setdefault(thing, []).append(n)
    else:
        D = {}
        q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
        if upper_bound is not None and upper_bound < q:
            break

def prime_sieve_gen_orig(upper_bound=None, save_path=None):
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        print(D)
        q += 1
        if upper_bound is not None and upper_bound < q:
            break

# @lru_cache(maxsize=None)
# @json_cash(path.join(path.abspath(path.join(getcwd())), 'txt_files'))
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
    def __init__(self,n=10, save_path = None):
        if save_path is None:
            self.save_path = path.join(path.dirname(inspect.getfile(OctopusPrime)), 'octopus.prime')
        else:
            self.save_path = save_path

        try:
            list.__init__(self, self.load())
        except ValueError:
            print("AM HERE")
            list.__init__(self, list(OctopusPrime.prime_sieve_gen(known_primes=[2],
                                                                  upper_bound=10)))
            self.append_save(start_ind=0)
        self.max_saved = len(self)+1

    def __del__(self):
        print("deleting")
        print(self)
        print("saving")
        self.append_save(self.max_saved)


    def load(self):
        if path.isfile(self.save_path):
            with open(self.save_path, 'r') as f:
                primes = [int(line) for line in f.readlines() if line is not '\n']
            if len(primes) > 0:
                return primes
            elif len(primes) == 0:
                raise ValueError
        raise FileNotFoundError("{} Not file".format(self.save_path))

    def append_save(self, start_ind = None):
        if start_ind is None:
            start_ind = self.max_saved+2

        with open(self.save_path, 'a', encoding='utf-8') as f:
            for i in range(start_ind, len(self)):
                f.write(str(self[i]))
                f.write('\n')

    def save(self):
        with open(self.save_path, 'w', encoding='utf-8') as f:
            for prime in self:
                f.write(str(prime))
                f.write('\n')

    @staticmethod
    def prime_sieve_gen(upper_bound=None, known_primes=None):
        if known_primes is not None:
            D = {p**2: [p] for p in known_primes}
            q = known_primes[-1]+2
            for n in known_primes:
                thing = ((q//n)*n)+n
                D.setdefault(thing, []).append(n)
        else:
            D = {}
            q = 2

        while True:
            if q not in D:
                yield q
                D[q * q] = [q]
            else:
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]
            q += 1
            if upper_bound is not None and upper_bound < q:
                break

    def check(self, n):
        if n <= self.primes[-1]:
            return n in self
        else:
            for p in self:
                if n % p == 0:
                    return False
            return True

    def grow(self, n = None):
        n = n if n is not None else self[-1] * 10
        self.extend(list(OctopusPrime.prime_sieve_gen(upper_bound=n, known_primes=self)))

    def is_prime(self, number):
        if number > self[-1]:
            self.grow(number+1)
        if number in self:
            return True
        else:
            return False

