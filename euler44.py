def p(n):
    return (divmod((3 * n * n - n ), 2)[0])



pCash = {}

for i in range(1, 10):
    print(p(i))
