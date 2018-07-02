# Solution to Python problem 74

## Solution code
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Digit factorial chains
Problem 74 
The number 145 is well known for the property that the sum of the factorial of
its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of
numbers that link back to 169; it turns out that there are only three such
loops that exist:

169 >>> 363601 >>> 1454 >>> 169
871 >>> 45361 >>> 871
872 >>> 45362 >>> 872

It is not difficult to prove that EVERY starting number will eventually get
stuck in a loop. For example,

69 >>> 363600 >>> 1454 >>> 169 >>> 363601 (>>> 1454)
78 >>> 45360 >>> 871 >>> 45361 (>>> 871)
540 >>> 145 (>>> 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest
non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly
sixty non-repeating terms?
"""

from pupy.listless import digits_list
from pupy.decorations import cash_it
from math import factorial

digfact = {i:factorial(i) for i in range(10)}
chain_lengths = {}

@cash_it
def digit_factorial(n):
    return sum(digfact[i] for i in digits_list(n))


@cash_it
def chain_length(n):
    visited = set()

    def curses(n):
        if n in visited:
            return len(visited)
        else:
            visited.add(n)
            n = digit_factorial(n)
            return curses(n)

    curses(n)
    return len(visited)


def p074():
    sixties = 0
    for i in range(1000000):
        if chain_length(i) == 60:
            sixties += 1
    return sixties


if __name__ == '__main__':
    ANSWER = p074()
    print("ANSWER: {}".format(ANSWER))

```

## Home made solution dependencies
