#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler


from lib.maths import divisors_list

def square_lams(upperlimit):
    divfours = [i for i in range(upperlimit+1) if i % 4 == 0 and i >4]
    total = 0
    for num in divfours:
        divs = divisors_list(num//4)
        total += len(divs)//2

    return (total)

assert 41 == square_lams(100)
ans = square_lams(1000000)
print("ANSWER: {}".format(ans))

