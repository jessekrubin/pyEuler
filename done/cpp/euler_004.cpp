#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

int reverse(int num)
{
    int digit = 0;
    int rev = 0;
    int n = num;
    while (n != 0)
    {
        digit = n % 10;
        rev = (rev * 10) + digit;
        n = n / 10;
    }
    return rev;
}

int p004()
{
    int max_pal = 0;
    for (int i = 100; i < 1000; i++)
    {
        for (int j = 100; j < 1000; j++)
        {
            int m = i * j;
            if (m == reverse(m) && m > max_pal)
            {
                max_pal = m;
            }
        }
    }
    return max_pal;
}

int main()
{
    cout << p004() << endl;
    return 0;
}
