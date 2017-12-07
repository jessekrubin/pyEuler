def isPanDigit(n):
    nset = set(digitsList(n))
    return(nset == set([(i+1) for i in range(b10length(n))]))


def b10length(n):
    l = 0
    cur = n
    while(cur > 0):
        l += 1
        cur = cur // 10
    return l


def digitsList(n):
    digits = []
    cur = n
    while(cur > 10):
        digits.append(cur % 10)
        cur = cur // 10
    digits.append(cur)
    return digits

def factors(x):
    leeest = []
    for i in range(1, int(x/2)+1 ):
        if x % i == 0:
            leeest.append(i)
    leeest.append(x)
    return leeest


def divList(x):
    leeest = []
    for i in range(1, int(x/2)+1 ):
        if x % i == 0:
            leeest.append(i)
    return leeest

def numDivs(x):
    n = 0
    for i in range(int((1 + x)/2),0, -1):
        # print(i)
        if x % i == 0:
            n += 1
    return n
