#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Counting Sundays
Problem 19 
You are given the following information, but you may prefer to do some research
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""

from datetime import date


def p019():
    START = date(1901, 1, 1)
    START_ORD = START.toordinal()
    FINISH = date(2000, 12, 31)
    FINISH_ORD = FINISH.toordinal()
    N_SUNDAYS = 0

    for day in range(START_ORD, FINISH_ORD):
        d = date.fromordinal(day)
        if (d.weekday() == 6) and (d.day == 1):
            N_SUNDAYS += 1
    return N_SUNDAYS


if __name__ == '__main__':
    answer = p019()
    print("Number of Sunday 1'st days is {}".format(answer))