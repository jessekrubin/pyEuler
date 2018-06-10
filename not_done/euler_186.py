#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse Rubin ~ project Euler ~
"""
Connectedness of a network
http://projecteuler.net/problem=186
Here are the records from a busy telephone system with one million users:

                        ╔═══════╦════════╦════════╗
                        ║ RecNr ║ Caller ║ Called ║
                        ╠═══════╬════════╬════════╣
                        ║     1 ║ 200007 ║ 100053 ║
                        ║     2 ║ 600183 ║ 500439 ║
                        ║     3 ║ 600863 ║ 701497 ║
                        ║   ... ║    ... ║    ... ║
                        ╚═══════╩════════╩════════╝

The telephone number of the caller and the called number in record n are
Caller(n) = S2n-1 and Called(n) = S2n where S1,2,3,... come from the "Lagged
Fibonacci Generator":

For 1 ≤ k ≤ 55, Sk = [100003 - 200003k + 300007k3] (modulo 1000000)
For 56 ≤ k, Sk = [Sk-24 + Sk-55] (modulo 1000000)

If Caller(n) = Called(n) then the user is assumed to have misdialled and the
call fails; otherwise the call is successful.

From the start of the records, we say that any pair of users X and Y are
friends if X calls Y or vice-versa. Similarly, X is a friend of a friend of Z
if X is a friend of Y and Y is a friend of Z; and so on for longer chains. The
Prime Minister's phone number is 524287. After how many successful calls, not
counting misdials, will 99% of the users (including the PM) be a friend, or a
friend of a friend etc.
"""
from __future__ import division, print_function, generators
from itertools import count
from collections import defaultdict
from bib import xrange
from bib.decorations import cash_it


@cash_it  # cached 4 recursing
def lagged_fib_gen(k):
    """pretty self explanatory"""
    if 1 <= k <= 55:
        return int((100003 - 200003 * k + 300007 * k**3) % 1000000)
    else:
        return int((lagged_fib_gen(k - 24) + lagged_fib_gen(k - 55)) % 1000000)


def phone_records_gen():
    """phone records generator"""
    return ((lagged_fib_gen(2 * n - 1), lagged_fib_gen(2 * n))
            for n in count(1))

n = phone_records_gen()
for i in range(3):
    print(next(n))

pm, percentage = 555552, 10
# 525542
# pm = 524287 # prime minister's personal cell
# percentage = 10
# records = phone_records_gen()
# gee = defaultdict(set)
#
# while pm not in gee:
#     caller, called = next(records)
#     if caller != called:
#         gee[caller].add(called)
#         gee[called].add(caller)
#
# def friends(phone=pm, ratio=percentage):
#     seen = {pm}
#
#     def _trevor(numb):
#         for friendnumb in gee[numb]:
#             if friendnumb not in seen:
#                 seen.add(friendnumb)
#                 _trevor(friendnumb)
#     _trevor(pm)
#     return len(seen)
#
# for called, caller in records:
#     caller, called = next(records)
#     gee[caller].add(called)
#     gee[called].add(caller)
#     # print(gee)
#     f = friends()
#     print(f, len(gee), f/len(gee))
#
#     if len(gee)>550000:
#         break


# networks = defaultdict(set)
# for i in count():
#     call = set(next(records))
#     # print(call)
#     overlaps = []
#     overlap = False
#     for network in networks.values():
#         # print(network)
#         if not network.isdisjoint(call):
#             network.update(call)
#             for n in call:
#                 networks[n] = network
#             overlap = True
#     if overlap is False:
#         for numb in call:
#             networks[numb] = call
#     # print(networks)
#     if pm in call:
#         print("YEA")
#         print(len(networks))
#         print(networks[pm])
#         print(len(networks[pm]) / len(networks))
#     print(networks)
#     if i > 526000:
#
#         break

    # if i > 1000:
    #     break
