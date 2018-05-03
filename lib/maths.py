#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
from __future__ import division, generators, print_function, absolute_import
from math import sqrt, pi, acos
from operator import add, sub, methodcaller, truediv, floordiv
from lib.decorations import cash_muney

try: xrange
except NameError: xrange = range


@cash_muney
def cash_factorial(n):
    if n == 1:
        return 1
    else:
        return cash_factorial(n-1)*n


def radians_2_degrees(rads):
    return 180*rads/pi


def degrees_2_radians(degs):
    return degs*pi/180


def power_mod(number, exponent, mod):
    if exponent > 0:
        if exponent%2 == 0:
            return power_mod(number, floordiv(exponent, 2), mod)
        else:
            return power_mod(number, floordiv(exponent, 2), mod)*number
    else:
        return 1


def divisors_gen(n):
    large_divisors = []
    for i in xrange(1, int(sqrt(n)+1)):
        if n%i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n//i)
    for divisor in reversed(large_divisors):
        yield divisor


def gcd(a, b):
    while a:
        a, b = b%a, a
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
        reversed += n%10
        n //= 10
    return reversed


@cash_muney
def fib_r(n):
    """Recursively the nth fibonacci number

    Args:
        n (int): nth fibonacci sequence number

    Returns:
        int: the nth fibonacci number

    Examples:
        >>> fib_r(1)
        1
        >>> fib_r(2)
        2
        >>> fib_r(6)
        13
    """
    return n if n < 3 else fib_r(n-1)+fib_r(n-2)


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
    while c%d == 0:
        c //= d
        divs += 1
    return divs


def pytriple_gen(max_c):
    """primative pythagorean triples generator

    special thanks to 3Blue1Brown's video on pythagorean triples
    https://www.youtube.com/watch?v=QJYmyhnaaek&t=300s

    Args:
        max_c (int): max value of c to yeild triples up to

    Yields:
        tuple: pythagorean triple (a, b, c)
    """
    for real_pts in xrange(2, int(sqrt(max_c))+1, 1):
        for imag_pts in xrange(real_pts%2+1, real_pts, 2):
            comp = complex(real_pts, imag_pts)
            sqrd = comp*comp
            real = int(sqrd.real)
            imag = int(sqrd.imag)
            if abs(real-imag)%2 == 1 and gcd(imag, real) == 1:
                sea = int((comp*comp.conjugate()).real)
                if sea > max_c:
                    break
                else:
                    yield (imag, real, sea) if real > imag else (real, imag, sea)


class Trigon(object):
    """
    Trigon object composed of three points connected by lines.
    """

    def __init__(self, pt1, pt2, pt3):
        self.pt1 = Vuple(pt1)
        self.pt2 = Vuple(pt2)
        self.pt3 = Vuple(pt3)

    @classmethod
    def from_points(cls, pts):
        if len(pts) == 3:
            return Trigon(*pts)
        if len(pts) == 6:
            it = iter(pts)
            return Trigon(*zip(it, it))

    def __str__(self):
        return "<< {}, {}, {} >>".format(self.pt1, self.pt2, self.pt3)

    def __contains__(self, point):
        if type(point) is not Vuple:
            point = Vuple(point)
        return self.area() == sum(map(methodcaller('area'),
                                      self.inner_triangles(point)))

    def inner_triangles(self, point):
        t1 = Trigon(point, self.pt2, self.pt3)
        t2 = Trigon(self.pt1, point, self.pt3)
        t3 = Trigon(self.pt1, self.pt2, point)
        return t1, t2, t3

    def is_perimeter_point(self, point):
        if type(point) is not Vuple:
            point = Vuple(point)
        return any(tri_area == 0 for tri_area in
                   map(methodcaller('area'), self.inner_triangles(point)))

    def points(self):
        return self.pt1, self.pt2, self.pt3

    def contains_origin(self):
        return (0, 0) in self

    def area(self):
        return abs(truediv(Vuple.cproduct(self.pt1-self.pt2,
                                          self.pt3-self.pt2), 2))

    @staticmethod
    def area_from_points(pt1, pt2, pt3):
        return abs(truediv(Vuple.cproduct(pt1-pt2, pt3-pt2), 2))


class Vuple(tuple):
    """
    Vector-Tuple class
    """

    def __gt__(self, other):
        """Greater than based on magnitude (proportional)

        :param other:
        :return:
        """
        return Vuple.mag_sqrd(self) > Vuple.mag_sqrd(other)

    def __eq__(self, other):
        return Vuple.mag_sqrd(self) == Vuple.mag_sqrd(other)

    def __add__(self, other):
        return Vuple(map(add, self, other))

    def __sub__(self, other):
        return Vuple(map(sub, self, other))

    def __mul__(self, k):
        if type(k) is int or type(k) is float:
            return self._mul_scalar(k)
        # return Vuple(map(sub, self, k))

    def __imul__(self, k):
        if type(k) is int or type(k) is float:
            return self._mul_scalar(k)

    def _mul_scalar(self, k):
        return Vuple((k*el for el in self))

    def __truediv__(self, k):
        if type(k) is int or type(k) is float:
            return self._truediv_scalar(k)
        # return Vuple(map(sub, self, k))

    def __itruediv__(self, k):
        if type(k) is int or type(k) is float:
            return self._truediv_scalar(k)

    def _truediv_scalar(self, k):
        return Vuple((el/k for el in self))

    def normalize(self):
        return Vuple.unit_vuple(self)

    @staticmethod
    def unit_vuple(voop):
        return Vuple(voop)/Vuple.mag(voop)

    def get_mag_sqrd(self):
        return Vuple.mag_sqrd(self)

    @staticmethod
    def mag_sqrd(voop):
        return sum(el*el for el in voop)

    def get_mag(self):
        return Vuple.mag(self)

    @staticmethod
    def mag(voop):
        return sqrt(Vuple.mag_sqrd(voop))

    @staticmethod
    def dproduct(a, b):
        return sum(va*vb for va, vb in zip(a, b))

    @staticmethod
    def cproduct(v1, v2):
        """Cross product of two 2d vectors

        :param v1: first vector
        :param v2: second vector
        :return: cproduct product
        """
        if len(v1) == 2 and len(v2) == 2:
            return (v1[0]*v2[1])-(v1[1]*v2[0])

    @staticmethod
    def angle(v1, v2, radians=True):
        # return acos(Vuple.dproduct(v1, v2)/(Vuple.mag(v1)*Vuple.mag(v2)))
        q = 1 if radians else (180)/(pi)
        return q*acos(Vuple.dproduct(Vuple.unit_vuple(v1),
                                     Vuple.unit_vuple(v2)))
