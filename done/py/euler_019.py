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
from bib.decorations import tictoc

@tictoc(runs=1000)
def p019():
    return sum(1 for day in  # count 1 for each day...
               range(date(1901, 1, 1).toordinal(),  # from the start ord
                     date(2000, 12, 31).toordinal())  # to the end ord
               if date.fromordinal(day).weekday() == 6  # IF it is a sunday
               and date.fromordinal(day).day == 1)  # AND the date is the 1st


if __name__ == '__main__':
    answer = p019()
    print("Number of Sunday 1'st days is {}".format(answer))
