# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - Project Euler Tests

from lib.maths import prime_gen, pfactors_gen, is_prime, OctopusPrime

p_lt50 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
p_lt100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
           61, 67, 71, 73, 79, 83, 89, 97]
p_lt200 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
           61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
           131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
           197, 199]
p_gt100_lt200 = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
                 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
p_gt50_lt200 = [53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
                113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
                181, 191, 193, 197, 199]


def test_is_prime():
    assert all(is_prime(n) for n in p_lt200)


def test_pfactors_gen():
    assert [pf for pf in pfactors_gen(12)] == [2, 3]


class TestOctopusPrimeMethods(object):

    def test_lt100_no_save_load(self):
        op = OctopusPrime(n=100, savings_n_loads=False)
        assert op == p_lt100
        assert op.primes_below(100) == p_lt100

    def test_primes_gt50_lt200(self):
        op = OctopusPrime(n=100, savings_n_loads=False)
        assert p_gt50_lt200 == op.primes_between(50, 200)


class TestPrimeSieve(object):

    def test_prime_seive_gen(self):
        """
        test if can generate primes below 100
        """
        assert p_lt100 == [p for p in prime_gen(100)]

    def test_use_prime_list(self):
        """
        testing if the dictionary recreation is good
        """
        assert list(prime_gen(200, kprimes=p_lt100)) == p_gt100_lt200

    def test_small_primes(self):
        """
        testing the generator with smaller primes
        """
        assert list(prime_gen(2)) == [2]
        assert list(prime_gen(3)) == [2, 3]
        assert list(prime_gen(5)) == [2, 3, 5]
        assert list(prime_gen(7)) == [2, 3, 5, 7]
        assert list(prime_gen(11)) == [2, 3, 5, 7, 11]

    def test_small_ub_large_known_primes(self):
        """
        test handling an upper_bound < max prime
        """
        assert list(prime_gen(50, kprimes=p_lt100)) == p_lt50
