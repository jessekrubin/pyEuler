# Consider the divisors of 30: 1,2,3,5,6,10,15,30.
# It can be seen that for every divisor d of 30, d+30/d is prime.

# Find the sum of all positive integers n not exceeding 100 000 000
# such that for every divisor d of n, d+n/d is prime.


import helpme

def dothing(number):
    divs = helpme.factors(number)
    for divisor in divs:
        print("++++")
        print(divisor)
        print((number+divisor)/divisor)
        

    print(divs)

dothing(30)
