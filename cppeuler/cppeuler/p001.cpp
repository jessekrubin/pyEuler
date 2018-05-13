#include "stdafx.h"
#include "p001.h"

int p001()
{
	int total = 0;
	for (int i = 0; i < 1000; i++)
		if (i % 3 == 0 || i % 5 == 0)
			total += i;
	return total;
}