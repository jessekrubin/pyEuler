#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Problem Name
prob #

Prompt
"""
#
# Cyclical figurate numbers
# Problem 61
# Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:
#
# Triangle
# P3,n=n(n+1)/2
# 1, 3, 6, 10, 15, ...

# Square
# P4,n=n2
# 1, 4, 9, 16, 25, ...

# Pentagonal
# P5,n=n(3n−1)/2
# 1, 5, 12, 22, 35, ...

# Hexagonal
# P6,n=n(2n−1)
# 1, 6, 15, 28, 45, ...

# Heptagonal
# P7,n=n(5n−3)/2
# 1, 7, 18, 34, 55, ...
#
# Octagonal
# P8,n=n(3n−2)
# 1, 8, 21, 40, 65, ...


# The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.
#
# The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
# Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
# This is the only set of 4-digit numbers with this property.
# Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.

from __future__ import division


p3 = lambda n: ((n*n)+n)//2
p4 = lambda n: (n*n)
p5 = lambda n: ((3*n*n)-(n))//2
p6 = lambda n: (2*n*n)-n
p7 = lambda n: ((5*n*n)-(3*n))//2
p8 = lambda n: (3*n*n)-(2*n)

from itertools import count
def gt1000_lt10000(f):
    l = []
    for i in count(1):
        a = f(i)

        if 1000 < a < 10000:
            l.append(a)
        elif a > 100000:
            return l


p3_list  = gt1000_lt10000(p3)
p4_list  = gt1000_lt10000(p4)
p5_list  = gt1000_lt10000(p5)
p6_list  = gt1000_lt10000(p6)
p7_list  = gt1000_lt10000(p7)
p8_list  = gt1000_lt10000(p8)
pn = [p3_list,p4_list,p5_list,p6_list,p7_list,p8_list]





def curses(has, cur):
    if sum(has) == 6 and cur[0]//100 == cur[-1]%100: return cur
    for n in range(6):
        if has[n]==0:
            for nexto in pn[n]:
                if cur[-1]%100 == nexto//100:
                    tc = cur[:]
                    tc.append(nexto)
                    thas = has[:]
                    thas[n] = 1
                    recurse = curses(thas, tc)
                    if recurse is not None:
                        return recurse
    return


for n in p3_list:
    has = [1, 0, 0, 0, 0, 0]
    ans = curses(has, [n])
    if ans is not None:
        print(ans)
        print(sum(ans))


# 28684
# for i in range(1,4):
    # print(p3(i))
    # print(p4(i))
    # print(p5(i))
    # print(p6(i))
    # print(p7(i))
    # print(p8(i))



def p000():
    pass


if __name__ == '__main__':
    p000()
