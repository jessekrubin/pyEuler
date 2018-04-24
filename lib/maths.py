#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
from math import sqrt, pi
from lib.decorations import cash_muney

try: xrange
except NameError: xrange = range

@cash_muney
def cash_factorial(n):
    if n == 1:
        return 1
    else:
        return cash_factorial(n - 1) * n

from tqdm import tqdm
def pytriple_gen(max_c, primatives_only=True):
    """
    primative pythagorean triples generator

    thanks to 3Blue1Brown
    special thanks to 3Blue1Brown's video on pythagorean triples
    https://www.youtube.com/watch?v=QJYmyhnaaek&t=300s

    :param max_c:
    :return:
    """
    count = 0
    for real_pts in tqdm(xrange(2, int(sqrt(max_c))+1, 1), ascii=True):
        county = 0
        start = 1 if real_pts%2==0 else 2
        # step = 1 if real_pts%2==0 else 2
        for imag_pts in xrange(start, real_pts, 2):
            comp = complex(real_pts, imag_pts)
            sqrd = comp * comp
            real = int(sqrd.real)
            imag = int(sqrd.imag)
            if abs(real-imag)%2 == 1 and gcd(imag, real) == 1:
                sea = int((comp * comp.conjugate()).real)
                triple = (imag, real, sea) if real > imag else (real, imag, sea)

                # print("good")
                # print(triple)
                # print("")
                if triple[2] > max_c:
                    break
                else:
                    county += 1
                    yield triple
            else:
                print(imag, real)
        count += county


def rad2deg(n):
    return 180 * n / pi


def power_mod(number, exponent, mod):
    if exponent>0:
        if exponent%2==0:
            return power_mod(number, exponent//2, mod)
        else:
            return power_mod(number, exponent//2, mod)*number
    else:
        return 1

def divisors_gen(n):
    large_divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor

def gcd(a,b):
    while a:
        a,b = b%a,a
    return b

def n_divisors(n):
    """
    >>> n_divisors(12)
    6
    >>> n_divisors(10)
    4
    """
    return sum(1 for _ in divisors_gen(n))

@cash_muney
def gcd_cash_muny(a,b):
    """
    cashed gcd from some stack overfloat thign cuz there are five+
    """
    r=a%b
    if r==0:
        return b
    if r==1:
        return 1
    return gcd_cash_muny(b,r)

def divisors_list(n):
    return [i for i in divisors_gen(n)]

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
