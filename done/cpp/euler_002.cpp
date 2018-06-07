#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

int fib(int n)
{
	if (n < 2)
		return n;
	return fib(n - 1) + fib(n - 2);
}

int p002(int upper_bound = 4000000)
{
	int even_fibs = 0;
	int i = 0;
	int cfib = fib(i);
	while (cfib < upper_bound)
	{
		cfib = fib(i);
		if (cfib % 2 == 0)
			even_fibs += cfib;
		i++;
	}
	return even_fibs;
}

int main()
{
	int ANSWER = p002();
	cout << ANSWER << endl;
	return 0;
}
