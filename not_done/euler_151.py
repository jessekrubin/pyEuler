#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Problem Name
prob #

Prompt
"""
from __future__ import division
from bib.decorations import cash_it

def cutpaper(p):
    return sorted([p//2] + cutpaper(p//2)) if p > 1 else [p]

# a = cutpaper(16)
# print(a)
@cash_it
def paper(e):
    print(e)
    # print(len(e))
    if sum(e) == 1:
        return 0, 1
    c = 1 if 16 > sum(e) > 1 and len(e)==1 else 0
    bbb = len(e)
    # thing = tuple(cutpaper(e[0]))
    for i in range(len(e)):
        ne = sorted([e[j] for j in range(len(e)) if j != i])
        if e[i] > 1:
            cut = cutpaper(e[i])
            # print(cut)
            ne.extend(cut)
            ne.sort()
        if len(ne)>1:
            # print(ne)
            a, b = paper(tuple(ne))
            c += a
            bbb += b


    print(c, bbb)
    print(c/bbb)
    return c, bbb

print(paper(tuple([16])))






# """
# abcd
# efgh
# ijkl
# mnop
# """
#
# start = ['abefijmn','cdgh', 'ko', 'l']
#
# def cutpaper(p):
#     if len(p) == 1: return [p]
#     return [p[0:len(p)//2]] + list(cutpaper(p[len(p)//2:]))[:-1]
#
# a = cutpaper('abcdefghijklmnop')
# print(a)
# t = 0
#
# def paper(envelope):
#     global t
#     # print(envelope)
#     if len(envelope)==1 and len(envelope[0])==1:
#         t += 1
#         return 0
#     elif len(envelope)==1 and len(envelope[0])!=1:
#         c = 1
#     else:
#         c = 0
#
#     for i in range(len(envelope)):
#         # a = cutpaper(envelope[i])
#         # print(a)
#         ne = envelope[0:i]+cutpaper(envelope[i])[0:-1]+envelope[i+1:]
#         # print(ne)
#         c += paper(ne)
#
#     return c
#
# ans = paper(start)
# print(ans, t)




# def p240():
#     pass
#
#
# if __name__ == '__main__':
#     p240()
