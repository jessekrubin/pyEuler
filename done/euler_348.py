#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Problem 0
template
"""
# THIS IS A TEMPLATEEEEE

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Problem 0
template
"""
from tqdm import tqdm


def is_palindrome(n):
    return str(n) == str(n)[::-1]

def square(n):
    return n*n

def cube(n):
    return n*n*n


def find_square_cube_pals():
    pals_dict = {}
    # takes like 5 mins to run, so walk away and grab a snack
    for i in tqdm(range(1, 30000)):
        isq = square(i)
        delthis = []
        for pal, count in pals_dict.items():
            if pal < isq and count < 4:
                delthis.append(pal)
        for key in delthis:
            pals_dict.pop(key)

        for j in range(1, i+1):
            # nermber: int = isq + (j*j*j)
            nermber = isq + cube(j)
            if is_palindrome(nermber):
                pals_dict[nermber] = pals_dict.get(nermber, 0) + 1

    # {5229225: 4, 37088073: 4, 108909801: 4, 56200265: 4, 796767697: 4}
    return {k: v for k, v in pals_dict.items() if v == 4}


five_four_pals = {5229225: 4, 37088073: 4, 108909801: 4, 56200265: 4, 796767697: 4}
answer = sum(k for k in five_four_pals.keys())
print("ANSWER:", answer)