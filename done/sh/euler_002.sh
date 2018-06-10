#!/bin/bash
# Jesse K Rubin ~ peuler p002
SUM=0
N1=0
N2=1

while [ $N2 -lt 4000000 ]
do
    TN=$(($N1+$N2))
    N1=$N2
    N2=$TN
    if (($N2%2==0))
    then
        ((SUM += $N2))
    fi
done
echo "ANSWER:" $SUM
