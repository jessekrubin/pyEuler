#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler


from lib.maths import divisors_list

def square_lams2(upperlimit):
    divfours = [i for i in range(upperlimit+1) if i % 4 == 0 and i >4]
    total = 0
    for num in divfours:
        divs = divisors_list(num//4)
        num_lams = len(divs)//2
        if 0 < num_lams < 11:
            total += 1

    return (total)


ans = square_lams2(1000000)
print("ANSWER: {}".format(ans))

