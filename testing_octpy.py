from lib.octopus_prime import OctopusPrime
from lib.octopus_prime import prime_sieve_gen

#
# octpy = OctopusPrime()
# print(octpy)
#
#
# # octpy.is_prime(2009)
# octpy.grow(100)
# print(octpy)

print("___")
someprimes = [i for i in prime_sieve_gen(upper_bound=20)]
print(someprimes)

print("___")
print("___")
print("___")
another = list(prime_sieve_gen(known_primes=someprimes, upper_bound=100))
another = sorted(another)
print(another)

for p in prime_sieve_gen(known_primes=someprimes, upper_bound=100):
    print("prime found ", p)
