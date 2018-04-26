#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler


"""
Idempotents
Problem 407
If we calculate a2 mod 6 for 0 ≤ a ≤ 5 we get: 0,1,4,3,4,1.

The largest value of a such that a2 ≡ a mod 6 is 4.
Let's call M(n) the largest value of a < n such that a2 ≡ a (mod n).
So M(6) = 4.

Find ∑M(n) for 1 ≤ n ≤ 107.
"""
from tqdm import tqdm
from bisect import bisect_left
from lib.octopus_prime import prime_sieve_gen



def S_M(max_n):

    primes = [p for p in prime_sieve_gen(max_n)]
    squares = [n*n for n in range(max_n+1)]
    def M(n):
        # print("_")
        # print(n)
        if n<=primes[-1] and primes[bisect_left(primes, n)] == n:
            return 1
        if squares[bisect_left(squares, n)] == n:
            return 1
        for a in range(n-1, -1, -1):
            right = (a%n)
            # left = (a*a)%n
            sq = squares[a]
            left = squares[a]%n
            if right == left:
                return a

    assert 4 == M(6)

    # for n in range(1, 1000):
    #     print(M(n))

    m_sum = 0
    for n in tqdm(range(1, max_n+1)):
        print("_")
        print(n,M(n)**2,  M(n))
        m_sum += M(n)
    m_sum -= 1
    print("MSUM", m_sum)
    return m_sum

S_M(20)
S_M(10) # 17
S_M(10**2) #2549
S_M(50) # 538
# S_M(10**3)
# S_M(10**4)
# S_M(10**5)
# S_M(10**6)
