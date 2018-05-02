#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Singleton difference
Problem 136
The positive integers, x, y, and z, are consecutive terms of an arithmetic
progression. Given that n is a positive integer, the equation,
x2 − y2 − z2 = n, has exactly one solution when n = 20:

132 − 102 − 72 = 20

In fact there are twenty-five values of n below one hundred for which the
equation has a unique solution.

How many values of n less than fifty million have exactly one solution?
"""
from itertools import count

upper_limit = 100

squares = [i*i for i in range(upper_limit)]
siv = [0]*(upper_limit+1)


def thing(z, y, x):
    return squares[x]-squares[y]-squares[z]


print(thing(13, 10, 7))

for arithmetic_stuff in count(1):
    for i in range(1, upper_limit*2):
        try:
            eval = thing(i, i+arithmetic_stuff, i+(2*arithmetic_stuff))
            if eval > 0:
                print(i, i+arithmetic_stuff, i+(2*arithmetic_stuff))
                print(eval)
                if eval < upper_limit:
                    siv[eval] += 1
        except:
            pass

    if arithmetic_stuff > 2*upper_limit:
        break

# for i in range(3, upper_limit, 3):
#     for j in range(1, (i//3)+1):
#         print("___")
#         eval = (thing(i, i-j, i-(2*j)))
#         print(i, i-j, i-(2*j), eval)
#         if 0 < eval < upper_limit:
#             siv[eval] += 1

print(siv)

answer = sum(1 for n in siv if n == 1)
# for i in range(len(siv)):
#     print(i+1, siv[i])
print(answer)

#
