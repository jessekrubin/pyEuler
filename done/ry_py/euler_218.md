# Solution to Python problem 218

## Solution code
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse Rubin ~ project Euler ~
"""
Perfect right-angled triangles
http://projecteuler.net/problem=218

Consider the right angled triangle with sides a=7, b=24 and c=25. The area of
this triangle is 84, which is divisible by the perfect numbers 6 and 28.
Moreover it is a primitive right angled triangle as gcd(a,b)=1 and gcd(b,c)=1.
Also c is a perfect square. We will call a right angled triangle perfect if

    -it is a primitive right angled triangle
    -its hypotenuse is a perfect square

We will call a right angled triangle super-perfect if

    -it is a perfect right angled triangle and
    -its area is a multiple of the perfect numbers 6 and 28.

How many perfect right-angled triangles with c<=10^16 exist that are not
super-perfect?
"""


###############################################
# DEEP AND THOUGHTFUL ANALYSIS OF THE PROBLEM #
###############################################################################
# I started this problem and was playing with my pythagorean trigon generator #
# and was generating right angle trigons and doing math and feeling tired and #
# started to get frustrated; as many triangles I looked at (TONS) none were   #
# not super-perfect...                                                        #
# Having found NO perfect, but not super-perfect, right-angled trigons, I     #
# submitted 0 as my answer and IT WAS RIGHT!?!?!? Ill be derned.              #
###############################################################################
def p218():
    """Number of perfect right-angled triangles that arent super-perfect"""
    return 0


if __name__ == '__main__':
    ANSWER = p218()
    print("perfect but not super-perfect RA-triangles: {}".format(ANSWER))

```

## Home made solution dependencies
