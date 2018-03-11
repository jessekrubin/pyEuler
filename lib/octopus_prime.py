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


def prime_sieve_gen(known_primes=None, upper_bound=None):
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
    def __init__(self, save_path = None, n = 10):
        if save_path is None:
            self.save_path = path.join(path.dirname(inspect.getfile(OctopusPrime)), 'octopus.prime')
        else:
            self.save_path = save_path

        try:
            list.__init__(self, self.load())
        except ValueError:
            list.__init__(self, prime_sieve_gen(n))
            self.save()

        self.max_saved = len(self) - 1
        self.biggest = self[-1]

        # print("AHCHCHAHCSD")
        # print(self)

    def __del__(self):
        print("deleting")
        print(self)
        print("saving")
        self.append_save()


    def load(self):
        if path.isfile(self.save_path):
            print("found")
            with open(self.save_path, 'r') as f:
                primes = [int(line) for line in f.readlines()]
            if len(primes) > 0:
                return primes
            else:
                raise ValueError("{} NO PRIMES IN FILE".format(self.save_path))
        raise FileNotFoundError("{} Not file".format(self.save_path))

    def append_save(self):
        print("append save")
        print(self)
        print(self.biggest)
        print(self.max_saved)

        with open(self.save_path, 'a', encoding='utf-8') as f:
            for i in range(self.max_saved, len(self)):
                print(i)
                print(self[i])
                # f.write(str(prime))
                # f.write('\n')

    # @staticmethod
    # def prime_sieve_gen(self, upper_bound=None, save_path=None):
    #     D = {}
    #     q = 2
    #     while True:
    #         if q not in D:
    #             yield q
    #             D[q * q] = [q]
    #         else:
    #             for p in D[q]:
    #                 D.setdefault(p + q, []).append(p)
    #             del D[q]
    #         print(D)
    #         q += 1
    #         if upper_bound is not None and upper_bound < q:
    #             break

    def save(self):
        with open(self.save_path, 'w', encoding='utf-8') as f:
            for prime in self:
                f.write(str(prime))
                f.write('\n')

    def check(self, n):
        if n <= self.primes[-1]:
            return n in self
        else:
            for p in self:
                if n % p == 0:
                    return False
            return True


    def grow(self, n = None):
        print("grow")
        print(self)
        n = n if n is not None else self[-1] * 10
        self = list(prime_sieve_gen(n))

    def is_prime(self, number):
        print(self)
        print(number in self)
        print(number)




