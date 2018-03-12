#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
from os import path
import inspect
import bisect

def prime_sieve_gen(upper_bound=None, known_primes=None):
    if known_primes is not None and max(known_primes) > 2:
        D = { p**2 : [p] for p in known_primes}
        q = known_primes[-1]
        for n in known_primes:
            D.setdefault(((q//n)*n)+n, []).append(n)
        q+=1
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
            list.__init__(self, self.__load())
            self.max_loaded = self[-1]
        except ValueError:
            print("AM HERE")
            list.__init__(self, list(prime_sieve_gen(upper_bound=10)))
            self.max_loaded = 0

    def __del__(self):
        if len(self)> self.max_loaded:
            print("herm")
            self.__save()

    def __load(self):
        if path.isfile(self.save_path):
            with open(self.save_path, 'r') as f:
                primes = [int(line) for line in f.readlines() if line is not '\n']
            if len(primes) > 0:
                return primes
            elif len(primes) == 0:
                raise ValueError
        raise FileNotFoundError("{} Not file".format(self.save_path))

    def __save(self):
        with open(self.save_path, 'w', encoding='utf-8') as f:
            for prime in self:
                f.write(str(prime))
                f.write('\n')

    def transform(self, n = None):
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
        return self.prime_range(1, upper_bound)

    def prime_range(self, lower_bound, upper_bound):
        if upper_bound > self[-1]:
            self.transform(upper_bound)
        return self[bisect.bisect_right(self, lower_bound):bisect.bisect_left(self, upper_bound)]

#########
# TESTS #
#########



