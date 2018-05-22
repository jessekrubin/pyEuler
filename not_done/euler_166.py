#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Criss Cross
Problem 166
A 4x4 grid is filled with digits d, 0 ≤ d ≤ 9.

It can be seen that in the grid

6 3 3 0
5 0 4 3
0 7 1 4
1 2 4 5

the sum of each row and each column has the value 12. Moreover the sum of each diagonal is also 12.

In how many ways can you fill a 4x4 grid with the digits d, 0 ≤ d ≤ 9 so that each row, each column, and both diagonals have the same sum?
"""
# INDICES
# [0,  1,  2,  3,
#  4,  5,  6   7,
#  8,  9, 10, 11,
# 12, 13, 14, 15]
from collections import defaultdict
from itertools import permutations, combinations, combinations_with_replacement

bslash = [0, 5, 10, 15]
fslash = [3, 6, 9, 12]


def flatten(l):
    return [item for sublist in l for item in sublist]


def rowi(r):
    return [i for i in range(r*4, r*4+4)]


def coli(c):
    return [i for i in range(c, 16, 4)]


# def is_criss_cross(arr):
#     firstrowsum = sum(arr[i] for i in rowi(0))
#     for ci in range(4):
#         if firstrowsum != sum(arr[i] for i in coli(ci)):
#             return False
#             # return 1 == len((set.union({sum(arr[i] for i in coli(i)) for i in range(4)},
#             #                            {sum(arr[i] for i in rowi(i)) for i in range(4)},
#             #                            {sum(arr[i] for i in bslash)},
#             #                            {sum(arr[i] for i in fslash)})))
#     if sum(arr[i] for i in bslash)!=firstrowsum or firstrowsum!=sum(arr[i] for i in fslash):
#         return False
#     return True


sum_combos = defaultdict(set)
for combo in combinations_with_replacement([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4):
    # sum_combos[sum(combo)].add(tuple(p for p in permutations(combo)]))
    csum = sum(combo)
    for perm in permutations(combo):
        sum_combos[csum].add(perm)

thirty_five = sum_combos[35]
thirty_three = sum_combos[33]


# for k, v in sum_combos.items():
#     print(k, len(v))
# print(sum_combos)
# print(thirty_five)

# for cr in combinations_with_replacement(thirty_five, 4):
#     print(cr)

def p166():
    pass


dictionary = {}

for k, v in sum_combos.items():
    # print(v)
    dictionary[k] = {}
    for i in range(1, 10):
        dictionary[k][i] = set(n for n in v if n[0] == i)

# things_test= 0
#
# for i in range(33, 35):
#     for k, v in dictionary[i].items():
#         if len(v)>0:
#             for co in combinations_with_replacement(v, 2):
#                 print(co)
#                 co2 = (co[1], co[0])
#
#                 things_test += 1
#
#
#
# print(things_test)
#

def is_criss_cross2(arr):
    firstrowsum = sum(arr[i] for i in rowi(0))
    for ci in range(4):
        if tuple((arr[i] for i in coli(ci))) not in sum_combos[firstrowsum]:
            return False
            # return 1 == len((set.union({sum(arr[i] for i in coli(i)) for i in range(4)},
            #                            {sum(arr[i] for i in rowi(i)) for i in range(4)},
            #                            {sum(arr[i] for i in bslash)},
            #                            {sum(arr[i] for i in fslash)})))
    if tuple((arr[i] for i in bslash)) not in sum_combos[firstrowsum]:
        return False
    if tuple((arr[i] for i in fslash)) not in sum_combos[firstrowsum]:
        return False
    return True
# ncc = 0
# for sumthing in range(35):
#     print("")
#     print(sumthing)
#     sumthingtot = 0
#     for comb in combinations_with_replacement(sum_combos[sumthing], 4):
#         # print(comb)
#         flat = flatten(comb)
#         # print(flat)
#         if is_criss_cross2(flat):
#             sumthingtot+= 1
#             # print(flat)
#         # print(is_criss_cross(flat))
#     print(sumthingtot)

# 0
# 1
#
# 1
# 0
#
# 2
# 4
#
# 3
# 9
#
# 4
# 35
#
# 5
# 79
#
# 6
# 219
#
# 7
# 447

cc = [6, 3, 3, 0,
      5, 0, 4, 3,
      0, 7, 1, 4,
      1, 2, 4, 5]
scc = ['6', '3', '3', '0',
       '5', '_', '4', '_',
       '0', '7', '_', '_',
       '1', '_', '_', '_']

def triangle_cc(tcc):
    print(tcc)
    ccsum = sum(int(tcc[n]) for n in range(4))
    print(ccsum)


triangle_cc(scc)

def criss_cross(total = 3):
    sumset = sum_combos[total]
    starts = defaultdict(set)
    for s in sumset:
        starts[s[0]].add(s)
    print(sumset, starts)

    arr = [0]*16
    for first_n, toopset in starts.items():
        print(first_n)
        for comba, combb in combinations_with_replacement(toopset, 2):
            print("")
            print(comba, combb)
            sss = set()
            for n in sumset:
                if n[0]== comba[3] and n[3] == combb[3]:
                    sss.add(n)
                if n[3]== comba[3] and n[0] == combb[3]:
                    sss.add(n)
            print(sss)






# criss_cross()



# for k, v in sum_combos.items():
#     print(k, len(v))

if __name__ == '__main__':
    cc = [6, 3, 3, 0,
          5, 0, 4, 3,
          0, 7, 1, 4,
          1, 2, 4, 5]
    assert is_criss_cross2(cc)
    p166()
