#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Problem 0
template
"""


def pascal_div_seven(n):
    nent = sum(i for i in range(1, n+1))
    ret_sum = 0
    loop_number = 1
    cur_thing = 6
    for i in range(1, 100 - 5):
        ret_sum += cur_thing
        if cur_thing < 0:
            loop_number += 1
            cur_thing = ((6*loop_number)//7)
        else:
            cur_thing -= loop_number
    print(")))))))))))))))))))")
    print(nent)
    print(ret_sum)

    return (nent - ret_sum)

answer = pascal_div_seven(100)
print(answer)






