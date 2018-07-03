#!/usr/bin/env bash
#Sum square difference ~ Problem 6 ~ Jesse R.

MAX_N=100                   # n natural numbers
a=0                         # squared_then_summed
b=0                         # summed_then_squared
for ((n=1;n<=MAX_N;n++));do # for each natural number under MAX_N
    ((a+=n**2))             # add n^2 to a
    ((b+=n))                # add n to b
done                        # done with the loop
ANSWER=$(($b**2-$a))        # square b and subtract a
echo "ANSWER: $ANSWER"
