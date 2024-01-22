#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse Rubin ~ project Euler ~
"""
Harshad Numbers
Problem 387
A Harshad or Niven number is a number that is divisible by the sum of its
digits. 201 is a Harshad number because it is divisible by 3 (the sum of its
digits.) When we truncate the last digit from 201, we get 20, which is a
Harshad number. When we truncate the last digit from 20, we get 2, which is
also a Harshad number.

Let's call a Harshad number that, while recursively truncating the last digit,
always results in a Harshad number a right truncatable Harshad number.

Also:
    201/3=67 which is prime.

Let's call a Harshad number that, when divided by the sum of its digits,
results in a prime a strong Harshad number. Now take the number 2011 which is
prime. When we truncate the last digit from it we get 201, a strong Harshad
number that is also right truncatable. Let's call such primes strong, right
truncatable Harshad primes. You are given that the sum of the strong, right
truncatable Harshad primes less than 10000 is 90619. Find the sum of the
strong, right truncatable Harshad primes less than 1014.
"""

from pupy.amazon import is_prime


def p387(LIMIT=10**14):
    # -i(10, ) - o(0, )
    # -i(100, ) - o(0, )
    # -i(1000, ) - o(2449, )
    # -i(10000, ) - o(90619, )
    # -i(100000, ) - o(388207, )
    # -i(1000000, ) - o(1188721, )
    # -i(10000000, ) - o(10057005, )
    # -i(100000000, ) - o(130459097, )
    # -i(1000000000, ) - o(1652107364, )
    # -i(10000000000, ) - o(36498117748, )
    # -i(100000000000, ) - o(497168223439, )
    # -i(1000000000000, ) - o(2897368636255, )
    # -i(10000000000000, ) - o(47175350800711, )
    # -i(100000000000000, ) - o(696067597313468, )

    rthp = set()

    def _harshad_primes(n):
        return set(
            a for a in (n * 10 + i for i in range(1, 10)) if is_prime(a) and a < LIMIT
        )

    def _strong_harshad_numbers(n, digits_sum):
        for i in range(10):
            next_n = (10 * n) + i
            dig_sum_i = digits_sum + i
            if next_n <= LIMIT and next_n % (dig_sum_i) == 0:
                if is_prime((next_n / dig_sum_i)):
                    rthp.update(_harshad_primes(next_n))
                _strong_harshad_numbers(next_n, dig_sum_i)

    for starting_number in range(1, 10):
        _strong_harshad_numbers(starting_number, starting_number)

    return sum(rthp)


io = {
    1000: 2449,
    10000: 90619,
    100000: 388207,
    1000000: 1188721,
    10000000: 10057005,
    100000000: 130459097,
    1000000000: 1652107364,
    10000000000: 36498117748,
    100000000000: 497168223439,
    1000000000000: 2897368636255,
    10000000000000: 47175350800711,
    100000000000000: 696067597313468,
}

from pprint import pprint

if __name__ == "__main__":
    ANSWER = p387()
    print("ANSWER :", ANSWER)
