#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

int multiples_lt(int limit, int divisor)
{
    int mul = limit / divisor;
    return ((mul * mul * divisor) + (mul * divisor)) / 2;
}

int p001(int upper_bound = 1000)
{
    return multiples_lt(upper_bound, 3) + multiples_lt(upper_bound, 5) - multiples_lt(upper_bound, 15);
}

int main()
{
    int ANSWER = p001();
    cout << ANSWER << endl;
    return 0;
}