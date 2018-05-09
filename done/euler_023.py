#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse and Graham Rubin
"""
Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper divisors_gen is
exactly equal to the number. For example, the sum of the proper divisors_gen of
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors_gen is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""

from biblioteca import divisors_list


def sum_divisors(n):
    return sum((divisor for divisor in divisors_list(n))) / 2


def p023():
    a_bun = set()
    d_fish = set()
    perf = set()

    for i in range(1, 28124):
        # print("___")
        # print(i)
        sum_divs = sum_divisors(i)
        if sum_divs == i:
            perf.add(int(sum_divs))
        else:
            if sum_divs > i:
                a_bun.add(i)
            else:
                d_fish.add(i)

    abun_sums = set()
    for abunNum in a_bun:
        for another_abun in a_bun:
            abun_sums.add(abunNum + another_abun)

    answer_sum = 0
    for i in range(28124):
        if i not in abun_sums:
            answer_sum += i
    return answer_sum


if __name__ == '__main__':
    ans = p023()
    print("Sum: {}".format(ans))  # Sum: 4179871