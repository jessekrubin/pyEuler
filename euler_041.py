"""We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?"""

from itertools import permutations

numslists = []
for i in range(1, 10):
    numslists.append([x+1 for x in range(i)])

nums = {}
for j in range(len(numslists)):
    print(numslists[j])
    l = []

    for i in permutations(numslists[j], len(numslists[j])):
        l.append(i)
    # print(l)
    print(len(l))
        

# print(numslists)

# for i in permutations(l, len(l)):
    # print(i)

# hm.digitsList(123)
# hm.digitsList(14352)
# # hm.digitsList(133333)

# hm.b10length(1000)

# hm.b10length(1)
# hm.b10length(1233333)
# hm.b10length(1234)



