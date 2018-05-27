#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Problem Name
prob #

Prompt
"""

from itertools import  combinations


from collections import defaultdict
from bisect import bisect
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

def less_than(arr, n):
    return arr[:bisect(arr, n)]



# d = defaultdict(set)
# for n in b:
#     d[n].add((n, ))
#
# print(d)
# nd = defaultdict(set)
# for s1, s2 in combinations((v for v in d.values()), 2):
#     for e in s1:
#         for e2 in s2:
#             print(e, e2)
#             print(e+e2)
#             if len(e+e2) < 3 + 1:
#                 nd[sum(e+e2)].add(tuple(sorted(e+e2)))
#
# print(d)
# print(nd)
#
#
# for c in combinations(b):
#     print(c)


# A Dynamic Programming solution for
# subset sum problem

# Returns true if there is a subset
# of set[] with sun equal to given sum

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
                return([array[0]] + with_v)
                # return None
            else:
                print(subsetsum(array[1:],num))
                return(subsetsum(array[1:],num))


b = [1, 3, 6, 8, 10, 11]
# Driver program to test above function
n = len(b)
sm = 19
print(subsetsum(b, 19))

# for thing in a:
#     ansd[sum(thing)].add(thing)
#
# b = {k:v.pop() for k, v in ansd.items() if len(v)==1}
# print(b)
# print(sum(k for k in b))
#
# ansd = defaultdict(set)
# b = [i*i for i in range(1, 101)]
# a = yew2(tuple(b), 14)
# for thing in a:
#     ansd[sum(thing)].add(thing)
#
# b = {k:v.pop() for k, v in ansd.items() if len(v)==1}
# print(b)
# print(sum(k for k in b))


# def ssum_h(list, n, subset, sum):
#     if sum == 0:
#         print subset
#         return
#
#     if n == 0:
#         return
#
#     if list[n-1] <= sum:
#         ssum_h(list, n-1, subset, sum)
#         ssum_h(list, n-1, subset+`list[n-1]`+" ", sum-list[n-1])
#     else:
#         ssum_h(list, n-1, subset, sum)

def ssum_h(list, n, subset, sum):
    if subset is None:
        subset = []
    if sum == 0:
        print subset
        return

    if n == 0:
        return

    if subset[n-1] <= sum:
        ssum_h(list, n-1, subset, sum)
        ssum_h(list, n-1, subset+[n-1], sum-list[n-1])
    else:
        ssum_h(list, n-1, subset, sum)


# ssum(b,19)
ssum_h(b, len(b), None,19)






# print(a)
# print(sum(sum(k) for k in a))
# b = [1, 3, 6, 8, 10, 11]
# a = yew2(b, 4)
# print(a)
# print(sum(k for k in a))
# #
# b = [i*i for i in range(1, 101)]
# a = yew2(b, 10)
# print(a)
# from collections import Counter
# print(Counter(sum(k) for k in a))







# sb = [i*i for i in range(1, 101)]
# yew1(sb, 50)


# def p000():
#     pass
#
#
# if __name__ == '__main__':
#     p000()
