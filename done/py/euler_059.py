#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
"""
XOR decryption
Problem 59
Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange). For
example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and without
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password
key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using cipher.txt (right click and 'Save Link/Target As...'),
a file containing the encrypted ASCII codes, and the knowledge that the plain
text must contain common English words, decrypt the message and find the sum
of the ASCII values in the original text.
"""

from string import ascii_lowercase
from itertools import permutations
from itertools import cycle


def decrypt(arr, key):
    return "".join(chr(a^b) for a, b in zip(arr, cycle(key)))


def p059():
    # well i just put in a few words and boom. super lucky.
    # only one decrypted message had the words and, the and was...
    with open(r'../../txt_files/p059_cipher.txt') as f:
        cipher = list(map(int, f.readline().split(',')))
    ascii_values = [ord(c) for c in ascii_lowercase]
    not_crypts = (decrypt(cipher, p) for p in permutations(ascii_values, 3))
    for decrypted in not_crypts:
        if "and" in decrypted and "the" in decrypted and "was" in decrypted:
            return sum(ord(c) for c in decrypted)


if __name__ == '__main__':
    ANSWER = p059()
    print("ANSWER: {}".format(ANSWER))