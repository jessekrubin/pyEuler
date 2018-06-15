// ~ JKR ~ cpPEuler ~ Problem 10
#include <iostream>
#include <vector>
#include <string>
#include <numeric>
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

vector<int> prime_sieve(long max)
{
    vector<int> sieve;
    vector<int> primes;
    for (int i = 1; i < max + 1; ++i)
        sieve.push_back(i);
    sieve[0] = 0;
    for (int i = 2; i < max + 1; ++i)
        if (sieve[i - 1] != 0)
        {
            primes.push_back(sieve[i - 1]);
            for (int j = 2 * sieve[i - 1]; j < max + 1; j += sieve[i - 1])
                sieve[j - 1] = 0;
        }
    return primes;
}

long p010(int lim)
{
    long total = 0;
    vector<int> primes = prime_sieve(lim);
    for (int i = 0; i < primes.size(); i++)
    {
        total += primes[i];
    }
    return total;
}

int main()
{
    long total = p010(2000000);
    cout << total << endl;
    return 0;
}