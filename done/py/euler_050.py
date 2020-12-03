#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Consecutive prime sum
Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from pupy.amazon import prime_gen


def consecutive_prime_sum(upper_bound):
    primes_list = [p for p in prime_gen(upper_bound)]
    primes_set = set(primes_list)
    longest_seq = 1
    max_sum = 1
    for p in range(len(primes_list), 0, -1):
        cur_sum = primes_list[p - 1]
        cur_seq_length = 1
        for j in range(p - 1, 0, -1):
            cur_sum += primes_list[j - 1]
            cur_seq_length += 1
            if cur_sum > upper_bound:
                break
            if (
                cur_seq_length >= longest_seq
                and cur_sum < upper_bound
                and cur_sum in primes_set
            ):
                max_sum = cur_sum
                longest_seq = cur_seq_length
    return longest_seq, max_sum


def p050():
    answer_sequence_length, prime_answer = consecutive_prime_sum(10 ** 6)
    return prime_answer


if __name__ == '__main__':
    assert 6, 41 == consecutive_prime_sum(100)
    assert 21, 953 == consecutive_prime_sum(1000)
    ANSWER = p050()
    print('Prime answer: {}'.format(ANSWER))
