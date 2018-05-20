#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Number Mind
Problem 185
The game Number Mind is a variant of the well known game Master Mind.

Instead of coloured pegs, you have to guess a secret sequence of digits. After
each guess you're only told in how many places youve guessed the , digit.
So, if the sequence was 1234 and you guessed 2036, you'd be told that you have
one , digit: however, you would NOT be told that you also have another
digit in the wrong place.

For instance, given the following guesses for a 5-digit secret sequence,

90342 :2 ,
70794 :0 ,
39458 :2 ,
34109 :1 ,
51545 :2 ,
12531 :1 ,

The , sequence 39542 is unique.

Based on the following guesses,

5616185650518293 :2 ,
3847439647293047 :1 ,
5855462940810587 :3 ,
9742855507068353 :3 ,
4296849643607543 :3 ,
3174248439465858 :1 ,
4513559094146117 :2 ,
7890971548908067 :3 ,
8157356344118483 :1 ,
2615250744386899 :2 ,
8690095851526254 :3 ,
6375711915077050 :1 ,
6913859173121360 :1 ,
6442889055042768 :2 ,
2321386104303845 :0 ,
2326509471271448 :2 ,
5251583379644322 :2 ,
1748270476758276 :3 ,
4895722652190306 :1 ,
3041631117224635 :3 ,
1841236454324589 :3 ,
2659862637316867 :2 ,

Find the unique 16-digit secret sequence.
"""

lil_test = {'90342':2, '70794':0, '39458':2, '34109':1, '51545':2, '12531':1}

guesses = {'5616185650518293':2, '3847439647293047':1, '5855462940810587':3,
           '9742855507068353':3, '4296849643607543':3, '3174248439465858':1,
           '4513559094146117':2, '7890971548908067':3, '8157356344118483':1,
           '2615250744386899':2, '8690095851526254':3, '6375711915077050':1,
           '6913859173121360':1, '6442889055042768':2, '2321386104303845':0,
           '2326509471271448':2, '5251583379644322':2, '1748270476758276':3,
           '4895722652190306':1, '3041631117224635':3, '1841236454324589':3,
           '2659862637316867':2}


def number_mind2(gd, pd=None):
    if pd is None:
        pd = ['0123456789',]*5
    zeros = [k for k, v in gd.items() if v==0]
    print(zeros)

    for z in zeros:
        for i in range(len(z)):
            pd[i] = pd[i].replace(z[i], '')

    ones = {k:v for k, v in gd.items() if v == 1}


    print(ones)
    print(pd)





# number_mind2(lil_test)


guessescount = 0
def number_mind3(d, length=None, seq=None):
    global guessescount
    if length is None: length = set(len(k) for k in d).pop()
    if seq is None: seq = ''
    if len(seq) == length:
        if sum(val for val in d.values())==0:
            print(seq)
            return seq
        else:
            return
    i = len(seq)
    possibles = set(k[i] for k in d)-set(k[i] for k, v in d.items() if v == 0)


    print(possibles)
    stats = dict()
    for p in possibles:
        print("+", p)
        for k, v in d.items():
            if v>0 and k[i]==p:
                stats[p] = stats.get(p, default=0)+v
    print(stats)
    print(len(stats))
    print(sum(v for v in stats.values()))
    print(possibles)


    # if len(possibles)==0:
    #     return
    # for p in possibles:
    #     for k, v in d.items():
    #         if k[i] == p:
    #             d[k] -= 1
    #     ns = seq+p
    #     guessescount += 1
    #     print(seq, guessescount)
    #     nm = number_mind3(d, length, ns)
    #     if nm is not None:
    #         return nm
    #     for k, v in d.items():
    #         if k[i] == p:
    #             d[k] += 1


# guessescount = 0
# def number_mind3(d, length=None, seq=None):
#     global guessescount
#     if length is None: length = set(len(k) for k in d).pop()
#     if seq is None: seq = ''
#     if len(seq) == length:
#         if sum(val for val in d.values())==0:
#             print(seq)
#             return seq
#         else:
#             return
#     i = len(seq)
#     possibles = set(k[i] for k in d)-set(k[i] for k, v in d.items() if v == 0)
#     if len(possibles)==0:
#         return
#     for p in possibles:
#         for k, v in d.items():
#             if k[i] == p:
#                 d[k] -= 1
#         ns = seq+p
#         guessescount += 1
#         print(seq, guessescount)
#         nm = number_mind3(d, length, ns)
#         if nm is not None:
#             return nm
#         for k, v in d.items():
#             if k[i] == p:
#                 d[k] += 1
#
# def p185():
#     return number_mind3(guesses)
#
#
if __name__ == '__main__':
    ans = number_mind3(lil_test)
    print(ans)
    assert ans == str(39542)
#     ANSWER = p185()
