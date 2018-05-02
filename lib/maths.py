#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
from math import sqrt, pi, acos
from operator import add, sub

from lib.decorations import cash_muney
from sys import version_info

# py2/3 range/xrange
if version_info.major > 2:
    xrange = range


@cash_muney
def cash_factorial(n):
    if n == 1:
        return 1
    else:
        return cash_factorial(n - 1) * n


def rad2deg(n):
    return 180 * n / pi


def power_mod(number, exponent, mod):
    if exponent > 0:
        if exponent % 2 == 0:
            return power_mod(number, exponent // 2, mod)
        else:
            return power_mod(number, exponent // 2, mod) * number
    else:
        return 1


def divisors_gen(n):
    large_divisors = []
    for i in xrange(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor


def gcd(a, b):
    while a:
        a, b = b % a, a
    return b


def n_divisors(n):
    """
    >>> n_divisors(12)
    6
    >>> n_divisors(10)
    4
    """
    return sum(1 for _ in divisors_gen(n))


def divisors_list(n):
    return [div for div in divisors_gen(n)]


def n_digits(number):
    return sum((1 for _ in str(number)))


def reverse(n):
    """
    Reverses a number

    :param n:
    :return:
    """
    reversed = 0
    while n > 0:
        reversed *= 10
        reversed += n % 10
        n //= 10
    return reversed


@cash_muney
def fib(n):
    """Return the nth fibonacci number

    :param n: nth fib number index
    :return: nth fib number

    >>> fib(1)
    1
    >>> fib(2)
    2
    >>> fib(6)
    13
    """
    if n < 3:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def expo(d, n):
    """
    returns the number of times a divisor divides n (is the exponent)

    :param d: divisor
    :param n: number being divided
    :return:
    """
    if n < d:  # flip
        d, n = n, d
    c = n
    divs = 0
    while c % d == 0:
        c //= d
        divs += 1
    return divs


def length(vector):
    return sqrt(dproduct(vector, vector))


def angle(v1, v2):
    return acos(dproduct(v1, v2) / (length(v1) * length(v2)))


def dproduct(v1, v2):
    return sum((a * b) for a, b in zip(v1, v2))


class Vuple(tuple):
    """
    Vector-Tuple class
    """
    def __gt__(self, other):
        return Vuple.mag_sqrd(self) > Vuple.mag_sqrd(other)

    def __eq__(self, other):
        return Vuple.mag_sqrd(self) == Vuple.mag_sqrd(other)

    def __add__(self, other):
        return Vuple(map(add, self, other))

    def __sub__(self, other):
        return Vuple(map(sub, self, other))

    # @staticmethod
    # def unit_vuple(voop):
    #     return Vuple.

    # def mag_sqrd(self):
    #     return sum(el * el for el in self)

    @staticmethod
    def mag_sqrd(voop):
        return sum(el * el for el in voop)

    # @staticmethod
    # def mag(voop):
    #     return sqrt(Vuple(voop).mag_sqrd())

    @staticmethod
    def dot(a, b):
        return sum(va * vb for va, vb in zip(a, b))

    @staticmethod
    def cross(v1, v2):
        """Cross product of two 2d vectors

        :param v1: first vector
        :param v2: second vector
        :return: cross product
        """
        if len(v1) == 2 and len(v2) == 2:
            return (v1[0] * v2[1]) - (v1[1] * v2[0])
