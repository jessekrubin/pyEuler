# coding=utf-8

from lib.octopus_prime import prime_gen, OctopusPrime


op = OctopusPrime(1000000)

# primes = [p for p in prime_gen(1000000)]
#
# print(primes)

# print("\n".join(str(p) for p in op.primes_between(100, 1000)))
# print("")
print(" ".join(str(p) for p in op.primes_between(100000, 1000000)))
