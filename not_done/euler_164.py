#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Number Mind
Problem 185
The game Number Mind is a variant of the well known game Master Mind.

Instead of coloured pegs, you have to guess a secret sequence of digits. After each guess you're only told in how
many places you've guessed the correct digit. So, if the sequence was 1234 and you guessed 2036, you'd be told
that you have one correct digit; however, you would NOT be told that you also have another digit in the wrong place.

For instance, given the following guesses for a 5-digit secret sequence,

90342 ;2 correct
70794 ;0 correct
39458 ;2 correct
34109 ;1 correct
51545 ;2 correct
12531 ;1 correct

The correct sequence 39542 is unique.

Based on the following guesses,

5616185650518293 ;2 correct
3847439647293047 ;1 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
3174248439465858 ;1 correct
4513559094146117 ;2 correct
7890971548908067 ;3 correct
8157356344118483 ;1 correct
2615250744386899 ;2 correct
8690095851526254 ;3 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2321386104303845 ;0 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
1748270476758276 ;3 correct
4895722652190306 ;1 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct
2659862637316867 ;2 correct

Find the unique 16-digit secret sequence.
"""

guesses_5 = """
90342 ;2 correct
70794 ;0 correct
39458 ;2 correct
34109 ;1 correct
51545 ;2 correct
12531 ;1 correct
"""
import itertools

def guess_dict(guesses_string):
    lines = [line.replace(';', '').split(' ') for line in guesses_string.split('\n') if len(line)>1]
    return {line[0]:int(line[1]) for line in lines}


def number_mind(guesses_dict):
    n_digits = len([k for k in guesses_dict.keys()].__getitem__(0))
    print(n_digits)

    def recursing(dict):
        print(dict)
        for k, v in dict.items():
            if v > 0:
                print(k, v)
                print(k[0])

    print(recursing(guesses_dict))

    # for combo in itertools.combinations(guesses_dict.keys(), 2):
    #     print(combo)



guesses_5dict = guess_dict(guesses_5)
number_mind(guesses_5dict)















