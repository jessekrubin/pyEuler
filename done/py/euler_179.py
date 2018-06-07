#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Consecutive positive divisors
Problem 179
Find the number of integers 1 < n < 10^7, for which n and n + 1 have the same
number of positive divisors. For example, 14 has the positive divisors
1, 2, 7, 14 while 15 has 1, 3, 5, 15.
"""

def p179(limit=10**7):
    divs = [0]*(limit+1)
    for i in range(1, (limit+1)//2):
        for j in range(i,limit+1, i):
            divs[j]+=1

    consecutive_pdivs_count=0
    for i in range(len(divs)-1):
        if divs[i]==divs[i+1]:
            consecutive_pdivs_count+=1
    return consecutive_pdivs_count

if __name__ == '__main__':
    ANSWER = p179()
    print("ANSWER: {}".format(ANSWER))
