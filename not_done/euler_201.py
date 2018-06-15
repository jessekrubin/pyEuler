#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Subsets with a unique sum
Problem 201
For any set A of numbers, let sum(A) be the sum of the elements of A.
Consider the set B = {1,3,6,8,10,11}.
There are 20 subsets of B containing three elements, and their sums are:

sum({1,3,6}) = 10,
sum({1,3,8}) = 12,
sum({1,3,10}) = 14,
sum({1,3,11}) = 15,
sum({1,6,8}) = 15,
sum({1,6,10}) = 17,
sum({1,6,11}) = 18,
sum({1,8,10}) = 19,
sum({1,8,11}) = 20,
sum({1,10,11}) = 22,
sum({3,6,8}) = 17,
sum({3,6,10}) = 19,
sum({3,6,11}) = 20,
sum({3,8,10}) = 21,
sum({3,8,11}) = 22,
sum({3,10,11}) = 24,
sum({6,8,10}) = 24,
sum({6,8,11}) = 25,
sum({6,10,11}) = 27,
sum({8,10,11}) = 29.

Some of these sums occur more than once, others are unique. For a set A, let
U(A,k) be the set of unique sums of k-element subsets of A, in our example we
find U(B,3) = {10,12,14,18,21,25,27,29} and sum(U(B,3)) = 156.

Now consider the 100-element set S = {1**2, 2**2, ... , 100**2}.
S has 100891344545564193334812497256 50-element subsets.

Determine the sum of all integers which are the sum of exactly one of the
50-element subsets of S, i.e. find sum(U(S,50)).
"""

from itertools import  combinations


from collections import defaultdict
from bisect import bisect
def greater_than(arr, n):
    return arr[bisect(arr, n):]

from bib.decorations import cash_it

def poss_nexts(arr, n, remaining):
    return greater_than(arr, n)[:-remaining]

def unique_sums(toople_list):
    d = defaultdict(set)
    for t in toople_list:
        d[sum(t)].add(t)
    retlist = []
    for k, v in d.items():
        if len(v) == 1:
            retlist.append(v.pop())
    return retlist

def less_than(arr, n):
    return arr[:bisect(arr, n)]


def subsetsum(array,num):

    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum(array[1:],(num - array[0]))
            if with_v:
                print([array[0]] + with_v)
                return [array[0]] + with_v
                # return None
            else:
                print(subsetsum(array[1:],num))
                return subsetsum(array[1:], num)


b = tuple([1, 3, 6, 8, 10, 11])
squares = tuple([i*i for i in range(1, 100+1)])




@cash_it
def subset_sums(nset, start_i, target_sum, size):
    if start_i >= len(nset):
        return 1 if target_sum == 0 and size == 0 else 0
    count = subset_sums(nset, start_i+1, target_sum, size)
    count += subset_sums(nset, start_i+1, target_sum-nset[start_i], size-1)
    return count

from tqdm import tqdm

def yewnu(b, subset_size):
    print(b, subset_size)
    smallest = sum(b[:subset_size])
    largest= sum(b[-subset_size:])
    print(smallest, largest)
    t =0
    for n in tqdm(range(smallest, largest+1)):
        subs = subset_sums(b, 0, n, 3)
        if subs == 1: t+=n
    print(t)


yewnu(b, 3)
# yewnu(squares, 50)




# def yew1(aset, sub_size):
#     print(aset, sub_size)
#     min_subsetsum = sum(aset[:sub_size])
#     maxsubsum = sum(aset[-sub_size:])
#     sums = [0]*(1+maxsubsum-min_subsetsum)
#     print(sums)
#     print(min_subsetsum, maxsubsum)
#     # d = {}
#     for c in combinations(aset, sub_size):
#         print(c)
#         print(sum(c))
#         sums[sum(c)-min_subsetsum] += 1
#     print(sums)
#     t = 0
#     for i in range(len(sums)):
#         if sums[i] == 1:
#             t += (i+min_subsetsum)
#     print(t)



# b = [1, 3, 6, 8, 10, 11]
# a = greater_than(b, 11)
# print(a)



# def yew2(aset, sub_size, total_size=None):
#     if sub_size == 2:
#         d = defaultdict(set)
#         combs = set()
#         for c in combinations(aset[:-(total_size-sub_size)], 2):
#             d[sum(c)].add(c)
#             combs.add(c)
#         # print(d)
#         # return {subs.pop() for subsum, subs in d.items() if len(subs) ==1}
#         # print(combs)
#         return combs
#     if sub_size > 2:
#         total_size = sub_size if total_size is None else total_size
#         subs=yew2(aset, sub_size-1, total_size)
#         d = defaultdict(set)
#         ds = set()
#
#         for subset in subs:
#             # print(subset)
#             maxs = subset[-1]
#             a = bisect(aset, maxs)
#             ns = aset[a:]
#             # print(ns)
#             if len(ns)>total_size-sub_size:
#                 # print(ns)
#                 for el in ns:
#                     # print(subsum+el)
#                     sss = subset + (el, )
#                     # print(sss)
#                     # d[sum(sss)].add(sss)
#                     d[sum(sss)].add(sss)
#                     ds.add(sss)
#                     # sss = subset, el
#                     # print(sss)
#         # return {subsum:subs.pop() for subsum, subs in d.items() if len(subs) == 1}
#         return {subs.pop() for subsum, subs in d.items() if len(subs) == 1}
# @cash_it
# def yew2(arr, remaining, target_size = None):
#     target_size = remaining if target_size is None else target_size
#     if remaining == 1:
#         return tuple([(arr[i], ) for i in range((1+len(arr)-target_size))])
#     elif remaining == 2:
#         a = yew2(arr, remaining-1, target_size)
#         d = defaultdict(set)
#         nextd = defaultdict(list)
#         subsya = []
#         for subsets in a:
#             for nexto in greater_than(tuple(arr), subsets[-1]):
#                 s = (subsets[-1], nexto)
#                 if len(s) > 0:
#                     nextd[nexto].append(subsets)
#                     subsya.append(s)
#         return tuple(subsya)
#     else:
#         last = yew2(arr, remaining-1, target_size)
#         # print(last)
#         d = defaultdict(set)
#         for toople in last:
#             # print(toople)
#             pn = greater_than(tuple(arr),toople[-1])
#             # print(pn)
#             for possible_next in pn:
#                 d[possible_next].add(toople)
#         # print(d)
#         l = []
#
#         anotherd = defaultdict(set)
#         for nexto, sets in d.items():
#             for toop in unique_sums(sets):
#                 l.append(toop+(nexto, ))
#                 # anotherd[sum(toop)+nexto].add((toop+(nexto, )))
#
#         # print(anotherd)
#         return tuple(l)
# @cash_it
# def yew2(arr, remaining, target_size = None):
#     target_size = remaining if target_size is None else target_size
#     if remaining == 1:
#         return tuple([(arr[i], ) for i in range((1+len(arr)-target_size))])
#     elif remaining == 2:
#         a = yew2(arr, remaining-1, target_size)
#         d = defaultdict(set)
#         nextd = defaultdict(list)
#         subsya = []
#         for subsets in a:
#             for nexto in greater_than(tuple(arr), subsets[-1]):
#                 s = (subsets[-1], nexto)
#                 if len(s) > 0:
#                     nextd[nexto].append(subsets)
#                     subsya.append(s)
#         return tuple(subsya)
#     else:
#         last = yew2(arr, remaining-1, target_size)
#         # print(last)
#         d = defaultdict(set)
#         for toople in last:
#             # print(toople)
#             pn = greater_than(tuple(arr),toople[-1])
#             # print(pn)
#             for possible_next in pn:
#                 d[possible_next].add(toople)
#         # print(d)
#         l = []
#
#         anotherd = defaultdict(set)
#         for nexto, sets in d.items():
#             for toop in unique_sums(sets):
#                 l.append(toop+(nexto, ))
#                 # anotherd[sum(toop)+nexto].add((toop+(nexto, )))
#
#         # print(anotherd)
#         return tuple(l)







