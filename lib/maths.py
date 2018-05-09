#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
from __future__ import division, generators, print_function, absolute_import

from bisect import bisect_right, bisect_left
from itertools import count, chain
from math import sqrt, pi, acos
from operator import add, sub, methodcaller, truediv, floordiv
from lib.decorations import cash_muney

try: xrange
except NameError: xrange = range


def partitions(n, I=1):
    yield (n,)
    for i in range(I, n//2+1):
        for p in partitions(n-i, i):
            yield (i,)+p


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


def itgcd(a, b):
    while a:
        a, b = b%a, a
    return b


@cash_muney
def rgcd(a, b):
    if b > a:
        return rgcd(b, a)
    r = a%b
    if r == 0:
        return b
    return rgcd(r, b)


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
            if abs(real-imag)%2 == 1 and itgcd(imag, real) == 1:
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
        q = 1 if radians else 180/pi
        return q*acos(Vuple.dproduct(Vuple.unit_vuple(v1),
                                     Vuple.unit_vuple(v2)))


def prime_gen(plim=0, kprimes=None):
    """
    infinite (within reason) prime number generator

    My big modification is the pdiv_dictionary() function that recreats the
    dictionary of divisors so that you can continue to generate prime numbers
    from a (sorted) list of prime numbers.

    BASED ON:
        eratosthenes by David Eppstein, UC Irvine, 28 Feb 2002
        http://code.activestate.com/recipes/117119/
        and
        the thread at that url


    :param plim: upper limit of numbers to check
    :param kprimes: known primes list
    :return:
    """

    if kprimes is None: kprimes = [2, 3, 5, 7, 11]

    def pdiv_dictionary():
        """
        Recreates the prime divisors dictionary used by the generator
        """
        div_dict = {}
        for pdiv in kprimes:  # for each prime
            multiple = kprimes[-1]//pdiv*pdiv
            if multiple%2 == 0:
                multiple += pdiv
            else:
                multiple += 2*pdiv
            while multiple in div_dict: multiple += pdiv*2
            div_dict[multiple] = pdiv
        return div_dict

    # [1]
    # See if the upper bound is greater than the known primes
    if 0 < plim <= kprimes[-1]:
        for p in kprimes:
            if p <= plim:
                yield p
        return  # return bc we are done

    # [2]
    # Recreate the prime divisibility dictionary using kprimes;
    # Set start and yield first 4 primes
    divz = pdiv_dictionary()
    start = kprimes[-1]+2  # max prime + 2 (make sure it is odd)
    if start == 13: yield 2; yield 3; yield 5; yield 7; yield 11
    # use count or range depending on if generator is infinite
    it = count(start, 2) if plim == 0 else xrange(start, plim, 2)

    for num in it:
        prime_div = divz.pop(num, None)
        if prime_div:
            multiple = (2*prime_div)+num
            while multiple in divz: multiple += (2*prime_div)
            divz[multiple] = prime_div
        else:
            divz[num*num] = num
            yield num


def pfactorization_gen(n):
    return (n for n in chain.from_iterable([p]*expo(p, n) for p in pfactors_gen(n)))


def pfactors_gen(n):
    """
    Returns prime factorization as a list

    :param n:
    :return:
    """
    return (p for p in divisors_gen(n) if is_prime(p))


@cash_muney
def is_prime(number):
    """
    Returns True if number is prime

    >>> is_prime(37)
    True
    >>> is_prime(100)
    False
    >>> is_prime(89)
    True
    """
    if number == 2 or number == 3:
        return True
    if number < 2 or number%2 == 0:
        return False
    if number < 9:
        return True
    if number%3 == 0:
        return False
    r = int(number**0.5)
    step = 5
    while step <= r:
        if number%step == 0:
            return False
        if number%(step+2) == 0:
            return False
        step += 6
    return True


class OctopusPrime(list):
    """
    OctopusPrime, the 8-leg autobot, here to help you find PRIMES

    ______OCTOPUS_PRIME ACTIVATE______
    ░░░░░░░▄▄▄▄█████████████▄▄▄░░░░░░░
    ████▄▀████████▀▀▀▀▀▀████████▀▄████
    ▀████░▀██████▄▄░░░░▄▄██████▀░████▀
    ░███▀▀█▄▄░▀▀██████████▀▀░▄▄█▀▀███░
    ░████▄▄▄▀▀█▄░░░▀▀▀▀░░░▄█▀▀▄▄▄████░
    ░░██▄▄░▀▀████░██▄▄██░████▀▀░▄▄██░░
    ░░░▀████▄▄▄██░██████░██▄▄▄████▀░░░
    ░░██▄▀▀▀▀▀▀▀▀░░████░░▀▀▀▀▀▀▀▀▄██░░
    ░░░██░░░░░░░░░░████░░░░░░░░░░██░░░
    ░░░███▄▄░░░░▄█░████░█▄░░░░▄▄███░░░
    ░░░███████░███░████░███░███████░░░
    ░░░███████░███░▀▀▀▀░███░███████░░░
    ░░░███████░████████████░███████░░░
    ░░░░▀█████░███░▄▄▄▄░███░█████▀░░░░
    ░░░░░░░░▀▀░██▀▄████▄░██░▀▀░░░░░░░░
    ░░░░░░░░░░░░▀░██████░▀░░░░░░░░░░░░
    """

    def __init__(self, n=10, savings_n_loads=True, save_path=None):
        list.__init__(self, list(prime_gen(plim=n)))
        self.max_loaded = self[-1]

    def transform(self, n=None):
        n = n if n is not None else self[-1]*10
        self.extend(list(prime_gen(plim=n, kprimes=self)))

    def is_prime(self, number):
        if number > self[-1]:
            self.transform(number+1)
        if number in self:
            return True
        else:
            return False

    def primes_below(self, upper_bound):
        return self.primes_between(1, upper_bound)

    def primes_between(self, lower_bound, upper_bound):
        if upper_bound > self[-1]:
            self.transform(upper_bound)
        return self[bisect_right(self, lower_bound):bisect_left(self, upper_bound)]