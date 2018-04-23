# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

"""
Coin sums
Problem 31
In England the currency is made up of pound, £, and pence, pytriplets_gen, and there are
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""


def coin_sums(n):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ok_coins = [i for i in coins if i < (n + 1)]
    # print(ok_coins)
    sums = [0] * (n + 1)
    sums[0] = 1
    for c in ok_coins:
        for i in range(c, n + 1):
            sums[i] += sums[abs(i - c)]
    # print(sums)
    return sums[n]


n1 = 5
ans1 = coin_sums(n1)
print("{} ways to make {}".format(ans1, n1))

n2 = 100
ans2 = coin_sums(n2)
print("{} ways to make {}".format(ans2, n2))

n3 = 200
ans3 = coin_sums(n3)
print("{} ways to make {}".format(ans3, n3))
