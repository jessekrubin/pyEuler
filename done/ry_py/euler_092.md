# Solution to Python problem 92

## Solution code
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin ~ Project Euler
"""
Square digit chains
Problem 92
A number chain is created by continuously adding the square of the digits in a 
number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless 
loop. What is most amazing is that EVERY starting number will eventually arrive
at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
from pupy.decorations import cash_it
from itertools import combinations_with_replacement

squares = {str(i):i*i for i in range(10)}


def next_num(n):
    return int(''.join(sorted(c for c in str(sum(squares[d] for d in str(n))))))


nexts = {int(''.join(c)):next_num(''.join(c))
         for c in combinations_with_replacement('0123456789', 8)}


@cash_it
def goes_to_89(n):
    if n == 89:
        return True
    elif n == 1:
        return False
    else:
        return goes_to_89(nexts[n])


def p092():
    return sum((1 for i in range(1, 10000000)
                if goes_to_89(next_num(i))))


if __name__ == '__main__':
    answer = p092()
    print("# of numbers that go to 89: {}".format(answer))

```

## Home made solution dependencies
