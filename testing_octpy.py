from lib.octopus_prime import OctopusPrime
from lib.octopus_prime import prime_sieve_gen

#
octpy = OctopusPrime()
print(octpy)


octpy.transform(20)
print(octpy)

print(octpy.is_prime(23))
print(octpy)

octpy.transform(40)
print(octpy)



octpy.transform(50)
print(octpy)


another = OctopusPrime()
print(another)
print(another.is_prime(99))
print(another)

print(another.prime_range(160, 200))
print(another.primes_below(20))
print(another)
