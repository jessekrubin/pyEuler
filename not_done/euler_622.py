#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler


# Riffle Shuffles
# Problem 622
# A riffle shuffle is executed as follows: a deck of cards is split into two equal halves, with the top half taken in the left hand and the bottom half taken in the right hand. Next, the cards are interleaved exactly, with the top card in the right half inserted just after the top card in the left half, the 2nd card in the right half just after the 2nd card in the left half, etc. (Note that this process preserves the location of the top and bottom card of the deck)
#
# Let s(n) be the minimum number of consecutive riffle shuffles needed to restore a deck of size n to its original configuration, where n is a positive even number.
#
# Amazingly, a standard deck of 52 cards will first return to its original configuration after only 8 perfect shuffles, so s(52)=8. It can be verified that a deck of 86 cards will also return to its original configuration after exactly 8 shuffles, and the sum of all values of n that satisfy s(n)=8 is 412.
#
# Find the sum of all values of n that satisfy s(n)=60.

from lib.maths import pfactors_gen


def s(n):
    if n%2 == 1:
        raise Exception("MUST BE EVEN")

    def riffle(cards):
        return [j for i in zip(cards[:hf+1], cards[hf:]) for j in i]

    hf = n//2

    cerdz = riffle([i for i in range(n)])
    count = 1
    while not all(cerdz[i] == i for i in range(n)):
        cerdz = riffle(cerdz)
        count += 1
        if count > 60:
            return None
    return count


print(2**8-1)

print(pfactors_gen(2**8-1))
# count = {j}
count = 0
# for i in trange(2, 100000, 2, ascii=True):
for i in range(2, 1000, 2):
    res = s(i)
    if res == 8:
        # if res == 60 or :
        #     count[res] = count.get(res, 0) + i
        count += i
        print("___")
        print(count, i)
        # print(pfactors_gen(i), i)
        # print(pfactors_gen(count[res]), count[res])

print(count)
