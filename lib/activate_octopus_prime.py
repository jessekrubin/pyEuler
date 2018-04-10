# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - update README.md
# Python script to update the README.md for this repo


from lib.octopus_prime import OctopusPrime

op = OctopusPrime()


print("transforming")
print(op)
while len(op) < 1000:
    somethign = int(op[-1]*10)
    print("transforming up to ", somethign)
    print("next ", somethign)
    op.transform(somethign)
    op._save()
