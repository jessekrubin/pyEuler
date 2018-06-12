# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Coin sums
Problem 31
In England the currency is made up of pound, £, and pence, pytriple_gen, and there are
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


def p031():
    return coin_sums(200)


if __name__ == '__main__':
    assert 4 == coin_sums(5)
    assert 4563 == coin_sums(100)
    ans3 = p031()
    print("{} ways to make {}".format(ans3, 200))
