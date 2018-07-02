# Solution to Python problem 173

## Solution code
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
Using up to one million tiles how many different "hollow" square laminae can be
formed?
Problem 173

We shall define a square lamina to be a square outline with a square "hole" so
that the shape possesses vertical and horizontal symmetry. For example, using
exactly thirty-two square tiles we can form two different square laminae:


With one-hundred tiles, and not necessarily using all of the tiles at one time,
it is possible to form forty-one different square laminae.

Using up to one million tiles how many different square laminae can be formed?
"""

from pupy.maths import divisors_gen


def square_lams(upperlimit):
    divfours = [i for i in range(upperlimit + 1) if i % 4 == 0 and i > 4]
    total = 0
    for num in divfours:
        total += len([d for d in divisors_gen(num // 4)])//2

    return total


def p173():
    return square_lams(1000000)


if __name__ == '__main__':
    assert 41 == square_lams(100)
    ANSWER = p173()
    print("Answer: {}".format(ANSWER))
```

## Home made solution dependencies
