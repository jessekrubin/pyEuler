#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - Biblioteca


cpdef long prime_pair_cy(long p1, long p2, int mod_tens):
    """speed up for problem 134"""
    cdef long two_p2 = 2*p2
    cdef int mul = 1
    while p2%mod_tens != p1:
        p2 += two_p2
        p2 %= mod_tens
        mul += 2
    return mul
