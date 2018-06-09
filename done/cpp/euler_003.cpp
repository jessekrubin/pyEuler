#include <iostream>
#include <vector>
#include <string>
#include <sstream>
// #include "./cbib.hpp"
#include "cbib.h"
using namespace std;

int main()
{
    int uno = 5;
    int dos = 25;
    // double a = 0.9231;
    int a = Add(uno, dos);
    cout << a << endl;

    return 0;
}
