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

from helpme import is_prime


def consecutive_prime_sum(number: int):
    primes_list = [i for i in range(2, number) if is_prime(i)]
    print(f'found primes below {number}')
    primes_set = set(primes_list)
    longest_seq = 1
    max_sum = 1
    for i in range(len(primes_list), 0, -1):
        cur_sum = primes_list[i - 1]
        cur_seq_length = 1
        for j in range(i - 1, 0, -1):
            cur_sum += primes_list[j - 1]
            cur_seq_length += 1
            if cur_sum > number:
                break
            if cur_seq_length >= longest_seq and cur_sum < number and cur_sum in primes_set:
                max_sum = cur_sum
                longest_seq = cur_seq_length
    return longest_seq, max_sum


below = 100
answer_sequence_length, prime_answer = consecutive_prime_sum(below)
print(
    f'{prime_answer} is the largest prime below {below} and can be written as the sum of {answer_sequence_length} consecutive primes')
below = 1000
answer_sequence_length, prime_answer = consecutive_prime_sum(below)
print(
    f'{prime_answer} is the largest prime below {below} and can be written as the sum of {answer_sequence_length} consecutive primes')
below = 1000000
answer_sequence_length, prime_answer = consecutive_prime_sum(below)
print(
    f'{prime_answer} is the largest prime below {below} and can be written as the sum of {answer_sequence_length} consecutive primes')
