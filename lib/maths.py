#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
from math import sqrt, pi
from lib.decorations import cash_muney

@cash_muney
def cash_factorial(n):
    if n == 1:
        return 1
    else:
        return cash_factorial(n - 1) * n


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

@cash_muney
def is_perfect_square(positive_n):
    if positive_n < 5:
        if positive_n == 4 or positive_n == 1:
            return True
        return False
    half = positive_n // 2
    seen_set = {half}
    while half * half != positive_n:
        half = (half + (positive_n // half)) // 2
        if half in seen_set:
            return False
        seen_set.add(half)
    return True


def divisors_gen(n):
    large_divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor


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
