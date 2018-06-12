#include <iostream>
#include <vector>
#include <string>
#include <sstream>
// #include "./cbib.hpp"
#include "cbib.h"
using namespace std;

int main()
{

    int n, digit, rev = 0;

    int num = 12321;

    n = num;

    do
    {
        digit = num % 10;
        rev = (rev * 10) + digit;
        num = num / 10;
    } while (num != 0);
    return 0;
}
