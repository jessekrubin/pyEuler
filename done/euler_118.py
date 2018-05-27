#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Pandigital prime sets
Problem 118
Using all of the digits 1 through 9 and concatenating them freely to form
decimal integers, different sets can be formed. Interestingly with the set
{2,5,47,89,631}, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly
once contain only prime elements?
"""
from collections import Counter
from itertools import combinations, product, permutations
from bib.maths import partitions_gen
from bib.amazon_prime import is_prime
from bib.decorations import Jasm

try: xrange
except NameError: xrange = range

pandaprimespath = '../txt_files/panda_primes_set.txt'


@Jasm(pandaprimespath)
def no_repeating_dijits_primes():
    panda_primes = {}
    for i in range(1, 9):  # dont have to go all the way up bc there are no pan dig primes
        thing = []
        for perm in permutations('123456789', i):
            pn = int("".join(perm))
            if is_prime(pn):
                thing.append(pn)
        panda_primes[i] = thing
    return panda_primes


def is_pandigital_set(st):
    return True if len(set(dijit for dijit in "".join(str(n) for n in st))) == 9 else False


def p118():
    norep_primes = {int(k):v for k, v in no_repeating_dijits_primes().items()}
    okparts = [p for p in partitions_gen(9) if len(p) > 1 and sum(1 for n in p if n == 1) < 5]
    pandigital_prime_sets = set()
    for party in okparts:
        c = Counter(p for p in party)
        permutation_combinations = [[i for i in combinations(norep_primes[k], v)]
                                    for k, v in c.items()]
        for prod in product(*permutation_combinations):
            a = tuple(sorted([n for combo in prod for n in combo]))
            if is_pandigital_set(a):
                pandigital_prime_sets.add(tuple(a))
    return len(pandigital_prime_sets)


if __name__ == '__main__':
    ANSWER = p118()
    print("# pandigital prime sets: {}".format(ANSWER))