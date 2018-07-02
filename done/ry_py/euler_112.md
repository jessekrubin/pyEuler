# Solution to Python problem 112

## Solution code
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Bouncy numbers
Problem 112
Working from left-to-right if no digit is exceeded by the digit to its left it
is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a
"is_bouncy" number; for example, 155349.

Clearly there cannot be any is_bouncy numbers below one-hundred, but just over
half of the numbers below one-thousand (525) are is_bouncy. In fact, the least
number for which the proportion of is_bouncy numbers first reaches 50% is 538.

Surprisingly, is_bouncy numbers become more and more common and by the time we
reach 21780 the proportion of is_bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly
99%
"""
from __future__ import division
from pupy.listless import digits_list

try: range
except NameError: range = range


def is_bouncy(n):
    digits = digits_list(n)
    increasing = False
    decreasing = False
    for i in range(0, len(digits)-1):
        if digits[i+1] < digits[i]:
            increasing = True
        elif digits[i+1] > digits[i]:
            decreasing = True
        if increasing and decreasing:
            return True
    return False


def find_proportion(percent):
    i = 100
    bouncy_count = 0
    while True:
        i += 1
        if is_bouncy(i):
            bouncy_count += 1
        if (bouncy_count/i) == (percent/100):
            return i




def p112(percentage=99):
    return find_proportion(percentage)


if __name__ == '__main__':
    assert 21780 == find_proportion(90)
    ANSWER = p112()
    print("Smallest n where proportion bouncy is 99%: {}".format(ANSWER))
```

## Home made solution dependencies
