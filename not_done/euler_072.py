#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Counting fractions
Problem 72
Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, ...
... 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions
for d ≤ 1,000,000?
"""

import bisect


def genprimes(limit):
    D = {}
    q = 2
    count = 0
    primes = []

    while q <= limit:
        if q % 100 == 0:
            print(q)
        if q not in D:
            count += q - 1
            primes.append(q)
            D.setdefault(q + q, set()).add(q)
            D.setdefault(q * q, set()).add(q)
        else:
            dos = (len(D[q]))
            uno = bisect.bisect_left(primes, q)
            count += uno - dos + 1
            for p in D[q]:
                D.setdefault(p + q, set()).add(p)
            del D[q]
        q += 1
    return count - 1


p = genprimes(8)
print(p)
p = genprimes(1000000)
print(p)

# def counting_fractions(upper_bound=None, known_primes=None):
#     div_dict = {}
#     pytriple_gen = 2
#     count = 0
#     primes = []
#     while True:
#         prime_div = div_dict.pop(pytriple_gen, None)
#         if prime_div:
#             divisible_num = prime_div + pytriple_gen
#             print(div_dict)
#             while divisible_num in div_dict:
#                 divisible_num += prime_div
#             div_dict.setdefault(divisible_num, []).append(prime_div)
#         else:
#             div_dict.setdefault(pytriple_gen*pytriple_gen, []).append(pytriple_gen)
#             count += pytriple_gen - 1
#             primes.append(pytriple_gen)
#             # yield pytriple_gen
#         print(primes)
#         pytriple_gen += 1
#         if upper_bound is not None and upper_bound < pytriple_gen:
#             break
#     return count

# def counting_fractions(d):
#     primes = [i for i in prime_sieve_gen(d)]
#     primes_set = set(primes)
#
#     n2 = 0
#     for denom in tqdm(range(2, d + 1)):
#         # for i in range(1, denom):
#         #     if gcd(i, denom) == 1:
#         #         num_fracs += 1
#         if denom in primes_set:
#             n2 += denom - 1
#         else:
#             # smaller_primes = [pytriple_gen for pytriple_gen in primes[0:bisect.bisect_left(primes, denom)] if denom % pytriple_gen != 0]
#             # smaller_primes = sum(1 for pytriple_gen in primes[0:bisect.bisect_left(primes, denom)] if denom % pytriple_gen != 0)
#             smaller_primes = [pytriple_gen for pytriple_gen in primes[0:bisect.bisect_left(primes, denom)] if denom % pytriple_gen != 0]
#             # print("here", denom)
#             # print(smaller_primes)
#             # for ppp in smaller_primes:
#             #     primes.remove(ppp)
#             # primes.remove()
#
#             # n2 += smaller_primes + 1
#             n2 += len(smaller_primes) + 1
#     return n2

# def p072():
#     answer = counting_fractions(8)
#     # answer = counting_fractions(1000000)
#     print(answer)
#
# if __name__ == '__main__':
#     p072()
