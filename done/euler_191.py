#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Prize Strings
Problem 191
A particular school offers cash rewards to children with good attendance and
punctuality. If they are absent for three consecutive days or late on more
than one occasion then they forfeit their prize.

During an n-day period a trinary string is formed for each child consisting of
L's (late), O's (on time), and A's (absent).

Although there are eighty-one trinary strings for a 4-day period that can be
formed, exactly forty-three strings would lead to a prize:

OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
LAOO LAOA LAAO

How many "prize" strings exist over a 30-day period?
"""

from bib.decorations import cash_it


@cash_it
def prize_strings(remaining_days, two_back=False, one_back=False, late=False):
    if remaining_days == 0:
        return 1
    else:
        scount = 0
        if not late:
            scount += prize_strings(remaining_days-1, one_back, False, True)
        if two_back and one_back:
            scount += prize_strings(remaining_days-1, one_back, False, late)
        else:
            scount += prize_strings(remaining_days-1, one_back, True, late)
            scount += prize_strings(remaining_days-1, one_back, False, late)
        return scount


def p191():
    return prize_strings(30)


if __name__ == '__main__':
    assert prize_strings(4) == 43
    ANSWER = p191()
