# -*- coding: utf-8 -*-
# ~ Jesse Rubin ~ project Euler ~
"""
Problem Name
prob #

Prompt
"""

from copy import copy
from bib.maths import repermutations


def p(toppings, slices):
    za = [i for i in range(toppings)] * slices

    # print(za, repermutations(za))
    pizzas = set()
    ppp = []

    def _r(p, rem):

        if len(rem) == 0:
            print(p)
            pizzas.add(''.join(str(i) for i in p))
            ppp.append(''.join(str(i) for i in p))

            return
        else:
            # print(p, rem)
            sp = set(rem)
            # print(sp)
            for n in sp:
                rrem = copy(rem)
                rrem.remove(n)
                # print(rrem)
                tp = copy(p) + [n]
                _r(tp, rrem)

    za2 = copy(za)
    za2.sort()
    print(za2)
    _r([0], za2[1:])
    print(pizzas, ppp, len(pizzas), len(ppp))


p(3, 2)

# def p000():
#     pass

# if __name__ == '__main__':
#     ANSWER = p000()
#     print("ANSWER: {}".format(ANSWER))
