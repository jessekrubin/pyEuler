# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - update README.md
# Python script to update the README.md for this repo


from lib.octopus_prime import OctopusPrime

class TestOctopusPrimeMethods(object):

    def test_lt100_no_save_load(self):
        op = OctopusPrime(n=100, savings_n_loads=False)
        p_lt100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                   43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        assert op == p_lt100
        assert op.primes_below(100) == p_lt100

    def test_primes_gt50_lt200(self):
        op = OctopusPrime(n=100, savings_n_loads=False)
        l = op.primes_between(50, 200)
        assert l == [53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
                     113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199]
#     def test_lt100(self):
