# -*- coding: utf-8 -*-
# ~ Jesse Rubin ~ project Euler ~
"""
Problem Name
prob #

Prompt
"""

from itertools import product
from collections import defaultdict

#         0    1    2    3    4    5
paths = ['│', '─', '┌', '└', '┐', '┘']
row_paths = {
    '│':'│┌└',
    '─':'─┐┘',
    '┌':'─┐┘',
    '└':'─┐┘',
    '┐':'┌└',
    '┘':'│┌└'
}
above = {'│':1, '─':0, '┌':0, '└':1, '┐':0, '┘':1}
below = {'│':1, '─':0, '┌':1, '└':0, '┐':1, '┘':0}

STARTINGS = {(1, 1, 1, 1), (1, 1, 0, 0), (0, 0, 1, 1), (0, 1, 1, 0)}
#            '┐  ┌  ┐  ┌'  '┐  ┌  ─  ─'  '─  ─  ┐  ┌'  '─  ┐  ┌  ─'
START = {
    (1, 1, 1, 1):'┐┌┐┌',
    (1, 1, 0, 0):'┐┌──',
    (0, 0, 1, 1):'──┐┌',
    (0, 1, 1, 0):'─┐┌─'
}

staring = [0, 2, 3]
ends = [0, 4, 5]

stuff = []
ad = defaultdict(set)
bd = defaultdict(set)
belowrow = defaultdict(tuple)
lasts = {(1, 0, 0, 1):'└──┘', (1, 1, 1, 1):'└┘└┘'}

TERMINATES = {'└┘┌┐', '┌┐└┘'}

for p in product(paths, repeat=4):
    if all(p[i+1] in row_paths[p[i]] for i in range(3)) and any(p[0] == paths[i] for i in staring) and any(p[-1] == paths[i] for i in ends):
        stuff.append(''.join(p))
        colstr = ''.join(p)
        u = tuple([above[pc] for pc in p])
        d = tuple([below[pc] for pc in p])
        if sum(u) > 0 and sum(d) > 0 and sum(u)%2==0 and sum(d)%2==0 and colstr not in TERMINATES:
            ad[u].add(colstr)
            bd[d].add(colstr)
            print(colstr, d)
            belowrow[colstr] = d

print(ad)
print(bd)
print(lasts)


# def tours(remaining, prev, cur, left_terminate=False, right_terminate=False):
#     # print(remaining, prev, cur)
#     if remaining == 0:
#         # print(cur, len(cur), terms)
#         if prev == (1, 0, 0, 1):
#             cur.append('└──┘')
#             print("\n".join(str(i)+' '+cur[i] for i in range(len(cur))))
#             return 1
#
#         elif prev == (1, 1, 1, 1):
#             if left_terminate or right_terminate:
#                 return 0
#             else:
#                 cur.append('└┘└┘')
#                 print("\n".join(str(i)+' '+cur[i] for i in range(len(cur))))
#                 return 1
#         else:
#             return 0
#     t = 0
#     for nextrow in ad[prev]:
#         tc = cur[:]
#         if nextrow[:3] == '┌┐':
#             if left_terminate:
#                 return 0
#             else:
#                 left_terminate = True
#         if nextrow[2:] == '┌┐':
#             if right_terminate:
#                 return 0
#             else:
#                 right_terminate= True
#         #     t += 2
#         # if '└┘' in nextrow:
#         #     t += 2
#         t += tours(remaining-1, belowrow[nextrow], cur + [nextrow], left_terminate, right_terminate)
#     return t
def tours(remaining, prev, cur):
    # print(remaining, prev, cur)
    if remaining == 0:
        # print(cur, len(cur), terms)
        if prev == (1, 0, 0, 1):
            cur.append('└──┘')
            print("\n".join(str(i)+' '+cur[i] for i in range(len(cur))))
            return 1

        elif prev == (1, 1, 1, 1):
            cur.append('└┘└┘')
            print("\n".join(str(i)+' '+cur[i] for i in range(len(cur))))
            return 1
        else:
            return 0
    t = 0
    for nextrow in ad[prev]:
        tc = cur[:]
        # if nextrow[:3] == '┌┐':
        #     if left_terminate:
        #         return 0
        #     else:
        #         left_terminate = True
        # if nextrow[2:] == '┌┐':
        #     if right_terminate:
        #         return 0
        #     else:
        #         right_terminate= True
        #     t += 2
        # if '└┘' in nextrow:
        #     t += 2
        t += tours(remaining-1, belowrow[nextrow], cur + [nextrow])
    return t

    # (1, 1, 1, 1):'┐┌┐┌',
    # (1, 1, 0, 0):'┐┌──',
    # (0, 0, 1, 1):'──┐┌',
    # (0, 1, 1, 0):'─┐┌─'

def T(n):
    total = 0
    for starting in START:
        total += tours(n, starting, [START[starting]])
    return total


# for i in range(1, 5):
#     print(i, T(i))
# print(T(10))


def p237():
    pass


if __name__ == '__main__':
    p237()
