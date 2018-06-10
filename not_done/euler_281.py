#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Pizza Toppings
Problem 281
You are given a pizza (perfect circle) that has been cut into m·n equal pieces
and you want to have exactly one topping on each slice.

Let f(m,n) denote the number of ways you can have toppings on the pizza with m
different toppings (m ≥ 2), using each topping on exactly n slices (n ≥ 1).
Reflections are considered distinct, rotations are not.

Thus, for instance, f(2,1) = 1, f(2,2) = f(3,1) = 2 and f(3,2) = 16.
f(3,2) is shown below:

p281_pizza.gif

Find the sum of all f(m,n) such that f(m,n) ≤ 10**15.
"""



def pizza(toppings, slices):

    def _r(p, rem):
        if len(rem)==0:
            print(p)
        else:
            for i in range(len(rem)):
                print(p, rem)

    p = ''.join([str(i) for i in range(toppings)] * slices)
    print(p, int(p, 3))
    _r([], p)

pizza(3, 2)




