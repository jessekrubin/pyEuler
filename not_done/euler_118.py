#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Pandigital prime sets
Problem 118
Using all of the digits 1 through 9 and concatenating them freely to form
decimal integers, different sets can be formed. Interestingly with the set
{2,5,47,89,631}, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly
once contain only prime elements?
"""

from itertools import permutations

from lib.octopus_prime import is_prime


# primes = [pytriplets_gen for pytriplets_gen in prime_sieve_gen(10000000000)]
# print(len(primes))
#
def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
         for y in partition(number - x):
             answer.add(tuple(sorted((x, ) + y)))
    return answer
#
one_to_nine = [i+1 for i in range(9)]
print(one_to_nine)
allperms = [i for i in permutations(one_to_nine)]
print(len(allperms))
#
partitions_of_nine = partition(9)
partition_perms = {partition: {part_perm for part_perm in permutations(partition)}
                   for partition in partitions_of_nine}
# print(allperms)

# for i in permutations(one_to_nine):
#     print(i)

from lib.listless import dig_list_2_int

def check_partitions(perm):
    print(perm)
    lests = []
    if len(perm) == 1:
        lests.append([])
    for i in range(len(perm)):
        num = dig_list_2_int(perm[0:i+1])
        if is_prime(num):
            # print([num])
            l = check_partitions(perm[i+1:])
            if l is not None and len(l)>1:
                lests.append([num, l])
    print(lests)
    return lests


permtrial = (2, 5, 4, 7, 8, 9, 6, 3, 1)
print(check_partitions(permtrial))
sets = set()
# for i in permutations(one_to_nine):
#     thing = check_partitions(i)
#     if thing is not None:
#         sets.add(tuple(sorted((thing))))

    # sets.add(thing)
    # print(thing)

print(len(sets))

