import string
import random

s = random.choices(string.ascii_lowercase, k = 5)

def count_letters(s):

    d = dict()

    for c in s:

        if c not in d:
            d[c] = 1
        else: d[c] +=1

    print(s)
    print(d)

count_letters(s)