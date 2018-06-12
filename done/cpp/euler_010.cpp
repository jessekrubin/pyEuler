// ~ JKR ~ cpPEuler ~
// Summation of primes
// Problem 10
// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
// Find the sum of all the primes below two million.
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

bool is_prime(int num)
{ // is_prime!!! written like a true pythoner
    if (num <= 3)
        return num > 1;
    if (num % 2 == 0 || num % 3 == 0)
        return false;
    for (int i = 5; i * i <= num; i += 6)
        if (num % i == 0 || num % (i + 2) == 0)
            return false;
    return true;
}

int main()
{
    long total = 2; // WE SKIP TWOOOO
    for (int i = 3; i < 2000000; i += 2)
    {
        if (is_prime(i))
        {
            total += i;
        }
    }
    cout << total << endl;
    return 0;
}