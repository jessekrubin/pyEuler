from lib.octopus_prime import OctopusPrime
from lib.octopus_prime import prime_sieve_gen

#
octpy = OctopusPrime()
print(octpy)


octpy.grow(20)
print(octpy)

print(octpy.is_prime(23))
print(octpy)

octpy.grow(40)
print(octpy)



octpy.grow(50)
print(octpy)


another = OctopusPrime()
print(another)


####
# print("___")
# someprimes = [i for i in prime_sieve_gen(upper_bound=20)]
# print(someprimes)
#
# another = list(prime_sieve_gen(known_primes=someprimes, upper_bound=100))
# another = sorted(another)
# print(another)
#
# for p in prime_sieve_gen(known_primes=someprimes, upper_bound=100):
#     print("prime found ", p)
