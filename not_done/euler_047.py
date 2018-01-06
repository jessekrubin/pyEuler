# coding=utf-8
def prime_factors_set(n):
    i = 2
    factors = []
    while(i * i < n + 1):
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return set(factors)


print(prime_factors_set(52))
print(prime_factors_set(700))
print(len(prime_factors_set(52)))
print(len(prime_factors_set(700)))
