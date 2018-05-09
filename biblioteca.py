#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - Biblioteca
"""
My (Jesse Rubin) library of functions/methods and classes that I use on the reg
"""
from __future__ import division, generators, print_function, absolute_import
from bisect import bisect_right, bisect_left
from cProfile import Profile
from collections import Counter, deque
from functools import wraps, reduce
from inspect import getfile
from itertools import count, chain
from math import sqrt, pi, acos
from operator import add, sub, methodcaller, truediv, floordiv, mul
from time import time
import json as jasm

try: xrange
except NameError: xrange = range

##############
# GENERATORS #
##############


# DECORATORS #

# CLASSES #



def partitions(n, I=1):
    yield (n,)
    for i in xrange(I, n//2+1):
        for p in partitions(n-i, i):
            yield (i,)+p


def cash_it(funk):
    """for when you want that lru cach money but are working w py2

    Args:
        funk (function): function to be cached

    Returns:
        function: wrapped function

    """
    cash_money = {}

    @wraps(funk)
    def cash_wrap(*argz):
        if argz in cash_money:
            return cash_money[argz]
        else:
            rv = funk(*argz)
            cash_money[argz] = rv
            return rv

    return cash_wrap


@cash_it
def cash_factorial(n):
    if n == 1:
        return 1
    else:
        return cash_factorial(n-1)*n


def radians_2_degrees(rads):
    """Converts radians to degrees"""
    return 180*rads/pi


def degrees_2_radians(degs):
    """Converts degrees to radians"""
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
    """iterative gcd"""
    while a:
        a, b = b%a, a
    return b


@cash_it
def rgcd(a, b):
    """recursive greatest common divisor"""
    if b > a:
        return rgcd(b, a)
    r = a%b
    if r == 0:
        return b
    return rgcd(r, b)


def reverse(n):
    """Reverses a number

    Args:
        n (int): number to be reversed

    Returns:
        int: reversed of a number

    """

    reversed = 0
    while n > 0:
        reversed *= 10
        reversed += n%10
        n //= 10
    return reversed


@cash_it
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
    """greatest exponent for a divisor of n

    Args:
        d (int): divisor
        n (int): number be divided

    Returns:
        int: number of times a divisor divides n
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


@cash_it
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


class Jasm(object):
    """Jasm the Grundle Bug"""

    def __init__(self, path):
        self.file_path = path

    def __call__(self, funk):
        """Json saving and loading"""

        def savings_n_loads(*args, **kwargs):
            """Jasm funk (w)rapper"""
            try:
                dat_data = Jasm.read(self.file_path)
            except IOError:
                dat_data = funk(*args, **kwargs)
                self.write(self.file_path, dat_data)
            return dat_data

        return savings_n_loads

    @staticmethod
    def read(fpath):
        """Jasm load static method

        Args:
            fpath(str): filepath

        Returns:
            object: object/data stored in the json file
        """
        with open(fpath) as f: return jasm.load(f)

    @staticmethod
    def write(fpath, obj):
        """Jasm dump static method

        Args:
            fpath (str): filepath
            obj (object): data/object to be saved
        """
        with open(fpath, 'wb') as f:
            jasm.dump(obj=obj, encoding='utf8', indent=4,
                      sort_keys=True, ensure_ascii=True)


def cprof(funk):
    """
    cProfiling decorator
    src: https://zapier.com/engineering/profiling-python-boss/

    :param funk:
    :return:
    """

    @wraps(funk)
    def profiled_funk(*args, **kwargs):
        profile = Profile()
        try:
            profile.enable()
            ret_val = funk(*args, **kwargs)
            profile.disable()
        finally:
            print("__CPROFILE__")
            profile.print_stats()
        return ret_val

    return profiled_funk


class tictoc(object):
    """Timing decorator object

    Args:
        runs: # of runs to time over (defaults to 1)
    """

    def __init__(self, runs=1):
        self.runs = runs

    def __str__(self, t_total, funk, args_string):
        str_list = ['__TICTOC__',
                    '    file: {}'.format(getfile(funk)),
                    '    funk: {}'.format(funk.__name__),
                    '    args: {}'.format(args_string),
                    '    time: {}'.format(tictoc.ftime(t_total)),
                    '    runs: {}'.format(self.runs)]
        return '\n'.join(str_list)

    def __call__(self, time_funk, printing=True):
        @wraps(time_funk)
        def time_wrapper(*args, **kwargs):
            self.args = str(args)
            ts = time()
            for i in xrange(self.runs):
                result = time_funk(*args, **kwargs)
            te = time()
            t_total = (te-ts)/self.runs
            if printing: print(self.__str__(t_total, time_funk, str(args)))
            return result

        return time_wrapper

    @staticmethod
    def ftime(t1, t2=None):
        if t2 is not None: return tictoc.ftime((t2-t1))
        elif t1 == 0.0: return "~0.0~"
        elif t1 >= 1: return "%.3f s"%t1
        elif 1 > t1 >= 0.001: return "%.3f ms"%((10**3)*t1)
        elif 0.001 > t1 >= 0.000001: return "%.3f μs"%((10**6)*t1)
        elif 0.000001 > t1 >= 0.000000001: return "%.3f ns"%((10**9)*t1)
        else: return tictoc.ftime((t2-t1))


def list_product(l):
    return reduce(mul, l)


def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


def is_permutation(a, b):
    """
    Checks if two integers or lists are permutations lists are permutations

    Args:
        a (int or list): possible perumtation of b
        b (int or list): possible perumtation of a

    Returns:
        bool: True if a and b are permutations of one another; False otherwise

    """

    if type(a) == int:
        a = digits_list(a)
    if type(b) == int:
        b = digits_list(b)
    return len(a) == len(b) and Counter(a) == Counter(b)


def rotate_list(l, n=1):
    return l[-n:]+l[:-n]


def list_rotation_gen(l):
    for i in xrange(len(l)):
        yield (l[-i:]+l[:-i])


def digits_list(num):
    """Returns a list of the digits in num

    Args:
        num (int): number w/ digits to be listsed

    Returns:
        list of digits

    Examples:
        >>> digits_list(1111)
        [1, 1, 1, 1]
        >>> digits_list(982)
        [9, 8, 2]
        >>> digits_list(101)
        [1, 0, 1]
        >>> digits_list(123)
        [1, 2, 3]
    """

    digits = deque()
    for _ in xrange(len(str(num))):
        num, r = divmod(num, 10)
        digits.appendleft(r)
    return list(digits)


def digits_to_int(l):
    """
    >>> digits_to_int([3, 2, 1])
    321
    >>> digits_to_int([1, 1, 1, 1, 2, 3])
    111123
    >>> digits_to_int([1, 2, 3])
    123
    """
    return sum((l[len(l)-i-1]*10**i) for i in xrange(0, len(l), 1))


def is_palindrome(string):
    """True a string is a palindrome.

    Doctests:
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("greg")
    False
    """
    for index, character in enumerate(string):
        if character != string[-index-1]:
            return False
    return True


def binary_string(number):
    """Number to binary"""
    return bin(number)[2:]


def string_score(name):
    """
    >>> string_score('me')
    18
    >>> string_score('poooood')
    95
    >>> string_score('gregory')
    95
    """
    return sum((ord(character)-96 for character in name.lower()))


class SodokuError(ValueError):

    def __init__(self, message, row=None, col=None):
        self.message = message
        self.row, self.col = row, col
        super(SodokuError, self).__init__(message, row, col)


class Sodoku(object):
    """Sodoku class

    [ 0,  1,  2,  3,  4,  5,  6,  7,  8]
    [ 9, 10, 11, 12, 13, 14, 15, 16, 17]
    [18, 19, 20, 21, 22, 23, 24, 25, 26]
    [27, 28, 29, 30, 31, 32, 33, 34, 35]
    [36, 37, 38, 39, 40, 41, 42, 43, 44]
    [45, 46, 47, 48, 49, 50, 51, 52, 53]
    [54, 55, 56, 57, 58, 59, 60, 61, 62]
    [63, 64, 65, 66, 67, 68, 69, 70, 71]
    [72, 73, 74, 75, 76, 77, 78, 79, 80]
    """

    def __init__(self, board):
        self.is_solved = False
        self.board = board.replace('.', '0')

    def solve(self):
        if 17 > sum(1 for n in self.board if n != '0'):
            raise SodokuError("not enough info")
        full_set = '123456789'
        d = {i:("".join(c for c in full_set)
                if self.board[i] == '0'
                else self.board[i])
             for i in xrange(81)}
        d = Sodoku.update_dictionary(d)
        tf, d = Sodoku.reduce_dictionary(d)
        if not tf:
            raise SodokuError("check_unsolvable")
        a = [d[ind] for ind in xrange(81)]
        self.board = "".join(a)
        self.is_solved = True

    def euler_096_three_digit_number(self):
        if not self.is_solved:
            self.solve()
        return int(self.board[0:3])

    @staticmethod
    def first_unknown(d):
        for i in xrange(81):
            if len(d[i]) > 1:
                return i

    @staticmethod
    def unsolvable(rcbd):
        return any(len(v) == 0 for v in rcbd.values())

    @staticmethod
    def check_unsolvable(d):
        nd = {k:v for k, v in d.items()}
        for rcb in xrange(9):
            box = {str(n):[ind for ind in Sodoku.box_inds(*divmod(rcb, 3))
                           if str(n) in d[ind]]
                   for n in xrange(1, 10)}
            row = {str(n):[ind for ind in Sodoku.row_inds(rcb)
                           if str(n) in d[ind]]
                   for n in xrange(1, 10)}
            col = {str(n):[ind for ind in Sodoku.col_inds(rcb)
                           if str(n) in d[ind] or str(n) == d[ind]]
                   for n in xrange(1, 10)}
            if Sodoku.unsolvable(box) or Sodoku.unsolvable(row) or Sodoku.unsolvable(col):
                raise SodokuError("UNSOLVABLE")
        return nd

    @staticmethod
    def update_dictionary(d):
        nd = {k:v for k, v in d.items()}
        for i in xrange(81):
            if len(nd[i]) == 1:
                for nay in Sodoku.neighbors(i):
                    if len(nd[nay]) != 1 and nd[i] in nd[nay]:
                        nd[nay] = nd[nay].replace(nd[i], '')
        return nd

    @staticmethod
    def reduce_dictionary(d):
        if all(len(v) == 1 for v in d.values()):
            return True, d
        try:
            d = Sodoku.check_unsolvable(d)
        except SodokuError:
            return False, d
        d = Sodoku.update_dictionary(d)
        if any(len(v) == 0 for k, v in d.items()):
            return False, d
        fz = Sodoku.first_unknown(d)
        if fz is None:
            if Sodoku.hasdup(d): return False, d
            return Sodoku.reduce_dictionary(d)
        for poss in d[fz]:
            nd = {k:v for k, v in d.items()}
            nd[fz] = str(poss)
            if not Sodoku.hasdup(nd):
                valid, ret = Sodoku.reduce_dictionary(nd)
                if valid:
                    return valid, ret
        return False, d

    # def __str__(self):
    #
    #     header = "  S   O   D   O   K   U  "
    #     top_border = "╔═══════╦═══════╦═══════╗"
    #     mid_border = "╠═══════╬═══════╬═══════╣"
    #     bot_border = "╚═══════╩═══════╩═══════╝"
    #     top_boxes = "\n".join(
    #             "║ {} {} {} ║ {} {} {} ║ {} {} {} ║".format(*self.row(l))
    #             for l in range(0, 3))
    #     mid_boxes = "\n".join(
    #             "║ {} {} {} ║ {} {} {} ║ {} {} {} ║".format(*self.row(l))
    #             for l in range(3, 6))
    #     bot_boxes = "\n".join(
    #             "║ {} {} {} ║ {} {} {} ║ {} {} {} ║".format(*self.row(l))
    #             for l in range(6, 9))
    #     strings = [
    #         header, top_border, top_boxes, mid_border, mid_boxes, mid_border,
    #         bot_boxes, bot_border
    #         ]
    #     return "\n".join(strings)
    @staticmethod
    def hasdup(d):
        for i in xrange(81):
            if len(d[i]) == 1:
                for n in Sodoku.neighbors(i):
                    if d[n] == d[i]:
                        return True
        return False

    def get_oneline_str(self):
        return self.board

    @staticmethod
    def neighbors(index, size=9):
        return {ni for ni in chain(Sodoku.row_inds(index//size),
                                   Sodoku.col_inds(index%size),
                                   Sodoku.cell_box(index))}-{index}

    @staticmethod
    def row_inds(n, bsize=9):
        return {i for i in xrange(n*bsize, n*bsize+bsize)}

    @staticmethod
    def col_inds(n, bsize=9):
        return {i for i in xrange(n, bsize**2, bsize)}

    @staticmethod
    def box_inds(box_r, box_c, bsize=9):
        return {i*bsize+j
                for i in xrange((box_r*3), (box_r*3)+3)
                for j in xrange((box_c*3), (box_c*3)+3)}

    @staticmethod
    @cash_it
    def cell_box(index, bsize=9):
        for box_r in xrange(3):
            for box_c in xrange(3):
                box = Sodoku.box_inds(box_r, box_c)
                if index in box:
                    return box


if __name__ == '__main__':
    import doctest

    doctest.testmod()
